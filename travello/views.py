from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Goa'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 500
    dest1.offer=False
    #if i place dest1.offer=False the down dest.offer all are becoming false so better to add first dest with offer at first and wiithout offer at last
    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'biryani and culture'
    dest2.img = 'hyderabad.jpg'
    dest2.price = 650 #if you want to enjoy entire hyderabad city this is the amount u have to pay
    dest2.offer=True

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    dest3.offer=False
    
    dest4= Destination()
    dest4.name="Warangal"
    dest4.desc="Beautiful city with spectacular tourist attractions like the Warangal Fort, Thousand Pillar Temple, and more"
    dest4.img="WarangalMontage.jpg"
    dest4.price=100
    dest4.offer=True

    dests = [dest1, dest2, dest3,dest4]

    return render(request, "index.html", {'dests': dests})
