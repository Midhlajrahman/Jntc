import datetime

from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField


class IQACSpotlight(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=220)
    image = VersatileImageField("Image", upload_to="iqac/spotlight/image/")

    class Meta:
        db_table = "iqac_iqac_spotlight"
        verbose_name = _("IQAC Spotlight")
        verbose_name_plural = _("IQAC Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class IQACAbout(models.Model):
    title = models.CharField(max_length=120)
    highlight_word = models.CharField(max_length=120, default="", null=True, blank=True)
    description = models.TextField()

    class Meta:
        db_table = "iqac_iqac_about"
        verbose_name = _("IQAC About")
        verbose_name_plural = _("IQAC Abouts")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class IQACAboutGallery(models.Model):
    about = models.ForeignKey(
        "iqac.IQACAbout", related_name="gallery", on_delete=models.CASCADE
    )
    image = VersatileImageField("Image", upload_to="iqac/about/image/")

    class Meta:
        db_table = "iqac_iqac_about_gallery"
        verbose_name = _("IQAC About Gallery")
        verbose_name_plural = _("IQAC About Galleries")
        ordering = ("-id",)

    def __str__(self):
        return str(self.about)


class IQACOurVision(models.Model):
    member = models.ForeignKey(
        "iqac.IQACTeam", related_name="vision", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    highlight_word = models.CharField(max_length=120, default="", null=True, blank=True)
    description = models.TextField()

    class Meta:
        db_table = "iqac_iqac_our_vision"
        verbose_name = _("IQAC Our Vision")
        verbose_name_plural = _("IQAC Our Visions")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class IQACObjective(models.Model):
    member = models.ForeignKey(
        "iqac.IQACTeam", related_name="objective", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    highlight_word = models.CharField(max_length=120, default="", null=True, blank=True)
    description = models.TextField()

    class Meta:
        db_table = "iqac_iqac_objective"
        verbose_name = _("IQAC Objective")
        verbose_name_plural = _("IQAC Objectives")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class IQACTeam(models.Model):
    name = models.CharField(max_length=220)
    designation = models.CharField(max_length=250)
    image = VersatileImageField("Image", upload_to="iqac/team/images/")
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "iqac_iqac_team"
        verbose_name = _("IQAC Team")
        verbose_name_plural = _("IQAC Teams")
        ordering = ("-id",)

    def __str__(self):
        return self.name


class LocalSociety(models.Model):
    name = models.CharField(max_length=120)
    panchayat = models.CharField(max_length=220)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "iqac_Local_Society"
        verbose_name = _("Local Society")
        verbose_name_plural = _("Local Societies")
        ordering = ("id",)

    def __str__(self):
        return self.name


class IQACFunctionName(models.Model):
    name = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "iqac_iqac_function_name"
        verbose_name = _("IQAC Function Name")
        verbose_name_plural = _("IQAC Function Names")
        ordering = ("-id",)

    def __str__(self):
        return self.name


class IQACFunctionRecord(models.Model):
    event = models.ForeignKey(
        "iqac.IQACFunctionName", related_name="event", on_delete=models.CASCADE
    )
    year_of_event = models.CharField(max_length=55)
    file = models.FileField(upload_to="iqac/function/files/")

    class Meta:
        db_table = "iqac_iqac_function_record"
        verbose_name = _("IQAC Function Record")
        verbose_name_plural = _("IQAC Function Records")
        ordering = ("-year_of_event",)

    def __str__(self):
        return self.year_of_event


class IQACComplaint(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_of_batch = models.ForeignKey(
        "alumni.YearOfStudyChoice", related_name="years", on_delete=models.PROTECT
    )
    subject = models.ForeignKey(
        "alumni.BEdSubjectChoice", related_name="subjects", on_delete=models.PROTECT
    )
    complaint = models.TextField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "iqac_iqac_complaint"
        verbose_name = _("IQAC Complaint")
        verbose_name_plural = _("IQAC Complaints")
        ordering = ("-year_of_batch",)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
