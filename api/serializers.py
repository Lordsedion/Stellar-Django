from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                         validated_data['email'], 
                                         validated_data['password'])

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})


def generate_id():
    length = 20
    while True:
        id = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase +string.digits, k=length))
        if TextDefault.objects.filter(rec=id).count() == 0:
            break
    return id


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextDefault
        fields = ("name", "text", "speaker")



class CreateTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextDefault
        fields = ("name", "text", "speaker")


class CreateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileDefault
        fields = ("name", "text_file", "speaker",)

