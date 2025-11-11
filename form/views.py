from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Book
from .forms import BookForm
def home(request):
    if request.method == "POST":
        data = BookForm(request.POST, request.FILES)
        print("Forma yuborildi:", data.is_valid())

        if data.is_valid():
            Book.objects.create(
                title=data.cleaned_data["title"],
                author=data.cleaned_data["author"],
                desc=data.cleaned_data["desc"],
                image=data.cleaned_data["image"],
                price=data.cleaned_data["price"],
                is_active=data.cleaned_data["is_active"],
            )
    else:
        data = BookForm()

    

    context = {
        'books':Book.objects.all(),
        'form':BookForm()
    }

    return render(request,'index.html',context=context)
