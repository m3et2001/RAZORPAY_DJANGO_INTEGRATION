from django.http import response
from django.shortcuts import render,redirect
from django.conf import settings
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
import razorpay
from .models import *
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User

razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

        
@login_required
def payment_page(request):
    if request.method == "POST":
        print('request.GET.get("amount")')
    return render(request,'payment_page.html')


def user_payment(request):
    if request.GET.get('event') == "pay" :
        amount = int(request.GET.get("amount")) * 100
        currency = 'INR'
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
        razorpay_order_id = razorpay_order['id']
        callback_url = '/payment/payment-details/'
        # user_payment=UserPayment(Username=request.user,Order_id=razorpay_order_id)
        # user_payment.save()
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        return JsonResponse(context)

from django.utils.decorators import method_decorator


@csrf_exempt
@login_required
def payment_details(request):
    if request.method == "POST":
        print(request.body)
        payment_id = request.POST.get("razorpay_payment_id", "")
        payment_client = razorpay_client.payment.fetch(payment_id)
        create_at=datetime.fromtimestamp(payment_client['created_at']).strftime("%A, %B %d, %Y %I:%M:%S")
            
        payment_detail=Payment_Detail(Username=request.user,Order_id=payment_client['order_id'],
                                    Payment_id=payment_client['id'],Status=payment_client['status'],
                                    Method=payment_client['method'],
                                    Upi_id=payment_client['vpa'],Email=payment_client['email'],
                                    Contact=payment_client['contact'],
                                    Upi_Transaction_id=payment_client['acquirer_data']['upi_transaction_id'],Create_at=create_at,
                                    Amount=payment_client['amount']/100,Currency=payment_client['currency'],
                                    International=payment_client['international'],
                                    Amount_refunded=payment_client['amount_refunded'],
                                    )
        payment_detail.save()
        
        messages.success(request,"your payment has successful")
        return redirect('/')
    else:
        return HttpResponseBadRequest()