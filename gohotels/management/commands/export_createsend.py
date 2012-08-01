#from django.core.management.base import BaseCommand, CommandError
#from django.contrib.auth.models import User
#import datetime
#from createsend import *
#from youtubeapi import *
#import logging
#logger = logging.getLogger("battles.custom")
#
#class Command(BaseCommand):
#    help = 'Exports FB Emails to CreateSend for Newsletters'
#    def handle(self, *args, **options):
#        try:
#            logger.debug('Start nightly export of emails to create send.')
##            CreateSend.api_key = '0a0c4a9a11ca37073a017fe525ce6b7d'
##            listid = "4c31ef91114f235a2d4af223cc6c3813"
##            subscriber = Subscriber(listid, "ben@thegamestation.tv")
##
##            #OPTIMIZE TO PULL BY DATE RANGE
##            signups = User.objects.all()
##            subscribers = []
##
##            now = datetime.datetime.now()
##            count = 0
###            for s in signups:
##            for s in range(1, 25000):
##                #IMPORT ALL EMAILS
##                count+=1
##                print count, count%1000
##
###                subscribers.append({"EmailAddress": "{0}".format(s.email), "Name": ""})
##
##                #IMPORT ONLY BY TODAY'S Date
###                if datetime.date(s.date_joined.year, s.date_joined.month, s.date_joined.day) == datetime.date(now.year, now.month, now.day):
###                    subscribers.append({"EmailAddress": "{0}".format(s.email), "Name": ""})
##
###            subscriber.import_subscribers(listid, subscribers, True)
#            logger.debug('Finished nightly export of emails to create send.')
#
#        except Exception, e:
#            logger.error('Error exporting emails to createsend: {0}'.format(e))
