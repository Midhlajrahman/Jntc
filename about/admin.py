from django.contrib import admin

from .models import (
    AboutUsSpotlight,
    AnnualReport,
    FutureGoalGallery,
    History,
    Objective,
    OurAdministrativeStaff,
    OurStaff,
    OurOfficeStaff,
    OurManagement,
    Planning,
    RulesAndRegulation,
    Foundation,
    PtaCommitee,
    Commitee
)


class AboutUsSpotlightAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title")


class HistoryAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title")


class FutureGoalGalleryAdmin(admin.ModelAdmin):
    list_display = ("image_title",)


class PlanningAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")


class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ("description",)


class OurManagementAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "designation")


class OurAdministrativeStaffAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "designation")


class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ("year_of_report",)


class RulesAndRegulationAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(Foundation)
class FoundationAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title", "description", "image")
    
@admin.register(OurStaff)
class OurStaffAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "designation")
    
@admin.register(OurOfficeStaff)
class OurOfficeStaffAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "designation")
    
@admin.register(PtaCommitee)
class PtaCommiteeAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "designation")
    
@admin.register(Commitee)
class CommiteeAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "designation")


admin.site.register(AboutUsSpotlight, AboutUsSpotlightAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(FutureGoalGallery, FutureGoalGalleryAdmin)
admin.site.register(Planning, PlanningAdmin)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(OurManagement, OurManagementAdmin)
admin.site.register(OurAdministrativeStaff, OurAdministrativeStaffAdmin)
admin.site.register(AnnualReport, AnnualReportAdmin)
admin.site.register(RulesAndRegulation, RulesAndRegulationAdmin)
