from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from jokes.choices import joke_choices

from .models import Listing
from jokes.models import Joke


def index (request):
    jokes=Joke.objects.order_by('-contact_date')

    paginator = Paginator(jokes, 6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    context={'jokes':paged_listings}
    return render(request, 'listings/listings.html', context)

def listing (request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context={
        'listing':listing
        }
    return render(request, 'listings/listing.html', context)

def search (request):
    queryset_list=Joke.objects.order_by('-contact_date')

    #keywords
    if 'keywords' in request.GET:
      keywords=request.GET['keywords']
      if keywords:
          queryset_list=queryset_list.filter(joke__icontains=keywords) 

    #jtype
    if 'jtype' in request.GET:
      jtype=request.GET['jtype']
      if jtype:
          queryset_list=queryset_list.filter(jtype__iexact=jtype) 

    context={
        'joke_choices': joke_choices,
        'jokes': queryset_list,
        'values': request.GET ##saves search values
    }
    return render(request, 'listings/search.html', context)

