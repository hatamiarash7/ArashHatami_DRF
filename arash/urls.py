from django.conf.urls import url
from django.urls import include, path

from . import views

url(r'^api-auth/', include('rest_framework.urls'))

urlpatterns = [
    path('', views.index, name='index'),
]
