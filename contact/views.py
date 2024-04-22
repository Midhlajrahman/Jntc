from django.http import JsonResponse
from django.shortcuts import render

from .forms import ContactUsEnquiryForm
from .models import ContactUsSpotlight


# rendering contact page
def render_contact_page(request):
    if request.method == "POST":
        form = ContactUsEnquiryForm(request.POST)

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
        spotlight = ContactUsSpotlight.objects.first()
        form = ContactUsEnquiryForm()
        context = {
            "title": "Jamia Nadwiyya | Contact Us",
            "spotlight": spotlight,
            "form": form,
        }
        return render(request, "home/contact.html", context)
