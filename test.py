import torch
import os
import torch.nn as nn
import numpy as np
from torch import optim
from torch.autograd import Variable
from torch.utils.data import DataLoader  
import torchvision.datasets
import torchvision.transforms
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#transform picture to appropriate form
batch_size = 270
transfrom = torchvision.transforms.Compose([torchvision.transforms.ToTensor(), torchvision.transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])
train_dataset = torchvision.datasets.ImageFolder('./split_picture/train', transform=transfrom)
train_loader = torch.utils.data.DataLoader(dataset = train_dataset, batch_size = batch_size)

test_dataset = torchvision.datasets.ImageFolder('./split_picture/test', transform=transfrom)
test_loader = torch.utils.data.DataLoader(dataset = test_dataset, batch_size = batch_size)

print(train_loader)

for idx, (images, labels) in enumerate(train_loader): #train data
    print(idx)
    # print(images.shape())
    print(labels.size())