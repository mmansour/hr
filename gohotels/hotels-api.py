import requests
import json

########################################## HOTEL LIST ################################################

#hotellist = requests.get('http://api.ean.com/ean-services/rs/hotel/v3/list?\
#cid=55505\
#&apiKey=5vmbsthq9569w8f25xzzggmf\
#&customerUserAgent=xxx\
#&customerIpAddress=xxx\
#&locale=en_US\
#&currencyCode=USD\
#&city=Ojai\
#&stateProvinceCode=CA\
#&countryCode=US\
#&supplierCacheTolerance=MED\
##&arrivalDate=09/04/2012\
##&departureDate=09/05/2012\
#&room1=2\
##&numberOfResults=20\
#&supplierCacheTolerance=MED_ENHANCED')
#
#keywords = ["retreat", "organic", "wellness", "spa", "boutique", "green", "eco"]
##keywords = [""]
#responsedict = json.loads(hotellist.content)
##print responsedict
#for h in responsedict['HotelListResponse']['HotelList']['HotelSummary']:
#    for word in keywords:
#        if word.lower() in h['shortDescription'].lower():
#            print h['shortDescription'].replace('&lt;','<').replace('&gt;', '>')

########################################## HOTEL DETAIL ################################################

#hoteldetail = requests.get('http://api.ean.com/ean-services/rs/hotel/v3/info?\
#cid=55505\
#&apiKey=5vmbsthq9569w8f25xzzggmf\
#&customerUserAgent=xxx\
#&customerIpAddress=xxx\
#&customerSessionId=xxx\
#&locale=en_US\
#&currencyCode=USD\
#&hotelId=106347\
#&options=HOTEL_DETAILS')
#
#responsedict = json.loads(hoteldetail.content)
#
##print responsedict
#print responsedict['HotelInformationResponse']['HotelDetails']['propertyDescription'].replace('&lt;','<').replace('&gt;', '>')

########################################## HOTEL ROOM IMAGES ################################################

hotelimages = requests.get('http://api.ean.com/ean-services/rs/hotel/v3/roomImages?\
&cid=55505\
&apiKey=5vmbsthq9569w8f25xzzggmf\
&customerUserAgent=xxx\
&customerIpAddress=xxx\
&customerSessionId=xxx\
&hotelId=106347')

responsedict = json.loads(hotelimages.content)

print responsedict['HotelRoomImageResponse']['RoomImages']['RoomImage']

for img in responsedict['HotelRoomImageResponse']['RoomImages']['RoomImage']:
    print img['url'].replace('expedia', 'hotelretreats')

