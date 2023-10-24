from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calendar(request):
    # Render the HTML template index.html
    return render(request, 'calendar.html')
