from piston.handler import BaseHandler
from piston.utils import rc
from bonus.models import Bonus
from bonus.models import Comment

class BonusHandler(BaseHandler):
    model = Bonus
    allowed_methods = ('GET',)
    fields = (
        "date",
        "title",
        "description",
        "png",
        "svg",
    )

    def read(self, request, number=None):
        """
        Request from the API for bonus :
            - if number is not given, we return all the bonus
            - if it is, we return the bonus with the corresponding
            number
            - if the bonus doesn't exist, we return a 404 error
        """
        base = Bonus.objects
        if (number):
            if ((int(number) == 0) or (int(number) > len(base.all()))):
                resp = rc.NOT_FOUND
                return resp
            else:
                return base.get(pk=number)
        else:
            return base.all()

class BonusCommentHandler(BaseHandler):
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
        This method is used to get comments on a bonus indicated by
        'number'
        """
        base = Bonus.objects
        if ((int(number) == 0) or (int(number) > len(base.all()))):
            resp = rc.NOT_FOUND
            return resp
        else:
            return base.get(number=number).comment_set.all()


