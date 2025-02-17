#ismaevselim13
from django.contrib import admin
from .models import Movie, Director, Review

# Register your models here.

admin.site.register(Director)
admin.site.register(Review)
admin.site.register(Movie)
