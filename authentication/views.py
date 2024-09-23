from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
# Create your views here.
def login_page_render(request):
    return render(request, 'authentication/login.html')

def register_page_render(request):
    return render(request, 'authentication/user_reg.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email-id')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Password and Confirm Password do not match!')
            return render(request, 'authentication/user_reg.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken!')
            return render(request, 'authentication/user_reg.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered!')
            return render(request, 'authentication/user_reg.html')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            user.save()
            messages.success(request, f'User {username} created successfully!')
            return redirect('/')  
        except ValidationError as e:
            messages.error(request, 'An error occurred during registration: ' + str(e))
            return render(request, 'authentication/user_reg.html')

    return render(request, 'authentication/user_reg.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)

            # Set session to never expire unless user logs out (persistent login)
            if not request.POST.get('remember_me'):  # Assuming 'remember_me' is a checkbox
                request.session.set_expiry(0)  # Session expires when the browser is closed
            else:
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)  # Default session age (usually 2 weeks)

            messages.success(request, f"Welcome back, {username}!")
            return redirect(f'/dashboard/{username}') 

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'authentication/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/')