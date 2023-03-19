from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

def generate_topics(documents, n_topics=5, n_top_words=10):
    # Vectorize the documents
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(documents)
    
    # Fit LDA model
    lda_model = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda_model.fit(X)
    
    # Get the most important words for each topic
    topic_words = []
    for topic_weights in lda_model.components_:
        top_word_indices = topic_weights.argsort()[::-1][:n_top_words]
        topic_words.append([vectorizer.get_feature_names()[i] for i in top_word_indices])
    
    # Return the topics
    return topic_words
