from django.contrib import admin

from .models import (
    HomeAbout,
    HomeAnnouncement,
    HomeInstitution,
    HomeInstitutionHeading,
    HomeLatestNews,
    HomeLatestNewsGallery,
    HomeNewsAndEventsSpotlight,
    HomeSpotlight,
    HomeSpotlightGallery,
    HomeUpcomingEvent,
    HomeUpcomingEventGallery,
)


class HomeSpotlightGalleryInline(admin.TabularInline):
    model = HomeSpotlightGallery


class HomeLatestNewsGalleryInline(admin.TabularInline):
    model = HomeLatestNewsGallery


class HomeUpcomingEventGalleryInline(admin.TabularInline):
    model = HomeUpcomingEventGallery


class HomeInstitutionInline(admin.TabularInline):
    model = HomeInstitution


class HomeLatestNewsAdmin(admin.ModelAdmin):
    inlines = [HomeLatestNewsGalleryInline]
    list_display = ("title", "description", "date", "is_deleted")


class HomeEventAdmin(admin.ModelAdmin):
    inlines = [HomeUpcomingEventGalleryInline]
    list_display = ("title", "description", "date", "is_deleted")


class HomeAnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "date", "is_deleted")


class HomeAboutAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


class HomeSpotlightAdmin(admin.ModelAdmin):
    inlines = [HomeSpotlightGalleryInline]
    list_display = ("title", "sub_title")


class HomeInstitutionHeadingAdmin(admin.ModelAdmin):
    inlines = [HomeInstitutionInline]


admin.site.register(HomeNewsAndEventsSpotlight)
admin.site.register(HomeLatestNews, HomeLatestNewsAdmin)
admin.site.register(HomeUpcomingEvent, HomeEventAdmin)
admin.site.register(HomeAnnouncement, HomeAnnouncementAdmin)
admin.site.register(HomeInstitutionHeading, HomeInstitutionHeadingAdmin)
admin.site.register(HomeAbout, HomeAboutAdmin)
admin.site.register(HomeSpotlight, HomeSpotlightAdmin)
