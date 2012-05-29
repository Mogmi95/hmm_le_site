from django.conf.urls.defaults import *
from piston.resource import Resource
from strip.handlers import StripHandler
from strip.handlers import StripCommentHandler

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

strip_resource = CsrfExemptResource(StripHandler)
strip_comment_resource = CsrfExemptResource(StripCommentHandler)

urlpatterns = patterns( '',
    url( r'^(?P<emitter_format>.+)/all/$', strip_resource),
    url( r'^(?P<emitter_format>.+)/(?P<number>\d+)/$', strip_resource),
    url( r'^(?P<emitter_format>.+)/comments/(?P<number>\d+)/$', strip_comment_resource),
)
