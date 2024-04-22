from django.urls import path

from . import views

app_name = "contact"

urlpatterns = [path("", views.render_contact_page, name="contact_us_page")]
