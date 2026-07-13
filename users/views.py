from django.shortcuts import render
from rest_framework import viewsets
from .models import Users
from .serializers import UsersSerializers
# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers