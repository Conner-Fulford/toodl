from django.shortcuts import render

# Create your views here.
def calendar(request):
    # Render the HTML template index.html
    return render(request, 'calendar.html')

# Create your views here.
def login(request):
    # Render the HTML template index.html
    return render(request, 'login.html')

def register(request):
    # Render the HTML template index.html
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')
