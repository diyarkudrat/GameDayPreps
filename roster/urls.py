from django.urls import path
from roster.views import RosterListView, PlayerCreateView

urlpatterns = [
    path('', RosterListView.as_view(), name='roster-list-page'),
    path('new/', PlayerCreateView.as_view(), name='player-create-page'),
]