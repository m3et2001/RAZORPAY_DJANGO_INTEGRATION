from urllib import response
from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail
import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from payment.models import Payment_Detail
from django.contrib.auth import logout

# Create your views here.
@login_required
def home(request):
    last_pay=Payment_Detail.objects.last()
    amount=last_pay.Amount
    return render(request,"home_page.html",{'last_payment':amount})

def logout_view(request):
    logout(request)
    return redirect('home')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user=User.objects.get(email=email)
            username=user.username
        except:
            username=''
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'login_page.html')
    

def send_otp(request):
    email=request.GET.get("email")
    password=request.GET.get("password")
    try:
        user=User.objects.get(email=email)
        username=user.username
    except:
        username=''
    user = auth.authenticate(username=username, password=password)
    print(user)
    context={}
    if user is not None:
        otp=random.randrange(1000,9999, 3)
        subject = 'email verification'
        message = f'Hi here is your OTP: {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
        context["isUserAuthorized"]= "True"
        context['otp']=otp
    else:
        messages.info(request, 'Invalid Username or Password')
        context["isUserAuthorized"]= "False"
    
    return JsonResponse(context)
