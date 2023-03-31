from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.get_routes_view, name="get_routes"),
    # auth
    path("", include("api.app.devsearch_auth.urls")),
    path("projects/", include("api.app.projects.urls")),
    path("users/", include("api.app.users.urls")),
]
