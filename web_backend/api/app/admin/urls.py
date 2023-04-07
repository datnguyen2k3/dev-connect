from django.urls import path
from .views import delete_user_view, get_number_login_user

urlpatterns = [
    path("users/delete/", delete_user_view, name="delete_user"),
    path("sessions/number/", get_number_login_user, name="get_number_login_user"),
]
