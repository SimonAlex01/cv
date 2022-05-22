from django.shortcuts import render
from django.views.generic import ListView
from .models import BioData

class HomePageView(ListView):
    model = BioData
    template_name = 'home.html'