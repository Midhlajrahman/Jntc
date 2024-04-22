from django.urls import path

from . import views

app_name = "iqac"

urlpatterns = [
    path("", views.render_iqac_page, name="iqac_page"),
    path("complaint-report/", views.render_complaint_page, name="complaint"),
]
