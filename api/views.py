from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter)
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from api.permissions import IsOwnerOrReadOnly
from api.serializers import (
    AuthorListSerializer,
    AuthorDetailSerializer,
    AuthorCreateSerializer,

    DeviceListSerializer,
    DeviceDetailSerializer,
    DeviceCreateSerializer,

    UserCreateSerializer,
    UserLoginSerializer
)
from main.models import Author, Device

User = get_user_model()


class UserCreate(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLogin(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Authors(ListAPIView):
    serializer_class = AuthorListSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # DRF filter = http://localhost:8000/api/authors/?search=ar&ordering=id
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']

    # builtin django filter
    def get_queryset(self, *args, **kwargs):
        queryset_list = Author.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
            ).distinct()
        return queryset_list


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
