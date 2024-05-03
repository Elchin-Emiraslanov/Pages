from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Card
# Create your views here.


def home(request):
    cards = Card.objects.all()
    ctx = {  # context
        "cards":cards
    }
    return render(request, 'switch/home.html', ctx)


def card_details(request):
    return render(request, 'switch/card_details.html')




