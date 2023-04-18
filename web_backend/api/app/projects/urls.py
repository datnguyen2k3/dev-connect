from django.urls import path
from . import views

urlpatterns = [
    #projects
    path("", views.get_projects_view, name="get_projects"),
    path("add/", views.put_project_view, name="put_project"),
    path(
        "<uuid:project_id>/", views.get_single_project_view, name="get_single_project"
    ),
    path("<uuid:project_id>/edit/", views.edit_project_view, name="edit_project"),
    path("<uuid:project_id>/delete/", views.delete_project_view, name="delete_project"),
    # reviews
    path("<uuid:project_id>/reviews/", views.get_reviews_view, name="get_reviews"),
    path(
        "<uuid:project_id>/reviews/<uuid:review_id>/",
        views.get_single_review_view,
        name="get_single_review",
    ),
    path(
        "<uuid:project_id>/reviews/add/",
        views.put_review_view,
        name="put_review",
    ),
    path(
        "<uuid:project_id>/reviews/<uuid:review_id>/delete/",
        views.delete_review_view,
        name="delete_review",
    ),
    path(
        "<uuid:project_id>/reviews/<uuid:review_id>/edit/",
        views.edit_review_view,
        name="edit_review",
    ),
]
