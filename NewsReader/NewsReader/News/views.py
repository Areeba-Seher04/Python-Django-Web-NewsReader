from django.shortcuts import render,get_object_or_404,redirect
from .models import Channel,FChannel
import urllib.request as urlr
import json
from gtts import gTTS
import os
#verify the password as it is in database or not
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages


def get_user_channels(request):
    user = request.user
    userid = user.id
    user_channels = Channel.objects.filter(users_id=userid)
    return user_channels

def list(request):
    all_channels = FChannel.objects.all()
    param = {'all_channels': all_channels}
    return render(request, 'News/list.html',param)


def add_channels(request,album_id):
    if request.user.is_authenticated:
        album = get_object_or_404(FChannel, pk=album_id)
        channel = Channel(users=request.user, channel_title=album.channel_title, channel_logo=album.channel_logo, album=album,
                        channel_call=album.channel_call)
        channel.save()
        params = {'channel':channel}
        return render(request,'News/index.html',params)
    else:
        messages.info(request, 'You should be login to add channels')
        return redirect("News:list")
    

def userchannel(request):
    if request.user.is_authenticated:
        user_channels = get_user_channels(request)
        params = {'user_channels':user_channels}
        return render(request, 'News/channel.html', params)
    else:
        messages.info(request, 'You should be login to see your channels')
        return redirect("News:list")


def delete(request,channel_id):
    if request.user.is_authenticated:
        channel = Channel.objects.get(pk=channel_id)
        channel.delete()
        user_channels = get_user_channels(request)
        params = {'user_channels': user_channels}
        return render(request, 'News/channel.html', params)
    else:
        messages.info(request, 'You should be login to delete channels')
        return redirect("News:list")


def detail(request,album_id):
    if request.user.is_authenticated:
        channel = get_object_or_404(Channel, pk=album_id)
        channel_code = channel.channel_call
        # S='https://newsapi.org/v2/top-headlines?sources='+str(channel_code)+'&apiKey=189258ea3b8d4fa6a6b9520456f8133c'
        channel_url = urlr.urlopen('https://newsapi.org/v2/top-headlines?sources='+str(channel_code)+'&apiKey=189258ea3b8d4fa6a6b9520456f8133c')
        myjson = channel_url.read()
        a = json.loads(myjson.decode())
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        language = 'en'
        dic = []
        count_id = 0
        for news in a["articles"]:
            dic.append(
                {
                'title':news['title'],
                'description':news['description'],
                'url':news['url'],
                'urlToImage':news['urlToImage'],
                'speechpath':'/media/TEXT{}.mp3'.format(count_id)
                }
                )
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media\TEXT{}.mp3'.format(count_id))
            myobj = gTTS(text=news['description'], lang=language, slow=False)
            myobj.save(MEDIA_ROOT)
            count_id += 1

        os.system("mpg321 welcome.mp3")
        params = {"dic":dic}
        return render(request, 'News/detail.html', params)
    else:
        messages.info(request, 'Login required')
        return redirect("News:list")


class UserFromView(View):
    form_class = UserForm              #forms.py
    template_name = 'News/registration_form.html'

    def get(self ,request):            #display blank form
        form = self.form_class(None)   #none means by default it has no data
        return render(request,self.template_name,{'form':form})

    def post(self,request):            #process form data into database(add info into database)
        form = self.form_class(request.POST)    #request.post , the information that they type in the forms
        if form.is_valid():
            user = form.save(commit=False)  #create the objects for the form but doesnot save it to database
            username = form.cleaned_data['username']     #clean normalized data (same format i/p)
            password = form.cleaned_data['password']
            user.set_password(password)   #to change user password
            user.save()    #save all in database
        return render(request, self.template_name, {'form': form})

