from typing import List, Dict


def extract_topics(articles: List[Dict]) -> Dict:
    """
    Extracts topics from the preprocessed articles by identifying frequently occurring
    words in the title and summary fields.
    """
    topics = {}
    for article in articles:
        words = article["title"].split() + article["summary"].split()
        for word in words:
            if word in topics:
                topics[word].append(article["link"])
            else:
                topics[word] = [article["link"]]
    return topics

def extract_tickers(topics: Dict) -> Dict:
    """
    Extracts stock tickers and relevant market sectors from the topics by identifying
    frequently occurring words and phrases associated with stocks and sectors.
    """
    tickers = {}
    for topic, links in topics.items():
        if "stock" in topic or "market" in topic or "sector" in topic:
            words = topic.split()
            for word in words:
                if word.isupper():
                    if word in tickers:
                        tickers[word].extend(links)
                    else:
                        tickers[word] = links
                elif word in ["technology", "finance", "energy", "healthcare", "consumer"]:
                    if word in tickers:
                        tickers[word].extend(links)
                    else:
                        tickers[word] = links
    return tickers
