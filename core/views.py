from django.shortcuts import render


# Create your views here.
def homePage(request):
    context = {"title": "Home"}
    return render(request, "core/home.html", context)
