from django.shortcuts import render

from alumni.models import Faculty

from .models import (
    AboutUsSpotlight,
    AnnualReport,
    FutureGoalGallery,
    History,
    Foundation,
    Objective,
    OurAdministrativeStaff,
    OurManagement,
    RulesAndRegulation,
    OurStaff,
    OurOfficeStaff,
    PtaCommitee,
    Commitee
)


# about page rending function
def render_about_page(request):
    spotlight = AboutUsSpotlight.objects.all().first()
    history = History.objects.all().first()
    foundation = Foundation.objects.all().first()
    goal_gallery = FutureGoalGallery.objects.all().first()
    objective = Objective.objects.all()[:3]
    management = OurManagement.objects.filter(is_deleted=False)[:4]
    Faculties = Faculty.objects.filter(is_deleted=False)
    administrative_staff = OurAdministrativeStaff.objects.filter(is_deleted=False)[:4]
    staffs = OurStaff.objects.filter(is_deleted=False)
    office_staffs = OurOfficeStaff.objects.filter(is_deleted=False)[:4]
    pta_commitee = PtaCommitee.objects.all()
    commitee = Commitee.objects.all()
    annual_reports = AnnualReport.objects.all()[:15]
    rules_and_regulations = RulesAndRegulation.objects.first()

    context = {
        "title": "Jamia Nadwiyya | About",
        "spotlight": spotlight,
        "history": history,
        "foundation": foundation,
        "goal_gallery": goal_gallery,
        "objective": objective,
        "management": management,
        "Faculty": Faculties,
        "administrative_staff": administrative_staff,
        "staffs": staffs,
        "office_staffs": office_staffs,
        "pta_commitee": pta_commitee,
        "commitee": commitee,
        "annual_reports": annual_reports,
        "rules_and_regulations": rules_and_regulations,
    }

    return render(request, "about/about.html", context)


def render_history_page(request):
    history = History.objects.all().first()

    context = {"title": "Jamia Nadwiyya | History", "history": history}

    return render(request, "about/history.html", context)


def render_foundation_page(request):
    foundation = Foundation.objects.all().first()

    context = {"title": "Jamia Nadwiyya | Foundation", "foundation": foundation}

    return render(request, "about/foundation.html", context)
