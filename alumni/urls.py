from django.urls import path

from . import views

app_name = "alumni"

urlpatterns = [
    path("", views.render_alumni_page, name="alumni_page"),
    path(
        "alumni-activity/<str:uuid>/",
        views.rending_alumni_activity,
        name="alumni_activity",
    ),
    path(
        "alumni-activities/", views.rending_alumni_activities, name="alumni_activities"
    ),
    path("alumni-network-registration/", views.register_alumni, name="register"),
]
