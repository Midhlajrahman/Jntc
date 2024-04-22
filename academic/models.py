import datetime
import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField


class AcademicCourseHeading(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "academic_academic_course_heading"
        verbose_name = _("Academic Course Heading")
        verbose_name_plural = _("Academic Course Headings")
        ordering = ("-id",)

    def __str__(self):
        return str(self.title)


class AcademicCourse(models.Model):
    title = models.CharField(max_length=255)
    arrow_tag = models.CharField(max_length=255, default="")
    description = models.TextField()
    image = VersatileImageField("Image", upload_to="academic/Course/images/")
    date = models.DateField(default=datetime.date.today)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "academic_academic_course"
        verbose_name = _("Academics Course")
        verbose_name_plural = _("Academics Courses")
        ordering = ("-id",)

    def __str__(self):
        return str(self.title)


class ProgramSpotlight(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    tag = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    sub_title = models.CharField(max_length=220, null=True, blank=True)
    image = VersatileImageField(
        "Image", upload_to="academic/programmes/spotlight/image/", null=True, blank=True
    )
    is_deleted = models.BooleanField(default=False)
    date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "academic_program_spotlight"
        verbose_name = _("Academic Programme")
        verbose_name_plural = _("Academic Programmes")
        ordering = ("-id",)

    def __str__(self):
        return str(self.title)


class ProgramAbout(models.Model):
    program = models.ForeignKey(
        "academic.ProgramSpotlight",
        related_name="about",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tag = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    highlight_word = models.CharField(max_length=120, default="", null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "academic_program_About"
        verbose_name = _("Academic Programmes About")
        verbose_name_plural = _("Academic Programmes Abouts")
        ordering = ("-id",)

    def __str__(self):
        return str(self.program)


class ProgramAboutGallery(models.Model):
    about = models.ForeignKey(
        "academic.ProgramAbout",
        related_name="gallery",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    image = VersatileImageField(
        "Image", upload_to="academic/programmes/about/images/", null=True, blank=True
    )

    class Meta:
        db_table = "academic_program_about_gallery"
        verbose_name = _("Academic Programmes About gallery")
        verbose_name_plural = _("Academic Programmes About galleries")
        ordering = ("-id",)

    def __str__(self):
        return str(self.about)


class ProgramObjective(models.Model):
    program = models.ForeignKey(
        "academic.ProgramSpotlight",
        related_name="objective",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tag = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    highlight_word = models.CharField(max_length=120, default="", null=True, blank=True)
    image = VersatileImageField(
        "Image",
        upload_to="academic/programmes/objectives/image/",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "academic_program_objective"
        verbose_name = _("Academic Programmes Objective")
        verbose_name_plural = _("Academic Programmes Objectives")
        ordering = ("-id",)

    def __str__(self):
        return str(self.program)


class ProgramObjectivePoint(models.Model):
    objective = models.ForeignKey(
        "academic.ProgramObjective",
        related_name="point",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        db_table = "academic_program_objective_point"
        verbose_name = _("Academic Programmes Objective Point")
        verbose_name_plural = _("Academic Programmes Objective Points")
        ordering = ("-id",)

    def __str__(self):
        return str(self.objective)


class ProgramGatewayHeading(models.Model):
    program = models.ForeignKey(
        "academic.ProgramSpotlight",
        related_name="gateway",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tag = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "academic_program_gateway_heading"
        verbose_name = _("Academic Programmes Gateway Heading")
        verbose_name_plural = _("Academic Programmes Gateway Heading")
        ordering = ("-id",)

    def __str__(self):
        return str(self.program)


class ProgramGateway(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    object = models.ForeignKey(
        "academic.ProgramGatewayHeading",
        related_name="object",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tag = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    sub_title = models.CharField(max_length=220, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    image = VersatileImageField(
        "Image", upload_to="academic/programmes/gateway/image/", null=True, blank=True
    )

    class Meta:
        db_table = "academic_program_gateway"
        verbose_name = _("Academic Programmes Gateway")
        verbose_name_plural = _("Academic Programmes Gateways")
        ordering = ("-id",)

    def __str__(self):
        return str(self.id)


class ProgramInformation(models.Model):
    program = models.ForeignKey(
        "academic.ProgramSpotlight",
        related_name="information",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tag = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    highlight_word = models.CharField(max_length=120, default="", null=True, blank=True)
    sub_title = models.CharField(max_length=220, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = VersatileImageField(
        "Image",
        upload_to="academic/programmes/Information/image/",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "academic_program_information"
        verbose_name = _("Academic Programmes Information")
        verbose_name_plural = _("Academic Programmes Informations")
        ordering = ("-id",)

    def __str__(self):
        return str(self.program)


class ProgramInformationFile(models.Model):
    program = models.ForeignKey(
        "academic.ProgramSpotlight",
        related_name="data",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tag = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    sub_title = models.CharField(max_length=220, null=True, blank=True)
    file_name = models.CharField(default="", max_length=220, null=True, blank=True)
    file = models.FileField(
        upload_to="academic/programmes/Information/files/",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["pdf"])],
    )

    class Meta:
        db_table = "academic_program_information_file"
        verbose_name = _("Academic Programmes Information File")
        verbose_name_plural = _("Academic Programmes Information Files")
        ordering = ("-id",)

    def __str__(self):
        return str(self.program)


class AcademicCalenderSpotlight(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=220)
    image = VersatileImageField(
        "Image", upload_to="academic/academic_calender/spotlight/image/"
    )

    class Meta:
        db_table = "academic_academic_calender_spotlight"
        verbose_name = _("Academic Calender Spotlight")
        verbose_name_plural = _("Academic Calender Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return str(self.title)


class AcademicCalenderBatch(models.Model):
    batch = models.CharField(max_length=220)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "academic_academic_calender_batch"
        verbose_name = _("Academic Calender Batch")
        verbose_name_plural = _("Academic Calender Batchs")
        ordering = ("-batch",)

    def __str__(self):
        return self.batch


class AcademicCalenderBatchYear(models.Model):
    batch = models.ForeignKey(
        "academic.AcademicCalenderBatch", related_name="years", on_delete=models.CASCADE
    )
    year = models.CharField(max_length=120)
    file = models.FileField(
        upload_to="academic/academic_calender/files",
        validators=[FileExtensionValidator(["pdf"])],
    )

    class Meta:
        db_table = "academic_academic_calender_batch_year"
        verbose_name = _("Academic Calender Batch Year")
        verbose_name_plural = _("Academic Calender Batch Years")

    def __str__(self):
        return self.year


class AcademicCalenderBatchSemester(models.Model):
    batch = models.ForeignKey(
        "academic.AcademicCalenderBatch",
        related_name="semesters",
        on_delete=models.CASCADE,
    )
    semester = models.CharField(max_length=120)
    file = models.FileField(
        upload_to="academic/academic_calender/files",
        validators=[FileExtensionValidator(["pdf"])],
    )

    class Meta:
        db_table = "academic_academic_calender_batch_semester"
        verbose_name = _("Academic Calender Batch Semester")
        verbose_name_plural = _("Academic Calender Batch Semesters")

    def __str__(self):
        return self.semester


class EvaluationPolicySpotlight(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=220)
    image = VersatileImageField(
        "Image", upload_to="academic/evaluation_policy/spotlight/image/"
    )

    class Meta:
        db_table = "academic_evaluation_policy_spotlight"
        verbose_name = _("Evaluation Policy Spotlight")
        verbose_name_plural = _("Evaluation Policy Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return str(self.title)


class EvaluationPolicyFile(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(
        "Image", default="", upload_to="academic/evaluation_policy/files/images/"
    )
    file = models.FileField(
        upload_to="academic/evaluation_policy/files",
        validators=[FileExtensionValidator(["pdf", "jpg"])],
    )
    date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "academic_evaluation_policy_file"
        verbose_name = _("Evaluation Policy File")
        verbose_name_plural = _("Evaluation Policy Files")
        ordering = ("-id",)

    def __str__(self):
        return self.name


class AccountSpotlight(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=220)
    image = VersatileImageField("Image", upload_to="academic/account/spotlight/image/")

    class Meta:
        db_table = "academic_account_spotlight"
        verbose_name = _("Account Spotlight")
        verbose_name_plural = _("Account Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return str(self.title)


class AccountFile(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(
        "Image", default="", upload_to="academic/account/files/images/"
    )
    file = models.FileField(
        upload_to="academic/account/files",
        validators=[FileExtensionValidator(["pdf", "jpg"])],
    )
    date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "academic_account_file"
        verbose_name = _("Account File")
        verbose_name_plural = _("Account Files")
        ordering = ("-id",)

    def __str__(self):
        return self.name
