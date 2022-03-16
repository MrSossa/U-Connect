"""UConnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as mainViews
<<<<<<< HEAD
from account import views as accViews
from django.conf.urls.static import static
from django.conf import settings

=======
from main.views import showmap,showroute
>>>>>>> d67c80dffdf3129615cfc16296cac64457e5a531

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainViews.home),
<<<<<<< HEAD
    path('about/', mainViews.about),
=======
    path('<str:lat1>,<str:long1>,<str:lat2>,<str:long2>',showroute,name='showroute'),
    path('setroute',showmap,name='showmap'),
>>>>>>> d67c80dffdf3129615cfc16296cac64457e5a531
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
