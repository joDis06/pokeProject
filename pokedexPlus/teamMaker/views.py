from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Team
from .forms import TeamForm

class TeamListView(ListView):
    model = Team

class TeamDetailView(DetailView):
    model = Team

class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Team has been created.'.format(
                team_id=self.object.id
            )
        )

    
        return response
    
    # success_url
    def get_success_url(self):
        return reverse_lazy("teamMaker:teamDetail", args=[self.object.id])