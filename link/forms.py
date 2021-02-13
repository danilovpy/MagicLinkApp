from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CreateUserForm(UserCreationForm):
    email = forms.CharField(label='')


    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
