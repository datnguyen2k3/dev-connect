from . import views
from django.urls import path

app_name = 'jobs'

urlpatterns = [
    path('<uuid:job_id>/', views.single_job_view,name='single-job'),   
    path('', views.jobs_view,name='jobs'),
    path('add/', views.add_job_view,name='add-job'),
    path('edit/<uuid:job_id>/', views.edit_job_view,name='edit-job'),
    path('delete/<uuid:job_id>/', views.delete_job_view,name='delete-job'),
    path('<uuid:job_id>/appliedCVs/', views.applied_cvs_view,name='applied-cv'),
    path('<uuid:job_id>/applied_cv_form/', views.applied_cv_form_view, name='applied-cv-form'),
    
]
 