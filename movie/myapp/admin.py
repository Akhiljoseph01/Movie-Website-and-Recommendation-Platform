from django.contrib import admin
from .models import Category, Movie, Review


admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Review)