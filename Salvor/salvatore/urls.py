from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('sing-up/', views.SignUp, name="sing-up"),
    path('sing-in/', views.SignIn, name="sing-in"),
    path('logout/', views.logout_request, name='logout'),
    path('classes/', views.classes, name="classes"),
    path('quetion-test/', views.question, name="quetion-test")
]
