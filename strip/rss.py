from django.contrib.syndication.views import Feed
from strip.models import Strip
from django.conf import settings
from datetime import datetime, time

class LatestEntriesFeed(Feed):
    title = "Hmm-le-rss"
    link = "/rss/"
    description = "Les mises a jour de hmm-la-bd."
    item_author_name = 'Mickael <Mogmi> Bidon'


    def items(self):
        return Strip.objects.order_by('number')[:10].reverse()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        print('ITEM DESC : ' + item.description)
        return '<img src="{0}{1}" alt="{2}" />'.format(
                settings.MEDIA_URL,
                item.png,
                ''
                #item.description
        )

    def item_pubdate(self, item):
        return datetime.combine(item.date, time())

    def item_author_name(self):
        return self.item_author_name
