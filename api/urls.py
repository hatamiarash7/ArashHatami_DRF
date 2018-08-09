from django.conf.urls import url

from api.views import (
    Authors,
    AuthorDetail,
    AuthorDelete,
    AuthorEdit,
    AuthorCreate,
    Devices,
    DeviceDetail,
    DeviceDelete,
    DeviceEdit,
    DeviceCreate
)

urlpatterns = [
    url(r'^authors/$', Authors.as_view(), name='authors_index'),
    url(r'^authors/create/$', AuthorCreate.as_view(), name='authors_create'),
    url(r'^authors/(?P<id>\d+)/$', AuthorDetail.as_view(), name='authors_detail'),
    url(r'^authors/(?P<id>\d+)/edit/$', AuthorEdit.as_view(), name='authors_edit'),
    url(r'^authors/(?P<id>\d+)/delete/$', AuthorDelete.as_view(), name='authors_delete'),

    url(r'^devices/$', Devices.as_view(), name='devices_index'),
    url(r'^devices/create/$', DeviceCreate.as_view(), name='devices_create'),
    url(r'^devices/(?P<id>\d+)/$', DeviceDetail.as_view(), name='devices_detail'),
    url(r'^devices/(?P<id>\d+)/edit/$', DeviceEdit.as_view(), name='devices_edit'),
    url(r'^devices/(?P<id>\d+)/delete/$', DeviceDelete.as_view(), name='devices_delete')
]
