from django.urls import path
from . import views

# List that contains all the urls
#   [string url you want to support] => [pointer of view function when requester goes to url]
#   /challenges/january => 

urlpatterns = [
    path("secret_month", views.secret_month),
    path("<month>", views.monthly_challenges),
]
