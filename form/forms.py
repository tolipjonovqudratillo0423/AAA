from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    desc = forms.CharField(widget=forms.Textarea,max_length=30)
    image = forms.FileField(required=True)
    price = forms.IntegerField()
    is_active = forms.BooleanField(required=False, initial=True)

    def clean_title(self):
        tittle = self.cleaned_data["title"]
        if not tittle.istitle():
            raise forms.ValidationError("Title Notugri Yozilgan Iltimos Tug'ri Yozing!!!")
        return tittle
    