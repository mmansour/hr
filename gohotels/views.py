from django.shortcuts import render_to_response, get_object_or_404, Http404
from gohotels.models import *
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from django.core import serializers
import logging
from mezzanine.utils.views import paginate
from mezzanine.blog.models import BlogPost, BlogCategory
from exceptions import ValueError


def home(request):
    featured_hotel_list = HotelPage.objects.filter(status=2)[:7]
    blog_post_list = BlogPost.objects.filter(status=2)[:7]
    return render_to_response('index.html',
                            {'blog_post_list':blog_post_list,
                             'featured_hotel_list':featured_hotel_list},
                             context_instance=RequestContext(request))


def detail(request, hotelid, pageslug):
    try:
        thehotel = get_object_or_404(HotelPage, hotelid=hotelid)
        if pageslug != thehotel.slug:
            return HttpResponsePermanentRedirect(thehotel.get_absolute_url())
        else:
            return render_to_response('hotel_detail.html', {'thehotel':thehotel},
                                      context_instance=RequestContext(request))
    except ValueError:
        raise Http404
