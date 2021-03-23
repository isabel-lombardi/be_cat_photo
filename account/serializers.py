from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serialization is the process of transforming data into a format
    that can be stored or transmitted and then reconstructing it.
    """


    class Meta:
        model = User
        # to indicate that all fields in the model should be used
        fields = ["id", "password", "email", "username", "first_name", "last_name"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
