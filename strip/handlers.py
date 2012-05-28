from piston.handler import BaseHandler
from piston.utils import rc
from strip.models import Strip
from strip.models import Tag
from strip.models import Comment

class StripHandler(BaseHandler):
    model = Strip
    allowed_methods = ('GET',)
    fields = (
        "number",
        "date",
        "fr_title",
        "en_title",
        "fr_description",
        "en_description",
        "png_fr", ('url'),
        "png_en",
        "svg_fr",
        "svg_en",
        "tags",
    )

    def read(self, request, number=None):
        """
        Request from the API for strips :
            - if number is not given, we return all the strips
            - if it is, we return the strip with the corresponding
            number
            - if the strip doesn't exist, we return a 404 error
        """
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
    """
    This handler is only here to delete the 'id' value
    from tags in the API results
    """
    model = Tag
    allowed_methods = ('GET',)
    exclude = ('id',)

class StripCommentHandler(BaseHandler):
    model = Comment
    allowed_methods = ('GET',)
    fields = (
       'author_name', 
       'author_website', 
       'comment', 
       'date', 
    )

    def read(self, request, number):
        """
        This method is used to get comments on a strip indicated by
        'number'
        """
        base = Strip.objects
        if ((int(number) == 0) or (int(number) > len(base.all()))):
            resp = rc.NOT_FOUND
            return resp
        else:
            return base.get(number=number).comment_set.all()

