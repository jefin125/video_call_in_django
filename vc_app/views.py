from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def SignUp(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"User registered Successfully")
            return redirect('login')
    else:
        fm = SignupForm()
    return render(request,'vc/home.html',{'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Sucessfully')
                    return redirect('dash')
                else:
                    messages.success(request,'Error in credentials')
        else:
            fm = AuthenticationForm()
        return render(request,'vc/login.html',{"form":fm})
    else:
        return redirect('dash')

@login_required
def dashboard(request):
    return render(request,'vc/dashboard.html',{'name':request.user})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def meeting(request):
    return render(request,'vc/video_call.html',{'name':request.user})

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request,'vc/joinroom.html')