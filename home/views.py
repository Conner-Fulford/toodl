from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    # Render the HTML template index.html
    return render(request, 'login.html')

def register(request):
    # Render the HTML template index.html
    return render(request, 'register.html')