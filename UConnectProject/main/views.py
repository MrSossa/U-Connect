from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import Route
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from .models import *

import folium
import json
import random
from .forms import routesForms
from . import getroute

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created succesfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html', {'form':form})


def profile(request):
    return render(request, 'profile.html')

def myRoutes(request):
    routes = Route.objects.filter(Owner = request.user.username)
    myroutes = []
    lastroutes = []
    for i in routes:
        if (i.data()[5]):
            myroutes.append(i.data())
        else:
            lastroutes.append(i.data())
    context = {
        'myRoutes': myroutes,
        'lastRoutes': lastroutes
    }
    return render(request, 'myRoutes.html',context=context)

def myRoute(request,id):
    if (request.method == 'GET'):
        route = Route.objects.get(id = id)
        time =  ("%02d:%02d" % (route.startTime.hour,route.startTime.minute)) 
        f = routesForms({'route':route.route,
                        'description':route.description,
                        'petfriendly':route.petfriendly,
                        'startdate':route.startdate,
                        'startTime':time}
                        )
        figure = getroute.getRouteFigure(json.loads(route.route))
        context = {
            'form':f,
            'id':route.id,
            'map':figure,
        }
        return render(request, 'myRoute.html',context=context)
    return render(request, 'myRoute.html')

def deleteRoute(request,id):
    route = Route.objects.get(id = id)
    route.delete()
    return redirect('myRoutes')

def showmap(request):
    return render(request,'showmap.html')

def updateRoute(request,id):
    
    if request.method == 'POST':
        route = Route.objects.filter(id = id)
        route.update(Owner=request.user.username,
                            route=request.POST["route"].replace('\\\"',"\""),
                            startdate=request.POST["startdate"],
                            startTime=request.POST["startTime"],
                            description=request.POST["description"],
                            petfriendly = True if ("petfriendly" in request.POST) else False)
        
    return redirect('../../myRoutes')

def createRoute(request):
    if request.method == 'POST':
        print(type(json.loads(request.POST["route"])))
        Route.objects.create(Owner=request.user.username,
                            route=request.POST["route"],
                            startdate=request.POST["startdate"],
                            startTime=request.POST["startTime"],
                            description=request.POST["description"],
                            petfriendly = True if ("petfriendly" in request.POST) else False)
        
    return redirect('../myRoutes')

def showroute(request,lat1,long1,lat2,long2):
    #figure = folium.Figure()
    lat1,long1,lat2,long2=float(lat1),float(long1),float(lat2),float(long2)

    route=getroute.get_route(long1,lat1,long2,lat2)

    figure = getroute.getRouteFigure(route=route)
    f = routesForms({'route':json.dumps(route)})
    context={
        'map':figure,
        'form':f}
  
    return render(request,'showroute.html',context)

def generatePopPup(route):
    iframe = folium.IFrame("Usuario: "+str(route[1])
           +"<br> Reputacion: "+("★"*random.randint(0,5))
           +"<br> <a href=\"https://www.google.com/\">Entrar</a>")
    popup = folium.Popup(iframe, min_width=200,max_width=200)
    return popup

def showRoutes(request):
    routes = Route.objects.all()
    figure = folium.Figure()
    m = folium.Map(location=[6.1997147,-75.5814568], zoom_start=15)

    aux = 0
    for i in routes:
        r = i.data()

        route = json.loads(r[0])
        
        folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6,popup=generatePopPup(r)).add_to(m)
        folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)
        folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)
        aux += 1
    m.add_to(figure)
    figure.render()
    context={'map':figure}
    return render(request,'showAllRoutes.html',context)