from django.shortcuts import render, HttpResponseRedirect
from .forms import BuildingAdd
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def customer(request):
    return render(request, "Review/review.html")


# Registration
def building_form(request):
    if request.method == "POST":
        frm = BuildingAdd(request.POST)
        if frm.is_valid():
            frm.save()

    else:

        frm = BuildingAdd
    return render(request,"Review/building.html", {"form" : frm})



# Login
def login_form(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request, data = request.POST)
        if frm.is_valid():
            usern = frm.cleaned_data["username"]
            userp = frm.cleaned_data["password"]
            user = authenticate(username = usern, password = userp)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/rew/success')
    else:
        frm = AuthenticationForm()
        return render(request, "Review/login.html", {"form" : frm})



# Successfully Login
def login_success(request):
    return render(request,"Review/success.html")



# Log out
def logout_form(request):
    logout(request)
    return HttpResponseRedirect("/rew/login/")