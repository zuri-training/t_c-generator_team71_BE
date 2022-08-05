from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.PPCreateAPIView.as_view(), name='create-policy'),
    path('<int:pk>/', views.GetPPDetailAPIView.as_view(), name='get-policy'),
    path('<int:pk>/delete', views.DeletePPAPIView.as_view(), name='delete-policy'),
    path('<int:pk>/update/', views.UpdatePPDetailAPIView.as_view(), name='edit-policy')
]
