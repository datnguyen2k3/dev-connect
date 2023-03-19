from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('create-project/', views.create_project_view, name="create-project"),
    path('<uuid:project_id>/', views.single_project_view, name='single-project'),
    path('<uuid:project_id>/edit/', views.edit_project_view, name='edit-project'),
    path('<uuid:project_id>/delete/', views.delete_project_view, name='delete-project'),
]
