"""
Provides static helper functions for analyzing the sentiment of Reddit comments.
"""

import matplotlib.pyplot as plt

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, mean
from pyspark.sql.types import DoubleType
from textblob import TextBlob


def create_spark():
    """
    Create a Spark object
    """

    return SparkSession(sparkContext=SparkContext.getOrCreate())


def get_comment_polarity(comment):
    """
    Given a comment, return a tuple of comment, and its polarity score.
    """
    comment = TextBlob(comment)

    return comment.sentiment.polarity


def get_comment_subjectivity(comment):
    """
    Given a comment, return a tuple of comment, and its subjectivity score.
    """
    comment = TextBlob(comment)

    return comment.sentiment.subjectivity


def get_plot(dataframe):
    """
    Plots the dataframe

    TODO: labels, legend and title all need to be manually changed. This is more for demo purposes.
    """

    plt.figure()

    df_pandas = dataframe.toPandas()

    df_plot = df_pandas.plot(
        kind='bar', title='Average Polarity per Subreddit')

    df_plot.set_xlabel('subreddit')

    df_plot.set_ylabel('average polarity')

    # TODO: need to manually change it here, should be dynamic
    df_plot.legend(['reddit.com'])

    plt.show()


def main():
    """
    Main method (for testing)
    """

    spark = create_spark()

    data = spark.read.json('../dump/RC_2005-12-clean.json')

    polarity_udf = udf(get_comment_polarity, DoubleType())
    subjectivity_udf = udf(get_comment_subjectivity, DoubleType())

    data = data.withColumn('polarity', polarity_udf(data.body)) \
               .withColumn('subjectivity', subjectivity_udf(data.body))

    average_polarity = data.groupby('subreddit').agg(mean('polarity'))

    get_plot(average_polarity)

    #toxic_comments = data.orderBy('polarity')

    #fake_comments = data.orderBy('subjectivity')

    # pprint(toxic_comments.take(5))

    # pprint(fake_comments.take(5))


if __name__ == '__main__':
    main()
