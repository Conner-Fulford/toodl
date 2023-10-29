from django.shortcuts import render

# Create your views here.
def calendar(request):
    # Render the HTML template index.html
    return render(request, 'calendar.html')
