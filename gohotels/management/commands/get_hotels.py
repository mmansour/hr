from django.core.management.base import BaseCommand, CommandError
from gohotels.models import HotelPage
import requests
import json
import time
import csv
class Command(BaseCommand):
    help = 'Pulls the wellness hotels in from the expedia api'
    def handle(self, *args, **options):
        keywordlist = ["retreat", "organic", "wellness", "boutique", "green hotel", "bed and breakfast", "organic food", "organic wine", "art galleries"]

#        h, created = HotelPage.objects.get_or_create(
#        first_name='John', last_name='Lennon',
#        defaults={'birthday': date(1940, 10, 9)})
        
        with open('/users/mattmansour/django/sites/dev/hotelretreats/docs/hotel_all_active.csv', 'rU') as f:
            reader = csv.reader(f, delimiter=',')
            for col in reader:
#                col[0] Hotel Id
#                col[1] Hotel Name
#                col[3] Address 1
#                col[6] City
#                col[7] State/Province
#                col[8] Country
#                col[9] Postal Code
#                col[10] Longitude
#                col[11] Latitude
#                col[12] Low Rate
#                col[13] High Rate
#                col[17] Property Type
#                col[22] Native Currency
#                col[23] Number of Rooms
#                col[26] Check in time
#                col[27] Check out time
#                col[72] Property Description Etc...

                for word in keywordlist:
                    if word in col[72].lower():
                        print col[0], col[1], col[3], col[6], col[7], col[8], col[9], col[10], col[11], col[17]
#                        print col[72]



###################################################################################################################### API
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


