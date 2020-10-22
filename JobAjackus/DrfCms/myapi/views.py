from django.shortcuts import render
from rest_framework import viewsets
from myapi.models import customuser,content
from myapi.serializers import UserSerializer, contentSerializer
from rest_framework import generics,status
from rest_framework.response import Response

from rest_framework.permissions import AllowAny
from myapi.permissions import IsLoggedInUserOrAdmin, IsAdminUser

#from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = customuser.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ContentViewSet(viewsets.ModelViewSet):
    queryset = content.objects.all()
    serializer_class = contentSerializer
    
    def get_queryset(self): 
        user = self.request.user
        if content.creater == customuser.pk :
            return content.objects.filter(creater=customuser.pk)
        else:
            return content.objects.all
    
        
