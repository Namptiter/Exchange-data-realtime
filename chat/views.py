import json

from django.shortcuts import render
from .models import Message,Img,File
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# this view is the base view
@login_required(login_url='/login/')
def chat_index(request):
    context = {
        'messages': Message.objects.all()
    }
    return render(request, 'chat_index.html', context)

# this view must be csrf exempted to be able to accept XMLHttpRequests
@csrf_exempt
def save_message(request):
    # if the request method is a POST request
    if request.method == 'POST':

        msg_obj = json.loads(request.body.decode('utf-8'))

        # tries to create the message and save it in the db
        try:
            msg = Message.objects.create(user_name=msg_obj['user_name'], message=msg_obj['message'])
            msg.save()

        except:
            print("error saving message")
            return HttpResponse("error")
        return HttpResponse("success")
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
@login_required(login_url='/login/')
def save_img(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        save = Img.objects.create(user_name=data['user_name'], imglink=data['link'])
        save.save()
    else:
        HttpResponseRedirect('/')

@login_required
def save_file(request):
    return 0