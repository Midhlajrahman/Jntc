from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import (
    FacilityAdministrative,
    FacilityCollegeGround,
    FacilityHallTitle,
    FacilityHotelService,
    FacilityInternship,
    FacilityLabTitle,
    FacilityLibrary,
    GalleryEvent,
)


# rending gallery details image page
def render_gallery_page(request):
    events = list(GalleryEvent.objects.all())

    if index := request.GET.get("index"):
        event = get_object_or_404(GalleryEvent, id=index)
        events.remove(event)  # Remove the event from   the list
        events.insert(0, event)  # Insert the event at the beginning

    context = {"title": "Jamia Nadwiyya | Gallery", "events": events}
    return render(request, "resources/gallery/gallery.html", context)


# rending galleries cards page
def render_galleries_page(request):
    events = GalleryEvent.objects.all()

    # Number of items to display per page
    items_per_page = 8

    # Create a Paginator instance
    paginator = Paginator(events, items_per_page)

    # Get the current page number from   the request's GET parameters
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page_obj = paginator.get_page(1)

    context = {"title": "Jamia Nadwiyya | Galleries", "events": page_obj}
    return render(request, "resources/gallery/albums.html", context)


# rending facilities page
def render_facilities_page(request):
    administratives = FacilityAdministrative.objects.first()
    halls = FacilityHallTitle.objects.first()
    libraries = FacilityLibrary.objects.first()
    labs = FacilityLabTitle.objects.first()
    internships = FacilityInternship.objects.first()
    hotel_services = FacilityHotelService.objects.first()
    college_grounds = FacilityCollegeGround.objects.first()

    context = {
        "title": "Jamia Nadwiyya | Facilities",
        "administratives": administratives,
        "halls": halls,
        "libraries": libraries,
        "labs": labs,
        "internships": internships,
        "hotel_services": hotel_services,
        "college_grounds": college_grounds,
    }
    return render(request, "resources/facility/facilities.html", context)
