from datetime import date

from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from academic.models import AcademicCourse, AcademicCourseHeading
from resources.models import GalleryEvent

from .models import (
    HomeAbout,
    HomeAnnouncement,
    HomeInstitutionHeading,
    HomeLatestNews,
    HomeNewsAndEventsSpotlight,
    HomeSpotlight,
    HomeUpcomingEvent,
)


# rendering home page
def render_home_page(request):
    spotlight = HomeSpotlight.objects.first()
    about = HomeAbout.objects.first()
    academics_heading = AcademicCourseHeading.objects.first()
    academics = AcademicCourse.objects.filter(is_deleted=False)[:3]
    announcements = HomeAnnouncement.objects.all()[:8]
    latest_news = HomeLatestNews.objects.all()[:3]
    events = HomeUpcomingEvent.objects.all()[:3]
    moment_gallery = GalleryEvent.objects.first()
    institution_heading = HomeInstitutionHeading.objects.first()

    context = {
        "title": "Jamia Nadwiyya | Home",
        "spotlight": spotlight,
        "about": about,
        "academics_heading": academics_heading,
        "academics": academics,
        "latest_news": latest_news,
        "events": events,
        "announcements": announcements,
        "moment_gallery": moment_gallery,
        "institution_heading": institution_heading,
    }

    return render(request, "home/index.html", context)


# rendering Latest news and Upcoming events page
def render_news_and_events_page(request):
    spotlight = HomeNewsAndEventsSpotlight.objects.first()
    latest_news = HomeLatestNews.objects.all().order_by("-date")[:6]
    events = HomeUpcomingEvent.objects.all().order_by("-date")[:6]

    context = {
        "title": "Jamia Nadwiyya | Latest News and Upcoming Events",
        "spotlight": spotlight,
        "latest_news": latest_news,
        "events": events,
    }
    return render(request, "news-and-events/news-and-events.html", context)


# rendering Latest news page
def render_latest_news_page(request):
    latest_news = HomeLatestNews.objects.all().order_by("-date")

    # Number of items to display per page
    items_per_page = 9

    # Create a Paginator instance
    paginator = Paginator(latest_news, items_per_page)

    # Get the current page number from   the request's GET parameters
    page_number = request.GET.get("page")

    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page_obj = paginator.get_page(1)

    context = {"title": "Jamia Nadwiyya | Latest News", "latest_news": page_obj}
    return render(request, "news-and-events/all-news.html", context)


# rendering upcoming events page
def render_events_page(request):
    today = date.today()

    featured_events = HomeUpcomingEvent.objects.filter(is_featured=True).order_by(
        "-date"
    )

    upcoming_events = HomeUpcomingEvent.objects.filter(
        date__gte=today, is_featured=False
    ).order_by("date")

    # Number of items to display per page
    items_per_page = 9

    # Create a Paginator instance
    paginator_1 = Paginator(featured_events, items_per_page)
    paginator_2 = Paginator(upcoming_events, items_per_page)

    # Get the current page number from   the request's GET parameters
    page_number = request.GET.get("page")

    try:
        page_obj_1 = paginator_1.get_page(page_number)
        page_obj_2 = paginator_2.get_page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page_obj_1 = paginator_1.get_page(1)
        page_obj_2 = paginator_2.get_page(1)

    context = {
        "title": "Jamia Nadwiyya | Featured and Upcoming Events",
        "featured_events": page_obj_1,
        "upcoming_events": page_obj_2,
    }
    return render(request, "news-and-events/all-events.html", context)


# rendering Latest news single page
def render_news_single_page(request, uuid):
    news = get_object_or_404(HomeLatestNews, id=uuid)

    context = {"title": "Jamia Nadwiyya | Upcoming Detail page", "news": news}
    return render(request, "news-and-events/news-details.html", context)


# rendering Upcoming event single page
def render_events_single_page(request, uuid):
    events = get_object_or_404(HomeUpcomingEvent, id=uuid)

    context = {"title": "Jamia Nadwiyya | Events Detail page", "events": events}
    return render(request, "news-and-events/events-details.html", context)


# rendering coming soon page
def coming_soon_page(request):
    return render(request, "comingsoon.html")

def render_home_about_page(request):
    about = HomeAbout.objects.all().first()

    context = {"title": "Jamia Nadwiyya | About", "about": about}

    return render(request, "about/home_about.html", context)
