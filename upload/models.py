import os
from datetime import datetime

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