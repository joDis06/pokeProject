import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Pokemon, Types

# Create your views here.

def getApiData(pokemon):
    pokeListUrl = 'https://pokeapi.co/api/v2/pokemon/'
    pokeListResponse = requests.get(pokeListUrl)
    pokeListData = pokeListResponse.json()
    print(pokeListData.get("results"))
    for i in pokeListData.get("results"):
        pokeStatsUrl = 'https://pokeapi.co/api/v2/pokemon/'+i.get("name")
        pokeStatsResponse = requests.get(pokeStatsUrl)
        pokeStatsData = pokeStatsResponse.json()
        pokeStats = pokeStatsData.get('stats')
        pokeInstance = Pokemon.objects.create(
                                               name=pokeStatsData.get('name'), 
                                               generation = 1,
                                               hp=pokeStats[0].get('base_stat'), 
                                               atk=pokeStats[1].get('base_stat'),
                                               dfn=pokeStats[2].get('base_stat'),
                                               spatk=pokeStats[3].get('base_stat'),
                                               spdef=pokeStats[4].get('base_stat'),
                                               spd=pokeStats[5].get('base_stat'),
                                             )
    return JsonResponse(pokeListData)

def pokedexView(request):
    print("Hey!")
    getApiData('ditto')
    return render(request, 'pokedex/pokedex.html')

