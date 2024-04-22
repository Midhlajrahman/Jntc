from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField


class AboutUsSpotlight(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=255)
    image = VersatileImageField("Image", upload_to="about_us/spotlight/image/")

    class Meta:
        db_table = "about_about_us_spotlight"
        verbose_name = _("AboutUs Spotlight")
        verbose_name_plural = _("AboutUs Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class History(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=150)
    description = models.TextField()
    image = VersatileImageField("Image", upload_to="about_us/history/image/")

    class Meta:
        db_table = "about_history"
        verbose_name = _("History")
        verbose_name_plural = _("Histories")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class Foundation(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=150,blank=True,null=True)
    description = models.TextField()
    image = VersatileImageField("Image", upload_to="about_us/Foundation/image/")

    class Meta:
        db_table = "about_Foundation"
        verbose_name = _("Foundation")
        verbose_name_plural = _("Foundations")
        ordering = ("-id",)

    def __str__(self):
        return self.title

class FutureGoalGallery(models.Model):
    image_title = models.CharField(max_length=150)
    image = VersatileImageField(
        "Image", upload_to="about_us/future_goal_gallery/image/"
    )

    class Meta:
        db_table = "about_future_goal_gallery"
        verbose_name = _("Future Goal Gallery")
        verbose_name_plural = _("Future Goal Galleries")
        ordering = ("-id",)

    def __str__(self):
        return self.image_title


class Planning(models.Model):
    image = models.ForeignKey(
        "about.FutureGoalGallery", related_name="goal", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=120)
    description = models.TextField()

    class Meta:
        db_table = "about_planning"
        verbose_name = _("planning")
        verbose_name_plural = _("plannings")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class Objective(models.Model):
    description = models.TextField()

    class Meta:
        db_table = "about_objective"
        verbose_name = _("Objective")
        verbose_name_plural = _("Objectives")
        ordering = ("-id",)

    def __str__(self):
        return str(self.id)


class OurManagement(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField("Image", upload_to="about_us/our_management/images/")
    designation = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "about_our_management"
        verbose_name = _("Our Management")
        verbose_name_plural = _("Our Managements")
        ordering = ("id",)

    def __str__(self):
        return self.name


class OurAdministrativeStaff(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(
        "Image", upload_to="about_us/administrative_staff/images/"
    )
    designation = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "about_our_administrative_staff"
        verbose_name = _("Our Administrative Staff")
        verbose_name_plural = _("Our Administrative Staffs")
        ordering = ("id",)

    def __str__(self):
        return self.name


class OurStaff(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(
        "Image", upload_to="about_us/staff/images/"
    )
    designation = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "about_our_staff"
        verbose_name = _("Our Staff")
        verbose_name_plural = _("Our Staffs")
        ordering = ("id",)

    def __str__(self):
        return self.name
    

class OurOfficeStaff(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(
        "Image", upload_to="about_us/Office_staff/images/"
    )
    designation = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "about_our_Office_staff"
        verbose_name = _("Our Office Staff")
        verbose_name_plural = _("Our Office Staffs")
        ordering = ("id",)

    def __str__(self):
        return self.name
    
class PtaCommitee(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(
        "Image", upload_to="about_us/pta_commitee/images/"
    )
    designation = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "about_our_PTA_commitee"
        verbose_name = _("Our PTA Commitee")
        verbose_name_plural = _("Our PTA Commitees")
        ordering = ("id",)

    def __str__(self):
        return self.name
    
class Commitee(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(
        "Image", upload_to="about_us/commitee/images/"
    )
    designation = models.CharField(max_length=120)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "about_our_commitee"
        verbose_name = _("Our Commitee")
        verbose_name_plural = _("Our Commitees")
        ordering = ("id",)

    def __str__(self):
        return self.name

class AnnualReport(models.Model):
    year_of_report = models.CharField(max_length=55)
    file = models.FileField(upload_to="about_us/annual_report/files/")

    class Meta:
        db_table = "about_annual_report"
        verbose_name = _("Annual Report")
        verbose_name_plural = _("Annual Reports")
        ordering = ("-year_of_report",)

    def __str__(self):
        return self.year_of_report


class RulesAndRegulation(models.Model):
    title = models.CharField(max_length=120)
    file = models.FileField(upload_to="about_us/rules_and_regulations/files/")

    class Meta:
        db_table = "about_rules_and_regulation"
        verbose_name = _("Rules And Regulation")
        verbose_name_plural = _("Rules And Regulations")
        ordering = ("-id",)

    def __str__(self):
        return self.title
