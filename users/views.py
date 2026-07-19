from .models import Users
from .serializers import UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def UsersListView(request):
    serializer = UsersSerializer(Users.objects.all(), many=True)
    return Response(serializer.data)


@api_view(["GET"])
def UsersDetailView(request, pk):
    serializer = UsersSerializer(Users.objects.get(pk=pk))
    return Response(serializer.data)


@api_view(["POST"])
def UsersCreateView(request):
    serializer = UsersSerializer(data=request.data)
    serializer.is_valid()
    serializer.save()
    return Response(serializer.data)


@api_view(["PUT", "PATCH"])
def UsersUpdateView(request, pk):
    user = Users.objects.get(pk=pk)

    if request.method == "PUT":
        serializer = UsersSerializer(user, data=request.data)

    if request.method == "PATCH":
        serializer = UsersSerializer(user, data=request.data, partial=True)

    serializer.is_valid()
    serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def UsersDeleteView(request, pk):
    user = Users.objects.get(pk=pk)
    user.delete()
    return Response({"message": "Deleted"})