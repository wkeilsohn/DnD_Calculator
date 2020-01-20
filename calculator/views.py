from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def results(request):
	return render(request, 'results.html')