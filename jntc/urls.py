from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web.urls", namespace="web")),
    path("about/", include("about.urls", namespace="about")),
    path("alumni/", include("alumni.urls", namespace="alumni")),
    path("iqac/", include("iqac.urls", namespace="iqac")),
    path("contact_us/", include("contact.urls", namespace="contact")),
    path("resources/", include("resources.urls", namespace="resources")),
    path("academics/", include("academic.urls", namespace="academic")),
    path("student-zone/", include("student_zone.urls", namespace="student_zone")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
