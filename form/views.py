from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Book
from .forms import BookForm
def home(request):
    data = BookForm(request.POST, request.FILES)
    if request.method == "POST":
        
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
            return redirect("home")
        else:
            print(data.errors)
        
    context = {
        'books':Book.objects.all(),
        'form':data
    }
    return render(request,'index.html',context=context)
