from django.core.management.base import BaseCommand, CommandError
from gohotels.models import HotelPage, HotelImage

class Command(BaseCommand):
    help = 'Remove duplicate hotels'
    def handle(self, *args, **options):
        for row in HotelPage.objects.all():
            if HotelPage.objects.filter(hotelid=row.hotelid).count() > 1:
                row.delete()
                print 'Deleted row {0}'.format(row.hotelid)




  