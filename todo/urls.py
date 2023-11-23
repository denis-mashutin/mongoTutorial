from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllToDos.as_view(), name="index"),
    path("today/", views.TodayToDos.as_view(), name="today")
]