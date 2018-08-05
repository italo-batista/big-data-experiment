from pyspark.sql import SparkSession

my_spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .config("spark.driver.port", "5000") \
    .config("spark.port.maxRetries", "20") \
    .config("spark.driver.blockManager.port", "5100") \
    .config("spark.blockManager.port", "5200") \
    .getOrCreate()

df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

c = df.count()

print(c)

