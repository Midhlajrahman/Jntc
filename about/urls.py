from django.urls import path

from . import views

app_name = "about"

urlpatterns = [
    path("", views.render_about_page, name="about_page"),
    path("history/", views.render_history_page, name="history_page"),
    path("foundation/", views.render_foundation_page, name="foundation_page"),
]
