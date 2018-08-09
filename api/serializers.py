from rest_framework.serializers import ModelSerializer

from main.models import Author, Device


class AuthorCreateSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'name',
            'email'
        ]


class AuthorListSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
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
    class Meta:
        model = Device
        fields = [
            'id',
            'name',
            'author'
        ]


class DeviceDetailSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'id',
            'name',
            'author'
        ]
