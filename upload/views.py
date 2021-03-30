from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .serializers import ImageSerializer
from PIL import Image
import os
from django.conf import settings

from upload.classification.classification import Classification


def image_resize(file_path_rel):
    file_path_rel = os.path.normpath(file_path_rel)
    # removes any initial slash
    if file_path_rel[0] != os.sep:
        file_path_rel = file_path_rel[1:]
    file_path_abs = os.path.join(os.path.normpath(settings.BASE_DIR), file_path_rel)
    # print("file_path_abs ", file_path_abs)

    file_name, file_extension = os.path.splitext(file_path_abs)
    file_path_thumb_abs = os.path.join(file_name + '_thumbnail' + file_extension)
    # print("file_path_thumb_abs:", file_path_thumb_abs)
    try:
        image = Image.open(file_path_abs)
        image.thumbnail((400, 400))
        image.save(file_path_thumb_abs)
        return True
    except OSError:
        print('cannot open', file_path_abs)
        return False


class UploadAPIView(APIView):
    # Specify what authentication to use
    authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    permission_classes = [IsAuthenticated]

    # Parses multipart HTML form content, which supports file uploads
    parser_classes = (MultiPartParser, )

    def post(self, request, *args, **kwargs):
        # serializer
        serializer = ImageSerializer(data=request.data)  # handle incoming json requests

        # request.FILES is a MultiValueDict
        files = request.FILES.getlist("image")   # .getlist("") to get multiple files

        # validate the input data and confirm that all required fields are correct
        if serializer.is_valid():

            # to do custom processing on the object before saving it
            obj = serializer.save()

            # list with all the images present in the request
            images = [f for f in files]

            # check len list
            if len(images) > 10:
                return Response("No more than 10 images allowed", status=status.HTTP_400_BAD_REQUEST)

            # return classification result
            classification = Classification(images)
            obj.result = classification.use_template()

            serializer.save()

            if not image_resize(serializer.data['image']):
                return Response(serializer.errors, status=status.HTTP_507_INSUFFICIENT_STORAGE)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
