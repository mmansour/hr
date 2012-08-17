from django.core.management.base import BaseCommand, CommandError
from gohotels.models import HotelPage, HotelImage
import csv


class Command(BaseCommand):
    help = 'Pulls hotel images'
    def handle(self, *args, **options):
        filteredimageslist = []
#        with open('/users/mattmansour/django/sites/dev/hotelretreats/docs/HotelImageList.txt', 'rU') as f:
        with open('/home/mattym/webapps/hotelretreats/docs/HotelImageList.txt', 'rU') as f:

            reader = csv.reader(f, delimiter='|')
            reader.next() # SKIPS HEADER LINE

            hotel = HotelPage.objects.all()
            hotel_id_list = [i.hotelid for i in hotel]
            csv_id_list = [[int(col[0]), col[1], col[2], col[6]]  for col in reader]

############ GET ALL IMAGES POPULATE RELATED IMAGE MODEL
#            l3 = [h for h in csv_id_list if h[0] in hotel_id_list]
#            for i in l3:
#                each_hotel = HotelPage.objects.get(hotelid=i[0])
#                img = HotelImage(
#                    hotel=each_hotel,
#                    alt=i[1],
#                    image_url=i[2].replace('media.expedia.com', 'media.hotelretreats.com').replace('images.travelnow.com', 'media.hotelretreats.com'),
#                    thumbnail_url=i[3].replace('media.expedia.com', 'media.hotelretreats.com').replace('images.travelnow.com', 'media.hotelretreats.com'),
#                )
#                img.save()

########### ADD A THUMBNAIL TO MAIN MODEL
            thumb_list = [[h[0], h[3]] for h in csv_id_list if h[0] in hotel_id_list]
            thumbdict = {}
            
            for t in thumb_list:
                thumbdict[t[0]] = t[1].replace('media.expedia.com', 'media.hotelretreats.com').replace('images.travelnow.com', 'media.hotelretreats.com')

            for k,v in thumbdict.iteritems():
                hotelthumb = HotelPage.objects.get(hotelid=k)
                hotelthumb.thumbnail_url = v
                hotelthumb.save()

            print 'done'























