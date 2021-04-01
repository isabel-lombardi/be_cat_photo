from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .serializers import ImageSerializer


from upload.classification.classification import Classification


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
            obj = serializer.save(user=request.user)

            # list with all the images present in the request
            images = [f for f in files]

            # check len list
            if len(images) > 10:
                return Response("No more than 10 images allowed", status=status.HTTP_400_BAD_REQUEST)

            # return classification result
            classification = Classification(images)
            classification_result = classification.use_template()

            serializer.save(user=request.user, result=classification_result)


            return Response(classification_result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
