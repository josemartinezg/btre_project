from django.shortcuts import render
from .models import Listing
#Pasaremos datos del modelo desde un diccionario.
def index(request):
    #Trayendo "Listings" desde la DB:
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
