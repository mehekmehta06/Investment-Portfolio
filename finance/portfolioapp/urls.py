from django.urls import path, include
from .views import *
from . import views

urlpatterns= [
    path('userprofile/',UserProfileAPIView.as_view(),name='user'),
    path('user/<int:pk>/',UserProfileDetailAPIView.as_view(),name='user-delete/put/get'),
    path('user/<str:username>/', UserProfileDetailAPIView.as_view(), name='user-profile-detail'),
    path('portfolio/',PortfolioAPIView .as_view(), name='portfolio-get/post'),
    path('portfolio/<int:pk>/', PortfolioAPIView.as_view(), name='portfolio-delete/put'),
    path('current/', CurrentMarketAPIView.as_view(), name='current-get/post'),
    path('resource/', ResourceAPIView.as_view(), name='resource'),
    path('investments/', InvestmentAPIView.as_view(), name='investment-list'),
    path('investments/<int:pk>/', InvestmentAPIView.as_view(), name='investment-detail'),
    path('investments/<str:Fname>/', InvestmentAPIView.as_view(), name='investment-detail'),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('payment/<str:username>/',views.payment,name='payment'),
    path('success/<str:username>/',views.success,name='success_payment'),
    ]



