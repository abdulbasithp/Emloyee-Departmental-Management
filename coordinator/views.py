from xml.dom import ValidationErr
from django.shortcuts import render, redirect
from account.forms import InspectorModelForm
from account.models import Account
from coordinator.models import Client, Job, JobAssign, Notification
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.serializers import serialize





coordinator_login_required = user_passes_test(lambda user: user.role=='coordinator', login_url='coordinator/login')
def coordinator_user_required(view_func):
    decorated_view_func = login_required(coordinator_login_required(view_func))
    return decorated_view_func


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def coordinator_login(request):
    if request.user.is_authenticated:
        return redirect('coordinator:inspector-master')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request , email=email, password=password)
        if user is not None:
            if user.is_staff == False:
                print(user.is_staff)
                print(user.role)
                if user.role == 'coordinator':
                    login(request,user)
                    return redirect('coordinator:inspector-master')
                else:
                    print('you are not allowed here')
                    return redirect("coordinator:coordinator-login")
            else: 
                return redirect('account:superadmin-login')
        else:
            return redirect("coordinator:coordinator-login") 
    return render(request, 'coordinator/login.html')

# --------------------inspector----------------------------

@coordinator_user_required
def inspector_master(request):
    inspectors = Account.objects.filter(role='inspector')
    return render(request, 'coordinator/base.html',{'inspectors':inspectors})

@coordinator_user_required
def add_inspector(request):
    form = InspectorModelForm()
    if request.method == 'POST':
        form = InspectorModelForm(request.POST, request.FILES)
        if form.is_valid():
            print('form valid')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            create_notification = Notification()
            create_notification.message = f'{user.full_name} inspector registered'
            create_notification.save()
            return redirect('account:manage-inspector')
        else:
            messages.error(request, 'Form filling is not valid please check it!!')
            print("form not valid")
    else:
        form = InspectorModelForm()
    context = {
        'form': form , 
    }
    return render(request, 'coordinator/add_inspector.html', context)

@coordinator_user_required
def edit_inspector(request,id):
    inspector = Account.objects.get(id=id)
    form = InspectorModelForm(instance=inspector)
    if request.method == 'POST':
        form = InspectorModelForm(request.POST, request.FILES, instance=inspector)
        if form.is_valid():
            print('form valid')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            create_notification = Notification()
            create_notification.message = f'{user.full_name} inspector data edited'
            create_notification.save()
            return redirect('account:manage-inspector')
        else:
            messages.error(request, 'Form filling is not valid please check it!!')
            print("form not valid")
          
    else:
        form = InspectorModelForm(instance=inspector)
    context = {
        'form': form , 
        'manager': inspector,
    }
    return render(request, 'coordinator/edit_inspector.html',context)

@coordinator_user_required
def view_inspector(request, id):
    inspector = Account.objects.get(id=id)
    context = {
        'inspector':inspector
    }
    return render(request, 'coordinator/view_inspector.html', context)

# -------------------client ----------------------------

@coordinator_user_required
def client_master(request):
    clients = Client.objects.all()
    p = Paginator(clients, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'coordinator/client_master.html', context)

# ------------------------job-------------------------

@coordinator_user_required
def job_master(request):
    clients = Client.objects.all()
    jobs = Job.objects.all()
    inspectors = Account.objects.filter(role='inspector')
    
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        job_id = request.POST.get("job_id")
        inspector_id = request.POST.get("inspector_id")
        date = request.POST.get('date')
        if client_id == '':
            messages.error('client not selected')
            return redirect('coordinator:job-master')
        elif job_id == '':
            messages.error('job not selected')
            return redirect('coordinator:job-master')
        elif inspector_id == '':
            messages.error('inspector not selected')
            return redirect('coordinator:job-master')
        elif date == '':
            messages.error('date not selected')
            return redirect('coordinator:job-master')
        else:
            client = Client.objects.get(id=client_id)
            job_assign = JobAssign()
            job_assign.client = client
            job_assign.job = Job.objects.get(id=job_id)
            job_assign.inspector = Account.objects.get(id=inspector_id)
            job_assign.location = client.location
            job_assign.date = date
            job_assign.save()
            create_notification = Notification()
            create_notification.message = f'{job_assign.inspector.full_name} -> {job_assign.client.name} -> {job_assign.job.title}'
            create_notification.save()
            return redirect('coordinator:job-master')    
    jobs_assigned = JobAssign.objects.all().order_by("-id")
    context = {
        'clients':clients,
        'jobs':jobs,
        'inspectors':inspectors,
        'jobs_assigned':jobs_assigned
    }
    return render(request, 'coordinator/job_master.html', context)



@coordinator_user_required
def add_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title == '':
            raise ValueError('Empty title is not acceptable')
        else:
            new_job = Job()
            new_job.title = title
            new_job.save()
        
    jobs = Job.objects.all().order_by('-id')
    context = {
        'jobs':jobs,
    }
    return render(request, 'coordinator/add_job.html', context)

# -------------------profile-----------------------

@coordinator_user_required
def profile_details(request):
    user = request.user
    return render(request, 'coordinator/profile.html',{'user':user})


# -------------------ajax worlks ---------------------
import json

def get_client_details(request):
    if is_ajax(request=request):
        if request.method == 'POST':
            id = request.POST.get('id')
            client = Client.objects.get(id=id)
            client_data = {
                'name':client.name,
                'serial_number': client.serial_number,
                'location': client.location
            }
            data = json.dumps(client_data)
            # data = serialize('json',client_data)
    return JsonResponse(data, safe=False)
