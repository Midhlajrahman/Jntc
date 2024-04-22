import datetime
import uuid

from django.db import models
from django.utils.translation import gettext as _
from versatileimagefield.fields import VersatileImageField


class HomeSpotlight(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    class Meta:
        db_table = "web_home_spotlight"
        verbose_name = _("Home Spotlight")
        verbose_name_plural = _("Home Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class HomeSpotlightGallery(models.Model):
    spotlight = models.ForeignKey(
        "web.HomeSpotlight", related_name="gallery", on_delete=models.CASCADE
    )
    image = VersatileImageField("Image", upload_to="home/spotlight/images/")

    class Meta:
        db_table = "web_home_spotlight_gallery"
        verbose_name = _("Home Spotlight Gallery")
        verbose_name_plural = _("Home Spotlight Galleries")

    def __str__(self):
        return str(self.spotlight)


class HomeAbout(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = VersatileImageField("Image", upload_to="home/about/images/")

    class Meta:
        db_table = "web_home_About"
        verbose_name = _("Home About")
        verbose_name_plural = _("Home Abouts")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class HomeNewsAndEventsSpotlight(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    image = VersatileImageField(
        "Image", upload_to="home/news_and_events/spotlight/image/"
    )

    class Meta:
        db_table = "web_home_news_and_events_spotlight"
        verbose_name = _("Home News and Events Spotlight")
        verbose_name_plural = _("Home News and Events Spotlights")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class HomeLatestNews(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "web_home_latest_news"
        verbose_name = _("Home Latest News")
        verbose_name_plural = _("Home Latest News")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class HomeLatestNewsGallery(models.Model):
    news = models.ForeignKey(
        "web.HomeLatestNews", related_name="gallery", on_delete=models.CASCADE
    )
    image = VersatileImageField(
        "Image", upload_to="home/news_and_events/latest_news/images/"
    )

    class Meta:
        db_table = "web_home_latest_news__gallery"
        verbose_name = _("Home Latest News Gallery")
        verbose_name_plural = _("Home Latest News Galleries")

    def __str__(self):
        return str(self.news)


class HomeUpcomingEvent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    is_featured = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "web_home_upcoming_event"
        verbose_name = _("Home Upcoming Event")
        verbose_name_plural = _("Home Upcoming Events")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class HomeUpcomingEventGallery(models.Model):
    events = models.ForeignKey(
        "web.HomeUpcomingEvent", related_name="gallery", on_delete=models.CASCADE
    )
    image = VersatileImageField(
        "Image", upload_to="home/news_and_events/events/images/"
    )

    class Meta:
        db_table = "web_home_Upcoming_Event__gallery"
        verbose_name = _("Home Upcoming Event Gallery")
        verbose_name_plural = _("Home Upcoming Event Galleries")

    def __str__(self):
        return str(self.events)


class HomeAnnouncement(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=200, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "web_home_announcement"
        verbose_name = _("Home Announcement")
        verbose_name_plural = _("Home Announcements")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class HomeInstitutionHeading(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = "web_home_institution_heading"
        verbose_name = _("Home Institution Heading")
        verbose_name_plural = _("Home Institution Headings")
        ordering = ("-id",)

    def __str__(self):
        return self.title


class HomeInstitution(models.Model):
    institution = models.ForeignKey(
        "web.HomeInstitutionHeading",
        related_name="institution",
        default="1",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = VersatileImageField("Image", upload_to="home/institution/images/")
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "web_home_institution"
        verbose_name = _("Home Institution")
        verbose_name_plural = _("Home Institutions")
        ordering = ("-id",)

    def __str__(self):
        return self.title
