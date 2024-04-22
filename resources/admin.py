from django.contrib import admin

from .models import (
    FacilityAdministrative,
    FacilityAdministrativeGallery,
    FacilityCollegeGround,
    FacilityHall,
    FacilityHallGallery,
    FacilityHallTitle,
    FacilityHotelService,
    FacilityInternship,
    FacilityInternshipGallery,
    FacilityLab,
    FacilityLabTitle,
    FacilityLibrary,
    GalleryEvent,
    GalleryEventAlbum,
    GallerySpotlight,
)


class GallerySpotlightAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title", "image")


class GalleryEventAlbumInline(admin.TabularInline):
    model = GalleryEventAlbum


class GalleryEventAdmin(admin.ModelAdmin):
    inlines = [GalleryEventAlbumInline]
    list_display = ("title", "date", "video", "is_deleted")


class FacilityAdministrativeGalleryInline(admin.TabularInline):
    model = FacilityAdministrativeGallery


class FacilityHallGalleryInline(admin.TabularInline):
    model = FacilityHallGallery


class FacilityInternshipGalleryInline(admin.TabularInline):
    model = FacilityInternshipGallery


class FacilityLabInline(admin.TabularInline):
    model = FacilityLab


class FacilityAdministrativeAdmin(admin.ModelAdmin):
    inlines = [FacilityAdministrativeGalleryInline]
    list_display = ["title", "sub_title"]


class FacilityHallAdmin(admin.ModelAdmin):
    inlines = [FacilityHallGalleryInline]
    list_display = ["title", "sub_title"]


class FacilityLibraryAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]


class FacilityLabTitleAdmin(admin.ModelAdmin):
    inlines = [FacilityLabInline]
    list_display = ["title"]


class FacilityInternshipAdmin(admin.ModelAdmin):
    inlines = [FacilityInternshipGalleryInline]
    list_display = ["title", "description"]


class FacilityHotelServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]


class FacilityCollegeGroundAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]


admin.site.register(GallerySpotlight, GallerySpotlightAdmin)
admin.site.register(GalleryEvent, GalleryEventAdmin)

admin.site.register(FacilityAdministrative, FacilityAdministrativeAdmin)
admin.site.register(FacilityHallTitle)
admin.site.register(FacilityHall, FacilityHallAdmin)
admin.site.register(FacilityLibrary, FacilityLibraryAdmin)
admin.site.register(FacilityLabTitle, FacilityLabTitleAdmin)
admin.site.register(FacilityInternship, FacilityInternshipAdmin)
admin.site.register(FacilityHotelService, FacilityHotelServiceAdmin)
admin.site.register(FacilityCollegeGround, FacilityCollegeGroundAdmin)
