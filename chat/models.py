from django.db import models

# Message model
class Message(models.Model):
    user_name = models.CharField(max_length=20,Null=True)
    message = models.CharField(max_length=140, Null=true)
    time = models.DateTimeField(auto_add_now = True)
    is_img = models.BooleanField(default=False)
class Img(models.Model):
	user_name1 = models.CharField(max_length=20)
	Img = models.ImageField()

class File(models.Model):
	user_name2 = models.CharField(max_length=20)
	filelink = models.CharField(max_length=40)