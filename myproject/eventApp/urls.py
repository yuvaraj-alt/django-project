from django.urls import path
from .import views

urlpatterns = [
   path("events/",views.eventView,name = "event"),
   path("addEvents",views.eventAdd,name = "evnt" ),
   path("updateEvent/<int:id>/",views.eventUPdte, name = "uptevnt"),
   path("deleteEvent/<int:id>",views.eventDelete,name = "dltevent"),
]