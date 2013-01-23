import random
from django.template import Context, loader
from django.http import HttpResponse
from strip.models import Strip
from django.conf import settings

def index(request, number = None):
    '''
    Displaying the main page.
    If number is Null, then we display the last strip.
    Else, we display the strip indicated by the number.
    '''
    strip_max = Strip.objects.all().count()
    # Test of the argument 'number'
    if ((number == None) or (int(number) == 0) or (int(number) > strip_max)):
        number = strip_max
    else:
        number = int(number)

    # Getting numbers of the next, previous and random strip
    if (number > 1):
        prev_number = number - 1
    else:
        prev_number = 1
    if (number < strip_max):
        next_number = number + 1
    else:
        next_number = strip_max
    random_number = random.randint(1, strip_max)

    # We get the strip from the db
    strip = Strip.objects.all()[number - 1]
    # We get comments and tags for this strip
    comments = strip.comment_set.all()
    tags = strip.tags.all()

    template = loader.get_template('strips/index.html')
    cont = Context({
            'strip' : strip,
            'comments' : comments,
            'tags' : tags,
            'prev_strip_number' : prev_number,
            'next_strip_number' : next_number,
            'random_strip_number' : random_number,
            'last_strip_number' : strip_max,
            'STATIC_URL' : settings.STATIC_URL,
            'MEDIA_URL' : settings.MEDIA_URL,
        })
    return HttpResponse(template.render(cont))
