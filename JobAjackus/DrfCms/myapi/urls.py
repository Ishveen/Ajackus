from django.urls import path

from django.conf.urls import url, include
from rest_framework import routers
from myapi.views import UserViewSet, ContentViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),  
    url(r'^auth/', include('rest_auth.urls')),
]