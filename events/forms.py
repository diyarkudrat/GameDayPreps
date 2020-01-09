from django import forms
from events.models import Event
from roster.models import Player, Attendance

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('event_type', 'location', 'time', 'description', )

class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Event 
        fields = ('time', 'event_type', 'members' )

