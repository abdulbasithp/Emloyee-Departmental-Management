from django.db import models

from account.models import Account


class Client(models.Model):
    serial_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title

class JobAssign(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    date = models.DateField(null=True)
    inspector = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)    
    
    
    
class Notification(models.Model):
    message = models.CharField(max_length=300)
    is_admin_viewed = models.BooleanField(default=False)
    
    