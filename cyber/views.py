from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# from cyber.models import UserCheck

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# @login_required(login_url="/login")
def start(request):
    user = User.objects.get(username = request.user)
    check_seller = User.objects.filter(userx = user).last()
    print(check_seller, "xxxxxxxxxxx")
    if check_seller:
        if check_seller.is_seller:
                return render(request, "index.html")
        else:
                return HttpResponse("your are not authorize....")
    else:
            return HttpResponse("your are not authorize....")
    return render(request,"index.html") 



# @login_required(login_url="/login")
def index(request):
    return render(request,"index.html")



def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passwrd = request.POST.get("pass")

        checkuser = authenticate(username = username, password = passwrd)

        if checkuser is not None:
            login(request, checkuser)
            return redirect("index.html")


    return render(request, "loginpage.html")



def signuppage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        passsword = request.POST.get("pass")

        newuser = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = passsword)
        newuser.save()

        checkdata = User(userx = newuser, User = True)
        checkdata.save()

    return render(request, "signuppage.html")


def logutnow(request):
    logout(request)
    return redirect("login")