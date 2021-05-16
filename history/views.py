from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from upload.models import Image
from upload.serializers import ImageSerializer


class ImageList(generics.ListAPIView):
    # from https://www.django-rest-framework.org/api-guide/filtering/

    # Specify what authentication to use
    authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    permission_classes = [IsAuthenticated]

    serializer_class = ImageSerializer

    def get_queryset(self):
        """
        This view should return a list of all the images
        for the currently authenticated user.
        """
        user = self.request.user
        return Image.objects.filter(user=user)
