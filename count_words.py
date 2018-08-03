import re, string
from pyspark import SparkContext

print("\n\n\n-----------------------------------------\n\n\n")

sc = SparkContext()
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
