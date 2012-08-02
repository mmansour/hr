from django.core.management.base import BaseCommand, CommandError
import requests
import json
import time
class Command(BaseCommand):
    help = 'Pulls the wellness hotels in from the expedia api'
    def handle(self, *args, **options):
        hotellist = requests.get('''http://api.ean.com/ean-services/rs/hotel/v3/list?cid=55505\
        &apiKey=5vmbsthq9569w8f25xzzggmf&customerUserAgent=xxx&customerIpAddress=xxx&locale=en_US\
        &currencyCode=USD&city=Big Sur&stateProvinceCode=CA&countryCode=US&supplierCacheTolerance=MED\
        &room1=2&supplierCacheTolerance=MED_ENHANCED''')
        hotelidlist = []
        responsedictlist = json.loads(hotellist.content)
        
        try:
            ## BUILD A LIST OF HOTEL IDS
            for h in responsedictlist['HotelListResponse']['HotelList']['HotelSummary']:
                hotelidlist.append(h['hotelId'])

            def get_hotel_images(hid):
                hotelimagelist = []
                hotelimages = requests.get('''http://api.ean.com/ean-services/rs/hotel/v3/info?cid=55505\
                    &apiKey=5vmbsthq9569w8f25xzzggmf&customerUserAgent=xxx&customerIpAddress=xxx&customerSessionId=xxx\
                    &locale=en_US&currencyCode=USD&hotelId={0}&options=HOTEL_IMAGES'''.format(hid))

                responsedictimages = json.loads(hotelimages.content)

                for img in responsedictimages['HotelInformationResponse']['HotelImages']['HotelImage']:
                    hotelimagelist.append(img)

                return hotelimagelist

            def get_hotel_details(hlist):
                keywordlist = ["retreat", "organic", "wellness", "boutique", "green hotel", "bed and breakfast", "organic food", "organic wine", "art galleries"]
                for h in hlist:
                    hoteldetail = requests.get('''http://api.ean.com/ean-services/rs/hotel/v3/info?cid=55505\
                            &apiKey=5vmbsthq9569w8f25xzzggmf&customerUserAgent=xxx&customerIpAddress=xxx&customerSessionId=xxx\
                            &locale=en_US&currencyCode=USD&hotelId={0}&options=HOTEL_DETAILS'''.format(h))

                    responsedictdetail = json.loads(hoteldetail.content)

                    for word in keywordlist:

                        if word.lower() in responsedictdetail['HotelInformationResponse']['HotelDetails']['propertyDescription'].lower():
                            print '------------------------------------------------------------'
    #                        print responsedictdetail['HotelInformationResponse']['HotelDetails']
                            print responsedictdetail['HotelInformationResponse']['HotelDetails']['propertyDescription'].replace('&lt;','<').replace('&gt;', '>')\
                                                                                                        .replace("&apos;","'").replace("&#x0D","")
                            time.sleep(1)


            ### TEST GET IMAGES (WORKS)
    #        for img in get_hotel_images('193092'):
    #            print img['url'].replace('images.travelnow.com', 'media.hotelretreats.com')
            
            get_hotel_details(hotelidlist)

        except Exception:
            pass

#        print responsedict


