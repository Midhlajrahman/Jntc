from django.contrib import admin

from .models import (
    BEdExaminationResult,
    BEdResultStatusBatch,
    BEdResultStatusBatchSemester,
    BEdResultStatusBatchYear,
    BEdStudent,
    DownloadFile,
    DownloadSpotlight,
    MagazineFile,
)


class BEdResultStatusBatchYearInline(admin.TabularInline):
    model = BEdResultStatusBatchYear


class BEdResultStatusBatchSemesterInline(admin.TabularInline):
    model = BEdResultStatusBatchSemester


class BEdResultStatusBatchAdmin(admin.ModelAdmin):
    inlines = [BEdResultStatusBatchYearInline, BEdResultStatusBatchSemesterInline]


class BEdStudentInline(admin.TabularInline):
    model = BEdStudent


class BEdExaminationResultAdmin(admin.ModelAdmin):
    inlines = [BEdStudentInline]


admin.site.register(BEdResultStatusBatch, BEdResultStatusBatchAdmin)

admin.site.register(BEdExaminationResult, BEdExaminationResultAdmin)

admin.site.register(DownloadSpotlight)
admin.site.register(DownloadFile)
admin.site.register(MagazineFile)
