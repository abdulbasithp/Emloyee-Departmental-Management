from django.urls import path
from account import views
from django.contrib.auth.views import LogoutView
from django.conf import settings


app_name = 'account'


urlpatterns = [
    
    path('', views.superadmin_login, name='superadmin-login'),
    path('superadmin_home/', views.superadmin_home, name='superadmin-home'),
   
    path('manage_manager/', views.manage_manager, name='manage-manager'),
    path('manage_manager/<str:id>/', views.manager_detail, name='manager-detail'),
    path('manage_manager/edit/<str:id>/', views.edit_manager, name="edit-manager"),
    path('manager/create/', views.add_manager, name="add-manager"),
   
    path('manage_coordinator/', views.manage_coordinator, name='manage-coordinator'),
    path('manage_coordinator/<str:id>/', views.coordinator_detail, name='coordinator-detail'),
    path('manage_coordinator/edit/<str:id>/', views.edit_coordinator, name="edit-coordinator"),
    path('manage_coordinators/create/', views.add_coordinator, name="add-coordinator"),
    
    path('manage_inspector/', views.manage_inspector, name='manage-inspector'),
    path('manage_inspector/<str:id>/', views.inspector_detail, name='inspector-detail'),
    path('manage_inspector/edit/<str:id>/', views.edit_inspector, name="edit-inspector"),
    path('manage_inspectors/create/', views.add_inspector, name="add-inspector"),
    
    path('notifications/', views.notification, name="notifications"),
    
    path('superadmin_logout/', LogoutView.as_view(next_page=settings.SUPERADMIN_LOGOUT_REDIRECT_URL), name='superadmin-logout'),
    
    
    
]
