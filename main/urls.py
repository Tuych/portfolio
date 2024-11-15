from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio-detail/<str:pk>/', views.portfolio_detail, name='portfolio-detail'),
    path('success/', views.success, name='success'),

]
