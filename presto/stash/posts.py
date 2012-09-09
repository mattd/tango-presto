"""
site: presto
routes:
 - json: /posts/
exports:
 - posts

"""
import feedparser


RSS_FEEDS = {
    'nytimes': 'http://feeds.nytimes.com/nyt/rss/HomePage',
    'reddit': 'http://www.reddit.com/r/programming/.rss',
    'slate': 'http://feeds.slate.com/slate'
}

posts = []
current_id = 0

for name, url in RSS_FEEDS.iteritems():
    feed = feedparser.parse(url)
    for entry in feed.entries:
        current_id += 1
        posts.append(
            {
                'description': entry.description,
                'id': current_id,
                'link': entry.link,
                'source': name,
                'title': entry.title
            }
        )
