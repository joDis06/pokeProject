from django.urls import path

from . import views

app_name = "teamStats"

urlpatterns = [
   path("", views.teamStatsView, name="teamStats"),
   
]