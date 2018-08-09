from django.conf.urls import url
from django.urls import include

url(r'^api-auth/', include('rest_framework.urls'))
