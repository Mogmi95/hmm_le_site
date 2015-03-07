from django.db import models

class Bonus(models.Model):
    """
    This class describes a bonus, which is a single drawing which
    possesses comments
    """
    def __unicode__(self):
        return "Bonus : " + self.title

    # The date of publication
    date = models.DateField()

    # The title of the bonus
    title = models.CharField(max_length=50)

    # The description of the bonus
    description = models.CharField(max_length=250)

    # The PNG file for the bonus
    png = models.ImageField(upload_to="bonus/png_fr/")

    # The SVG file for the bonus
    svg = models.FileField(upload_to="bonus/svg_fr/")

class Comment(models.Model):
    """
    This class describes a comment, which is a message posted by a user on a
    a Bonus
    """
    def __unicode__(self):
        return self.author_name + " (" + str(self.date) + ") : " +\
            self.comment

    # The author's name
    author_name = models.CharField(max_length=50)

    # The author's website
    author_website = models.CharField(max_length=50, blank=True)

    # The comment
    comment = models.CharField(max_length=250)

    # Date of the comment
    date = models.DateField()

    # Strip where the comment was posted
    strip = models.ForeignKey(Bonus)

    # Is validated by the admin
    validated = models.BooleanField(default=False)

    # Admin display
    class Admin:
        list_display = ('date', 'author_name', 'validated')
        search_field = ('author_name')
