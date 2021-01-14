from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class formUser(UserCreationForm):
	password1 = forms.CharField(
		label= "Password",
		strip=False,
		widget= forms.PasswordInput(attrs={
			'class':'form-control',
			'placeholder':"Password"
			}),
		)

	password2 = forms.CharField(
		label= "Confirm Password",
		strip=False,
		widget= forms.PasswordInput(attrs={
			'class':'form-control',
			'placeholder':"Confirm Password"
			}),
		)

	class Meta:
		model = User
		fields = ["username", "email", 'password1']
		widgets = {
			'username': forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':"Username"
				}),
			'email': forms.EmailInput(attrs={
				'class':'form-control',
				'placeholder':"Email address"
				})
		}

	
