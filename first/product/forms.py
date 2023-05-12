from django import forms

class RecentProduct(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    laptop = forms.CharField(label= "Enter your laptop name: ")
    email = forms.EmailField(initial = "shuvo-sir@gmail.com")
    about = forms.CharField(help_text = "Describe about your laptop")
    text_area = forms.CharField(widget=forms.Textarea(attrs={"rows": 15, "cols": 50}))
    check_box = forms.CharField(widget=forms.CheckboxInput)
    files = forms.CharField(widget=forms.FileInput)
    shuvo = forms.BooleanField(label = "Do you love Shuvo?")

    def clean(self):
        cleaned_data = super().clean()
        password_match = self.cleaned_data["password"]
        re_password_match = self.cleaned_data["re_password"]

        if password_match != re_password_match:
            raise forms.ValidationError("Password dosen't match")