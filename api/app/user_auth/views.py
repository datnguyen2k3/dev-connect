from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from app.user_auth.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



@api_view(["PUT"])
def register_view(request):
    form = RegisterForm(request.POST)

    if not form.is_valid():
        return Response("An error has occurred during registration")

    user = form.save(commit=False)
    user.username = user.username.lower()

    if User.objects.filter(username=user.username).exists():
        return Response("Username already exists")

    if User.objects.filter(email=user.email).exists():
        return Response("Email already exists")

    user.save()
    return Response("User was created successfully")

@api_view(["POST"])
def login_view(request):
    username = request.data.get("username", "")
    password = request.data.get("password", "")
    
    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response("Username or password is incorrect")
    
    login(request, user)
    return Response("User was logged in successfully")
    