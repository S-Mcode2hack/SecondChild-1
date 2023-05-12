from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . import forms


# Create your views here.
def loginPage(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = forms.LoginForm()

    context = {"form": form, "title": "Login"}
    return render(request, "users/login.html", context=context)


def logoutPage(request):
    logout(request)
    return redirect("home")


def signUpPage(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(user)
            return redirect("edit_profile")
    else:
        form = forms.UserForm()

    context = {"form": form, "title": "Sign Up"}
    return render(request, "users/signup.html", context=context)


def editProfilePage(request):
    if request.method == "POST":
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = forms.ProfileForm()

    return render(request, "users/edit_profile.html", context={"form": form})


def ProfilePage(request, username):
    user = User.objects.get(username=username)
    return render(request, "users/profile.html", context={"user": user})
