from django.contrib import admin
from .models import Event
from roster.models import Attendance, Player

class AttendanceInLine(admin.StackedInline):
    model = Attendance


class EventAdmin(admin.ModelAdmin):
    inlines = (AttendanceInLine, )

admin.site.register(Event, EventAdmin)
