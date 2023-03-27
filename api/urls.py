from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("", views.get_routes_view, name="get_routes"),
    # auth
    path("users/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # projects
    path("projects/", views.get_projects_view, name="get_projects"),
    path(
        "projects/<str:project_id>/",
        views.get_single_project_view,
        name="get_single_project",
    ),
    path("projects/<str:project_id>/edit/", views.edit_project_view, name="edit_project"),
    # reviews
    path(
        "projects/<str:project_id>/reviews/", views.get_reviews_view, name="get_reviews"
    ),
    path(
        "projects/<str:project_id>/reviews/<str:review_id>/",
        views.get_single_review_view,
        name="get_single_review",
    ),
    path(
        "projects/<str:project_id>/reviews/add/",
        views.post_review_view,
        name="post_review",
    ),
    path(
        "projects/<str:project_id>/reviews/<str:review_id>/delete/",
        views.delete_review_view,
        name="delete_review",
    ),
    path(
        "projects/<str:project_id>/reviews/<str:review_id>/edit/",
        views.edit_review_view,
        name="edit_review",
    ),
]
