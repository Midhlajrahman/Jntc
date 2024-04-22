from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField


class JNTCLogo(models.Model):
    title = models.CharField(max_length=120)
    image = VersatileImageField("Image", upload_to="logo/image/")

    class Meta:
        db_table = "contact_jntc_logo"
        verbose_name = _("JNTC Logo")
        verbose_name_plural = _("JNTC Logo")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class ContactUsSpotlight(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="contact_us/spotlight/image/")

    class Meta:
        db_table = "contact_contact_us_spotlight"
        verbose_name = _("ContactUs Spotlight")
        verbose_name_plural = _("ContactUs Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class ContactUsDetail(models.Model):
    address = models.TextField()
    map_link = models.URLField(max_length=290, default="", null=True, blank=True)
    phone_number = models.CharField(max_length=120)
    email = models.EmailField()

    class Meta:
        db_table = "contact_contact_us_detail"
        verbose_name = _("ContactUs Detail")
        verbose_name_plural = _("ContactUs Details")
        ordering = ("-id",)

    def __str__(self):
        return self.phone_number


class SocialMedia(models.Model):
    title = models.CharField(max_length=180)
    url = models.URLField(max_length=200, null=True, blank=True)
    icon = models.FileField(
        default="image.svg", upload_to="contact_us/social_media/icons/"
    )

    class Meta:
        db_table = "contact_social_media"
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")
        ordering = ("id",)

    def __str__(self):
        return self.title


class ContactUsEnquiry(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField(max_length=250)

    class Meta:
        db_table = "contact_contact_us_enquiry"
        verbose_name = _("ContactUs Enquiry")
        verbose_name_plural = _("ContactUs Enquiries")
        ordering = ("-id",)

    def __str__(self):
        return self.phone_number
