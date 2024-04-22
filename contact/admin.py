from django.contrib import admin

from .models import (
    ContactUsDetail,
    ContactUsEnquiry,
    ContactUsSpotlight,
    JNTCLogo,
    SocialMedia,
)


class ContactUsSpotlightAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title", "image")


admin.site.register(ContactUsSpotlight, ContactUsSpotlightAdmin)


class ContactUsDetailAdmin(admin.ModelAdmin):
    list_display = ("address", "phone_number", "email")


admin.site.register(ContactUsDetail, ContactUsDetailAdmin)


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("title", "url")


admin.site.register(SocialMedia, SocialMediaAdmin)


class ContactUsEnquiryAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "email", "message")


admin.site.register(ContactUsEnquiry, ContactUsEnquiryAdmin)
admin.site.register(JNTCLogo)
