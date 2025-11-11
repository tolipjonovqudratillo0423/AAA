from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    desc = forms.CharField(widget=forms.Textarea)
    image = forms.FileField(required=False)
    price = forms.IntegerField()
    is_active = forms.BooleanField(required=False, initial=True)


    