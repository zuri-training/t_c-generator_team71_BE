from rest_framework import generics, permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
from .models import User
from .serializers import (GetUserSerializer, GetUserDocumentsSerializer,
                          RegisterUserSerializer, ChangePasswordSerializer, SendMailSerializer,
                          MyTokenObtainPairSerializer)
from .permissions import IsUser


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer




class GetUserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsUser]


class DocumentsListAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserDocumentsSerializer
    permission_classes = [permissions.IsAuthenticated, IsUser]


class UpdateUserDetailAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsUser]


class DeleteUserAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsUser]




class ChangePasswordAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsUser]


class SendNewsLetterAPIView(generics.CreateAPIView):
    serializer_class = SendMailSerializer

class MyTokenObtainPairView(generics.CreateAPIView):
    serializer_class = MyTokenObtainPairSerializer
