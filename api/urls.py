from django.conf.urls import url

from api.views import AuthorList

urlpatterns = [
    url(r'^authors/$', AuthorList.as_view(), name='authors_index'),
]
