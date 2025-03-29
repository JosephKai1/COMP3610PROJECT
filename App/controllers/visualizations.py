from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

def create_bar_chart_for_ratings(counts):
    plt.bar(['Positive Ratings (>3)', 'Negative Ratings (<3)'], counts, color=['green', 'red'])
    plt.title('Count of Positive and Negative Ratings')
    plt.xlabel('Rating Categories')
    plt.ylabel('Count')
    plt.savefig('App/static/images/rating_categories.png')


def print_word_cloud(data):
    text = " ".join(review for review in data)
    print("There are {} words in the combination of all reviews".format(len(text)))
    return WordCloud(stopwords=set(stopwords.words('english')), background_color="white").generate(text)


def create_word_cloud(review_text):
    wordcloud = print_word_cloud(review_text)
    fig = plt.figure(1)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('App/static/images/wordcloud.png')


