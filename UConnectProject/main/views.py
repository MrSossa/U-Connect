from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import Route

import folium
from . import getroute

# Create your views here.

def home(request):
    return render(request, 'home.html')

def showmap(request):
    return render(request,'showmap.html')

def showroute(request,lat1,long1,lat2,long2):
    figure = folium.Figure()
    lat1,long1,lat2,long2=float(lat1),float(long1),float(lat2),float(long2)

    Route.objects.create(lat1=lat1,long1=long1,lat2=lat2,long2=long2)

    route=getroute.get_route(long1,lat1,long2,lat2)
    m = folium.Map(location=[(route['start_point'][0]),
                                 (route['start_point'][1])], 
                       zoom_start=15)
    m.add_to(figure)
    folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)
    folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)
    folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)
    figure.render()
    context={'map':figure}
    return render(request,'showroute.html',context)

def showRoutes(request):
    routes = Route.objects.all()
    #routes = [[6.2202708,-75.6181945],[6.2427035,-75.5831564],[6.275552,-75.6013728],[6.2750283,-75.5419109],[6.2327582,-75.5542372],[6.2076047,-75.5814088]]
    figure = folium.Figure()
    m = folium.Map(location=[6.1997147,-75.5814568], zoom_start=15)

    for i in routes:
        r = i.data()
        lat1,long1,lat2,long2=float(r[0]),float(r[1]),float(r[2]),float(r[3])
        route=getroute.get_route(long1,lat1,long2,lat2)
        folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)
        folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)
        folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)    
    m.add_to(figure)
    figure.render()
    context={'map':figure}
    return render(request,'showAllRoutes.html',context)