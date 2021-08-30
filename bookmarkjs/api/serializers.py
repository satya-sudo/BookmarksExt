from rest_framework import serializers

from .models import User



class UserRegisterSerializer( serializers.ModelSerializer):
    
    password = serializers.CharField(required=True)
    password1 =  serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "password1",
        ]
        extra_kwargs = {
            'password': {'write_only':True},
            'password1': {'write_only':True},
        }

    def create(self,validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        password1 = validated_data["password1"]
        if password == password1:
            user = User(email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({"password":"passwords do not match"})
