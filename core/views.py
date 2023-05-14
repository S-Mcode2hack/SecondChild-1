from django.shortcuts import render
from users.models import Profile


# Create your views here.
def homePage(request):
    currentUser = request.user
    profiles = Profile.objects.exclude(id=currentUser.id)

    q = request.GET.get("q") if request.GET.get("q") else ""

    context = {"title": "Home", "profiles": profiles}
    return render(request, "core/home.html", context)
