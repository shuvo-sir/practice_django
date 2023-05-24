from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request, "lo_up/login.html")


def SignUp(request):
    return render(request, "lo_up/signup.html")    