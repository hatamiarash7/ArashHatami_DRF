from rest_framework.generics import ListAPIView

from main.models import Author
from api.serializers import AuthorSerializer


class AuthorList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
