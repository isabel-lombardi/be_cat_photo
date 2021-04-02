from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Image
from PIL import Image as PilImage


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image       # model to serialize
        fields = ["result", "user", "image"]  # How many fields to display ("__all__")

    def validate_image(self, image_file):
        """
        Check that the image format is Jpeg or Png.
        """
        try:
            img = PilImage.open(image_file)
        except OSError:
            raise ValidationError("Cannot open", image_file)
        print("Image format", img.format)
        if not img.format in ['JPEG', 'PNG']:
            raise ValidationError("Image format is neither Jpeg nor Png")
        return image_file
