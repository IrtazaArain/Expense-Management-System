from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from . forms import UserRegisterForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request,user)
            return redirect('expenses:expense-list') 
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

#Handles user registration. Renders the form and processes POST data.

def Register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')       
    else:
        form = UserRegisterForm()
    return render(request,'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')