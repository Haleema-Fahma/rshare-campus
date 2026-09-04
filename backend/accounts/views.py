from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("dashboard")

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


class UserLoginView(LoginView):

    template_name = "accounts/login.html"

    redirect_authenticated_user = True

    def get_success_url(self):
        return "/dashboard/"


@login_required
def dashboard(request):

    return render(
        request,
        "accounts/dashboard.html"
    )