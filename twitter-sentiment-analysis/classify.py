from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import emoji
import pandas as pd

tokenizer = RegexpTokenizer(r'\w+')
stopWords = set(stopwords.words('english'))
wnl = WordNetLemmatizer()


def word_feats(words):
    return dict([(word, True) for word in words])


def data(classifier, tweets_file):
    count = {"positive_tweets": 0, "negative_tweets": 0, "neutral_tweets": 0}
    positive_threshold = 2
    negative_threshold = -2
    all_words = ''
    # get file dynamically
    data_frame = pd.read_csv(tweets_file, low_memory=False)
    count["total_tweets"] = len(data_frame)
    for data in data_frame.itertuples():
        data = emoji.demojize(unicode(data[1], "utf-8"), delimiters=(" ", " "))
        data = re.sub(r'\d+', '', data)
        data = data.lower()
        words = tokenizer.tokenize(data)
        words_filtered = []

        for word in words:
            if word not in stopWords:
                word = wnl.lemmatize(word)
                words_filtered.append(word)
                all_words = all_words + word + ' '
                neg = 0
                pos = 0

        for word in words_filtered:
            class_result = classifier.classify(word_feats(word))
            if class_result < 0:
                neg = neg + class_result
            if class_result > 0:
                pos = pos + class_result
        polarity = float(pos+neg)/len(words_filtered)

        if polarity >= positive_threshold:
            count["positive_tweets"] += 1
        elif polarity <= negative_threshold:
            count["negative_tweets"] += 1
        else:
            count["neutral_tweets"] += 1
    return count, all_words

