from django.contrib import admin

from .models import Joke


class JokeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'jtype', 'joke', 'contact_date','rating', 'user_id')
    list_display_links = ('id', 'name')
    lsearch_dfields = ('name', 'joke', 'jtype', 'rating')
    list_per_page=25

admin.site.register(Joke, JokeAdmin)
