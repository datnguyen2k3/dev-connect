from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.profiles_view, name="profiles"),
    path("<uuid:profile_id>/", views.single_profile_view, name="single-profile"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("account/", views.account_view, name="account"),
    path("account/skills/add/", views.add_skill_view, name='add-skill'),
    path("account/skills/<uuid:skill_id>/edit", views.edit_skill_view, name='edit-skill'),
    path("account/skills/<uuid:skill_id>/delete", views.delete_skill_view, name='delete-skill'),
    path('account/edit/', views.edit_profile_view, name='edit-profile'),
]
