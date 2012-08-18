from django.shortcuts import render_to_response, get_object_or_404, Http404
from gohotels.models import *
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from django.core import serializers
import logging
from mezzanine.utils.views import paginate
from mezzanine.blog.models import BlogPost, BlogCategory
from exceptions import ValueError
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D


def home(request):
    featured_hotel_list = HotelPage.objects.filter(status=2).filter(is_featured=True)[:7]
    blog_post_list = BlogPost.objects.filter(status=2)[:7]
    return render_to_response('index.html',
                            {'blog_post_list':blog_post_list,
                             'featured_hotel_list':featured_hotel_list},
                             context_instance=RequestContext(request))


def detail(request, hotelid, pageslug):
    try:
        thehotel = get_object_or_404(HotelPage, hotelid=hotelid)

        pnt = GEOSGeometry('POINT({0} {1})'.format(thehotel.latitude, thehotel.longitude), srid=4326)
        nearby_hotels = HotelPage.geomanager.all().distance(pnt).order_by('-distance')[:10]
#        nearby_hotels = HotelPage.geomanager.filter(point__distance_lt=(pnt, D(mi=200))).distance(pnt).order_by('distance')

        for h in nearby_hotels:
            print h
            
        if pageslug != thehotel.slug:
            return HttpResponsePermanentRedirect(thehotel.get_absolute_url())
        else:
            return render_to_response('hotel_detail.html', {'thehotel':thehotel,
                                        },
                                      context_instance=RequestContext(request))
    except ValueError:
        raise Http404
