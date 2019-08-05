"""
Provides static helper functions for analyzing the sentiment of Reddit comments.

if first time using:
    import nltk
    nltk.download('vader_lexicon')
"""

from textblob import TextBlob
from pyspark.sql.types import DoubleType
from pyspark.sql.functions import udf, mean
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()


def create_spark():
    """
    Create a Spark object
    """

    conf = SparkConf().setMaster("local[*]")
    #conf.set("spark.executor.heartbeatInterval", "3600s")
    spark_context = SparkContext(conf=conf)
    spark_context.setLogLevel("ERROR")
    return SparkSession(sparkContext=spark_context)


def get_comment_polarity(comment):
    """
    Given a comment, return its polarity score.
    """
    comment = TextBlob(comment)

    return comment.sentiment.polarity


def get_comment_subjectivity(comment):
    """
    Given a comment, return its subjectivity score.
    """
    comment = TextBlob(comment)

    return comment.sentiment.subjectivity


def get_comment_compound(comment):
    """
    Given a comment, return its compound score.
    """

    return analyser.polarity_scores(comment)['compound']


def textblob_sentiment_analysis():
    """
    TextBlob Sentiment Analysis
    """

    spark = create_spark()

    data = spark.read.json('../dump/cleanRC_2016-11')

    polarity_udf = udf(get_comment_polarity, DoubleType())
    subjectivity_udf = udf(get_comment_subjectivity, DoubleType())

    data = data.withColumn('polarity', polarity_udf(data.body)) \
               .withColumn('subjectivity', subjectivity_udf(data.body))

    average_polarity = data.groupby('subreddit').agg(mean('polarity'))

    average_subjectivity = data.groupby('subreddit').agg(mean('subjectivity'))

    average_polarity.toPandas().to_csv('../dump/RC_2016-11-polarity.csv')

    average_subjectivity.toPandas().to_csv('../dump/RC_2016-11-subjectivity.csv')

    # data.orderBy('polarity').show()

    # data.orderBy('subjectivity').show()


def vader_sentiment_analysis():
    """
    Vader Sentiment Analysis
    """

    spark = create_spark()

    data = spark.read.json('../dump/cleanRC_2016-11')

    compound_udf = udf(get_comment_compound, DoubleType())

    data = data.withColumn('compound', compound_udf(data.body))

    average_compound = data.groupBy('subreddit').agg(mean('compound'))

    average_compound.toPandas().to_csv('../dump/RC_2016-11-compound.csv')


if __name__ == '__main__':
    # textblob_sentiment_analysis()

    # vader_sentiment_analysis()
