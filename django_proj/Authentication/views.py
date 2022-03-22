from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	context = {}
	return render(request, "authentication/html/index.html", context=context)

def signin(request):
	context = {}
	return render(request, "authentication/html/signin.html", context=context)

def signup(request):
	context = {}
	return render(request, "authentication/html/signup.html", context=context)
