from typing import Dict


class Summary:
    def __init__(self):
        self.topics = {}
        self.tickers = {}
        
    def add_topics(self, topics: Dict):
        """
        Adds the generated topics to the summary.
        """
        for topic, links in topics.items():
            if topic in
