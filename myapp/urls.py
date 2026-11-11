from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('timer/', views.timer_page, name='timer'),
]
