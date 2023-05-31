from django.db import models

# Create your models here.
class regdb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    C_password=models.CharField(max_length=100,null=True,blank=True)

class cartdb(models.Model):
    username=models.CharField(max_length=30, null=True, blank=True)
    Pname=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    T_price=models.IntegerField(null=True,blank=True)