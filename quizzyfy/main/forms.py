from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models.models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    is_student = forms.BooleanField(required=False, widget=forms.RadioSelect(choices=[(True, 'Student'), (False, 'Professor')]))
    #is_professor = forms.BooleanField(required=False, widget=forms.RadioSelect(choices=[(True, 'Professor'), (False, 'Student')]))

    class Meta:
        model = UserProfile
        fields = ['is_student']
