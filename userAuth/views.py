from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from time import sleep

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'home.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password is Wrong!')
            return render(request, 'login.html')

    return render(request, 'login.html')

def createAccount(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        #Check if User Exists
        user = authenticate(username=username, password=password)

        if user is not None:
            #If Exists
            messages.warning(request, "User already Exists")
            return render(request, 'createAccount.html')
        else:
            #If not Exists
            #Create New User
            user = User.objects.create_user(username, email, password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            return redirect('/login')
    return render(request, 'createAccount.html')
