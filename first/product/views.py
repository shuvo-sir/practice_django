from django.shortcuts import render
from product.forms import RecentProduct
from django.http import HttpResponseRedirect



# Create your views here.
def product(request):
    return render(request, "Product/product.html")



def send(request):
    return render(request, "Product/submit.html")


def details(request):
    if request.method == "POST":
        frm = RecentProduct(request.POST)
        if frm.is_valid():
            print("Valid form")    
            return HttpResponseRedirect("/pro/successfully")


    else:
        frm = RecentProduct(auto_id= True, label_suffix= " ")
        print("GET statement")
    return render(request, "Product/recent.html",{"form" : frm})
