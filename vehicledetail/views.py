from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from vehicledetail.models import addvehicle
# Create your views here.
def home(request):
    return render(request, 'vehicledetail/home.html')

def about(request):
    return HttpResponse("about page")

def add(request):
    return render(request, 'vehicledetail/add.html')

def addfill(request):
    if request.method=="POST":
        name=request.POST['name']
        photo=request.POST['photo']
        route=request.POST['route']
        speed=request.POST['speed']
        avgspeed=request.POST['avgspeed']
        engstatus=request.POST['engstatus']
        fuel=request.POST['fuel']
        temp=request.POST['temp']
        staticmap=request.POST['staticmap']
        print(name, route, speed, avgspeed, engstatus, fuel, temp)
        ad = addvehicle(name=name, photo=photo, route=route, speed=speed, avgspeed=avgspeed, engstatus=engstatus, fuel=fuel, temp=temp, staticmap=staticmap)
        ad.save()
        messages.success(request, "Vehicle is successfully added. Please check view details for list")
        return redirect("/")
    else:
        messages.error(request, "please try to add details again")
        return redirect("/")

def viewdetail(request):
    det = addvehicle.objects.all()
    context={
        'det':det
    }
    return render(request, "vehicledetail/details.html", context)
def updatedata(request, Sr):
    if request.method=="POST":
        pi = addvehicle.objects.get(pk=Sr)
        name=request.GET['name']
        photo=request.GET['photo']
        route=request.GET['route']
        speed=request.GET['speed']
        avgspeed=request.GET['avgspeed']
        engstatus=request.GET['engstatus']
        fuel=request.GET['fuel']
        temp=request.GET['temp']
        staticmap=request.GET['staticmap']
        print(name, route, speed, avgspeed, engstatus, fuel, temp)
        ad = addvehicle(name=name, photo=photo, route=route, speed=speed, avgspeed=avgspeed, engstatus=engstatus, fuel=fuel, temp=temp, staticmap=staticmap)
        ad.save()
        messages.success(request, "Vehicle is successfully Updated. Please check view details for list")
        return redirect("/")


    return render(request, "vehicledetail/update.html",{'Sr':Sr})

def deletedata(request ,Sr):
    if request.method == "POST":
        pi = addvehicle.objects.get(pk=Sr)
        pi.delete()
        return redirect("/")


def handlesignup(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        pwd1=request.POST["pwd1"]
        pwd2=request.POST["pwd2"]

        #checkpoints
        if(len(username)>3 and pwd1 == pwd2):
            myuser = User.objects.create_user(username, email, pwd1)
            myuser.save()
            messages.success(request, "You have successfully registered")
            return redirect("/")
        else:
            messages.error(request, "please try to sign in again")
            return redirect("/")

def handlelogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user = authenticate(username=loginusername , password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect('/')
        else:
            messages.error(request, "Invalid login . please try to log in again")


def handlelogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out. Thankyou")
    return redirect('/')

def furtherdetail(request, slug):
    more=addvehicle.objects.filter(slug=slug).first()
    con = {
        'more':more
    }
    return render(request, "vehicledetail/further.html", con)
        
    
