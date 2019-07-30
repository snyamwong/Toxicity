from json_cleaner import clean_json
from sentiment_analysis import create_spark
from nltk.corpus import stopwords

def getFrequency(data):

    #set stops words using nltk library
    stop_words = set(stopwords.words('english'))

    #convert dataframe into rdd
    rdd = data.rdd.map(list)

    #get 'body' of df and filter out stop words
    body_rdd = rdd.flatMap(lambda x: x[1].split(" "))
    body_rdd_remove_stop = body_rdd.filter(lambda x: x.lower() not in stop_words)

    #get frequency of words
    freq = body_rdd_remove_stop.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

    #convert to dictionary
    return freq.collectAsMap()

def main():

    spark = create_spark()

    #file paths
    orig_file = '../dump/RC_2005-12'
    clean_file = '../dump/RC_2005-12-clean.json'

    #clean data
    clean_json(orig_file, clean_file)

    #open clean file
    data = spark.read.json(clean_file)

    #get dictionary
    dict = getFrequency(data)

    #test
    print(dict['look'])

if __name__ == '__main__':
    main()
