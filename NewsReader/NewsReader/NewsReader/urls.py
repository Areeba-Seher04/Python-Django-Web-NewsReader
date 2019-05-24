from django.contrib import admin
from django.urls import include , path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('News/',include('News.urls')),
path('login/',auth_views.LoginView.as_view(template_name='News/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='News/logout.html'),name='logout'),
    ]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)