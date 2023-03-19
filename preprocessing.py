import re

def preprocess_text(text):
    """
    Preprocesses the given text by removing unwanted characters and stop words
    """
    # Remove unwanted characters
    text = re.sub('[^A-Za-z0-9]+', ' ', text)

    # Convert to lowercase
    text = text.lower()

    # Remove stop words
    stop_words = ['the', 'a', 'an', 'in', 'to', 'of', 'for', 'by', 'on', 'with', 'at', 'from', 'is']
    words = text.split()
    words = [word for word in words if word not in stop_words]
    text = ' '.join(words)

    return text
