from django.contrib import admin

from .models import (
    AboutOurAlumniNetwork,
    ActivityGallery,
    AlumniActivity,
    AlumniNetworkRegistration,
    AlumniSpotlight,
    AlumniTeam,
    BEdSubjectChoice,
    EducationalStatusChoice,
    Faculty,
    GenderChoice,
    MaritalStatusChoice,
    Student,
    YearOfStudyChoice,
)


class ActivityGalleryInline(admin.TabularInline):
    model = ActivityGallery


class AlumniNetworkRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "gender",
        "phone_number",
        "date",
        "is_verified",
        "is_deleted",
    )


admin.site.register(AlumniNetworkRegistration, AlumniNetworkRegistrationAdmin)


class AlumniActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title", "description", "date", "is_deleted")
    inlines = [ActivityGalleryInline]


admin.site.register(AlumniActivity, AlumniActivityAdmin)


class AlumniTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "is_deleted")


admin.site.register(AlumniTeam, AlumniTeamAdmin)


admin.site.register(GenderChoice)
admin.site.register(MaritalStatusChoice)
admin.site.register(BEdSubjectChoice)
admin.site.register(YearOfStudyChoice)
admin.site.register(EducationalStatusChoice)

admin.site.register(AlumniSpotlight)
admin.site.register(AboutOurAlumniNetwork)
admin.site.register(Student)
admin.site.register(Faculty)
