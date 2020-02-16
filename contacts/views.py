from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
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

    contact = Contact( name=name, jtype=jtype, rating=rating, joke=joke, user_id = user_id )

    contact.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')


    return redirect('index')

