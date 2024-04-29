from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse_lazy


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


def login_view(request):
    content = {"message": None}
    if request.method == "POST":
        name = request.POST.get("username")
        passw = request.POST.get("password")

        if not User.objects.filter(username=name).exists():
            # messages.error(request, "User not available")
            content["message"] = "User not available"
        else:
            user = authenticate(username=name, password=passw)
            if user is not None:
                login(request, user)
                messages.success(request, f"{user} Logged in successfully")
                return redirect("home")
            else:
                content["message"] = "Password not matched"

    return render(request, "registration/login.html", content)


def logout_view(request):
    logout(request)
    return redirect("login")
