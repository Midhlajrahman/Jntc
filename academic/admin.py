from django.contrib import admin

from .models import (
    AcademicCalenderBatch,
    AcademicCalenderBatchSemester,
    AcademicCalenderBatchYear,
    AcademicCalenderSpotlight,
    AcademicCourse,
    AcademicCourseHeading,
    AccountFile,
    AccountSpotlight,
    EvaluationPolicyFile,
    EvaluationPolicySpotlight,
    ProgramAbout,
    ProgramAboutGallery,
    ProgramGateway,
    ProgramGatewayHeading,
    ProgramInformation,
    ProgramInformationFile,
    ProgramObjective,
    ProgramObjectivePoint,
    ProgramSpotlight,
)


class ProgramAboutGalleryInline(admin.TabularInline):
    model = ProgramAboutGallery


class ProgramObjectivePointInline(admin.TabularInline):
    model = ProgramObjectivePoint


class ProgramGatewayInline(admin.TabularInline):
    model = ProgramGateway


class AcademicCalenderBatchYearInline(admin.TabularInline):
    model = AcademicCalenderBatchYear


class AcademicCalenderBatchSemesterInline(admin.TabularInline):
    model = AcademicCalenderBatchSemester


class ProgramAboutAdmin(admin.ModelAdmin):
    model = ProgramAbout
    inlines = [ProgramAboutGalleryInline]


class ProgramObjectiveAdmin(admin.ModelAdmin):
    model = ProgramObjective
    inlines = [ProgramObjectivePointInline]


class ProgramGatewayHeadingAdmin(admin.ModelAdmin):
    model = ProgramGatewayHeading
    inlines = [ProgramGatewayInline]


class AcademicCalenderBatchAdmin(admin.ModelAdmin):
    inlines = [AcademicCalenderBatchYearInline, AcademicCalenderBatchSemesterInline]


admin.site.register(AcademicCourseHeading)
admin.site.register(AcademicCourse)

admin.site.register(ProgramSpotlight)
admin.site.register(ProgramInformation)
admin.site.register(ProgramInformationFile)
admin.site.register(ProgramAbout, ProgramAboutAdmin)
admin.site.register(ProgramObjective, ProgramObjectiveAdmin)
admin.site.register(ProgramGatewayHeading, ProgramGatewayHeadingAdmin)


admin.site.register(AcademicCalenderSpotlight)
admin.site.register(AcademicCalenderBatch, AcademicCalenderBatchAdmin)

admin.site.register(EvaluationPolicySpotlight)
admin.site.register(EvaluationPolicyFile)

admin.site.register(AccountSpotlight)
admin.site.register(AccountFile)
