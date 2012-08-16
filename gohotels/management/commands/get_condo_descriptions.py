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
    help = 'Pulls the condo descriptions'
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

        filteredcondodescdict = {}
        exactMatch = re.compile(r'\b%s\b' % '\\b|\\b'.join(keywordlist), flags=re.IGNORECASE)
#        with open('/users/mattmansour/django/sites/dev/hotelretreats/docs/condo_desc_utf.csv', 'rU') as f:
        with open('/home/mattym/webapps/hotelretreats/docs/condo_desc_utf.csv', 'rU') as f:

            reader = csv.reader(f, delimiter=',')
            reader.next() # SKIPS HEADER LINE
            for col in reader:
                for word in keywordlist:
                    if len(exactMatch.findall(col[1])) > 0:
                        filteredcondodescdict[col[0]] = col[1]

            for key, value in filteredcondodescdict.iteritems():
                try:
                    c, created = HotelPage.objects.get_or_create(
                        title="{0}".format('Condo {0}'.format(key)),
                        publish_date=datetime.datetime.now(),
                        status=1,
                        hotelid=key,
                        property_description=value,
                    )
                    print c, created
                except UnicodeEncodeError:
                    pass

















  