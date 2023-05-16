from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def customer(request):
    return render(request, "Review/review.html")



def building_form(request):
    if request.method == "POST":
        frm = UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()

    else:

        frm = UserCreationForm
    return render(request,"Review/building.html", {"form" : frm})

