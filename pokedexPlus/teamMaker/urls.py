from django.urls import path

from . import views

app_name = "teamMaker"

urlpatterns = [
    path("", views.TeamListView.as_view(), name="teamList"),
    path("new", views.TeamCreateView.as_view(), name="teamCreate"),
    path("<int:pk>", views.TeamDetailView.as_view(),
         name="teamDetail"),
]
