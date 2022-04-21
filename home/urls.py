from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('hos/signup', views.hos_signup, name='hos_signup'),
    path('hos/login', views.hos_login, name='hos_login'),
    path('don/signup', views.don_signup, name='don_signup'),
    path('don/login', views.don_login, name='don_login'),



]
