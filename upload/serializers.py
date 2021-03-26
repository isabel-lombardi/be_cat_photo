from rest_framework.serializers import ModelSerializer
from .models import Image


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image       # model to serialize
        fields = ["result", "user", "image"]  # How many fields to display ("__all__")







