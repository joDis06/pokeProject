from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core import serializers


from pokedex.models import Pokemon, Types
from teamMaker.models import Team

import requests, json
# Create your views here.

def teamStatsView(request):
    pokemon = Pokemon.objects.all()
    teams = Team.objects.all()
    teamsJSON = serializers.serialize("json", Team.objects.all())
    pkmnJSON = serializers.serialize("json", Pokemon.objects.all())

    return render(request, 'teamStats/teamStats.html', context={"pokemon": pokemon,
                                                                "teams" : teams,
                                                                "teamsJSON" : teamsJSON,
                                                                "pkmnJSON": pkmnJSON})