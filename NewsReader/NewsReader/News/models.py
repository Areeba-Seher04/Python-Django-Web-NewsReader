from django.db import models
from django.contrib.auth.models import User
#all_channels
class FChannel(models.Model):
   channel_title = models.CharField(default=True,max_length=250)
   channel_logo = models.FileField(default=True)
   channel_call = models.CharField(default=True,max_length=10000)


   def __str__(self):
       return (self.channel_title)
#userchannels
class Channel(models.Model):
    album = models.ForeignKey(FChannel,default=True, on_delete=models.CASCADE)
    users = models.ForeignKey(User,default=True,on_delete=models.CASCADE)
    channel_title = models.CharField(max_length=250)
    channel_logo = models.FileField(default=True)
    channel_call = models.CharField(default=True,max_length=10000)


    def __str__(self):
        #return (str(self.users))
        return (self.channel_title)


