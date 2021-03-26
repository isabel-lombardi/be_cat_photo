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

    # Transform the input image with values similar to those used during model training
    @staticmethod
    def transform_input_images(image):
        transform = transforms.Compose([
            transforms.Resize(256),      # Resize to 256×256 pixels
            transforms.CenterCrop(224),  # Crop to 224×224 pixels about the center
            transforms.ToTensor(),       # Convert to PyTorch Tensor data type

            # Normalize with mean and standard deviation
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
        return transform(image)