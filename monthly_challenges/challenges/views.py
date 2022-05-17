import string
from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse # create paths by refering to names

monthly_challenges = {
    "january": "Eat more vegetables.",
    "february": "Run a mile.",
    "march": "Learn something new.",
    "april": "Teamwork.",
    "may": "Plant a flower.",
    "june": "Read a book.",
    "july": "Adopt a dog.",
    "august": "Go outside.",
    "september": "Take a class.",
    "october": "Treat yoself.",
    "november": "Call your mom.",
    "december": "Call your dad."
}

# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    list_items = ""

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"""
        <ul>{list_items}</ul>
    """
    
    return HttpResponse(response_data)

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
        return HttpResponseNotFound("Month not found")

    response_data = f"<h1>Challenge Month: {month}</h1> <p>{challenge_text}</p>"
    return HttpResponse(response_data)
    
def get_monthly_challenge(month):
    if (type(month) is int) and (month < 0 or month > 12):
        return HttpResponseNotFound("Month index out of bound.")
    try:
        return monthly_challenges[month]
    except:
        return None
    