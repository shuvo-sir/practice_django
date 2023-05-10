from django.shortcuts import render
from product.forms import RecentProduct



# Create your views here.
def product(request):
    return render(request, "Product/product.html")



def details(request):
    frm = RecentProduct(auto_id= True, label_suffix= " ")
    return render(request, "Product/recent.html",{"form" : frm})
