from piston.handler import BaseHandler
from piston.utils import rc
from strip.models import Strip
from strip.models import Tag

class StripHandler(BaseHandler):
    model = Strip
    allowed_methods = ('GET',)
    exclude = ('id',)

    def read(self, request, number=None):
        base = Strip.objects
        if (number):
            if ((int(number) == 0) or (int(number) > len(base.all()))):
                resp = rc.NOT_FOUND
                return resp
            else:
                return base.get(number=number)
        else:
            return base.all()

class TagHandler(BaseHandler):
    model = Tag
    allowed_methods = ('GET',)
    exclude = ('id',)
