from json_cleaner import clean_json
from sentiment_analysis import create_spark
from nltk.corpus import stopwords
import os
from os import path
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import collections
import operator

def getFrequency(data, subreddit, text_file, mask, result, bar_plot, title, color, month):

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
    freq_plot = body_rdd_remove_stop.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

    freq_plot_remove = freq_plot.filter(lambda x: x[0] != '' and x[0] != '-')
    sorted_freq = freq.sortBy(lambda x: -x[1]).take(200)
    sorted_freq_plot = freq_plot_remove.sortBy(lambda x: -x[1]).take(50)

    d = dict(sorted_freq)
    d2 = dict(sorted_freq_plot)
    sorted_d2 = sorted(d2.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = collections.OrderedDict(sorted_d2)


    plt.ylabel('Count')
    plt.title('Frequency of words for ' + title + ' in ' + month)
    plt.bar(range(len(sorted_dict)), list(sorted_dict.values()), align='center', color= color)
    plt.xticks(range(len(sorted_dict)), list(sorted_dict.keys()), rotation="90")

    plt.savefig(bar_plot)

    plt.show()
    plt.close()

    if(text_file != 0):
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
    getFrequency(data_nov, "the_donald", "November/the_donald.txt", "trump_head.png", "wordclouds/trump.png", "trump_nov.png", "r/the_donald", "red", "November")
    getFrequency(data_nov, "politics", "November/politics.txt", 0, 0, "politics_nov.png", "r/politics", "purple","November")
    getFrequency(data_nov, "hillaryclinton", "November/hillaryclinton.txt", "hillary_head.png", "wordclouds/hillary.png", "hillary_nov.png", "r/hillaryclinton", "blue","November")
    getFrequency(data_nov, "sandersforpresident", "November/sandersforpresident.txt", 0, 0, "bernie_nov.png", "r/sandersforpresident", "green", "November")

    getFrequency(data_dec, "the_donald", "December/the_donald.txt", 0, 0, "trump_dec.png", "r/the_donald", "red", "December")
    getFrequency(data_dec, "politics", "December/politics.txt", 0, 0, "politics_dec.png", "r/politics", "purple", "December")
    getFrequency(data_dec, "hillaryclinton", "December/hillaryclinton.txt", 0, 0, "hillary_dec.png", "r/hillaryclinton", "blue", "December")
    getFrequency(data_dec, "sandersforpresident", "December/sandersforpresident.txt", "bernie_head.jpg", "wordclouds/bernie.png", "bernie_dec.png", "r/sandersforpresident", "green", "December")


if __name__ == '__main__':
    main()
