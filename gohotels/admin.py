from gohotels.models import HotelPage, HotelRoomImage, HotelImage
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin

class ChoiceInlineRoomImage(admin.TabularInline):
    model = HotelRoomImage
    extra = 2

class ChoiceInlineHotelImage(admin.TabularInline):
    model = HotelImage
    extra = 2

class HotelAdmin(DisplayableAdmin):

#    fieldsets = battles_fieldsets
    fieldsets = [
        ("Title",                 {'fields': ['title', 'hotelid']}),
        ("Published Date",        {'fields': ['publish_date']}),
        ("Published Status",      {'fields': ['status']}),
        ("Thunbnail",              {'fields': ['thumbnail_url']}),
        ("Video ID",              {'fields': ['video_youtube_id']}),
        ("Address",               {'fields': ['address1','city','state_province_code','postal_code','country_code']}),
        ("Geo Data",              {'fields': ['latitude','longitude']}),
        ("Description",           {'fields': ['location_description','area_information','property_description','hotel_policy',\
                                                  'room_information','checkin_instructions', 'driving_directions', 'room_types',\
                                                  'room_amenities', 'property_amenities']}),
        ("Rate Currency Code",              {'fields': ['rate_currency_code']}),
        ("Rates",              {'fields': ['low_rate', 'high_rate']}),
    ]

    inlines = [ChoiceInlineHotelImage, ChoiceInlineRoomImage,]
    list_display = ('title', 'status', 'publish_date',)
    list_editable = ('status',)
    list_filter = ['status','publish_date']
    search_fields = ['title']
    date_hierarchy = 'publish_date'

admin.site.register(HotelPage, HotelAdmin)