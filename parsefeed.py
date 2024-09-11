import feedparser

url = "https://aztty.azurewebsites.net/rss/updates"
feed = feedparser.parse(url)

entries = feed.entries

for post in entries:
    print('')
    # print(post.title)
    print(post.link)
    # print(post.tags[0].term)
    # print(post.published)
