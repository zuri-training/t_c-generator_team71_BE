# from django.shortcuts import render
from rest_framework import generics, permissions
# from datetime import datetime
from django.utils import timezone

# Create your views here.
from .models import Terms
from .serializers import GetTCSerializer
from users.permissions import IsOwner


class TCCreateAPIView(generics.CreateAPIView):
    queryset = Terms.objects.all()
    serializer_class = GetTCSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user_id=self.request.user, create_date=timezone.datetime.now(), last_edit=timezone.datetime.now())


class GetTCDetailAPIView(generics.RetrieveAPIView):
    queryset = Terms.objects.all()
    serializer_class = GetTCSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class UpdateTCDetailAPIView(generics.UpdateAPIView):
    queryset = Terms.objects.all()
    serializer_class = GetTCSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save(last_edit=timezone.datetime.now(), user_id=self.request.user)


class DeleteTCAPIView(generics.DestroyAPIView):
    queryset = Terms.objects.all()
    serializer_class = GetTCSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsOwner]
