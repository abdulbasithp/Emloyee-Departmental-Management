from django import forms
from account.models import Account

class ManagerModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['full_name','profile_picture','email','username','contact','password','role']
        widgets = {
        'full_name' : forms.TextInput(attrs= {'class': "form-control",})  ,
        'email' : forms.EmailInput(attrs= {'class':"form-control", 'id':"producttitle"}),
        'username' : forms.TextInput(attrs= {'class': "form-control",})  ,
        'contact' : forms.TextInput(attrs= {'class':"form-control"}),
        'password' : forms.PasswordInput(attrs= {'class':"form-control", 'id':'password-field'}),
        'profile_picture': forms.FileInput(attrs={'class':'form-control'}),
        'role':forms.HiddenInput(attrs= {"value":"manager"}),
        }
        
    # def save(self, commit=True):
    #     pass
        

class CoordinatorModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['full_name','profile_picture','email','username','contact','password','role']
        widgets = {
        'full_name' : forms.TextInput(attrs= {'class': "form-control",})  ,
        'email' : forms.EmailInput(attrs= {'class':"form-control", 'id':"producttitle"}),
        'username' : forms.TextInput(attrs= {'class': "form-control",})  ,
        'contact' : forms.TextInput(attrs= {'class':"form-control"}),
        'password' : forms.PasswordInput(attrs= {'class':"form-control", 'id':'password-field'}),
        'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
        'role':forms.HiddenInput(attrs= {"value":"coordinator"}),
        }
        
        
class InspectorModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['full_name','profile_picture','email','username','contact','password','role']
        widgets = {
        'full_name' : forms.TextInput(attrs= {'class': "form-control",})  ,
        'email' : forms.EmailInput(attrs= {'class':"form-control", 'id':"producttitle"}),
        'username' : forms.TextInput(attrs= {'class': "form-control",})  ,
        'contact' : forms.TextInput(attrs= {'class':"form-control"}),
        'password' : forms.PasswordInput(attrs= {'class':"form-control", 'id':'password-field'}),
        'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
        'role':forms.HiddenInput(attrs= {"value":"inspector"}),
        }