from django.db import models

# Message model
class Message(models.Model):
    user_name = models.CharField(max_length=20)
    message = models.CharField(max_length=140)
    time = models.CharField(max_length=20,null=True)

    is_img = models.BooleanField(default=False)

class File(models.Model):
	user_name2 = models.CharField(max_length=20)
	filelink = models.CharField(max_length=40)