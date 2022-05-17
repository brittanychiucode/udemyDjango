from django.urls import path
from . import views

# List that contains all the urls
#   [string url you want to support] => [pointer of view function when requester goes to url]
#   /challenges/january => 

urlpatterns = [
    path("", views.index), # /challenges
    path("secret_month", views.secret_month),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
