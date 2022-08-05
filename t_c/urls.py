from django.urls import path
from . import views

urlpatterns = [
    # path('', views.P.as_view()),
    path('create/', views.TCCreateAPIView.as_view(), name='create-terms-and-conditions'),
    path('<int:pk>/', views.GetTCDetailAPIView.as_view(), name='get-terms-and-conditions'),
    path('<int:pk>/delete', views.DeleteTCAPIView.as_view(), name='delete-terms-and-conditions'),
    path('<int:pk>/update/', views.UpdateTCDetailAPIView.as_view(), name='edit-terms-and-conditions')
]
