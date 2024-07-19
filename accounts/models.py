from django.db import models
import uuid

# Create your models here.
class Account(models.Model) :
    account_id =  models.CharField(max_length=100, unique=True)
    account_name = models.CharField(max_length=100)
    account_balance = models.DecimalField(max_digits=10,decimal_places=2)

def __str__(self):
   return f"{self.account_name} ({self.account_id})"


