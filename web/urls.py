from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.render_home_page, name="home_page"),
    path("coming-soon-page", views.coming_soon_page, name="coming_soon_page"),
    path(
        "news-and-events/",
        views.render_news_and_events_page,
        name="news_and_events_page",
    ),
    path(
        "news-and-events/upcoming-events/", views.render_events_page, name="events_page"
    ),
    path(
        "news-and-events/latest-news/", views.render_latest_news_page, name="news_page"
    ),
    path(
        "news-and-events/latest-news/<str:uuid>/",
        views.render_news_single_page,
        name="news_single_page",
    ),
    path(
        "news-and-events/upcoming-events/<str:uuid>/",
        views.render_events_single_page,
        name="events_single_page",
    ),
    path(
        "home_about/",
        views.render_home_about_page,
        name="home_about_page",
    ),
]
