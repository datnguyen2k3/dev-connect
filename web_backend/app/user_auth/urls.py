from django.urls import path
from app.user_auth import views

app_name = "user_auth"

urlpatterns = [
        
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    
    path(
        "reset_password/", 
        views.reset_password_email_view, 
        name="reset_password"
    ),
    path(
        "reset_password_sent/",
        views.reset_password_sent_view,
        name="reset_password_sent",
    ),
    path(
        "reset_password/<uidb64>/<token>/",
        views.reset_password_view,
        name="reset_password_confirm",
    ),
    path(
        "reset_password_complete/",
        views.reset_password_complete_view,
        name="reset_password_complete",
    ),
]