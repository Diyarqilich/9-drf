from django.urls import path
from .views import UsersViewSet

urlpatterns = [
    path("",view=UsersViewSet.as_view({"post":"create"}))
]