from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django import forms

CHOICES = (
    ('Wheat', 'Wheat'),
    ('Rice', 'Rice'),
)
months = (
    (1,'Jan'),
    (2,'Feb'),
    (3,'March'),
    (4,'Apr'),
    (5,'May'),
    (6,'Jun'),
    (7,'Jul'),
    (8,'Aug'),
    (9,'Sep'),
    (10,'Oct'),
    (11,'Nov'),
    (12,'Dec')
)


class NewFarmForm(forms.Form):
    latitude = forms.FloatField(label="Latitude")
    longitude = forms.FloatField(label="Longitude")
    Area = forms.FloatField(label="Area in Metric Units")
    flowRate = forms.FloatField(label="Flow Rate In Liter/Minute")
    crop = forms.ChoiceField(
        label="Crop", widget=forms.Select, choices=CHOICES)
    start_date = forms.ChoiceField(
        label="Start month", widget=forms.Select, choices=months)

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'calculator.html', {
            'form': NewFarmForm()
        })
    else:
        form = NewFarmForm(request.POST)
        if form.is_valid():
            request.session["farm_details"] = form.cleaned_data
            return HttpResponseRedirect(reverse('dashboard'))
            
def dashboard(request):
    if "farm_details" in request.session:
        return render(request, "dashboard.html", request.session["farm_details"])
    else:
        return redirect('index')
