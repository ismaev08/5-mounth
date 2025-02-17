#ismaevselim12
from django.contrib import admin
from .models import Movie
from .models import Director, HasTag
from .models import Review, Category
# Register your models here.


admin.site.register(HasTag)
admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Review)
admin.site.register(Movie)
