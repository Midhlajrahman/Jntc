import datetime

from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField


class GallerySpotlight(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=220)
    image = VersatileImageField(
        "Image", upload_to="resources/Galleries/spotlight/image/"
    )

    class Meta:
        db_table = "resources_gallery_spotlight"
        verbose_name = _("Gallery Spotlight")
        verbose_name_plural = _("Gallery Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class GalleryEvent(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField(default=datetime.date.today)
    video = models.FileField(
        upload_to="resources/Galleries/events/videos/",
        default="resources/Galleries/events/videos/video.mp4",
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "resources_gallery_event"
        verbose_name = _("Gallery Event")
        verbose_name_plural = _("Gallery Events")
        ordering = ("-date",)

    def __str__(self):
        return self.title


class GalleryEventAlbum(models.Model):
    event = models.ForeignKey(
        "resources.GalleryEvent", related_name="gallery", on_delete=models.CASCADE
    )
    image = VersatileImageField("Image", upload_to="resources/Galleries/events/images/")

    class Meta:
        db_table = "resources_gallery_event_album"
        verbose_name = _("Gallery Event Album")
        verbose_name_plural = _("Gallery Event Albums")
        ordering = ("-id",)

    def __str__(self):
        return str(self.event)


class FacilityAdministrative(models.Model):
    title = models.CharField(max_length=255)
    highlight_title = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    sub_title = models.CharField(max_length=255)

    class Meta:
        db_table = "resources_facility_administrative"
        verbose_name = _("Facility Administrative")
        verbose_name_plural = _("Facility Administratives")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class FacilityAdministrativeGallery(models.Model):
    administrative = models.ForeignKey(
        "resources.FacilityAdministrative",
        related_name="gallery",
        on_delete=models.CASCADE,
    )
    image = VersatileImageField(
        "Image", upload_to="resources/facility/administrative/images/"
    )

    class Meta:
        db_table = "resources_facility_administrative_gallery"
        verbose_name = _("Facility Administrative Gallery")
        verbose_name_plural = _("Facility Administrative Galleries")
        ordering = ("-id",)

    def __str__(self):
        return str(self.administrative)


class FacilityHallTitle(models.Model):
    title = models.CharField(max_length=255)
    highlight_title = models.CharField(
        max_length=255, default="", blank=True, null=True
    )

    class Meta:
        db_table = "resources_facility_hall_title"
        verbose_name = _("Facility Hall Title")
        verbose_name_plural = _("Facility Hall Titles")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class FacilityHall(models.Model):
    hall = models.ForeignKey(
        "resources.FacilityHallTitle", related_name="halls", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "resources_facility_hall"
        verbose_name = _("Facility Hall")
        verbose_name_plural = _("Facility Halls")
        ordering = ("-date",)

    def __str__(self):
        return str(self.hall)


class FacilityHallGallery(models.Model):
    hall = models.ForeignKey(
        "resources.FacilityHall", related_name="gallery", on_delete=models.CASCADE
    )
    image = VersatileImageField("Image", upload_to="resources/facility/hall/images/")

    class Meta:
        db_table = "resources_facility_hall_gallery"
        verbose_name = _("Facility Hall Gallery")
        verbose_name_plural = _("Facility Hall Galleries")
        ordering = ("-id",)

    def __str__(self):
        return str(self.hall)


class FacilityLibrary(models.Model):
    title = models.CharField(max_length=120)
    highlight_title = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    sub_title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    image = VersatileImageField("Image", upload_to="resources/facility/library/image/")

    class Meta:
        db_table = "resources_facility_library"
        verbose_name = _("Facility Library")
        verbose_name_plural = _("Facility Libraries")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class FacilityLabTitle(models.Model):
    title = models.CharField(max_length=255)
    highlight_title = models.CharField(
        max_length=255, default="", blank=True, null=True
    )

    class Meta:
        db_table = "resources_facility_lab_title"
        verbose_name = _("Facility Lab Title")
        verbose_name_plural = _("Facility Lab Titles")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class FacilityLab(models.Model):
    lab = models.ForeignKey(
        "resources.FacilityLabTitle", related_name="labs", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    image = VersatileImageField("Image", upload_to="resources/facility/lab/images/")
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "resources_facility_lab"
        verbose_name = _("Facility Lab")
        verbose_name_plural = _("Facility Labs")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class FacilityInternship(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "resources_facility_internship"
        verbose_name = _("Facility Internship")
        verbose_name_plural = _("Facility Internships")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class FacilityInternshipGallery(models.Model):
    internship = models.ForeignKey(
        "resources.FacilityInternship", related_name="gallery", on_delete=models.CASCADE
    )
    image = VersatileImageField(
        "Image", upload_to="resources/facility/internship/images/"
    )

    class Meta:
        db_table = "resources_facility_internship_gallery"
        verbose_name = _("Facility Internship Gallery")
        verbose_name_plural = _("Facility Internship Galleries")
        ordering = ("-id",)

    def __str__(self):
        return str(self.internship)


class FacilityHotelService(models.Model):
    title = models.CharField(max_length=120)
    highlight_title = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    description = models.TextField()
    image = VersatileImageField(
        "Image", upload_to="resources/facility/hotel_service/image/"
    )

    class Meta:
        db_table = "resources_facility_hotel_service"
        verbose_name = _("Facility Hotel Service")
        verbose_name_plural = _("Facility Hotel Services")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class FacilityCollegeGround(models.Model):
    title = models.CharField(max_length=120)
    highlight_title = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    description = models.TextField()
    image = VersatileImageField(
        "Image", upload_to="resources/facility/college_ground/image/"
    )

    class Meta:
        db_table = "resources_facility_college_ground"
        verbose_name = _("Facility College Ground")
        verbose_name_plural = _("Facility College Grounds")
        ordering = ("-id",)

    def __str__(self):
        return self.title
