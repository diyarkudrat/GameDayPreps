from django.urls import path
from roster.views import RosterListView, PlayerCreateView, PlayerDetailView

urlpatterns = [
    path('', RosterListView.as_view(), name='roster-list-page'),
    path('new/', PlayerCreateView.as_view(), name='player-create-page'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player-detail-page')
]