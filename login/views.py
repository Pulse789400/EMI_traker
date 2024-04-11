from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you have been logged in')
            return redirect('home')
        else:
            return render(request, 'login/index.html', {'error': 'Sorry. The Username and Passwords do not match.'})
    list=dir(request)
    for i in list:
        print(i)
    
    return render(request,"data/data.html",{'name':request.user})

def login_request(request):
    pass

def logout_request(request):
    logout(request)
    return redirect('home')