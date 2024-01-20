from django import forms

from .models import Team
from django.core.validators import MaxValueValidator
from pokedex.models import Pokemon

#validators

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['teamPKMN']
        
    teamPKMN = forms.ModelMultipleChoiceField(
        queryset=Pokemon.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def clean_teamPKMN(self):
        selected_pokemon = self.cleaned_data.get('teamPKMN')
        max_choices = 6

        if len(selected_pokemon) > max_choices:
            raise forms.ValidationError(f'You can only select up to {max_choices} Pokemon.')

        return selected_pokemon