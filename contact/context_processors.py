from .models import ContactUsDetail, JNTCLogo, SocialMedia


def common_context(request):
    contact_us_detail = ContactUsDetail.objects.first()
    logo = JNTCLogo.objects.first()
    social_media = SocialMedia.objects.all()

    return {
        "footer": {
            "logo": logo,
            "contact_us_detail": contact_us_detail,
            "social_media": social_media,
        }
    }
