from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomerUser(AbstractUser):
    phone=models.CharField(max_length=15,blank= True , null= True)
    bank_name=models.CharField(max_length=100, blank=True, null=True)
    account_number=models.CharField(max_length=30 , blank=True, null=True)
    account_type=models.CharField(max_length=30 , blank=True, null=True)
    fingerprint_token=models.CharField(max_length=255,blank=True,null=True)
    is_verified=models.BooleanField(default=False)

    
def __str__(self):
    return self.username


