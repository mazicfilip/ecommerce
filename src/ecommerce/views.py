from django.contrib.auth import authenticate, login,  get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .forms import ContactForm, LoginForm, RegisterForm


User = get_user_model()


def home_page(request):
    context = {
        "title": "Hello World!",
        "content": "Welcome to homepage"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAAAAAAAAH"

    return render(request, "home_page.html", context)


def orders_page(request):
    return render(request, "orders_page.html", {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Welcome to contact page",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    # print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # context["form"] = LoginForm()
            # print(request.user.is_authenticated)
            redirect("/login")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)


def register_page(request):
    form = RegisterForm(request.POST or None)
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
