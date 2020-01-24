from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import os
import io
from io import BytesIO
import pandas as pd

def index(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		print("Step 1")
		if form.is_valid():
			print("Success")
		else:
			print("Fail")
	else:
		form = UploadForm()
	return render(request, 'home.html', {'form':form})

def about(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			pass # Fill this in later.
	else:
		form = ContactForm()
	return render(request, 'about.html', {'form':form})

def results(request):
	return render(request, 'results.html')

def example(request):
	path = os.path.dirname(__file__)
	file = path + '/static/example.xlsx'
	data = pd.read_excel(file)
	data.set_index('Side', inplace=True)
	with BytesIO() as b:
		writer = pd.ExcelWriter(b, engine='xlsxwriter')
		data.to_excel(writer, sheet_name='Example')
		writer.save()
		return HttpResponse(b.getvalue(), content_type='application/vnd.ms-excel')