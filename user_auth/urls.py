from django.urls import path
from . import views

  
urlpatterns = [
    path('login/', views.login, name ='login'),
    path('logout/', views.logout_view, name ='logout'),
    path('send-otp/', views. send_otp, name =' send_otp'),
    path('',views.home,name="home" )
]
