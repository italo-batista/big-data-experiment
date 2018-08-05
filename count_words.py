import re, string
from pyspark import SparkContext, SparkConf

print("\n\n\n-----------------------------------------\n\n\n")

conf = SparkConf().setAll(
    [('spark.executor.memory', '6g'),
    ('spark.executor.cores', '4'),
    ("spark.driver.port", "1100"),
    ("spark.port.maxRetries", "20"),
    ("spark.driver.blockManager.port", "1200"),
    ("spark.blockManager.port", "1300"),
    ("spark.shuffle.blockTransferService", "nio"),
    ('spark.driver.memory','1g')])


master="spark://10.11.5.56:7077"
sc = SparkContext(master=master, appName= "app", conf=conf)
#sc = SparkContext()
text_file = sc.textFile('example_text.txt')

punc = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'
def uni_to_clean_str(x):
    converted = x.encode('utf-8')
    lowercased_str = converted.lower()
    lowercased_str = lowercased_str.replace('--',' ')
    clean_str = lowercased_str.translate(None, punc) #Change 1
    return clean_str

one_RDD = text_file.flatMap(lambda x: uni_to_clean_str(x).split())
one_RDD = one_RDD.map(lambda x: (x, 1))
one_RDD = one_RDD.reduceByKey(lambda x,y: x + y)

print("\n\n\n-----------------------------------------\n\n\n")
print(one_RDD.take(10))
