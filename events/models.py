from django.db import models



event_types = (
    ('Practice', 'Practice'),
    ('Game', 'Game'),
    ('Workout', 'Workout'),
    ('Meeting', 'Meeting'),
    ('Film', 'Film')
)

class Event(models.Model):

    event_type = models.CharField(max_length=50, choices=event_types, blank=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    members = models.ManyToManyField(
        'roster.Player',
        through='roster.Attendance',
        through_fields=('event', 'player'),
    )
    location = models.CharField(max_length=150)
    description = models.TextField(null=True)

    def __str__(self):
        return self.event_type
