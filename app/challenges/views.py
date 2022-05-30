import re
import string
from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from django.urls import reverse # create paths by refering to names

monthly_challenges = {
    "january": "Eat more vegetables.",
    "february": "Run a mile.",
    "march": "Learn something new.",
    "april": "Teamwork.",
    "may": "Plant a flower.",
    "june": "Read a book.",
    "july": None,
    "august": "Go outside.",
    "september": "Take a class.",
    "october": "Treat yoself.",
    "november": "Call your mom.",
    "december": "Call your dad."
}

# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def secret_month(request):
    return HttpResponse("This is SECRET!")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month < 0 or month > 12:
        return HttpResponseNotFound("Month not found")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    challenge_text = get_monthly_challenge(month)
    if challenge_text == None: 
        # This only works if DEBUG in settings is False
        # raise Http404()
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

    return render(request, "challenges/challenge.html", {
        "month_name": month,
        "chall_text": challenge_text,
    })
    
def get_monthly_challenge(month):
    if (type(month) is int) and (month < 0 or month > 12):
        return HttpResponseNotFound("Month index out of bound.")
    try:
        return monthly_challenges[month]
    except:
        return None
    