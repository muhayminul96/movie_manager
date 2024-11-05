from django.contrib import admin
from .models import Movie , Report, Rating

# Register your models here.

admin.site.register([Movie , Report, Rating])