import csv
import json

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

from .forms import CustomAuthenticationForm, CustomUserCreationForm

User = get_user_model()


def SignUp(request):
    if request.method == "POST":
        form = CustomUserCreationForm()
        f_login = CustomAuthenticationForm()
        if request.POST.get("submit") == "Sign Up":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user, backend="accounts.backend.EmailBackend")
                try:
                    url = request.GET["next"]
                except:
                    url = "home"
                return redirect(url)

        elif request.POST.get("submit") == "Login":
            f_login = CustomAuthenticationForm(data=request.POST)
            if f_login.is_valid():
                user = f_login.get_user()
                login(request, user, backend="accounts.backend.EmailBackend")
                try:
                    url = request.GET["next"]
                except:
                    url = "home"
                return redirect(url)

    else:
        form = CustomUserCreationForm()
        f_login = CustomAuthenticationForm()

    return render(request, "initsignup.html", {"form": form, "f_login": f_login})


def Logout(request):
    logout(request)
    return redirect("home")


# Create your views here.
