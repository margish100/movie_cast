from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Cast(models.Model):
    GENDER = (
        ("male", _("Male")),
        ("female", _("Female")),
        ("Trans", _("Trans")),
    )
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, choices=GENDER)
    dob = models.DateField()


class Movie(TimeStampedModel):
    title = models.CharField(max_length=250)
    runtime = models.PositiveIntegerField()
    language = models.CharField(max_length=20)
    tagline = models.CharField(max_length=250)

    casts = models.ManyToManyField(Cast, related_name="movies", blank=True)

    def __str__(self):
        return f"{self.title} | {self.runtime}"
