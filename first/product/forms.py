from django import forms

class RecentProduct(forms.Form):
    mobile = forms.CharField()
    laptop = forms.CharField()
    email = forms.EmailField()