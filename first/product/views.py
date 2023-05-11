from django.shortcuts import render
from product.forms import RecentProduct



# Create your views here.
def product(request):
    return render(request, "Product/product.html")



def details(request):
    if request.method == "POST":
        frm = RecentProduct(request.POST)
        print(frm)
        print("POST statement")
        print(frm.cleaned_data)


    else:
        frm = RecentProduct(auto_id= True, label_suffix= " ")
        print("GET statement")
    return render(request, "Product/recent.html",{"form" : frm})
