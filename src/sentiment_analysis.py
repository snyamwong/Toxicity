"""
Provides static helper functions for analyzing the sentiment of Reddit comments.
"""


from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType
from textblob import TextBlob


def create_spark():
    """
    Create a Spark object
    """

    conf = SparkConf().setMaster("local[*]")
    spark_context = SparkContext(conf=conf)
    spark_context.setLogLevel("ERROR")
    return SparkSession(sparkContext=spark_context)



def get_comment_polarity(comment):
    """
    Given a comment, return a tuple of comment, and its sentiment score.
    """
    comment = TextBlob(comment)

    return comment.sentiment.polarity


def get_comment_subjectivity(comment):
    """
    Given a comment, return a tuple of comment, and its polarity score.
    """
    comment = TextBlob(comment)

    return comment.sentiment.subjectivity


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

    data.show()


if __name__ == '__main__':
    main()
