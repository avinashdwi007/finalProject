from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from app2.models import data
from django.contrib.auth.decorators import login_required

from app2.models import data

# Create your views here.

def index(request):
    return render(request,'index.html')

def feature(request):
    return render(request,'feature.html')

def services(request):
    return render(request,'services.html')
def blog(request):
    return render(request,'blog.html')

def contact(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Here you can add your logic to process the form data
        # For example, sending emails, saving to database, etc.

        # Add success message
        messages.success(request, 'Your message has been sent successfully!')
    return render(request,'contact.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            #user in the custom data model
            user_data = data(username=username, email=email, password=password, confirm_password=confirm_password)
            user_data.save()

            # Creating a user in the default User model for authentication
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
    return render(request, 'signup.html')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')