from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from events.models import Event


attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present'),
    ('excused', 'Excused'),
    ('tardy', 'Tardy')
)

school_grade_choices = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=25)
    grade = models.CharField(max_length=50, choices=school_grade_choices, blank=True)
    jersey_number = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Attendance(models.Model):

    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    player = models.ForeignKey(Player, on_delete = models.CASCADE)

    attendance_status = models.CharField(max_length=20, choices=attendance_choices, blank=True)

    def __str__(self):
        return self.player.last_name + ' : ' + self.event.event_type
