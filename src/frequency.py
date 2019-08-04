from json_cleaner import clean_json
from sentiment_analysis import create_spark
from nltk.corpus import stopwords
import os
from os import path
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def getFrequency(data, subreddit, text_file, mask, result):

    #set stops words using nltk library
    stop_words = set(stopwords.words('english'))

    #convert dataframe into rdd
    rdd = data.rdd.map(list)

    rdd_subreddit = rdd.filter(lambda x: x[4] == subreddit)

    #get 'body' of df and filter out stop words
    body_rdd = rdd_subreddit.flatMap(lambda x: x[1].split(" "))
    body_rdd_remove_stop = body_rdd.filter(lambda x: x.lower() not in stop_words)


    #get frequency of words

    freq = body_rdd_remove_stop.map(lambda x: (x.encode("utf8"), 1)).reduceByKey(lambda x, y: x + y)

    sorted_freq = freq.sortBy(lambda x: -x[1]).take(200)

    if(text_file != 0):

        d = dict(sorted_freq)
        wordCloud(d, mask, result)

    with open(text_file, 'w') as f:
        for item in sorted_freq:
            print >> f, item

def wordCloud(dict, mask, result):

    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    m = np.array(Image.open(path.join(d, mask)))

    wc = WordCloud(background_color="white", max_words=200, mask=m,
                    contour_width=3, contour_color='steelblue').generate_from_frequencies(dict)

    #import matplotlib.pyplot as plt
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")

    wc.to_file(path.join(d, result))

    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.figure()
    plt.imshow(m, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def main():

    spark = create_spark()

    #file paths
    clean_file_nov = '../Clean-Reddit-Comments/cleanRC_2016-11'
    clean_file_dec = '../Clean-Reddit-Comments/cleanRC_2016-12'

    #open clean file
    data_nov = spark.read.json(clean_file_nov)
    data_dec = spark.read.json(clean_file_dec)

    #get frequency for each month
    getFrequency(data_nov, "the_donald", "November/the_donald.txt", "trump_head.png", "wordclouds/trump.png")
    getFrequency(data_nov, "politics", "November/politics.txt", 0, 0)
    getFrequency(data_nov, "hillaryclinton", "November/hillaryclinton.txt", "hillary_head.png", "wordclouds/hillary.png")
    getFrequency(data_nov, "sandersforpresident", "November/sandersforpresident.txt")

    getFrequency(data_dec, "the_donald", "December/the_donald.txt", 0, 0)
    getFrequency(data_dec, "politics", "December/politics.txt", 0, 0)
    getFrequency(data_dec, "hillaryclinton", "December/hillaryclinton.txt", 0, 0)
    getFrequency(data_dec, "sandersforpresident", "December/sandersforpresident.txt", "bernie_head.jpg", "wordclouds/bernie.png")


if __name__ == '__main__':
    main()
