import json
import datetime

from django.shortcuts import render
from .models import Message
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# this view is the base view
@login_required(login_url='/login/')
def chat_index(request):
    context = {
        'messages': Message.objects.all(),
        # 'path': 'upload_img'+Message.objects.all(),
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
            msg = Message.objects.create(user_name=msg_obj['user_name'], message=msg_obj['message'],time = datetime.datetime.now())
            msg.save()

        except:
            print("error saving message")
            return HttpResponse("error")
        return HttpResponse("success")
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def uploadfile(request):
    if request.method == 'POST':
        data_file = json.loads(request.body.decode('utf-8'))
        try:
            file = Message.objects.create(user_name = data_file['username'], message = data_file['namefile'], is_img=True, time = datetime.datetime.now())
            file.save()
        except:
            return HttpResponse('error')
        return HttpResponse('Success')
    else:
        return HttpResponseRedirect('/login')