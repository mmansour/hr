from django.shortcuts import render_to_response, get_object_or_404
from gohotels.models import *
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from django.core import serializers
import logging
from mezzanine.utils.views import paginate
from mezzanine.blog.models import BlogPost, BlogCategory


def home(request):
    blog_post_list = BlogPost.objects.filter(status=2)[:7]
    for b in blog_post_list:
        print b
##        logger.debug('View: home - Success')
    return render_to_response('index.html',
                            {'blog_post_list':blog_post_list},
                             context_instance=RequestContext(request))