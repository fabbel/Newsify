from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def generate_topics(articles, num_topics=5, num_top_words=10):
    """
    Generates topics for the given articles using Latent Dirichlet Allocation (LDA) model
    """
    # Preprocess articles
    preprocessed_articles = [preprocess_text(article['title'] + ' ' + article['summary']) for article in articles]

    # Vectorize articles
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=1000, stop_words='english')
    vectorized_articles = vectorizer.fit_transform(preprocessed_articles)

    # Apply LDA model
    lda_model = LatentDirichletAllocation(n_components=num_topics, max_iter=10, learning_method='online')
    lda_topics = lda_model.fit_transform(vectorized_articles)

    # Print topics and top words
    feature_names = vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(lda_model.components_):
        print("Topic %d:" % (topic_idx + 1))
        print(" ".join([feature_names[i] for i in topic.argsort()[:-num_top_words - 1:-1]]))
        print()

    return lda_topics
