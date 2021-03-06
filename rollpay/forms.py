from django.forms import ModelForm,Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,Merchant

class UserProfileForm(UserCreationForm):
	class Meta:
		model=UserProfile
		fields=("username","first_name","last_name","email",)

class Merchant(ModelForm):
	class Meta:
		model=Merchant


class UserProfileChange(ModelForm):
    class Meta:
        model=UserProfile
        fields=("first_name","last_name","email","payee","bank_name","bank_account","bank_ifsc",)


class TrackLinkForm(forms.Form):
	url=forms.URLField(max_length=500)
	



		 



