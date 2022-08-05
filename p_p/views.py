# from django.shortcuts import render
from rest_framework import generics, permissions
# from datetime import datetime
from django.utils import timezone

# Create your views here.
from .models import PrivacyPolicy
from .serializers import GetPrivacyPolicySerializer
from users.permissions import IsOwner


class PPCreateAPIView(generics.CreateAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = GetPrivacyPolicySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.user)
        if serializer.is_valid():
            serializer.save(user_id=self.request.user, create_date=timezone.datetime.now(), last_edit=timezone.datetime.now())


class GetPPDetailAPIView(generics.RetrieveAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = GetPrivacyPolicySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class UpdatePPDetailAPIView(generics.UpdateAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = GetPrivacyPolicySerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save(last_edit=timezone.datetime.now(), user_id=self.request.user)


class DeletePPAPIView(generics.DestroyAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = GetPrivacyPolicySerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsOwner]
