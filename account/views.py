from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import status  # for send status
from rest_framework.views import APIView  # class view


class SignupAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)  # get data from request

        if serializer.is_valid():  # check if serializer is valid

            serializer.save()

            return Response('Correctly registered', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):

    def get(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
