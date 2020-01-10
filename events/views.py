from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from events.models import Event
from events.forms import AttendanceForm, EventForm
from roster.models import Player, Attendance

class EventListView(ListView):
    
    model = Event

    def get(self, request):
        events = self.get_queryset()
        event_order = Event.objects.all().order_by('date')
        return render(request, 'events_list.html', {
          'events': events,
          'event_order': event_order
        })

class EventCreateView(CreateView):

    model = Event

    def get(self, request, *args, **kwargs):
        context = {'form': EventForm()}
        return render(request, 'events_new.html', context)

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            article = form.save()
            return HttpResponseRedirect(reverse_lazy('event-list-page'))

        return render(request, 'events_new.html', {'form': form})

class EventDetailView(View):

    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs['pk'])
        members = Player.objects.all()
        context = {'event': event, 'members': members}
        return render(request, 'events_detail.html', context)

class EditEventView(UpdateView):

    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs['pk'])
        players = Player.objects.all()
        status = Attendance.objects.filter(player__in=players, event=event)
        context = {'event': event, 'status': status, 'players': players}
        return render(request, 'events_edit.html', context)

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid:
            attendance = form.save()
            return HttpResponseRedirect(reverse_lazy('event-list-page'))
        
        return render(request, 'events_edit.html', {'form': form})
        

class EventDeleteView(DeleteView):

    model = Event
    template_name = 'events_delete.html'
    success_url = reverse_lazy('event-list-page')

class EventAttendanceView(ListView):
    model = Event

    def get(self, request):
        events = self.get_queryset()
        return render(request, 'attendance_list.html', {
          'events': events
        })

class AttendanceView(View):

    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs['pk'])
        members = Player.objects.all()
        context = {'event': event, 'members': members}
        return render(request, 'events_detail.html', context)


