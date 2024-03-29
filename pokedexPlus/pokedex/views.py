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

def populatePokemon():
    pokeListUrl = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1302'
    if(Pokemon.objects.all().count() == 0):
        pokeListResponse = requests.get(pokeListUrl)
        pokeListData = pokeListResponse.json()
        # print(pokeListData.get("results"))
        counter=0
        for i in pokeListData.get("results"):
            counter+= 1
            pokeStatsUrl = i.get('url')
            #print(pokeStatsUrl)
            pokeStatsResponse = requests.get(pokeStatsUrl)
            pokeStatsData = pokeStatsResponse.json()
            #print(pokeStatsData)
            pokeStats = pokeStatsData.get('stats')
            #print(pokeStats)
            pokeInstance = Pokemon.objects.create(
                                                   id=counter,
                                                   name=pokeStatsData.get('name'), 
                                                   hp=pokeStats[0].get('base_stat'), 
                                                   atk=pokeStats[1].get('base_stat'),
                                                   dfn=pokeStats[2].get('base_stat'),
                                                   spatk=pokeStats[3].get('base_stat'),
                                                   spdef=pokeStats[4].get('base_stat'),
                                                   spd=pokeStats[5].get('base_stat'),
                                                   image=pokeStatsData['sprites']['other']['home']['front_default']
                                                   
                                                   
                                                
                                                 )
            print(pokeInstance.image)
            for i in pokeStatsData.get('types'):
                pokeType = Types.objects.filter(name__iexact = i.get("type").get("name"))
                pokeInstance.types.add(pokeType[0])
            pokeInstance.save()
            print(pokeInstance.name)
        return JsonResponse(pokeListData)

def populateTypes():
    pokeTypeUrl = 'https://pokeapi.co/api/v2/type'
    if (Types.objects.all().count() == 0):
        pokeTypeResponse = requests.get(pokeTypeUrl)
        pokeTypeData = pokeTypeResponse.json()
        counter = 0
        for i in pokeTypeData.get('results'):
            counter += 1
            pokeInstance = Types.objects.create(id=counter, name=i.get('name'))
            pokeInstance.save()
            print(pokeInstance.name)
            
            
               
def pokedexView(request):
    # if not Types.objects.all():
    populateTypes()
    # if not Pokemon.objects.all():
    populatePokemon()
    
    pokemon = Pokemon.objects.all()

    # put the context in the return as data for all pokemon
    # so we are able to retrieve it on the other end in
    # the template and make a for loop / automated list
    # of the info

    return render(request, 'pokedex/pokedex.html', context={"pokemon": pokemon})
