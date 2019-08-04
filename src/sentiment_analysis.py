"""
Provides static helper functions for analyzing the sentiment of Reddit comments.
"""

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, mean
from pyspark.sql.types import DoubleType
from textblob import TextBlob


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


def main():
    """
    Main method (for testing)
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


if __name__ == '__main__':
    main()
