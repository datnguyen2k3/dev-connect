from django.shortcuts import redirect, render
from django.contrib import messages
from app.user_auth import utils
from app.user_auth.forms import RegisterForm
from django.http import Http404
from django.contrib.auth import logout


# Create your views here.
def reset_password_email_view(request):
    if request.method == "POST":
        user = utils.get_user_by_email_request(request)

        if user is not None:
            utils.send_forget_password_email(request, user, user.email)
            return redirect("user_auth:reset_password_sent")

    return render(request, "user_auth/reset_password_email.html", {})


def reset_password_sent_view(request):
    return render(request, "user_auth/reset_password_sent.html", {})


def reset_password_view(request, uidb64, token):
    user = utils.get_user_from_reset_password_link(uidb64, token)
    if user is None:
        return Http404("Page not found")

    if request.method == "POST":
        new_password = str(request.POST.get("new_password"))
        confirm_password = str(request.POST.get("comfirm_password"))

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("user_auth:reset_password_confirm", uidb64, token)
        else:
            user.set_password(new_password)
            user.save()
            return redirect("user_auth:reset_password_complete")

    return render(request, "user_auth/reset_password.html", {})


def reset_password_complete_view(request):
    return render(request, "user_auth/reset_password_complete.html", {})


def login_view(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("users:profiles")

    if request.method == "POST" and utils.login_web(request):
        return redirect("users:profiles")

    return render(request, "user_auth/login-register.html", {"page": page})


def logout_view(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect("user_auth:login")


def register_view(request):
    page = "register"
    form = RegisterForm()

    if request.method == "POST" and utils.register_web(request):
        return redirect("users:edit-profile")

    return render(request, "user_auth/login-register.html", {"page": page, "form": form})
