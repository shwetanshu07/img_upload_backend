from django.urls import path
from . import views

urlpatterns = [
    path('images/', views.ImageListView.as_view(), name='images'),
    path('images/<int:pk>/', views.ImageDetailView.as_view(), name='image_detail'),
    path('images/create/', views.ImageCreateView.as_view(), name='image_create'),
    path('images/delete/<int:pk>/', views.ImageDeleteView.as_view(), name='image_delete'),
    path('register_user/', views.RegisterView.as_view(), name='register_user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]