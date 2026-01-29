from django.urls import path
from .import ApiViews


urlpatterns = [
    path("ticket/",ApiViews.ticketApi.as_view()),
    path("ticket/<int:pk>/",ApiViews.ticketApiCon.as_view()),
]