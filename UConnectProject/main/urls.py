from django.urls import URLPattern, path
from main.views import showmap,showroute,showRoutes, login
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('myRoutes/',views.myRoutes,name='myRoutes'),
    path('login/',login, name='login'),
    path('setroute/<str:lat1>,<str:long1>,<str:lat2>,<str:long2>',showroute,name='showroute'),
    path('setroute',showmap,name='showmap'),
    path('showroutes',showRoutes,name='showroutes'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)