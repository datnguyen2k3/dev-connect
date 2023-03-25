from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_routes_view, name="get_routes"),
    path("projects/", views.get_projects_view, name="get_projects"),
    path(
        "projects/<str:project_id>",
        views.get_single_project_view,
        name="get_single_project",
    ),
    
]
