from django.shortcuts import render

# Create your views here.
def login_page_render(request):
    return render(request, 'authentication/login.html')

def register_page_render(request):
    return render(request, 'authentication/user_reg.html')