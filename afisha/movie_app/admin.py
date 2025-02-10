#ismaevselim12
from django.contrib import admin
from .models import Movie
from .models import Director
from .models import Review
# Register your models here.


admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Review)
