from django.urls import path
from payment import views

  
urlpatterns = [
    path('', views.payment_page, name ='payment'),
    path('user-payment/', views.user_payment, name ='user_payment'),
    path('payment-details/',views.payment_details,name="payment-detail")
]
