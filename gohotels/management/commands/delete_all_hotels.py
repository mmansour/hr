from django.core.management.base import BaseCommand, CommandError
from gohotels.models import HotelPage, HotelImage

class Command(BaseCommand):
    help = 'Clear the Database hotels'
    def handle(self, *args, **options):
        for row in HotelPage.objects.all():
            print 'Deleted row {0}'.format(row.hotelid)
            row.delete()





  