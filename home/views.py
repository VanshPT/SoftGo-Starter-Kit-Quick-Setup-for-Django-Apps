from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'home/landing/landing.html')