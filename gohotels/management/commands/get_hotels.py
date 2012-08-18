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
    help = 'Pulls the wellness hotels'
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
#       EXAMPLE print len(exactMatch.findall("health conscious, eco-friendly then there was the time when <p>SURFING</p>"))

#       Order of operations for import data
#       1. import filtered hotels active
#       2. import filtered condo descriptions
#       3. import remaining condo data filtered condos
#       4. import images

        with open('/users/mattmansour/django/sites/dev/hotelretreats/docs/hotel_all_active_utf.csv', 'rU') as f:
#        with open('/home/mattym/webapps/hotelretreats/docs/hotel_all_active_utf.csv', 'rU') as f:
            reader = csv.reader(f, delimiter=',')
            reader.next() # SKIPS HEADER LINE
            for col in reader:

#                col[0] Hotel Id, col[1] Hotel Name | Or property description in condo_desc.csv
#                col[3] Address 1, col[6] City, col[7] State/Province, col[8] Country, col[9] Postal Code
#                col[10] Longitude, col[11] Latitude, col[12] Low Rate, col[13] High Rate, col[17] Property Type
#                col[22] Native Currency, col[23] Number of Rooms, col[26] Check in time
#                col[27] Check out time, col[72] Property Description Etc...

                filteredkeywordlist = []
                for word in keywordlist:
                    if len(exactMatch.findall(col[72])) > 0:
                        filteredkeywordlist.append(col[0])

                dedupedfilteredkeywordlist = list(set(filteredkeywordlist))

                for h in dedupedfilteredkeywordlist:
                    try:
                        h, created = HotelPage.objects.get_or_create(
                            title="{0}".format(col[1].decode('utf-8')),
                            slug = slugify("{0} {1} {2} {3}".format(col[1], col[6], col[7], col[8])),
                            publish_date=datetime.datetime.now(),
                            status=2,
                            hotelid=col[0],
                            address1=col[3],
                            city=col[6],
                            state_province_code=col[7],
                            postal_code=col[9],
                            country_code=col[8],
                            rate_currency_code=col[22],
                            property_category=col[17],
                            latitude=col[11],
                            longitude=col[10],
                            low_rate=col[12],
                            high_rate=col[13],
                            number_of_rooms=col[23],
                            check_in_time=col[26],
                            check_out_time=col[27],
                            property_description=col[72],
                        )
                        print h, created
                    except UnicodeEncodeError:
                        pass

###############################################################  API EXAMPLES ############################################################### 

#        hotellist = requests.get('''http://api.ean.com/ean-services/rs/hotel/v3/list?cid=55505\
#        &apiKey=5vmbsthq9569w8f25xzzggmf&customerUserAgent=xxx&customerIpAddress=xxx&locale=en_US\
#        &currencyCode=USD&city=Big Sur&stateProvinceCode=CA&countryCode=US&supplierCacheTolerance=MED\
#        &room1=2&supplierCacheTolerance=MED_ENHANCED''')
#        hotelidlist = []
#        responsedictlist = json.loads(hotellist.content)
#
#        try:
#            ## BUILD A LIST OF HOTEL IDS
#            for h in responsedictlist['HotelListResponse']['HotelList']['HotelSummary']:
#                hotelidlist.append(h['hotelId'])
#
#            def get_hotel_images(hid):
#
#                hotelimagelist = []
#                try:
#                    hotelimages = requests.get('''http://api.ean.com/ean-services/rs/hotel/v3/info?cid=55505\
#                        &apiKey=5vmbsthq9569w8f25xzzggmf&customerUserAgent=xxx&customerIpAddress=xxx&customerSessionId=xxx\
#                        &locale=en_US&currencyCode=USD&hotelId={0}&options=HOTEL_IMAGES'''.format(hid))
#
#                    responsedictimages = json.loads(hotelimages.content)
#
#                    for img in responsedictimages['HotelInformationResponse']['HotelImages']['HotelImage']:
#                        hotelimagelist.append(img)
#                except Exception:
#                    pass
#
#                return hotelimagelist
#
#            def get_hotel_details(hlist):
##                keywordlist = [" "]
#                keywordlist = ["retreat", "organic", "wellness", "boutique", "green hotel", "bed and breakfast", "organic food", "organic wine", "art galleries"]
#
#                for h in hlist:
#
#                    hoteldetail = requests.get('''http://api.ean.com/ean-services/rs/hotel/v3/info?cid=55505\
#                            &apiKey=5vmbsthq9569w8f25xzzggmf&customerUserAgent=xxx&customerIpAddress=xxx&customerSessionId=xxx\
#                            &locale=en_US&currencyCode=USD&hotelId={0}&options=HOTEL_DETAILS'''.format(h))
#                    responsedictdetail = json.loads(hoteldetail.content)
#
#                    try:
#                        for word in keywordlist:
#                            if word.lower() in responsedictdetail['HotelInformationResponse']['HotelDetails']['propertyDescription'].lower():
#                                print '------------------------------------------------------------'
#                                print responsedictdetail['HotelInformationResponse']['HotelDetails']['propertyDescription'].replace('&lt;','<').replace('&gt;', '>')\
#                                                                                                            .replace("&apos;","'").replace("&#x0D","")
#                                for img in get_hotel_images(responsedictdetail['HotelInformationResponse']['@hotelId']):
#                                    print img['url'].replace('images.travelnow.com', 'media.hotelretreats.com')
#
#                            time.sleep(1)
#                    except Exception:
#                        pass
#
#
#            get_hotel_details(hotelidlist)

#        except Exception:
#            pass

#        print responsedict


