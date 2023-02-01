from django.http import HttpResponse
from django.shortcuts import render
from . import forms

def old_home_Page(request):
    return HttpResponse('Hello Mse, yoh')

def home_page(request):
    context = {
        "title" : "Hello world",
        "content": "Welcome to the home page"
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        "title" : "About page",
        "content": "This is the about page"
    }
    return render(request, 'home_page.html', context)

def contact_page(request):
    contact_form = forms.ContactForm(request.POST or None)

    context = {
        "title" : "contact page",
        "content": "Welcome to the contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("conent"))
    return render(request, 'contact/view.html', context)