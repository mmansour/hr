#from django.core.management.base import BaseCommand, CommandError
#from battles.models import Battle
#from youtubeapi import *
#import logging
#logger = logging.getLogger("battles.custom")
#
#class Command(BaseCommand):
#    help = 'Pulls the youtube view count for each video nightly'
#    def handle(self, *args, **options):
#        try:
#            logger.debug('Starting Nightly pull of most popular videos.')
#            channel = ['nicepeter', 'nicepetertoo','erb','erb2']
#            for channel in channel:
#                uri = "https://gdata.youtube.com/feeds/api/users/{0}/uploads?start-index=1&max-results=10& \
#                       key=AI39si7GciMohA5tLUWNcjlHeLAtM8XxlltFcIZFkig4S2jXO5FhyUrvPRVoeto262rleIs5I-V8fB_W6IPjYLfVZDpkUL4m_Q".format(channel)
#                yt_service = gdata.youtube.service.YouTubeService()
#                feed = yt_service.GetYouTubeVideoFeed(uri)
#                total_results = feed.total_results.text
##                print 'total results, ', total_results
#                number_of_pages = float(total_results) / 10
#                which_page = 0
#                rs_start_index = 1
#
#
#                def UpdateMostViewed(self, url):
#                    yt_service = gdata.youtube.service.YouTubeService()
#                    feed = yt_service.GetYouTubeVideoFeed(url)
#                    for entry in feed.entry:
#                        ytvideoidlist = entry.id.text.split('/')
#                        ytvideoid = ytvideoidlist[6] # GET Video ID at End of String
#                        try:
#                            video = Battle.objects.get(video_youtube_id=ytvideoid)
#                            video.video_view_count = entry.statistics.view_count
#                            video.save()
#    #                        logger.debug('Feed Video View Count {0}, Feed Youtube Video ID {1} DB Video ID {2} DB Video View Count {3}\n' \
#    #                        .format(entry.statistics.view_count, ytvideoid, video.video_youtube_id, video.video_view_count))
#                        except Battle.DoesNotExist:
#                            logger.warn("Battles does not exist for video id {0} - getmostviewed.py \n".format(ytvideoid))
#                            pass
#
#
#                while  which_page <= number_of_pages:
#                    which_page += 1
#    #                logger.debug("Getting feed for %s. \n Getting page: %s. \n"  % (channel, which_page))
#                    UpdateMostViewed(self, "https://gdata.youtube.com/feeds/api/users/{0}/uploads?start-index={1}&max-results=10&"
#                       "key=AI39si7GciMohA5tLUWNcjlHeLAtM8XxlltFcIZFkig4S2jXO5FhyUrvPRVoeto262rleIs5I-V8fB_W6IPjYLfVZDpkUL4m_Q".format(channel, rs_start_index))
#                    rs_start_index += 10
#    #                logger.debug("Start Index: {0} \n".format(rs_start_index))
#            logger.debug('Nightly pull of most popular videos complete')
#        except Exception, e:
#            logger.error('Error pulling most popular videos from youtube api: {0}'.format(e))
