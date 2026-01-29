
from django.urls import path
from .import views

urlpatterns = [
    path("booking/",views.getData,name="book"),
    path("booking/<int:id>/",views.deleteData,name="deleteInfo"),
    # path("update/<int:id>/", views.updateData, name="dataUpdate"),

]