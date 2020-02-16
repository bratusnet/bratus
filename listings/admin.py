from django.contrib import admin

class ListingAmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price', 'list_date', 'realtor')
    list_display_links=('id','title')
    list_filter=('realtor', )
    list_editable=('is_published', )
    search_fields=('title', 'description', 'address', 'city', 'state', 'zipcode', 'price',)
    list_per_page=25


from .models import Listing
admin.site.register(Listing,ListingAmin )
