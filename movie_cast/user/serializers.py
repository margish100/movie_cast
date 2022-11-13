from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "confirm_password",
            "created",
            "modified",
        ]

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        password = validated_data.pop("password")
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()

        return user

    def validate(self, attrs):
        password = attrs["password"]
        confirm_password = attrs["confirm_password"]
        if password != confirm_password:
            raise serializers.ValidationError(
                {"password": ["password and confirm_password must be same"]}
            )
        return super(UserSerializer, self).validate(attrs)


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
