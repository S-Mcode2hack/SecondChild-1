from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Profile
from . import forms

# main dashboard content
# cards with profiles
# search filter to filter out profiles
# profile


# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    profile = Profile.objects.get(user=user)
                    print(profile)
                    if not profile.is_complete:
                        return redirect("edit-profile")
                    else:
                        return redirect("home")
                else:
                    messages.error(request, "Invalid username or password")
        else:
            form = forms.LoginForm()

    context = {"form": form, "title": "Login"}
    return render(request, "users/login.html", context=context)


@login_required(login_url="login")
def logoutPage(request):
    logout(request)
    return redirect("home")


def signUpPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = forms.UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("edit_profile")
        else:
            form = forms.UserForm()

    context = {"form": form, "title": "Sign Up"}
    return render(request, "users/signup.html", context=context)


@login_required(login_url="login")
def editProfilePage(request):
    if request.method == "POST":
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            Profile.objects.filter(user=request.user).update(is_complete=True)
            return redirect("home")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = forms.ProfileForm()

    context = {"form": form, "title": "Edit Profile"}
    return render(request, "users/edit_profile.html", context=context)


@login_required(login_url="login")
def ProfilePage(request, username):
    user = User.objects.get(username=username)

    context = {"title": "Profile", "user": user}
    return render(request, "users/profile.html", context=context)
