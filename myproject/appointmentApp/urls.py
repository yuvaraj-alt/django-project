from django.urls import path
from .import views

urlpatterns = [
    path("appoint/",views.appointView,name = "appointMent"),
    path("addAppointment/",views.addAppoint,name = "addNew" ),
    path("dlt/<int:id>/",views.deleteView,name = "dlete"),
    path("updateStock/<int:id>/", views.UpdateView, name="upt")

]