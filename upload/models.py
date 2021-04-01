import os
from datetime import datetime
from PIL import Image as pilImg

from django.db import models
from django.contrib.auth.models import User

"""
This function creates a "user-image" folder within "media"
Each user will have a folder with their ID number
Each loaded image will be renamed with the loading time and date
"""


def image_path(instance, filename):
    # to separate filename and extension
    file_name, file_extension = os.path.splitext(filename)

    # get the current date and time
    now = datetime.now()
    time = now.strftime("%d-%m-%Y-%H-%M-%S")

    return 'user-image/{userid}/{time}{ext}'.format(
        userid=instance.user.id, time=time, ext=file_extension)


class Image(models.Model):
    # If blank=True, the field is allowed to be blank
    # if null=True, Django will store empty values as NULL in the database

    # ForeignKey to define a many-to-one relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    #  a FileField with uploads restricted to image formats only
    image = models.ImageField(upload_to=image_path, null=False)   # height_field=300, width_field=300,
    result = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        if self.image:
            super().save()  # saving image first

            img = pilImg.open(self.image.path)  # Open image using self
            if img.height > 300 or img.width > 300:
                new_img = (300, 300)
                img.thumbnail(new_img)
                img.save(self.image.path)  # saving image at the same path
