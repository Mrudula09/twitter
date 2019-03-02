from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np


activities = ['Positive Tweets', 'Negative Tweets', 'Neutral Tweets']


def pie_chart(sentiment_count):
    del sentiment_count["total_tweets"]
    activities.remove('Total Tweets')
    plt.pie(sentiment_count.values(), labels=activities, startangle=90, autopct='%.1f%%')
    plt.show()


def bar_chart(sentiment_count):
    activities.reverse()
    activities.append('Total Tweets')
    count = sentiment_count.values()
    count.reverse()
    y_pos = np.arange(len(activities))
    colors = ['cyan', 'red', 'green', 'blue']
    plt.barh(y_pos, sentiment_count.values(), color=colors, align='center', alpha=0.5)
    plt.yticks(y_pos, activities)
    plt.xlabel('Number Of Tweets')
    plt.show()


def word_cloud(words):
    cloud = WordCloud().generate(words)
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def print_count(sentiment_count):
    print('Number Of Positive Tweets: ' + str(sentiment_count["positive_tweets"]))
    print('Number Of Negative Tweets: ' + str(sentiment_count["negative_tweets"]))
    print('Number Of Neutral Tweets: ' + str(sentiment_count["neutral_tweets"]))

