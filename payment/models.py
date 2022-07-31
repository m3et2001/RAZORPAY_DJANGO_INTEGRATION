from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Payment_Detail(models.Model):
    Username=models.ForeignKey(User,on_delete=models.CASCADE)
    Order_id=models.CharField(max_length=250,default="",null=True)
    Payment_id = models.CharField(max_length=100,default="",null=True)
    Amount=models.BigIntegerField(default=0,null=True)
    Currency=models.CharField(max_length=20,default="",null=True)
    Status=models.CharField(max_length=20,default="",null=True)
    International=models.BooleanField(default=False,null=True)
    Method=models.CharField(max_length=30,default="",null=True)
    Amount_refunded=models.BigIntegerField(default=0,null=True)
    Upi_id=models.CharField(max_length=30,default="",null=True)
    Email=models.CharField(max_length=230,default="",null=True)
    Contact=models.CharField(max_length=32,default=0,null=True)
    Upi_Transaction_id=models.CharField(max_length=250,default="",null=True)
    Create_at=models.CharField(max_length=50,default="",null=True)
        
    
    def __str__(self):
        return str(self.Username)