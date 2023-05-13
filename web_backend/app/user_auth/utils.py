from django.contrib.auth.models import User
from django.contrib import messages
from src import settings
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate, login
from app.user_auth.forms import RegisterForm
from .tasks import send_email_task


def get_user_by_email_request(request) -> User:
    if request.method != "POST":
        return None

    email = request.POST.get("email")
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, "No user with that email address exists.")
        return None

    return user


def send_forget_password_email(request, user, email) -> bool:
    token_generator = PasswordResetTokenGenerator()
    token = token_generator.make_token(user)

    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

    subject = "Reset your password"
    reset_password_link = f"http://127.0.0.1:8000/reset_password/{uidb64}/{token}"

    message = f"Hi {user.username}, you can reset your password by clicking on the link below:{reset_password_link}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_email_task.apply_async(args=[subject, message, email_from, recipient_list])
    return True


def get_user_from_reset_password_link(uidb64, token) -> User:
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and PasswordResetTokenGenerator().check_token(user, token):
        return user
    else:
        return None


def login_web(request) -> bool:
    user = get_user_from_request(request)

    if user is None:
        messages.error(request, "Username or email is not exists")
        return False

    password = request.POST["password"]
    user = authenticate(request, username=user.username, password=password)
    if user is None:
        messages.error(request, "Password is incorrect")
        return False

    login(request, user)
    return True


def register_web(request) -> bool:
    form = RegisterForm(request.POST)

    if not form.is_valid():
        messages.error(request, "An error has occurred during registration")
        return False

    user = form.save(commit=False)
    user.username = user.username.lower()

    if User.objects.filter(username=user.username).exists():
        messages.error(request, "Username already exists")
        return False

    if User.objects.filter(email=user.email).exists():
        messages.error(request, "Email already exists")
        return False

    user.save()
    messages.success(request, "User was created successfully")
    login(request, user)
    return True


def get_user_from_request(request) -> User:
    username = request.POST["username"]
    print(username)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

    return user
