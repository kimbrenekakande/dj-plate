from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

class Dashboard(TemplateView):
    template_name = "dashboard.html"

class Home(TemplateView):
    template_name = "home.html"

class List(TemplateView):
    template_name = "list.html"

class Billing(TemplateView):
    template_name = "billing.html"

class Profile(TemplateView):
    template_name = "profile.html"

class Settings(TemplateView):
    template_name = "settings.html"

    
    
