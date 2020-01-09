from django.urls import path
from events.views import EventListView, EventCreateView, EventDetailView, EventDeleteView, EditEventView, EventAttendanceView, CreateAttendanceView
urlpatterns = [
    path('', EventListView.as_view(), name='event-list-page'),
    path('new/', EventCreateView.as_view(), name='event-create-page'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail-page'),
    path('<int:pk>/delete/', EventDeleteView.as_view(),name='event-delete-page'),
    path('<int:pk>/edit/', EditEventView.as_view(), name="edit-event-page"),
    path('attendance/', EventAttendanceView.as_view(), name='attendance-list-page'),
    path('attendance/new', CreateAttendanceView.as_view(), name='attendance-create-page'),
]