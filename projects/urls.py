from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('<uuid:project_id>/', views.single_project_view, name='single-project'),
    path('create-project/', views.createProject, name="create-project"),
    path('<uuid:project_id>/edit/', views.editProject, name='edit-project'),
    path('<uuid:project_id>/delete/', views.deleteProject, name='delete-project'),
]
