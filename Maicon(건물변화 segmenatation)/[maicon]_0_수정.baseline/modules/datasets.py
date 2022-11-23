"""Datasets
"""

from torch.utils.data import Dataset
import numpy as np
import cv2
import os
from albumentations import *

#-----------------------------------------
# tfms
def get_aug():
    return Compose([

        VerticalFlip(p=0.5),
        Blur(p=0.5),
        MedianBlur(p=0.5),
        RandomGamma(gamma_limit=(40,160), p=0.5),
        RandomContrast(p=0.5),
        Sharpen(p=0.5),
        #RGBShift(p=1.0),
        #HueSaturationValue(p=1.0),
        CLAHE(p=0.5),
        RandomBrightnessContrast(p=0.5)

    ])




class SegDataset(Dataset):
    """Dataset for image segmentation

    Attributs:
        x_dirs(list): 이미지 경로
        y_dirs(list): 마스크 이미지 경로
        input_size(list, tuple): 이미지 크기(width, height)
        scaler(obj): 이미지 스케일러 함수
        logger(obj): 로거 객체
        verbose(bool): 세부 로깅 여부
    """
    def __init__(self, paths, input_size, scaler, mode='train', logger=None, verbose=False, tfms=get_aug()):

        self.x_paths = paths
        #---------------------------------------------------------------------
        # Eric x=>x_3
        self.y_paths = list(map(lambda x : x.replace('x', 'y'),self.x_paths))
        self.input_size = input_size
        self.scaler = scaler
        self.logger = logger
        self.verbose = verbose
        self.mode = mode
        #
        self.tfms = tfms


    def __len__(self):
        return len(self.x_paths)

    def __getitem__(self, id_: int):

        filename = os.path.basename(self.x_paths[id_]) # Get filename for logging
        x = cv2.imread(self.x_paths[id_], cv2.IMREAD_COLOR)
        orig_size = x.shape
        x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)

        x = cv2.resize(x, self.input_size)
        x = self.scaler(x)
        x = np.transpose(x, (2, 0, 1))


        if self.mode in ['train']:
            # x ---------------------------------
            filename = os.path.basename(self.x_paths[id_]) # Get filename for logging
            x = cv2.imread(self.x_paths[id_], cv2.IMREAD_COLOR)
            orig_size = x.shape
            x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)

            # y ---------------------------------
            y = cv2.imread(self.y_paths[id_], cv2.IMREAD_GRAYSCALE)

            # transfomr--------------------------
            if self.tfms is not None:
                augmented = self.tfms(image=x,mask=y)
                x,y = augmented['image'],augmented['mask']
            # resize ----------------------------
            x = cv2.resize(x, self.input_size)
            x = self.scaler(x)
            x = np.transpose(x, (2, 0, 1))
            y = cv2.resize(y, self.input_size, interpolation=cv2.INTER_NEAREST)
            # ------------------------------------

            return x,y,filename


        if self.mode in ['valid']:

            y = cv2.imread(self.y_paths[id_], cv2.IMREAD_GRAYSCALE)
            y = cv2.resize(y, self.input_size, interpolation=cv2.INTER_NEAREST)

            return x, y, filename

        elif self.mode in ['test']:
            return x, orig_size, filename

        else:
            assert False, f"Invalid mode : {self.mode}"