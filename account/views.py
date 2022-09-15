from re import M
from django.shortcuts import render,redirect

from account.forms import CoordinatorModelForm, InspectorModelForm, ManagerModelForm
from coordinator.models import Notification
from .models import Account
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

superadmin_login_required = user_passes_test(lambda user: user.is_staff, login_url='coordinator:coordinator-login')
def superadmin_user_required(view_func):
    decorated_view_func = login_required(superadmin_login_required(view_func))
    return decorated_view_func


def superadmin_login(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('account:superadmin-home')
        elif user.is_staff == False and user.role == 'coordinator':
            return redirect('coordinator:inspector-master')
            
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email = email, password = password)
    
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('account:manage-manager')
            elif user.is_staff == False and user.role == 'coordinator':
                login(request,user)
                return redirect('coordinator:inspector-master') 
            else:
                messages.error(request, 'Email is not verified. Please check your inbox..')
           
        else:
            messages.error(request, 'Invalid Credentials!')
    return render(request, 'superadmin/login.html')

@superadmin_user_required
def superadmin_home(request):
    return render(request, 'superadmin/base.html',{})

# ---------------------manager----------------------------------
@superadmin_user_required
def manage_manager(request):
    managers = Account.objects.filter(role = 'manager')
    return render(request, 'superadmin/manager.html',{'managers':managers})


@superadmin_user_required
def manager_detail(request, id):
    manager = Account.objects.get(id=id)
    return render(request, 'superadmin/manager_detail.html', {'manager':manager})

@superadmin_user_required
def edit_manager(request, id):
    manager = Account.objects.get(id=id)
    form = ManagerModelForm(instance=manager)
    if request.method == 'POST':
        form = ManagerModelForm(request.POST, request.FILES, instance=manager)
        if form.is_valid():
            print('form valid')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            form.save(commit=True)
            return redirect('account:manage-manager')
        else:
            messages.error(request, 'Form filling is not valid please check it!!')
            print("form not valid")
           
    else:
        form = ManagerModelForm(instance=manager)
    context = {
        'form': form , 
        'manager': manager,
    }
    return render(request, 'superadmin/edit_manager.html',context)

@superadmin_user_required
def add_manager(request):
    form = ManagerModelForm()
    if request.method == 'POST':
        form = ManagerModelForm(request.POST, request.FILES)
        if form.is_valid():
            print('form valid')
            user = form.save(commit=False)
            
            user.set_password(form.cleaned_data['password'])
            form.save(commit=True)
            return redirect('account:manage-manager')
        else:
            messages.error(request, 'Form filling is not valid please check it!!')
            print("form not valid")
    else:
        form = ManagerModelForm()
    context = {
        'form': form , 
    }
    return render(request, 'superadmin/add_manager.html', context)
    

# ----------------------coordinator-----------------------------
@superadmin_user_required
def manage_coordinator(request):
    coordinators = Account.objects.filter(role= 'coordinator')
    return render(request, 'superadmin/coordinator.html', {'coordinators':coordinators})

@superadmin_user_required
def edit_coordinator(request, id):
    coordinator = Account.objects.get(id=id)
    form = CoordinatorModelForm(instance=coordinator)
    if request.method == 'POST':
        form = CoordinatorModelForm(request.POST, request.FILES, instance=coordinator)
        if form.is_valid():
            print('form valid')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('account:manage-coordinator')
        else:
            messages.error(request, 'Form filling is not valid please check it!!')
            print("form not valid")
           
    else:
        form = CoordinatorModelForm(instance=coordinator)
    context = {
        'form': form , 
        'manager': coordinator,
    }
    return render(request, 'superadmin/edit_coordinator.html',context)

@superadmin_user_required
def add_coordinator(request):
    form = CoordinatorModelForm()
    if request.method == 'POST':
        form = CoordinatorModelForm(request.POST, request.FILES)
        if form.is_valid():
            print('form valid')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('account:manage-coordinator')
        else:
            messages.error(request, 'Form filling is not valid please check it!!')
            print("form not valid")
    else:
        form = CoordinatorModelForm()
    context = {
        'form': form , 
    }
    return render(request, 'superadmin/add_coordinator.html', context)
    


@superadmin_user_required
def coordinator_detail(request, id):
    coordinator = Account.objects.get(id=id)
    return render(request, 'superadmin/coordinator_detail.html', {'coordinator':coordinator})

# ------------------------inspector-----------------------------
@superadmin_user_required
def manage_inspector(request):
    inspectors = Account.objects.filter(role="inspector")
    return render(request, 'superadmin/inspector.html', {'inspectors':inspectors})

@superadmin_user_required
def edit_inspector(request, id):
    inspector = Account.objects.get(id=id)
    form = InspectorModelForm(instance=inspector)
    if request.method == 'POST':
        form = InspectorModelForm(request.POST, request.FILES, instance=inspector)
        if form.is_valid():
            print('form valid')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
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
    return render(request, 'superadmin/edit_inspector.html',context)

@superadmin_user_required
def add_inspector(request):
    form = InspectorModelForm()
    if request.method == 'POST':
        form = InspectorModelForm(request.POST, request.FILES)
        if form.is_valid():
            print('form valid')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('account:manage-inspector')
        else:
            messages.error(request, 'Form filling is not valid please check it!!')
            print("form not valid")
    else:
        form = InspectorModelForm()
    context = {
        'form': form , 
    }
    return render(request, 'superadmin/add_inspector.html', context)
    


@superadmin_user_required
def inspector_detail(request, id):
    inspector = Account.objects.get(id=id)
    return render(request, 'superadmin/inspector_detail.html', {'inspector':inspector})


#----------------------notification-----------------------------

def notification(request):
    notifications = Notification.objects.all().order_by('-id')
    return render(request, 'superadmin/notification.html', {'notifications':notifications})


