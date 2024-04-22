from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from .forms import StudentResultForm
from .models import (
    BEdExaminationResult,
    BEdResultStatusBatch,
    BEdStudent,
    DownloadFile,
    DownloadSpotlight,
    MagazineFile,
)


# BEd Results page rending
def render_results_page(request):
    results = BEdExaminationResult.objects.all()
    top_results = BEdExaminationResult.objects.all()[:4]

    # search handling
    if q := request.GET.get("q"):
        results = results.filter(Q(title__icontains=q))

    # Number of items to display per page
    items_per_page = 10

    # Create a Paginator instance
    paginator = Paginator(results, items_per_page)

    # Get the current page number from   the request's GET parameters
    page_number = request.GET.get("page")

    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page_obj = paginator.get_page(1)

    # initializing the form
    form = StudentResultForm()

    if request.method == "POST":
        form = StudentResultForm(request.POST)
        if form.is_valid():
            exam_id = form.cleaned_data["exam_id"]
            register_no = form.cleaned_data["register_no"]
            date_of_birth = form.cleaned_data["date_of_birth"]

            result = BEdStudent.objects.get(
                results__id=exam_id,
                register_number=register_no,
                date_of_birth=date_of_birth,
            )

            # Return a JSON response
            response_data = {
                "status": 200,
                "success": True,
                "message": "Form submitted successfully",
                "redirect": "/coming-soon-page",
            }
            return JsonResponse(response_data, status=200)
        else:
            response_data = {"error": True, "message": form.errors}
            return JsonResponse(response_data, status=400)
    context = {
        "title": "Jamia Nadwiyya | B.Ed Examination Results",
        "results": page_obj,
        "top_results": top_results,
        "search": q,
        "form": form,
    }
    return render(request, "student-zone/results.html", context)


# Year wise and semester wise status
def render_results_status(request):
    results = BEdResultStatusBatch.objects.filter(is_deleted=False)[:4]
    context = {"title": "Jamia Nadwiyya | B.Ed Results Status", "results": results}
    return render(request, "student-zone/year-and-semester-wise-results.html", context)


# Download page rending
def render_downloads_page(request):
    spotlight = DownloadSpotlight.objects.first()
    files = DownloadFile.objects.all()
    magazines = MagazineFile.objects.all()

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
        "title": "Jamia Nadwiyya | Downloads",
        "spotlight": spotlight,
        "files": page_obj,
        "magazines": magazines,
    }
    return render(request, "student-zone/downloads.html", context)
