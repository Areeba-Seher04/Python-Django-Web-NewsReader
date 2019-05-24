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
#189258ea3b8d4fa6a6b9520456f8133c
def list(request):
    all_channels = FChannel.objects.all()
    param = {'all_channels': all_channels}
    return render(request, 'News/list.html',param)


def index(request,album_id):
        #album = FChannel.objects.get(pk=album_id)
        album = get_object_or_404(FChannel, pk=album_id)
        print(album)
        print(album.channel_title)
        print(album.channel_logo)
        print(album_id)
        print("user",request.user)
        a = Channel(users=request.user, channel_title=album.channel_title, channel_logo=album.channel_logo, album=album,
                    channel_call=album.channel_call)
        a.save()
        print("a",a)
        params = {'a':a}
       

        return render(request,'News/index.html',params)

def userchannel(request):
    user = request.user
    userid = user.id
    all_channels = Channel.objects.filter(users_id=userid)
    print("all",all_channels)
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
    print("D2",D2)
    print("D1",D1)
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
    # params= {'U':U,'S':S}
    params = {'channel': channel,'N1':N1 , 'I1':I1 , 'N2':N2 , 'I2':I2,'D1':D1,'D2':D2,'U':U,'N3':N3 , 'I3':I3,'D3':D3,'U1':U1,'U2':U2,'U3':U3}
    # params = {'channel': channel}
    print("chan",channel)
    return render(request, 'News/detail.html', params)


#def detail(request,albums_id):
    #channel = get_object_or_404(Channel, pk=album_id)##instead of above line
 #   channel = Channel.objects.filter(albums_id=albums_id)
  #print("channel",channel)
  #  t = channel.chan_set.all()
   # U=t[0]

    #S='https://newsapi.org/v2/top-headlines?sources='+str(U)+'&apiKey=189258ea3b8d4fa6a6b9520456f8133c'

    #raw = urlr.urlopen('https://newsapi.org/v2/top-headlines?sources='+str(U)+'&apiKey=189258ea3b8d4fa6a6b9520456f8133c')

    #myjson = raw.read()
    #a = json.loads(myjson.decode())
    #N1 = a['articles'][1]['title']
    #D1 = a['articles'][1]['description']
    #I1 = a['articles'][1]['urlToImage']
    #N2 = a['articles'][2]['title']
    #D2 = a['articles'][2]['description']
    #I2 = a['articles'][2]['urlToImage']
    #language = 'en'
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #MEDIA_ROOT = os.path.join(BASE_DIR, 'media\TEXT.mp3')
    #MEDIA_ROOT1 = os.path.join(BASE_DIR, 'media\TEXT1.mp3')
    #myobj = gTTS(text=D1, lang=language, slow=False)
    #myobj1 = gTTS(text=D2, lang=language, slow=False)
    #myobj.save(MEDIA_ROOT)
    #myobj1.save(MEDIA_ROOT1)
    #os.system("mpg321 welcome.mp3")
    #params= {'U':U,'S':S}
    #params = {'channel': channel,'N1':N1 , 'I1':I1 , 'N2':N2 , 'I2':I2,'D1':D1,'D2':D2}
    #params = {'channel': channel}
    #params = {'a':a,'t':t,'U':U}
    #return render(request,'News/detail.html',params)




class UserFromView(View):
    form_class = UserForm #forms.py
    template_name = 'News/registration_form.html'

    #display blank form
    def get(self ,request):
        form = self.form_class(None) #none means by default it has no data
        return render(request,self.template_name,{'form':form})

    #process form data into database(add info into database)
    def post(self,request):
        #request.post , the information that they type in the forms
        form = self.form_class(request.POST)
        if form.is_valid():
            #create the objects for the form but doesnot save it to database
            user = form.save(commit=False)

            #clean normalized data (same format i/p)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #to change user password
            user.set_password(password)
            #save all in database
            user.save()

            #user is now registered for the website


            #authenticate and login the user and returns user objectsif credentials are correct
            #ser = authenticate(username=username,password=password)
            #user returns name either bucky etc

           # user is not None:
            #   if user.is_active:
             #      login(request,user)
                    #after login return to homepage
              #     return redirect('News:index')


        #if not login correctly then return to the blank form
        return render(request, self.template_name, {'form': form})




def profile(request):
    args = {'user':request.user}
    return render(request,'News/index.html',args)