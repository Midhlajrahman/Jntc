from django.contrib import admin

from .models import (
    IQACAbout,
    IQACAboutGallery,
    IQACComplaint,
    IQACFunctionName,
    IQACFunctionRecord,
    IQACObjective,
    IQACOurVision,
    IQACSpotlight,
    IQACTeam,
    LocalSociety,
)


class IQACSpotlightAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title")


admin.site.register(IQACSpotlight, IQACSpotlightAdmin)


class IQACAboutGalleryInline(admin.TabularInline):
    model = IQACAboutGallery


class IQACFunctionRecordInline(admin.TabularInline):
    model = IQACFunctionRecord


class IQACAboutAdmin(admin.ModelAdmin):
    inlines = [IQACAboutGalleryInline]
    list_display = ("title",)


class IQACOurVisionAdmin(admin.ModelAdmin):
    list_display = ("member", "title")


class IQACObjectiveAdmin(admin.ModelAdmin):
    list_display = ("member", "title")


class IQACTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "is_deleted")


class LocalSocietyAdmin(admin.ModelAdmin):
    list_display = ("name", "panchayat", "is_deleted")


class IQACFunctionNameAdmin(admin.ModelAdmin):
    inlines = [IQACFunctionRecordInline]


class IQACComplaintAdmin(admin.ModelAdmin):
    list_display = ("date", "first_name", "last_name", "year_of_batch", "subject")


admin.site.register(IQACAbout, IQACAboutAdmin)
admin.site.register(IQACOurVision, IQACOurVisionAdmin)
admin.site.register(IQACObjective, IQACObjectiveAdmin)
admin.site.register(LocalSociety, LocalSocietyAdmin)
admin.site.register(IQACTeam, IQACTeamAdmin)
admin.site.register(IQACFunctionName, IQACFunctionNameAdmin)
admin.site.register(IQACComplaint, IQACComplaintAdmin)
