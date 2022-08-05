from rest_framework import generics, permissions, status

# Create your views here.
from .models import User
from .serializers import (GetUserSerializer, GetUserDocumentsSerializer,
                          RegisterUserSerializer, ChangePasswordSerializer, SendMailSerializer)
from .permissions import IsUser


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        print(user.subscribed_to_newsletter)
        if user.subscribed_to_newsletter:
            user.send_newspaper_mail()


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

    def perform_update(self, serializer):
        user = serializer.save()
        if user.subscribed_to_newsletter:
            user.send_newspaper_mail()


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
