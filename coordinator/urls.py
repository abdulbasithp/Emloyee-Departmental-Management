from django.urls import path
from coordinator import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

app_name = 'coordinator'

urlpatterns = [
    path('login/', views.coordinator_login, name='coordinator-login'),
    
    path('inspector_master/', views.inspector_master, name='inspector-master'),
    path('inspector_master/add/', views.add_inspector, name='create-inspector'),
    path('inspector_master/<str:id>/edit/', views.edit_inspector, name='edit-inspector'),
    path('inspector_master/<str:id>/view/', views.view_inspector, name="view-inspector"),
    
    path('client_master/', views.client_master, name='client-master'),
    
    path('job_master/', views.job_master, name="job-master"),
    path('job_master/add_job/', views.add_job, name="add-job"),
    
    path('profile/', views.profile_details, name='profile-detail'),
    
    path('superadmin_logout/', LogoutView.as_view(next_page=settings.COORDINATOR_LOGOUT_REDIRECT_URL), name='coordinator-logout'),

    
    path('get_client/',views.get_client_details, name="get-client"),
   
    
]
