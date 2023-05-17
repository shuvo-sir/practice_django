from django.shortcuts import render
from .forms import BuildingAdd
# Create your views here.
def customer(request):
    return render(request, "Review/review.html")



def building_form(request):
    if request.method == "POST":
        frm = BuildingAdd(request.POST)
        if frm.is_valid():
            frm.save()

    else:

        frm = BuildingAdd
    return render(request,"Review/building.html", {"form" : frm})

