from django.urls import path
from app.users import views

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
    path(
        "account/work-experience/add/", views.add_work_experience_view, name="add-skill"
    ),
    path(
        "account/work-experience/<uuid:skill_id>/edit",
        views.edit_work_experience_view,
        name="edit-work-experience",
    ),
    path(
        "account/work-experience/<uuid:skill_id>/delete",
        views.delete_work_experience_view,
        name="delete-work-experience",
    ),
    path("account/edit/", views.edit_profile_view, name="edit-profile"),
    path("inbox/", views.inbox, name="inbox"),
    path("message/<str:pk>/", views.viewMessage, name="message"),
    path("create-message/<str:pk>/", views.createMessage, name="create-message"),
]
