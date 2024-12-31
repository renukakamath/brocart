from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from customers.models import Customer
from django.contrib import messages


from django.contrib.auth import authenticate, login , logout


# Create your views here.
def signout(request):
    logout(request)
    return redirect('index')

def account(request):
    error_messages = None
    if  request.POST and 'register' in request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            user = User.objects.create_user(username=username, password=password, email=email)
            customer = Customer.objects.create(user=user, address=address, phone=phone)
            return redirect('account')
        except Exception as e:
            error_messages='Duplicate username or invalid'
            messages.error(request,error_messages)
           
            
            
    if request.POST and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            error_messages1='username  invalid'
            messages.error(request,error_messages1)
       
        
        
    return render(request,'account.html')