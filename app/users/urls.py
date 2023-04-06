from django.urls import path
from app.users import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("", views.profiles_view, name="index"),
    path("developers/", views.profiles_view, name="profiles"),
    path(
        "developers/<uuid:profile_id>/",
        views.single_profile_view,
        name="single-profile",
    ),
    path("account/", views.account_view, name="account"),
    path("account/skills/add/", views.add_skill_view, name="add-skill"),
    path(
        "account/skills/<uuid:skill_id>/edit", views.edit_skill_view, name="edit-skill"
    ),
    path(
        "account/skills/<uuid:skill_id>/delete",
        views.delete_skill_view,
        name="delete-skill",
    ),
    path("account/edit/", views.edit_profile_view, name="edit-profile"),
    path("inbox/", views.inbox, name="inbox"),
    path("message/<str:pk>/", views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),
]
