from django import forms
from django.forms import ModelForm

class UploadForm(forms.Form):
	file = forms.FileField(label = '.csv or .xlsx')

class ContactForm(forms.Form):
	email = forms.EmailField(label = 'Your Email:', required = True)
	message = forms.CharField(label = 'Your Message:', max_length = 3000, widget=forms.Textarea)