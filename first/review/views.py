from django.shortcuts import render


# Create your views here.
def customer(request):
    return render(request, "Review/review.html")