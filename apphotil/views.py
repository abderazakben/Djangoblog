from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import Group 
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Hotel
from .forms import CreateUserForm 

from .decoratos import unauthenticated_user , allowd_user , admin_only
# page home 
#### @ login_required ana kanhadad  achman page li ganwirilo 
@login_required(login_url='apphotil:login') # hta ikon login 3ad warilo page d home mital
@allowd_user(allowed_roles=['admin'])
#@admin_only
def my_page_home(request):
    context = {}
    return render(request,"pages/home.html",context)

   

#############################################
# page Register
def registrPage(request):
    if request.user.is_authenticated:
        return redirect('apphotil:home')
    else:    
        form = CreateUserForm()       
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user =  form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='customer')
                user.groups.add(group)
                messages.success(request,'Account was created for ' + username)
                return redirect('apphotil:login')
        context = {'form':form}
        return render(request,'registration/register.html' , context)
# page Login
@unauthenticated_user
def loginPage(request):   
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request , username=username , password=password)
            if user is not None:
                login(request , user)
                return redirect('apphotil:home_page')
            else:
                messages.info(request, 'Username OR passwored')    
        context = {}
        return render(request, 'registration/login.html' , context)


#  def logout 
def logoutUser(request):
    logout(request)
    return redirect('apphotil:login')

@login_required(login_url='apphotil:login')
@allowd_user(allowed_roles=['admin'])        
#@admin_only
def my_page_prof(request):
    context = {}
    return render(request,"pages/main.html",context)     