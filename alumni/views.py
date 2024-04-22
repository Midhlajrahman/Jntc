from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .forms import RegistrationForm1, RegistrationForm2, RegistrationForm3
from .models import (
    AboutOurAlumniNetwork,
    AlumniActivity,
    AlumniNetworkRegistration,
    AlumniSpotlight,
    AlumniTeam,
    Faculty,
    Student,
)


# rending alumni main page
def render_alumni_page(request):
    alumni_spotlights = AlumniSpotlight.objects.first()
    about_our_alumni_networks = AboutOurAlumniNetwork.objects.first()
    alumni_activities = AlumniActivity.objects.all()[:3]
    alumni_teams = AlumniTeam.objects.filter(is_deleted=False)[:7]
    students = Student.objects.filter(is_deleted=False)[:5]
    faculties = Faculty.objects.filter(is_deleted=False)[:5]

    context = {
        "title": "Jamia Nadwiyya | Alumni",
        "alumni_spotlights": alumni_spotlights,
        "about": about_our_alumni_networks,
        "alumni_activities": alumni_activities,
        "alumni_teams": alumni_teams,
        "students": students,
        "faculties": faculties,
    }
    return render(request, "alumni/alumni-page.html", context)


# Rending alumni activities
def rending_alumni_activities(request):
    alumni_activities = AlumniActivity.objects.all()
    # Number of items to display per page
    items_per_page = 9

    # Create a Paginator instance
    paginator = Paginator(alumni_activities, items_per_page)

    # Get the current page number from   the request's GET parameters
    page_number = request.GET.get("page")

    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page_obj = paginator.get_page(1)

    context = {
        "title": "Jamia Nadwiyya | Alumni Activities",
        "alumni_activities": page_obj,
    }
    return render(
        request, "alumni/alumni-activities/activities-single-page.html", context
    )


# Rending alumni activity
def rending_alumni_activity(request, uuid):
    alumni_activity = get_object_or_404(AlumniActivity, id=uuid)

    context = {"title": "Jamia Nadwiyya | Alumni", "alumni_activity": alumni_activity}
    return render(request, "alumni/alumni-activities/activities-details.html", context)


# register alumni network forms
def register_alumni(request):
    if request.method == "POST":
        form1 = RegistrationForm1(request.POST, request.FILES)
        form2 = RegistrationForm2(request.POST)
        form3 = RegistrationForm3(
            request.POST
        )  # Include request.FILES to handle the image field

        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            # Save form data to the model
            alumni_registration = AlumniNetworkRegistration()
            alumni_registration.first_name = form1.cleaned_data["first_name"]
            alumni_registration.last_name = form1.cleaned_data["last_name"]
            alumni_registration.gender = form1.cleaned_data["gender"]
            alumni_registration.marital_status = form1.cleaned_data["marital_status"]
            alumni_registration.phone_number = form1.cleaned_data["phone_number"]
            alumni_registration.email = form1.cleaned_data["email"]
            alumni_registration.address = form1.cleaned_data["address"]
            alumni_registration.image = form1.cleaned_data[
                "image"
            ]  # Handle the image field
            alumni_registration.b_ed_subject = form2.cleaned_data["b_ed_subject"]
            alumni_registration.year_of_study = form2.cleaned_data["year_of_study"]
            alumni_registration.educational_status = form2.cleaned_data[
                "educational_status"
            ]
            alumni_registration.jntc_period = form3.cleaned_data["jntc_period"]
            alumni_registration.suggestion = form3.cleaned_data["suggestion"]

            alumni_registration.save()
            # Return a JSON response
            response_data = {
                "status": 200,
                "success": True,
                "message": "Form submitted successfully",
            }
            return JsonResponse(response_data, status=200)
        else:
            response_data = {
                "error": True,
                "messages": {
                    "form1": form1.errors,
                    "form2": form2.errors,
                    "form3": form3.errors,
                },
            }
            return JsonResponse(response_data, status=400)

    else:
        form_1 = RegistrationForm1()
        form_2 = RegistrationForm2()
        form_3 = RegistrationForm3()

        context = {
            "title": "Jamia Nadwiyya | Alumni Registration",
            "form_1": form_1,
            "form_2": form_2,
            "form_3": form_3,
        }
    return render(request, "alumni/registration-form/registration.html", context)
