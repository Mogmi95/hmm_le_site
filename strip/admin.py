from strip.models import Strip, Comment, Tag
from django.contrib import admin


admin.site.register(Strip, Strip.Admin)
admin.site.register(Comment, Comment.Admin)
admin.site.register(Tag)
