from .models import Users
from rest_framework.serializers import ModelSerializer

class UsersSerializers(ModelSerializer):
    class Meta :
        model = Users
        fields = ["name", "surename", "age", "create_at"]
        read_only_fields = ["create_at"]