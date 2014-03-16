from django.contrib.syndication.views import Feed
from strip.models import Strip

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
        return item.description

    def item_pubdate(self, item):
        return item.date

    def item_author_name(self):
        return self.item_author_name
