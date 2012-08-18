from django.core.management.base import BaseCommand, CommandError
from gohotels.models import HotelPage, HotelImage
from django.utils.encoding import force_unicode
from mezzanine.core.models import slugify
import requests
import json
import time
import datetime
import csv
import re

class Command(BaseCommand):
    help = 'Pulls the condos'
    def handle(self, *args, **options):
        keywordlist = ["retreat",
                       "organic",
                       "organic food",
                       "organic wine",
                       "wellness",
                       "wellness spa",
                       "eco friendly",
                       "meditation",
                       "new age",
                       "spiritual",
                       "spirituality",
                       "power vortex",
                       "therapeutic",
                       "zen",
                       "healing",
                       "yoga",
                       "eco-friendly",
                       "health conscious",
                       "rejuvenation",
                       "creativity",
                       "spiritual vortex",
                       "vortex",
                       "inner reflection",
                       "chakras",
                       "self improvement",
                       "transformational",
                       "creativity",
                       "artists haven",
#                       "crystals",
#                       "eco",
#                       "ocean",
#                       "beachfront",
#                       "mountains",
#                       "skiing",
#                       "surfing",
#                       "boutique hotel",
#                       "boutique inn"
        ]
        exactMatch = re.compile(r'\b%s\b' % '\\b|\\b'.join(keywordlist), flags=re.IGNORECASE)
        with open('/users/mattmansour/django/sites/dev/hotelretreats/docs/condo_all_active_utf8.txt', 'rU') as f:
#        with open('/home/mattym/webapps/hotelretreats/docs/condo_all_active_utf8.txt', 'rU') as f:

            reader = csv.reader(f, delimiter='|')
            reader.next() # SKIPS HEADER LINE
            for col in reader:
                try:
                    try:
                        hotel = HotelPage.objects.get(hotelid=col[0])
                        hotel.title="{0}".format(col[1].decode('utf-8'))
                        hotel.slug = slugify("{0} {1} {2} {3}".format(col[1], col[6], col[7], col[8]))
                        hotel.publish_date=datetime.datetime.now()
                        hotel.status=2
                        hotel.address1=col[3]
                        hotel.city=col[6]
                        hotel.state_province_code=col[7]
                        hotel.postal_code=col[9]
                        hotel.country_code=col[8]
                        hotel.rate_currency_code=col[22]
                        hotel.property_category=col[17]
                        hotel.latitude=col[11]
                        hotel.longitude=col[10]
                        hotel.low_rate=col[12]
                        hotel.high_rate=col[13]
                        hotel.number_of_rooms=col[23]
                        hotel.check_in_time=col[26]
                        hotel.check_out_time=col[27]
                        hotel.save()
                        print "Saved hotel {0}".format(hotel)
                    except HotelPage.DoesNotExist:
                        pass
                except UnicodeEncodeError:
                    pass
















  