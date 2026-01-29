from django.urls import path
from .import views

urlpatterns = [
    path("signup/",views.signup,name='log account'),
    path("login/",views.login,name='log'),

]