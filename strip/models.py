from django.db import models

class Tag(models.Model):
    def __unicode__(self):
        return tag_name
    # The name of the tag
    tag_name = models.CharField(max_length=50)

class Strip(models.Model):
    def __unicode__(self):
        return str(self.number) + " - " + self.fr_title

    # The number of the strip
    number = models.IntegerField()

    # The date of publication
    date = models.DateField()

    # The title of the strip, in french
    fr_title = models.CharField(max_length=50)
    # The title of the strip, in english
    en_title = models.CharField(max_length=50)

    # The french description of the strip
    fr_desc = models.CharField(max_length=250)
    # The english description of the strip
    en_desc = models.CharField(max_length=250)

    # The PNG file for the french version
    png_file_fr = models.ImageField(upload_to="png_fr/")
    # The PNG file for the english version
    png_file_en = models.ImageField(upload_to="png_en/")

    # The SVG file for the french version
    svg_file_fr = models.FileField(upload_to="svg_fr/")
    # The SVG file for the english version
    svg_file_en = models.FileField(upload_to="svg_en/")

    # The tags linked to this Strip
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    def __unicode__(self):
        return "[" + str(self.related_strip.number) + "] " +\
            self.author_name + " (" + str(self.date) + ") : " +\
            self.comment

    # The author's name
    author_name = models.CharField(max_length=50)
    # The author's website
    author_website = models.CharField(max_length=50)

    # The comment
    comment = models.CharField(max_length=250)

    # Date of the comment
    date = models.DateField()

    # Strip where the comment was posted
    related_strip = models.ForeignKey(Strip)

    # Is validated by the admin
    validated = models.BooleanField()

    # Admin display
    class Admin:
        list_display = ('date', 'author_name', 'validated')
        search_field = ('author_name')

