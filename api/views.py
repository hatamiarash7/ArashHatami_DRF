from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import (
    IsAuthenticated
)

from api.permissions import IsOwnerOrReadOnly
from api.serializers import (
    AuthorListSerializer,
    AuthorDetailSerializer,
    AuthorCreateSerializer,
    DeviceListSerializer,
    DeviceDetailSerializer,
    DeviceCreateSerializer
)
from main.models import Author, Device


class Authors(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class AuthorCreate(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):


class AuthorDetail(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    lookup_field = 'id'


class AuthorDelete(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class AuthorEdit(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class Devices(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceListSerializer


class DeviceCreate(CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceCreateSerializer
    permission_classes = [IsAuthenticated]


class DeviceDetail(RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceDetailSerializer
    lookup_field = 'id'


class DeviceDelete(DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class DeviceEdit(RetrieveUpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
