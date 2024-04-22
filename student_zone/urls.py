from django.urls import path

from . import views

app_name = "student_zone"

urlpatterns = [
    path("b-ed-examination/results/", views.render_results_page, name="results_page"),
    path(
        "b-ed-examination/results/status/",
        views.render_results_status,
        name="results_status",
    ),
    path("downloads/", views.render_downloads_page, name="downloads_page"),
]
