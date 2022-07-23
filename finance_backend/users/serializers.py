from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



from users.models import User

class UserRegistraionSerializer(serializers.ModelSerializer):
    PASSWORD_MIN_LENGTH = 6
    email = serializers.EmailField(max_length=250, min_length=6)
    username = serializers.CharField(max_length=250, min_length=3)
    password = serializers.CharField(max_length=250, min_length=PASSWORD_MIN_LENGTH, style={'input_type': 'password'}, write_only=True)


    def validate(self, attrs):
        username = attrs.get("username","")
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        user = User(**attrs)

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError
            ({"username_exists","An account with that username already exists"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email_exists":"An account with that email already exists"}
            )

        # if len(password) < self.PASSWORD_MIN_LENGTH:
        #     raise serializers.ValidationError(
        #         {"password": f"The new password must be at least ${self.PASSWORD_MIN_LENGTH} characters long"}
        #     )

        # password validation

        errors = dict()

        try:
             # validate the password and catch the exception
             validators.validate_password(password=password, user=user)

         # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
             errors['password'] = list(e.messages)

        if errors:
             raise serializers.ValidationError(errors)

        return super(UserRegistraionSerializer, self).validate(attrs)


    class Meta:
            model = User
            fields = ['first_name', 'last_name', 'username', 'email', 'password']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token
