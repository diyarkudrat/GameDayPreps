from django.contrib import admin
from .models import Event
from roster.models import Attendance

class AttendanceInLine(admin.TabularInline):
    model = Attendance
    extra = 10

class EventAdmin(admin.ModelAdmin):
    inlines = (AttendanceInLine, )

admin.site.register(Event, EventAdmin)
