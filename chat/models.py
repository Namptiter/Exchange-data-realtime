from django.db import models

# Message model
class Message(models.Model):
    user_name = models.CharField(max_length=20)
    message = models.CharField(max_length=140)

class Img(models.Model):
	user_name1 = models.CharField(max_length=20)
	imglink = models.CharField(max_length=40)

class File(models.Model):
	user_name2 = models.CharField(max_length=20)
	filelink = models.CharField(max_length=40)