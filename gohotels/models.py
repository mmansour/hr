from mezzanine.core.models import Displayable, RichTextField
from django.db import models
from django.utils import simplejson
from django.utils.translation import ugettext, ugettext_lazy as _
from mezzanine.generic.fields import KeywordsField

class HotelPage(Displayable):
    hotelid = models.IntegerField(max_length=400, verbose_name="Hotel ID", blank=True, null=True)
    address1 = models.CharField(max_length=400, verbose_name="Address 1", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="City", blank=True, null=True)
    state_province_code = models.CharField(max_length=10, verbose_name="State Province Code", blank=True, null=True)
    postal_code = models.CharField(max_length=10, verbose_name="Postal Code", blank=True, null=True)
    country_code = models.CharField(max_length=10, verbose_name="Country Code", blank=True, null=True)
    property_category = models.IntegerField(max_length=10, verbose_name="Country Code", blank=True, null=True)
    hotel_rating = models.IntegerField(max_length=10, verbose_name="Hotel Rating", blank=True, null=True)
    trip_advisor_rating = models.IntegerField(max_length=10, verbose_name="Trip Advisor Rating", blank=True, null=True)
    location_description = models.CharField(max_length=400, verbose_name="Location Description", blank=True, null=True) 
    high_rate = models.CharField(max_length=10, verbose_name="Hi Rate", blank=True, null=True)
    low_rate = models.CharField(max_length=10, verbose_name="Low Rate", blank=True, null=True)
    latitude = models.CharField(max_length=10, verbose_name="Latitude", blank=True, null=True)
    longitude = models.CharField(max_length=10, verbose_name="Longitude", blank=True, null=True)
    number_of_rooms = models.IntegerField(max_length=10, verbose_name="Number of rooms", blank=True, null=True)
    number_of_floors = models.IntegerField(max_length=10, verbose_name="Number of floors", blank=True, null=True)
    check_in_time = models.DateTimeField(blank=True, null=True, verbose_name="Check in time",)
    check_out_time = models.DateTimeField(blank=True, null=True, verbose_name="Check out time",)
#    keywords = KeywordsField(verbose_name=_("Keywords"))
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

    def __unicode__(self):
        return self.title