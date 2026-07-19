from django.urls import path
from .views import *

urlpatterns = [
    path("users/", UsersListView),
    path("users/<int:pk>/", UsersDetailView),
    path("users/create/", UsersCreateView),
    path("users/update/<int:pk>/", UsersUpdateView),
    path("users/delete/<int:pk>/", UsersDeleteView),
]