from urlparse import urljoin
from flask import Module, request, url_for
from werkzeug.contrib.atom import AtomFeed

from ims.models import Wiki, Todo

mod = Module(__name__)

class Feed(AtomFeed):
    def add_feed(self, post):
        self.add(post.title,
                 unicode(post.text),
                 content_type="html",
                 author=post.title,
                 url=urljoin(request.url_root, 'wiki/' + post.title),
                 updated=post.update_date,
                 published=post.pub_date)


@mod.route("/")
@mod.route("/wiki")
def wiki():
    feed = Feed('Recent Wiki Pages',
                    feed_url=request.url, url=request.url_root)
                    
    wikis = Wiki.query.order_by(Wiki.id).limit(15).all()

    for t in wikis:
        feed.add_feed(t)

    return feed.get_response()
