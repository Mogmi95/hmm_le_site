from django.conf.urls.defaults import *
from piston.resource import Resource
from bonus.handlers import BonusHandler
from bonus.handlers import BonusCommentHandler

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

bonus_resource = CsrfExemptResource(BonusHandler)
bonus_comment_resource = CsrfExemptResource(BonusCommentHandler)

urlpatterns = patterns( '',
    url( r'^(?P<emitter_format>.+)/all/$', bonus_resource),
    url( r'^(?P<emitter_format>.+)/(?P<number>\d+)/$', bonus_resource),
    url( r'^(?P<emitter_format>.+)/comments/(?P<number>\d+)/$', bonus_comment_resource),
)
