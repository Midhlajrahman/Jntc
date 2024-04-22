import datetime
import uuid

from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField


class GenderChoice(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        db_table = "alumni_gender_choice"
        verbose_name = _("Gender Choice")
        verbose_name_plural = _("Gender Choices")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class MaritalStatusChoice(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        db_table = "alumni_marital_status_choice"
        verbose_name = _("Marital Status Choice")
        verbose_name_plural = _("Marital Status Choices")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class BEdSubjectChoice(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        db_table = "alumni_b_ed_subject_choice"
        verbose_name = _("B.Ed Subject Choice")
        verbose_name_plural = _("B.Ed Subject Choices")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class YearOfStudyChoice(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        db_table = "alumni_year_of_study_choice"
        verbose_name = _("Year of Study Choice")
        verbose_name_plural = _("Year of Study Choices")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class EducationalStatusChoice(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        db_table = "alumni_educational_status_choice"
        verbose_name = _("Educational Status Choice")
        verbose_name_plural = _("Educational Status Choices")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class AlumniNetworkRegistration(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    gender = models.ForeignKey("GenderChoice", on_delete=models.PROTECT)
    marital_status = models.ForeignKey("MaritalStatusChoice", on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    image = VersatileImageField(
        "Image", upload_to="alumni/registration/image/", blank=True, null=True
    )
    b_ed_subject = models.ForeignKey("BEdSubjectChoice", on_delete=models.PROTECT)
    year_of_study = models.ForeignKey("YearOfStudyChoice", on_delete=models.PROTECT)
    educational_status = models.ForeignKey(
        "EducationalStatusChoice", on_delete=models.PROTECT
    )
    jntc_period = models.TextField(blank=True, null=True)
    suggestion = models.TextField(blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "alumni_alumni_network_registration"
        verbose_name = _("Alumni Network Registration")
        verbose_name_plural = _("Alumni Network Registrations")
        ordering = ("-date",)

    def __str__(self):
        return self.phone_number


class AlumniSpotlight(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=220)
    image = VersatileImageField("Image", upload_to="alumni/spotlight/image/")

    class Meta:
        db_table = "alumni_alumni_spotlight"
        verbose_name = _("Alumni Spotlight")
        verbose_name_plural = _("Alumni Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class AboutOurAlumniNetwork(models.Model):
    title = models.CharField(max_length=120)
    highlight_word = models.CharField(max_length=120, default="", null=True, blank=True)
    description = models.TextField()
    image = VersatileImageField("Image", upload_to="alumni/about_our/image/")

    class Meta:
        db_table = "alumni_about_our_alumni_network"
        verbose_name = _("About Our Alumni Network")
        verbose_name_plural = _("About Our Alumni Networks")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class AlumniActivity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "alumni_alumni_activity"
        verbose_name = _("Alumni Activity")
        verbose_name_plural = _("Alumni Activities")
        ordering = ("-date",)

    def __str__(self):
        return self.title


class ActivityGallery(models.Model):
    activity = models.ForeignKey(
        "alumni.AlumniActivity", related_name="gallery", on_delete=models.CASCADE
    )
    image = VersatileImageField("Image", upload_to="alumni/activities/image/")

    class Meta:
        db_table = "alumni_activity_gallery"
        verbose_name = _("Activity Gallery")
        verbose_name_plural = _("Activity Galleries")
        ordering = ("id",)

    def __str__(self):
        return str(self.activity)


class AlumniTeam(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=220)
    image = VersatileImageField("Image", upload_to="alumni/team/images/")
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "alumni_alumni_team"
        verbose_name = _("Alumni Team")
        verbose_name_plural = _("Alumni Teams")
        ordering = ("id",)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=120)
    batch = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "alumni_student"
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
        ordering = ("id",)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField("Image", upload_to="alumni/faculty/images/")
    designation = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "alumni_faculty"
        verbose_name = _("Faculty")
        verbose_name_plural = _("Faculties")
        ordering = ("id",)

    def __str__(self):
        return self.name
