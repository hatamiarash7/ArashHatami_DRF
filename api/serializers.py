from rest_framework.serializers import ModelSerializer

from main.models import Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'email'
        ]
