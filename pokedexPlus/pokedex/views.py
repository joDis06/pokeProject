from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Pokemon, Types

import requests, json

# Create your views here.

def getApiData(pokemon):
    pokeListUrl = 'https://pokeapi.co/api/v2/pokemon/'
    pokeListResponse = requests.get(pokeListUrl)
    pokeListData = pokeListResponse.json()
    # print(pokeListData.get("results"))
    for i in pokeListData.get("results"):
        pokeStatsUrl = i.get('url')
        #print(pokeStatsUrl)
        pokeStatsResponse = requests.get(pokeStatsUrl)
        pokeStatsData = pokeStatsResponse.json()
        #print(pokeStatsData)
        pokeStats = pokeStatsData.get('stats')
        #print(pokeStats)
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
    getApiData('bulbasaur')

    # put the context in the return as data for all pokemon
    # so we are able to retrieve it on the other end in
    # the template and make a for loop / automated list
    # of the info

    return render(request, 'pokedex/pokedex.html')


# make detail view

def pokeDetailView(request):
    print("Hi!")

    # have a button on pokedexview template that gives the id for the pokemon,
    # then get data with https://pokeapi.co/api/v2/pokemon/[ID]
    # put data into table thru context

    return render(request, 'pokedex/pokeDetail.html')