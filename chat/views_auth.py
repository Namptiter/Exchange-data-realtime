from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def loginn(request):
	return render(request, 'index.html')

def register(request):
	return render(request, 'register.html')

@csrf_exempt
def postregister(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['pass']
		email = request.POST['email']
		user = User.objects.create_user(username, email, password)
	else:
		return HttpResponseRedirect('/register')
	return HttpResponseRedirect('/')	

@csrf_exempt
def postlogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['pass']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/login')

def logoutt(request):
	logout(request)
	return HttpResponseRedirect('/login')