from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms.widgets import RadioSelect

class CustomUserCreationForm(UserCreationForm):
    CHOICES = (
        ('True', 'T'),
        ('False', 'F')
    )

    is_buyer = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_buyer')

class CustomUserChangeForm(UserChangeForm):

    CHOICES = (
        ('True', 'T'),
        ('False', 'F')
    )

    is_buyer = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_buyer')