from django.contrib import admin

from account.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username','id','email','contact','role']
    
