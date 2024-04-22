from django.urls import path

from . import views

app_name = "academic"

urlpatterns = [
    path("programmes/", views.render_programmes_page, name="programmes_page"),
    path(
        "programmes/<str:uuid>/",
        views.render_programmes_single_page,
        name="programmes_single_page",
    ),
    path(
        "academic-calender/", views.render_academic_calender, name="academic_calender"
    ),
    path(
        "evaluation-policies/",
        views.render_evaluation_policies,
        name="evaluation_policies",
    ),
    path("accounts/", views.render_accounts, name="accounts"),
]
