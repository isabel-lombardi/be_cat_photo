import os

from torchvision import models, transforms
import torch

# imagenet_classes file
imagenet_classes_file_path = os.path.join("classification", "imagenet_classes.txt")
file_abs_path = os.path.abspath(os.path.dirname(__file__))
imagenet_classes_file_path = os.path.join(file_abs_path, 'imagenet_classes.txt')


class Classification:

    def __init__(self, images):
        self.images = images

        # pre-trained model
        self.resnet = models.resnet50(pretrained=True)