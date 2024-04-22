from django.urls import path

from . import views

app_name = "resources"

urlpatterns = [
    path("gallery/", views.render_gallery_page, name="gallery_page"),
    path("view_galleries/", views.render_galleries_page, name="galleries_page"),
    path("facilities/", views.render_facilities_page, name="facilities_page"),
]
