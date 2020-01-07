from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse


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
    slug = models.CharField(max_length=200, blank=True, editable=False)
    position = models.CharField(max_length=25)
    grade = models.CharField(max_length=50, choices=school_grade_choices, blank=True)
    jersey_number = models.CharField(max_length=3, null=True)
    attendance_status = models.CharField(max_length=15, choices=attendance_choices, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
  
        path_components = {'slug': self.slug}
        return reverse('roster-detail-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.last_name, allow_unicode=True)

        # Call save on the superclass.
        return super(Player, self).save(*args, **kwargs)