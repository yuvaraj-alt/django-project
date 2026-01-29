from tkinter.font import names

from django.urls import path
from .import views


urlpatterns = [
    path('students/',views.studentApiView.as_view(),name='students'),
    path('students/<int:pk>/',views.studentSuperView.as_view(),name='studentView')
]