import torch
import torch.nn as nn
import numpy as np
import math
from dataclasses import dataclass
import time
from nsml import DATASET_PATH


def trainer(mode, config, dataloader, optimizer, model, criterion, metric, train_begin_time, device):

    log_format = "[INFO] step: {:4d}/{:4d}, loss: {:.6f}, " \
                              "cer: {:.2f}, elapsed: {:.2f}s {:.2f}m {:.2f}h, lr: {:.6f}"
    total_num = 0
    epoch_loss_total = 0.
    print(f'[INFO] {mode} Start')
    epoch_begin_time = time.time()
    cnt = 0
    for inputs, targets, input_lengths, target_lengths in dataloader:
        begin_time = time.time()

        optimizer.zero_grad()
        inputs = inputs.to(device)
        targets = targets.to(device)
        input_lengths = input_lengths.to(device)
        target_lengths = torch.as_tensor(target_lengths).to(device)
        model = model.to(device)

        if config.architecture.lower() == 'deepspeech2':
            outputs, output_lengths = model(inputs, input_lengths)
            #loss = criterion(outputs.transpose(0, 1),targets[:, 1:],tuple(output_lengths),tuple(target_lengths))
        elif config.architecture.lower() == 'las':

            if isinstance(model, nn.DataParallel):
                model.module.flatten_parameters()
                #print("flatten_parameters")

            outputs, encoder_output_lengths, encoder_log_probs = model(inputs, input_lengths, targets, teacher_forcing_ratio=0.99)
            
            #loss = criterion(outputs.transpose(0, 1),targets[:, 1:],tuple(outputs.size(-1))),tuple(target_lengths))
            # loss = criterion(
            #         outputs.contiguous().view(-1, outputs.size(-1)), targets[:, 1:].contiguous().view(-1)
            #     )
            # loss, ctc_loss, cross_entropy_loss = criterion(
            #     encoder_log_probs=encoder_log_probs.transpose(0, 1),
            #     decoder_log_probs=outputs.contiguous().view(-1, outputs.size(-1)),
            #     output_lengths=encoder_output_lengths,
            #     targets=targets[:, 1:],
            #     target_lengths=target_lengths)
                
            loss = criterion(outputs.contiguous().view(-1, outputs.size(-1)), targets[:, 1:].contiguous().view(-1))

        y_hats = outputs.max(-1)[1]

        if mode == 'train':
            optimizer.zero_grad()
            loss.backward()
            optimizer.step(model)

        total_num += int(input_lengths.sum())
        epoch_loss_total += loss.item()

        torch.cuda.empty_cache()

        if cnt % config.print_every == 0:

            current_time = time.time()
            elapsed = current_time - begin_time
            epoch_elapsed = (current_time - epoch_begin_time) / 60.0
            train_elapsed = (current_time - train_begin_time) / 3600.0
            #print(targets[:, 1:])
            #rint(y_hats)
            cer = metric(targets[:, 1:], y_hats)
            print(log_format.format(
                cnt, len(dataloader), loss,
                cer, elapsed, epoch_elapsed, train_elapsed,
                optimizer.get_lr(),
            ))
        cnt += 1
    return model, epoch_loss_total/len(dataloader), metric(targets[:, 1:], y_hats)