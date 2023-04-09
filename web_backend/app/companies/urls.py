from django.urls import path
from . import views

app_name = "companies"

urlpatterns = [
    path("", views.companies_view, name="companies"),
    path("add/", views.add_company_view, name="add-company"),
    path("<uuid:company_id>/", views.single_company_view, name="single-company"),
    path("<uuid:company_id>/edit/", views.edit_company_view, name="edit-company"),
    path("<uuid:company_id>/delete/", views.delete_company_view, name="delete-company"),
    path("<uuid:company_id>/jobs/", views.company_jobs_view, name="company-jobs"),
    path(
        "<uuid:company_id>/reviews/", views.company_reviews_view, name="company-reviews"
    ),
    path("<uuid:company_id>/review_form/", views.review_form_view, name="review-form"),
]
