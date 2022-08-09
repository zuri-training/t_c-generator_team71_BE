from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'),
    path('register/', views.UserCreateAPIView.as_view(), name='create-user'),
    path('<int:pk>/documents/', views.DocumentsListAPIView.as_view(), name='documents-list'),
    path('<int:pk>/', views.GetUserDetailAPIView.as_view(), name='user-detail'),
    path('<int:pk>/update-profile/', views.UpdateUserDetailAPIView.as_view(), name='update-profile'),
    path('<int:pk>/delete-profile/', views.DeleteUserAPIView.as_view(), name='delete-profile'),
    path('<int:pk>/change-password/', views.ChangePasswordAPIView.as_view(), name='change-password'),
    path('newsletter/', views.SendNewsLetterAPIView.as_view(), name='send-newsletter'),
    path('obtain-token/', views.MyTokenObtainPairView.as_view(), name='my-obtain-token'),
]
