from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import joke_choices

from .models import Joke


def joke(request):

  if request.method == 'POST':
    name = request.POST['name']
    jtype = request.POST['jtype']
    joke = request.POST['joke']
    rating = request.POST['rating']
    user_id = request.POST['user_id']
 

    #  Check if user has made inquiry already
 #   if request.user.is_authenticated:
 #     user_id = request.user.id
 #     has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
 #     if has_contacted:
 #       messages.error(request, 'You have already made an inquiry for this listing')
 #       return redirect('/listings/'+listing_id)

    joke = Joke( name=name, jtype=jtype, rating=rating, joke=joke, user_id=user_id )

    joke.save()



    messages.success(request, 'Your joke has been submitted')
    return redirect('dashboard')


#  From listing example
def index (request):
    jokes=Joke.objects.order_by('-contact_date')

    paginator = Paginator(jokes, 4)
    page=request.GET.get('page')
    paged_jokes=paginator.get_page(page)

    context={'jokes':paged_jokes}
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



