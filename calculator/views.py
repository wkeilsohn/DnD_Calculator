from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .forms import *
import os
import io
from io import BytesIO
import pandas as pd
from calculator.math import *
from calculator.note import *

def index(request):
	try:
		df = request.session['df']
		del request.session['df']
		del df
		return redirect('/home/')
	except:
		if request.method == 'POST':
			form = UploadForm(request.POST, request.FILES)
			if form.is_valid():
				file = request.FILES['file']
				name, extension = os.path.splitext(file.name)
				if extension == '.csv':
					df = pd.read_csv(file)
				elif extension == 'xlsx':
					df = pd.read_excel(file)
				else:
					messages.error(request, 'Incorrect File Type')
					return redirect('/home/')
				df = df.to_json(orient = 'index')
				request.session['df'] = df
				return redirect('/results/')
			else:
				messages.error(request, 'Form Failed to Submit')
		else:
			form = UploadForm()
	return render(request, 'home.html', {'form':form})

def about(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			semail = form.cleaned_data['email']
			smessage = form.cleaned_data['message']
			try:
				subject = 'DnD Site Inquery'
				message = noteWriter(semail, smessage)
				email_from = settings.EMAIL_HOST_USER
				recipient_list = ['librarywebdeveloper@gmail.com']
				send_mail(subject, message, email_from, recipient_list, fail_silently=False)
				messages.success(request, "Email Sent")
			except:
				messages.error(request, "Email Failed to Send")
		else:
			messages.error(request, "Email Failed to Send")
	else:
		form = ContactForm()
	return render(request, 'about.html', {'form':form})

def results(request):
	try:
		df = request.session['df']
		df = pd.read_json(df)
		freedeg = chiSquare.degFree(df)
		chi_val = chiSquare.calcChi(df)
		p_value =  chiSquare.pFinder(freedeg, chi_val)
		print("check2")
		if p_value < 0.05:
			verdict = "Foul" # A chi square test looks to see that things are DIFFERENT from the norm... so in this case you don't want a positive/significant result. 
		else:
			verdict = "Fair"
		del request.session['df']
		return render(request, 'results.html', {'chi_val': chi_val, 'p_value': p_value, 'verdict': verdict})
	except:
		return redirect('/home/')

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