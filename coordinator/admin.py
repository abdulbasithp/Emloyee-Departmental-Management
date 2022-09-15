from django.contrib import admin
from .models import Client, Job, JobAssign, Notification

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial_number', 'id', 'location']
    
    
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    

@admin.register(JobAssign)
class JobAssignAdmin(admin.ModelAdmin):
    list_display = ['id','job','client','location','date','inspector']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'is_admin_viewed']