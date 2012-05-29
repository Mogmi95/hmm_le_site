from django.db import models

class Informations(models.Model):
    """
    This class provides some information about Hmm-la-bd
    I created a class for this because :
        1/ It's prettier than in a config file (especially
        with API)
        2/ I want to use the Django's administration panel
        to edit those settings
    """

    # The date of the last configuration update
    last_update = models.DateField(auto_now = True)

    # The author (ME o/)
    author = models.CharField(max_length = 50)

    # Media URL, used to access the images on the server
    media_url = models.CharField(max_length = 100)
