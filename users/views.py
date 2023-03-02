from django.shortcuts import render

# Create your views here.

def profiles(requests):
    return render(requests, 'users/profiles.html')