from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
   path("", views.pokedexView, name="pokedex"),
   path("detail", views.pokeDetailView, name="pokedex"),
   
]