import feedparser

class FeedlyAPI:
    def __init__(self, feed_url, num_articles=10):
        self.feed_url = feed_url
        self.num_articles = num_articles

    def fetch_articles(self):
        """
        Fetches the latest articles from the Feedly RSS feed
        """
        articles = []
        feed = feedparser.parse(self.feed_url)

        for entry in feed.entries[:self.num_articles]:
            article = {
                'title': entry.title,
                'link': entry.link,
                'summary': entry.summary
            }
            articles.append(article)

        return articles


############
#
# different code, same function for feedly.py

# V1
#
############

# import feedparser

# class FeedlyClient:
#     def __init__(self, token):
#         self.token = token
#         self.feed_url = "https://cloud.feedly.com/v3/streams/contents?streamId=user/c805317b-3f2c-4ee3-a918-56d950010575/category/global.all&count=100"

#     def fetch_articles(self):
#         headers = {
#             "Authorization": f"Bearer {self.token}",
#             "Content-Type": "application/json"
#         }
#         response = feedparser.parse(self.feed_url, request_headers=headers)

#         articles = []
#         for entry in response.entries:
#             article = {
#                 "title": entry.title,
#                 "link": entry.link,
#                 "summary": entry.summary,
#                 "published": entry.published
#             }
#             articles.append(article)

#         return articles



############
#
# V2
#
############

# import feedparser
# from typing import List, Dict


# class Feedly:
#     def __init__(self, api_key: str):
#         self.api_key = api_key
#         self.feedly_url = f"https://cloud.feedly.com/v3/streams/contents?streamId=user/{self.api_key}/category/global.all&count=1000"
        
#     def get_articles(self) -> List[Dict]:
#         """
#         Fetches articles from the Feedly API.
#         """
#         feed = feedparser.parse(self.feedly_url)
#         articles = []
#         for entry in feed.entries:
#             article = {
#                 "title": entry.title,
#                 "published": entry.published,
#                 "summary": entry.summary,
#                 "link": entry.link
#             }
#             articles.append(article)
#         return articles


