from pyspark.sql import SparkSession

my_spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .getOrCreate()

df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

c = df.count()

print(c)

