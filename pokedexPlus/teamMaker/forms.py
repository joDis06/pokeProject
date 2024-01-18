from django import forms

from .models import Team
from pokedex.models import Pokemon

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['teamPKMN']