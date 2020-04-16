from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from applications.views import ApplicationViewSet


application_list = ApplicationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

application_detail = ApplicationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

application_test = ApplicationViewSet.as_view({
    'get': 'test'
})

application_change_key = ApplicationViewSet.as_view({
    'patch': 'change_key'
})

urlpatterns = format_suffix_patterns([
    path("admin/", admin.site.urls),
    path('api/', application_list, name='application-list'),
    path('api/<int:pk>/', application_detail, name='application-detail'),
    path('api/<int:pk>/change_key', application_change_key, name='application-change-key'),
    path('api/test', application_test, name='application-test'),
])
