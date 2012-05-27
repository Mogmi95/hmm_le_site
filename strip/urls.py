from django.conf.urls.defaults import *
from piston.resource import Resource
from strip.handlers import StripHandler

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

strip_resource = CsrfExemptResource(StripHandler)

urlpatterns = patterns( '',
    url( r'^(?P<emitter_format>.+)/strip/(?P<number>\d+)$', strip_resource),
    url( r'^(?P<emitter_format>.+)/strips$', strip_resource),
)
