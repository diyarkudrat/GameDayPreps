from django import forms
from roster.models import Player 

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player 
        fields = ('first_name', 'last_name', 'position', 'grade', 'jersey_number')