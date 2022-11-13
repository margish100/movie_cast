from django.contrib import admin

from movie.models import Movie, Cast

admin.site.register(Movie)
admin.site.register(Cast)
