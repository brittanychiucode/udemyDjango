from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def secret_month(request):
    return HttpResponse("This is SECRET!")

def monthly_challenges(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat more vegetables."
    elif month == 'februrary':
        challenge_text = "Run a mile."
    elif month == 'march':
        challenge_text = "Learn something new."
    else: 
        return HttpResponseNotFound("Month not found")
    return HttpResponse("<h1>Challenge Month: " + month + "</h1><p>"+ challenge_text + "</p>")