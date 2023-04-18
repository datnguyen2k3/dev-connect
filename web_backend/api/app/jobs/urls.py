from django.urls import path
from . import views

urlpatterns = [
    path("elasticsearch/delete_data/", views.delete_els_job_data_view, name="delete-els-job-data"),
]
