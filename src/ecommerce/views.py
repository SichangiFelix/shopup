from django.http import HttpResponse
from django.shortcuts import render ,redirect
from . import forms
from django.contrib.auth import authenticate, login, get_user_model

def old_home_Page(request):
    return HttpResponse('Hello Mse, yoh')

def login_page(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        print(form.cleaned_data.get("username"))
        password = form.cleaned_data.get("password")
        print(form.cleaned_data.get("password"))
        user = authenticate(request, username = username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            context["form"] = forms.LoginForm()
            return redirect("/")
        else:
            print("error")

    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = forms.RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)

def home_page(request):
    context = {
        "title" : "Hello world",
        "content": "Welcome to the home page",
        "premium_content": "Yeeeeey premium working"
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