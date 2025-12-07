from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TestUser
from .serializers import TestUserSerializer
from django.contrib.auth import authenticate


@api_view(['POST'])
def create_test_user(request):
    serializer = TestUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def list_test_users(request):
    users = TestUser.objects.all().order_by('-created_at')  # newest first
    serializer = TestUserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def admin_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user and user.is_superuser:
        return Response({"success": True})
    return Response({"success": False}, status=400)