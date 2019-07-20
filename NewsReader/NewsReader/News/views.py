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


def list(request):
    all_channels = FChannel.objects.all()
    param = {'all_channels': all_channels}
    return render(request, 'News/list.html',param)


def index(request,album_id):
        album = get_object_or_404(FChannel, pk=album_id)
        a = Channel(users=request.user, channel_title=album.channel_title, channel_logo=album.channel_logo, album=album,
                    channel_call=album.channel_call)
        a.save()
        params = {'a':a}
        return render(request,'News/index.html',params)
    

def userchannel(request):
    user = request.user
    userid = user.id
    all_channels = Channel.objects.filter(users_id=userid)
    params = {'all_channels':all_channels}
    return render(request, 'News/channel.html', params)


def delete(request,channel_id):
    channel = Channel.objects.get(pk=channel_id)
    channel.delete()
    user = request.user
    userid = user.id
    all_channels = Channel.objects.filter(users_id=userid)
    print("all", all_channels)
    params = {'all_channels': all_channels}
    return render(request, 'News/channel.html', params)


def detail(request,album_id):
    a = album_id
    channel = get_object_or_404(Channel, pk=album_id)
    U = channel.channel_call
    S='https://newsapi.org/v2/top-headlines?sources='+str(U)+'&apiKey=189258ea3b8d4fa6a6b9520456f8133c'
    raw = urlr.urlopen('https://newsapi.org/v2/top-headlines?sources='+str(U)+'&apiKey=189258ea3b8d4fa6a6b9520456f8133c')
    myjson = raw.read()
    a = json.loads(myjson.decode())
    N1 = a['articles'][1]['title']
    D1 = a['articles'][1]['description']
    U1 = a['articles'][1]['url']
    I1 = a['articles'][1]['urlToImage']
    N2 = a['articles'][2]['title']
    D2 = a['articles'][2]['description']
    U2 = a['articles'][2]['url']
    I2 = a['articles'][2]['urlToImage']
    N3 = a['articles'][3]['title']
    D3 = a['articles'][3]['description']
    U3 = a['articles'][3]['url']
    I3 = a['articles'][3]['urlToImage']
    language = 'en'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media\TEXT.mp3')
    MEDIA_ROOT1 = os.path.join(BASE_DIR, 'media\TEXT1.mp3')
    MEDIA_ROOT2 = os.path.join(BASE_DIR, 'media\TEXT2.mp3')
    myobj = gTTS(text=D1, lang=language, slow=False)
    myobj1 = gTTS(text=D2, lang=language, slow=False)
    myobj2 = gTTS(text=D3, lang=language, slow=False)
    myobj.save(MEDIA_ROOT)
    myobj1.save(MEDIA_ROOT1)
    myobj2.save(MEDIA_ROOT2)
    os.system("mpg321 welcome.mp3")
    params = {'channel': channel,'N1':N1 , 'I1':I1 , 'N2':N2 , 'I2':I2,'D1':D1,'D2':D2,'U':U,'N3':N3 , 'I3':I3,'D3':D3,'U1':U1,'U2':U2,'U3':U3}
    return render(request, 'News/detail.html', params)


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



