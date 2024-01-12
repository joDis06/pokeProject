from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Pokemon, Types, Stats

# Create your views here.

def pokedexView(request):
    print("Hey!")
    
    return render(request, 'pokedex/pokedex.html')

