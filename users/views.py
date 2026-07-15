from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UsersSerializers
# Create your views here.

class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers