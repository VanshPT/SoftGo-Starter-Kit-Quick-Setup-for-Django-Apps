from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    return render(request, 'home/landing/landing.html')

@login_required
def render_dashboard(request,username):
    user=request.user
    context={'username':user.username, 'first_name':user.first_name, 'last_name':user.last_name, 'email': user.email}
    return render(request, 'home/dashboard.html',context)