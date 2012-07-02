from piston.handler import BaseHandler
from piston.utils import rc
from api.models import Information

class BonusHandler(BaseHandler):
    model = Bonus
    allowed_methods = ('GET',)
    fields = (
        "last_update",
        "author",
        "media_url",
    )

    def read(self, request, number=None):
        """
        Get information about the website
        """
        base = Information.objects
        return base.get(pk=1)

