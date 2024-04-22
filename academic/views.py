from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import (
    AcademicCalenderBatch,
    AcademicCalenderSpotlight,
    AccountFile,
    AccountSpotlight,
    EvaluationPolicyFile,
    EvaluationPolicySpotlight,
    ProgramSpotlight,
)


# rendering programmes page
def render_programmes_page(request):
    programs = ProgramSpotlight.objects.all()[:2]
    context = {"title": "Jamia Nadwiyya | Programmes", "programs": programs}
    return render(request, "academics/programmes/programmes.html", context)


# rendering programmes single page
def render_programmes_single_page(request, uuid):
    program = get_object_or_404(ProgramSpotlight, id=uuid)
    context = {"title": f"Jamia Nadwiyya | {program.tag}", "program": program}
    return render(request, "academics/programmes/programmes-single-page.html", context)


# rendering academic calender page
def render_academic_calender(request):
    spotlight = AcademicCalenderSpotlight.objects.first()
    calender = AcademicCalenderBatch.objects.filter(is_deleted=False)[:4]

    context = {
        "title": "Jamia Nadwiyya | Academic Calender",
        "spotlight": spotlight,
        "calender": calender,
    }
    return render(request, "academics/academic-calender.html", context)


# rendering evaluation policy page
def render_evaluation_policies(request):
    spotlight = EvaluationPolicySpotlight.objects.first()
    files = EvaluationPolicyFile.objects.all()

    # add field for identify file extension
    for file in files:
        if file.file.url.lower().endswith(".jpg"):
            file.file_ext = "jpg"
        else:
            file.file_ext = "pdf"

    # Number of items to display per page
    items_per_page = 16

    # Create a Paginator instance
    paginator = Paginator(files, items_per_page)

    # Get the current page number from   the request's GET parameters
    page_number = request.GET.get("page")

    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page_obj = paginator.get_page(1)

    context = {
        "title": "Jamia Nadwiyya | Evaluation Policies",
        "spotlight": spotlight,
        "files": page_obj,
    }
    return render(request, "academics/evaluation-policies.html", context)


# rendering accounts page
def render_accounts(request):
    spotlight = AccountSpotlight.objects.first()
    files = AccountFile.objects.all()

    # add field for identify file extension
    for file in files:
        if file.file.url.lower().endswith(".jpg"):
            file.file_ext = "jpg"
        else:
            file.file_ext = "pdf"

    # Number of items to display per page
    items_per_page = 16

    # Create a Paginator instance
    paginator = Paginator(files, items_per_page)

    # Get the current page number from   the request's GET parameters
    page_number = request.GET.get("page")

    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page_obj = paginator.get_page(1)

    context = {
        "title": "Jamia Nadwiyya | Accounts",
        "spotlight": spotlight,
        "files": page_obj,
    }
    return render(request, "academics/accounts.html", context)
