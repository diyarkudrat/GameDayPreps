from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from roster.models import Player
from roster.forms import PlayerForm

class RosterListView(ListView):
    
    model = Player

    def get(self, request):
        players = self.get_queryset()
        return render(request, 'list.html', {
          'players': players
        })

class PlayerCreateView(CreateView):

    model = Player 

    def get(self, request, *args, **kwargs):
        context = {'form': PlayerForm()}
        return render(request, 'new.html', context)

    def post(self, request, *args, **kwargs):
        form = PlayerForm(request.POST)
        if form.is_valid():
            article = form.save()
            return HttpResponseRedirect(reverse_lazy('roster-list-page'))

        return render(request, 'new.html', {'form': form})

class PlayerDetailView(View):
    def get(self, request, *args, **kwargs):
        player = get_object_or_404(Player, pk=kwargs['pk'])
        context = {'player': player }
        return render(request, 'player_detail.html', context)


