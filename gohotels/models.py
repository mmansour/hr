from mezzanine.core.models import Displayable, RichTextField
from django.db import models
from django.utils import simplejson
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from mezzanine.generic.fields import CommentsField, RatingField

#Required for south to work with geo django
from south.modelsinspector import add_introspection_rules
rules = [
  (
    (),
    [],
    {
#        "to": ["rel.to", {}],
#        "to_field": ["rel.field_name", {"default_attr": "rel.to._meta.pk.name"}],
#        "related_name": ["rel.related_name", {"default": None}],
#        "db_index": ["db_index", {"default": True}],
    },
  )
]
add_introspection_rules(rules, ["^django\.contrib\.gis"])


class HotelPage(Displayable):
    hotelid = models.IntegerField(max_length=400, verbose_name="Hotel ID", blank=True, null=True)
    video_youtube_id = models.CharField(max_length=40, verbose_name="Youtube Video ID", blank=True, null=True)
    thumbnail_url = models.CharField(max_length=200, verbose_name="Thumbnail Url", blank=True, null=True)
    website = models.CharField(max_length=200, verbose_name="Website", blank=True, null=True)
    is_featured = models.BooleanField(default=False, verbose_name="Is This Hotel Featured?")
    address1 = models.CharField(max_length=400, verbose_name="Address 1", blank=True, null=True)
#    address2 = models.CharField(max_length=400, verbose_name="Address 2", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="City", blank=True, null=True)
    state_province_code = models.CharField(max_length=40, verbose_name="State Province Code", blank=True, null=True)
    postal_code = models.CharField(max_length=40, verbose_name="Postal Code", blank=True, null=True)
    country_code = models.CharField(max_length=40, verbose_name="Country Code", blank=True, null=True)
    rate_currency_code = models.CharField(max_length=40, verbose_name="Rate Currency Code", blank=True, null=True)
    property_category = models.CharField(max_length=40, verbose_name="Property Type", blank=True, null=True)
#    property_type = models.CharField(max_length=10, verbose_name="Property Type", blank=True, null=True)
    hotel_rating = models.IntegerField(max_length=40, verbose_name="Hotel Rating", blank=True, null=True)
    trip_advisor_rating = models.IntegerField(max_length=40, verbose_name="Trip Advisor Rating", blank=True, null=True)
    location_description = models.CharField(max_length=400, verbose_name="Location Description", blank=True, null=True) 
    high_rate = models.CharField(max_length=40, verbose_name="Hi Rate", blank=True, null=True)
    low_rate = models.CharField(max_length=40, verbose_name="Low Rate", blank=True, null=True)
    latitude = models.CharField(max_length=40, verbose_name="Latitude", blank=True, null=True)
    longitude = models.CharField(max_length=40, verbose_name="Longitude", blank=True, null=True)
    number_of_rooms = models.IntegerField(max_length=40, verbose_name="Number of rooms", blank=True, null=True)
    number_of_floors = models.IntegerField(max_length=40, verbose_name="Number of floors", blank=True, null=True)
    check_in_time = models.CharField(max_length=40, verbose_name="Check in Time", blank=True, null=True)
    check_out_time = models.CharField(max_length=40, verbose_name="Check out Time", blank=True, null=True)
    property_information = RichTextField(blank=True, verbose_name="Property Information")
    area_information = RichTextField(blank=True, verbose_name="Area Information")
    property_description = RichTextField(blank=True, verbose_name="Property Description")
    hotel_policy = RichTextField(blank=True, verbose_name="Hotel Policy")
    room_information = RichTextField(blank=True, verbose_name="Room Information")
    driving_directions = RichTextField(blank=True, verbose_name="Driving Directions")
    checkin_instructions = RichTextField(blank=True, verbose_name="Checkin Instructions")
    room_types = RichTextField(blank=True, verbose_name="Room Types")
    room_amenities = RichTextField(blank=True, verbose_name="Room Amenities")
    property_amenities = RichTextField(blank=True, verbose_name="Property Amenities")
    allow_comments = models.BooleanField(verbose_name=_("Allow comments"),
                                         default=True)
    comments = CommentsField(verbose_name=_("Comments"))
    rating = RatingField(verbose_name=_("Rating"))
    point = models.PointField(null=True, blank=True)
    geomanager = models.GeoManager()
    search_fields = {"title":5, "city": 10, "state_province_code": 5, "property_description":5 }
#    search_fields = {"city": 10}

    @models.permalink
    def get_absolute_url(self):
        return ('gohotels.views.detail', [self.slug, self.hotelid])

    def save(self, *args, **kwargs):
        self.point = Point(float(self.longitude), float(self.latitude))
        super(HotelPage, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class HotelImage(models.Model):
    image_url = models.CharField(max_length=200, verbose_name="Hotel Image URL", blank=True, null=True)
    thumbnail_url = models.CharField(max_length=200, verbose_name="Hotel Thumbmail URL", blank=True, null=True)
    alt = models.CharField(max_length=200, verbose_name="Alt", blank=True, null=True)
    hotel = models.ForeignKey(HotelPage, null=True, blank=True)


class HotelRoomImage(models.Model):
    image = models.CharField(max_length=200, verbose_name="Hotel Room Image URL", blank=True, null=True)
    alt = models.CharField(max_length=200, verbose_name="Alt", blank=True, null=True)
    hotel = models.ForeignKey(HotelPage, null=True, blank=True)
