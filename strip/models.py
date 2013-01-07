from django.db import models

class Tag(models.Model):
    """
    This class describes a Tag, which is a keyword used to give information
    about the strip who's linked to it.
    A Tag can describes more than one Strip, but a Strip cannot contains
    multiple links to the same Tag.
    """
    def __unicode__(self):
        return self.tag_name
    # The name of the tag
    tag_name = models.CharField(max_length = 50)

class Strip(models.Model):
    """
    This class describes a Strip, which represents every information concerning
    a strip (its number, its comments, etc).
    """
    def __unicode__(self):
        return str(self.number) + " - " + self.title

    def get_absolute_url(strip):
        return "http://hmm-la-bd.eu/" + str(strip.number)

    # The number of the strip
    number = models.IntegerField()

    # The date of publication
    date = models.DateField()

    # The title of the strip
    title = models.CharField(max_length = 50)

    # The description of the strip
    description = models.CharField(max_length = 500)

    # The PNG file
    png = models.ImageField(upload_to="strips/png/")

    # The SVG file
    svg = models.FileField(upload_to="strips/svg/")

    # The tags linked to this Strip
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    """
    This class describes a comment, which is a message posted by a user on a
    a Strip
    """
    def __unicode__(self):
        return self.author_name + " (" + str(self.date) + ") : " +\
            self.comment

    # The author's name
    author_name = models.CharField(max_length = 50)

    # The author's website
    author_website = models.CharField(max_length = 50, blank = True)

    # The comment
    comment = models.CharField(max_length = 500)

    # Date of the comment
    date = models.DateField()

    # Strip where the comment was posted
    strip = models.ForeignKey(Strip)

    # Is validated by the admin
    validated = models.BooleanField()

    # Admin display
    class Admin:
        list_display = ('date', 'author_name', 'validated')
        search_field = ('author_name')
