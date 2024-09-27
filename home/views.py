from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    if request.user:
        context={'username':request.user.username}
        return render(request, 'home/landing/landing.html', context)
    else:
        return render(request, 'home/landing/landing.html')

@login_required
def render_dashboard(request,username):
    user=request.user
    context={'username':user.username, 'first_name':user.first_name, 'last_name':user.last_name, 'email': user.email}
    return render(request, 'home/dashboard_main.html',context)

@login_required
def auto_clustering(request,username):
    user=request.user
    context={'username':user.username, 'first_name':user.first_name, 'last_name':user.last_name, 'email': user.email}
    return render(request, 'home/render_auto_clustering.html',context)

@login_required
def explore_topics(request,username):
    user=request.user
    context={'username':user.username, 'first_name':user.first_name, 'last_name':user.last_name, 'email': user.email}
    return render(request, 'home/render_explore_topics.html',context)

@login_required
def search_papers(request,username):
    user=request.user
    context={'username':user.username, 'first_name':user.first_name, 'last_name':user.last_name, 'email': user.email}
    return render(request, 'home/render_search_papers.html',context)