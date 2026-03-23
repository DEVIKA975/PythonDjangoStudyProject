from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def sign_up_user(request):
    user = None
    error_message = None
    if request.POST:
        #print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username, password=password)
        except Exception as err:
            error_message = err
 
    return render(request,'users/create.html',{'user':user,'error_message':error_message})


def login_user(request):
    user = None   
    error_message = None
    if request.POST:
        #print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('movie_list')
        else:
            error_message = 'Invalid username or password'
            
    return render(request,'users/login.html',{'user':user,'error_message':error_message})


def logout_user(request):
    logout(request)
    return redirect('login_user')


