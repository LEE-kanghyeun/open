"""
Predict
"""
from datetime import datetime
from tqdm import tqdm
import numpy as np
import random, os, sys, torch, cv2, warnings
from glob import glob
from torch.utils.data import DataLoader

prj_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(prj_dir)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

from modules.utils import load_yaml, save_yaml, get_logger
from modules.scalers import get_image_scaler
from modules.datasets import SegDataset
from models.utils import get_model
warnings.filterwarnings('ignore')


def pred(config):
    train_config = load_yaml(os.path.join(prj_dir, 'results', 'train', config['train_serial'], 'train.yaml'))
    # train_config = load_yaml(os.path.join(prj_dir, 'results', 'train', config2['train_serial'], 'train.yaml'))

    # Set random seed, deterministic
    torch.cuda.manual_seed(train_config['seed'])
    torch.manual_seed(train_config['seed'])
    np.random.seed(train_config['seed'])
    random.seed(train_config['seed'])
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    # Set device(GPU/CPU)
    os.environ['CUDA_VISIBLE_DEVICES'] = str(config['gpu_num'])
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load architecture
    model = get_model(model_str=train_config['architecture'])
    model = model(
        classes=train_config['n_classes'],
        encoder_name=train_config['encoder'],
        encoder_weights=train_config['encoder_weight'],
        activation=train_config['activation']).to(device)

    # logging_level = 'debug' if config['verbose'] else 'info'
    # logger = get_logger(name='train',
    #                     file_path=os.path.join(pred_result_dir, 'pred.log'),
    #                     level=logging_level)
    # logger.info(f"Load model architecture: {train_config['architecture']}")

    # ! Load weight
    check_point_path = os.path.join(prj_dir, 'results', 'train', config['train_serial'], 'model.pt')
    check_point = torch.load(check_point_path)
    model.load_state_dict(check_point['model'])
    # logger.info(f"Load model weight, {check_point_path}")

    # ! Set predict serial

    model.eval()

    return model #(y_pred, ori_size, pred_result_dir_mask)


if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    #! Load config
    config = load_yaml(os.path.join(prj_dir, 'config', 'predict_ensemble.yaml'))
    config_list = config['train_serial'].split(',')
    pred_serial = config['train_serial'].replace(',', '+') + '_' + datetime.now().strftime("%Y%m%d_%H%M%S")

    model_list = []
    for i, train_serial in enumerate(config_list):
        config['train_serial'] = train_serial.strip()
        model_list.append(pred(config))
        # print(model_list)


    train_config = load_yaml(os.path.join(prj_dir, 'results', 'train', config['train_serial'], 'train.yaml'))

    # Create train result directory and set logger
    pred_result_dir = os.path.join(prj_dir, 'results', 'pred', pred_serial)
    pred_result_dir_mask = os.path.join(prj_dir, 'results', 'pred', pred_serial, 'mask')
    os.makedirs(pred_result_dir, exist_ok=True)
    os.makedirs(pred_result_dir_mask, exist_ok=True)

    # Set logger
    logging_level = 'debug' if config['verbose'] else 'info'
    logger = get_logger(name='train',
                        file_path=os.path.join(pred_result_dir, 'pred.log'),
                        level=logging_level)

    # Set data directory
    data_dir = r'/content/gdrive/MyDrive/대회/MAICON 대회/대회 Data/'
    # train_dirs = os.path.join(data_dir, 'test')
    test_dirs = os.path.join(data_dir, 'test')
    test_img_paths = glob(os.path.join(test_dirs, 'x', '*.png'))
    print('테스트 이미지 개수: ',len(test_img_paths))

    # ! Load data & create dataset for train
    test_dataset = SegDataset(paths=test_img_paths,
                              input_size=[train_config['input_width'], train_config['input_height']],
                              scaler=get_image_scaler(train_config['scaler']),
                              mode='test',
                              logger=logger)

    # Create data loader
    test_dataloader = DataLoader(dataset=test_dataset,
                                 batch_size=config['batch_size'],
                                 num_workers=config['num_workers'],
                                 shuffle=False,
                                 drop_last=False)
    logger.info(f"Load test dataset: {len(test_dataset)}")


    # Save config
    # save_yaml(os.path.join(pred_result_dir, 'train_config.yml'), train_config)
    save_yaml(os.path.join(pred_result_dir, 'predict_config.yml'), config)

    # Predict
    logger.info(f"START PREDICTION")


    with torch.no_grad():
        count = 0
        for batch_id, (x, orig_size, filename) in enumerate(tqdm(test_dataloader)):
            x = x.to(device, dtype=torch.float)

            for i, model in enumerate(model_list):
                if i==0:
                    y_pred = model(x)
                else:
                    y_pred += model(x)

            y_pred_argmax = y_pred.argmax(1).cpu().numpy().astype(np.uint8)
            orig_size = [(orig_size[0].tolist()[i], orig_size[1].tolist()[i]) for i in range(len(orig_size[0]))]
            # Save predict result
            for filename_, orig_size_, y_pred_ in zip(filename, orig_size, y_pred_argmax):
                resized_img = cv2.resize(y_pred_, [orig_size_[1], orig_size_[0]], interpolation=cv2.INTER_NEAREST)
                cv2.imwrite(os.path.join(pred_result_dir_mask, filename_), resized_img)
    logger.info(f"END PREDICTION")