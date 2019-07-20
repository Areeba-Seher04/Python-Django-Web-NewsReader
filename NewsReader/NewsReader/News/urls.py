from django.urls import include , path
from .import views
from django.contrib.auth import views as auth_views
app_name ='News'

urlpatterns = [
    #News/
    path('', views.userchannel , name='userchannel'),
    #/News/1
    path('<int:album_id>/', views.index , name='index'),
    path('list/', views.list , name='list'),
    path('detail/<int:album_id>/',views.detail,name='detail'),
    #News/register/
    path('register/', views.UserFromView.as_view() , name='register'),
    #/News/id/
    path('delete/<int:channel_id>/',views.delete,name='delete'),
    path('login/',auth_views.LoginView.as_view(template_name='News/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='News/logout.html'),name='logout'), 
    ]
