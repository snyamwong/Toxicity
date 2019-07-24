from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext


def load_files(data_path):
    """
    This method reads all files in the data folder. Should only contain JSON,
    idk what will happen otherwise....
    :return:
    """

    df = sqlContext.read.json(data_path)
    return df


def target_subreddits(List_of_Subs):
    pass


def clean_data(filename):
    pass


def main():
    data_path = "data/*"
    raw_df = load_files(data_path)


if __name__ == "__main__":
    conf = SparkConf().setMaster("local[*]").setAppName("Toxicity-Cleaning")
    sc = SparkContext(conf = conf)
    sqlContext = SQLContext(sc)

    main()
