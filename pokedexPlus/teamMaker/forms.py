from django import forms

from .models import Team
from pokedex.models import Pokemon

#validators

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['teamPKMN']
        
    teamPKMN = forms.ModelMultipleChoiceField(
        queryset=Pokemon.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )