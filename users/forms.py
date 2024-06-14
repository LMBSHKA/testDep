from pyexpat.errors import messages
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from users.models import Upload_images, User


    
class UserLoginForm(AuthenticationForm):
    username = forms.CharField()                              
    password = forms.CharField()
    class Meta():
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            #"first_name",
            #"last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
    
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload_images
        fields={'image'}
        
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "about",)
            #"email",)

    image = forms.ImageField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField()
    about = forms.CharField(required=False)
    
    #email = forms.CharField()

class EditProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    about = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    class Meta:
        model=User
        fields=("email", "username", "first_name", "last_name", "about", "image")

