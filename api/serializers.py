from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    EmailField,
    CharField
)

from main.models import Author, Device

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'email2',
            'password'
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        if email1 != value:
            raise ValidationError("Email must match")
        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        if email1 != value:
            raise ValidationError("Email must match")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user_obj = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data.get("password")
        if not email and not username:
            raise ValidationError("A username or email is required to login")

        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exlude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password. Please try again")

        data["token"] = "Some Token"
        return data


class AuthorCreateSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'name',
            'email'
        ]


class AuthorListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api:authors_detail',
        lookup_field='id'
    )

    class Meta:
        model = Author
        fields = [
            'url',
            'id',
            'name'
        ]


class AuthorDetailSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'email'
        ]


class DeviceCreateSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'author',
            'name',
        ]


class DeviceListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api:devices_detail',
        lookup_field='id'
    )

    author = SerializerMethodField()

    class Meta:
        model = Device
        fields = [
            'url',
            'id',
            'name',
            'author'
        ]

    def get_author(self, obj):
        return obj.author.name


class DeviceDetailSerializer(ModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Device
        fields = [
            'id',
            'name',
            'author'
        ]

    def get_author(self, obj):
        return obj.author.name
