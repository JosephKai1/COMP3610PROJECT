from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import re

def create_sentiment_column(df):
    sentiment_map = {1:0, 2:0, 4:1, 5:1}
    df = df[df['Rating'] != 3]
    sentiment = df['rating'].map(sentiment_map)
    df['sentiment'] = sentiment
    
    
def clean_html(text):
    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE) # remove URLs
    text = re.sub(r'<.*?>', '', text) # remove HTML tags
    return text


def tokenize_text(text):
    if isinstance(text, str):
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token.isalpha()] # filter non-alphabetic tokens
        return tokens
    elif isinstance(text, (int, float)):
        return text # return the number itself
    else:
        return []


def filter_stop_words(tokens):
    stop_words = stopwords.words('english')
    return [token for token in tokens if token.lower() not in stop_words]


def lemmatize_text(tokens):
    if tokens is None:
        return []
    lemma = WordNetLemmatizer()
    return [lemma.lemmatize(token) for token in tokens if token is not None]


def clean_text(text):
    if not isinstance(text, str):
        return ''
    text = clean_html(text)
    tokens = tokenize_text(text) # Tokenise
    tokens = [token.lower() for token in tokens] # Convert to lowercase
    tokens = [token.translate(str.maketrans('', '', string.punctuation)) for token in tokens] # Filter punctuation
    tokens = filter_stop_words(tokens) # Filter stop words
    tokens = lemmatize_text(tokens) # Lemmatize
    return ' '.join(tokens)
