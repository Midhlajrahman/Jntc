import datetime
import uuid

from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField


class BEdResultStatusBatch(models.Model):
    batch = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "student_zone_bed_result_status_batch"
        verbose_name = _("B.Ed Result Status Batch")
        verbose_name_plural = _("B.Ed Result Status Batchs")
        ordering = ("-id",)

    def __str__(self):
        return self.batch


class BEdResultStatusBatchYear(models.Model):
    batch = models.ForeignKey(
        "student_zone.BEdResultStatusBatch",
        related_name="years",
        on_delete=models.CASCADE,
    )
    year = models.CharField(max_length=120)
    file = models.FileField(
        upload_to="student_zone/bed_result_status/files",
        validators=[FileExtensionValidator(["pdf"])],
    )

    class Meta:
        db_table = "student_zone_bed_result_status_batch_year"
        verbose_name = _("B.Ed Result Status Batch Year")
        verbose_name_plural = _("B.Ed Result Status Batch Years")

    def __str__(self):
        return self.year


class BEdResultStatusBatchSemester(models.Model):
    batch = models.ForeignKey(
        "student_zone.BEdResultStatusBatch",
        related_name="semesters",
        on_delete=models.CASCADE,
    )
    semester = models.CharField(max_length=120)
    file = models.FileField(
        upload_to="student_zone/bed_result_status/files",
        validators=[FileExtensionValidator(["pdf"])],
    )

    class Meta:
        db_table = "student_zone_bed_result_status_batch_semester"
        verbose_name = _("B.Ed Result Status Batch Semester")
        verbose_name_plural = _("B.Ed Result Status Batch Semesters")

    def __str__(self):
        return self.semester


class DownloadSpotlight(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=220)
    image = VersatileImageField("Image", upload_to="student_zone/downloads/image/")

    class Meta:
        db_table = "student_zone_download_spotlight"
        verbose_name = _("Download Spotlight")
        verbose_name_plural = _("Download Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class DownloadFile(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(
        "Image", default="", upload_to="student_zone/downloads/files/images"
    )
    file = models.FileField(
        upload_to="student_zone/downloads/files",
        validators=[FileExtensionValidator(["pdf", "jpg"])],
    )
    date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "student_zone_download_file"
        verbose_name = _("Download File")
        verbose_name_plural = _("Download Files")
        ordering = ("-id",)

    def __str__(self):
        return self.name


class MagazineFile(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(
        "Image", default="", upload_to="student_zone/magazines/files/images"
    )
    file = models.FileField(
        upload_to="student_zone/magazines/files",
        validators=[FileExtensionValidator(["pdf"])],
    )
    date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "student_zone_magazine_file"
        verbose_name = _("Magazine File")
        verbose_name_plural = _("Magazine Files")
        ordering = ("-id",)

    def __str__(self):
        return self.name


class BEdExaminationResult(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=120)
    date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "student_zone_bed_examination_result"
        verbose_name = _("B.Ed Examination Result")
        verbose_name_plural = _("B.Ed Examination Results")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class BEdStudent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    results = models.ForeignKey(
        "student_zone.BEdExaminationResult",
        related_name="students",
        on_delete=models.CASCADE,
    )
    register_number = models.CharField(
        max_length=21, validators=[RegexValidator(r"^[0-9]+$")]
    )
    name = models.CharField(max_length=120)
    date_of_birth = models.DateField(default=datetime.date.today)
    file = models.FileField(
        upload_to="student_zone/b_ed_students/results/files",
        validators=[FileExtensionValidator(["pdf"])],
    )

    class Meta:
        db_table = "student_zone_bed_student"
        verbose_name = _("B.Ed Student")
        verbose_name_plural = _("B.Ed Students")
        ordering = ("-id",)

    def __str__(self):
        return self.name
