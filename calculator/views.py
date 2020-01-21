from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def index(request):
	if request.method == 'POST':
		form = UploadForm(request.POST)
		if form.is_valid():
			pass # Add and action here later.
	else:
		form = UploadForm()
	return render(request, 'home.html', {'form':form})

def about(request):
	return render(request, 'about.html')

def results(request):
	return render(request, 'results.html')