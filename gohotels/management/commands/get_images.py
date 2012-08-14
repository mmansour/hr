from django.core.management.base import BaseCommand, CommandError
from gohotels.models import HotelPage, HotelImage
from django.utils.encoding import force_unicode
from mezzanine.core.models import slugify
import requests
import json
import time
import datetime
import csv


class Command(BaseCommand):
    help = 'Pulls hotel images'
    def handle(self, *args, **options):
        filteredimageslist = []
        with open('/users/mattmansour/django/sites/dev/hotelretreats/docs/HotelImageList.txt', 'rU') as f:
            reader = csv.reader(f, delimiter='|')
            reader.next() # SKIPS HEADER LINE
            for col in reader:
#                col[0] hotel id, col[1] caption, col[2] url, col[3] width,
#                col[4] height, col[6] Thumbnail url, col[6] default image
                try:
                    print 'Checking id {0}'.format(col[0])
                    print 'List length {0}'.format(len(filteredimageslist))
                    h = HotelPage.objects.get(hotelid=col[0])
                    print 'FOUND________________ id {0}'.format(col[0])
                    filteredimageslist.append([[h],[col[1], col[2], col[6]]])

                except HotelPage.DoesNotExist:
                    pass

            for item in filteredimageslist:
                img = HotelImage(
                    hotel=item[0][0],
                    alt=item[1][0],
                    image_url=item[1][1].replace('media.expedia.com', 'media.hotelretreats.com').replace('images.travelnow.com', 'media.hotelretreats.com'),
                    thumbnail_url=item[1][2].replace('media.expedia.com', 'media.hotelretreats.com').replace('images.travelnow.com', 'media.hotelretreats.com'),
                )
                img.save()





















