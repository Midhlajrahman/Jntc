from django.http import JsonResponse
from django.shortcuts import render

from alumni.models import AlumniTeam, Faculty, Student

from .forms import IQACComplaintForm
from .models import (
    IQACAbout,
    IQACFunctionName,
    IQACObjective,
    IQACOurVision,
    IQACSpotlight,
    IQACTeam,
    LocalSociety,
)


# iqac page rendering
def render_iqac_page(request):
    about = IQACAbout.objects.first()
    spotlight = IQACSpotlight.objects.first()
    vision = IQACOurVision.objects.first()
    objective = IQACObjective.objects.first()
    team_members = IQACTeam.objects.filter(is_deleted=False)[:6]
    society_member = LocalSociety.objects.filter(is_deleted=False).first()
    faculty_members = Faculty.objects.filter(is_deleted=False)[:7]
    students = Student.objects.filter(is_deleted=False)[:2]
    alumni_member = AlumniTeam.objects.filter(is_deleted=False).first()
    function_names = IQACFunctionName.objects.all()[:6]

    context = {
        "title": "Jamia Nadwiyya | IQAC",
        "about": about,
        "spotlight": spotlight,
        "vision": vision,
        "objective": objective,
        "team_members": team_members,
        "faculty_members": faculty_members,
        "students": students,
        "alumni_member": alumni_member,
        "society_member": society_member,
        "function_names": function_names,
    }

    return render(request, "iqac/iqac.html", context)


# iqac complaint form page
def render_complaint_page(request):
    if request.method == "POST":
        form = IQACComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            # Return a JSON response indicating success
            response_data = {
                "status": "200",
                "success": True,
                "message": "Form submitted successfully.",
            }
            return JsonResponse(response_data, status=200)
        else:
            # Return a JSON response with the form errors
            response_data = {"status": 400, "error": True, "message": form.errors}
            return JsonResponse(response_data, status=400)
    else:
        form = IQACComplaintForm()

        context = {"form": form, "title": "Jamia Nadwiyya | IQAC Complaint"}
        return render(request, "iqac/complaint-form/complaint.html", context)
