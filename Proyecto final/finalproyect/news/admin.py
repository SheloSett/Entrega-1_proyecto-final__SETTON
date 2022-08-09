from django.contrib import admin
from news.models import Noticias

@admin.register(Noticias)
class Noticias_admin(admin.ModelAdmin):
    list_display = ['title', 'creation_date', 'author']
