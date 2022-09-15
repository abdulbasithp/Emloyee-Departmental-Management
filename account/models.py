from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


class AccountManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):

        if email is None:
            raise TypeError('Email field must be required!')
        
        
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            
            email=email,	
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None,**extra_fields): 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser field is_staff must be True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser field is_superuser must be True')
        
        return self.create_user( email=email, password=password, **extra_fields)



class Account(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICE = [
        ('manager','Manager'),
        ('coordinator', 'Coordinator'),
        ('inspector', 'Inspector')
    ]
    
    full_name = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to = 'media/%Y/%m/%d/profile')
    email = models.EmailField(max_length=150, unique=True, db_index=True,)
    username = models.CharField(max_length=100, unique=True) 
    contact = PhoneNumberField(blank = True)
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, blank=True)
    
    is_staff = models.BooleanField(default=False)
    is_active  = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    
    objects = AccountManager()

    def __str__(self):
        return self.username