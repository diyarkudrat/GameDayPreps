from django.urls import path
from roster.views import RosterListView, PlayerCreateView, PlayerDetailView, PlayerDeleteView, EditPlayerView

urlpatterns = [
    path('', RosterListView.as_view(), name='roster-list-page'),
    path('new/', PlayerCreateView.as_view(), name='player-create-page'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player-detail-page'),
    path('<int:pk>/delete/', PlayerDeleteView.as_view(),name='player-delete-page'),
    path('<int:pk>/edit/', EditPlayerView.as_view(), name="edit-player-profile"),
]