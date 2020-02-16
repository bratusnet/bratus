from django.shortcuts import render
from django.http import HttpResponse


from listings.models import Listing

from jokes.models import Joke
from jokes.choices import joke_choices

# Create your views here.
def index(request):


    jokes=Joke.objects.order_by('-contact_date')[:9]

    context={
        'jokes': jokes,
        'joke_choices': joke_choices

    }

    return render(request, 'pages/index.html', context)

def about (request):

    jokes=Joke.objects.order_by('-contact_date').filter(jtype='American')[:9]

    context={
        'jokes': jokes,
        'joke_choices': joke_choices

    }

    return render(request, 'pages/about.html', context)  