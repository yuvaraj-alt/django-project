from django.urls import path
from .import views
urlpatterns = [
   path("page/",views.PageView.as_view(),name = 'pages'),
   path("paged/",views.PageNumView.as_view(),name = "pagePath")
]