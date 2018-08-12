from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, size, length
import time

my_spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .config('spark.executor.memory', '6656m') \
    .config("spark.driver.port", "5000") \
    .config("spark.port.maxRetries", "20") \
    .config("spark.driver.blockManager.port", "5100") \
    .config("spark.blockManager.port", "5200") \
    .getOrCreate()

df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
f = open("cluster_10gb.txt", "w")


print("\n\n\n")
# -----------------
init = time.time()
df.count()
end = time.time()
f.write("\nQuery Count:" +str(end-init))
print("Query Count:", end-init)


print("\n\n\n")
# ------------------
init = time.time()
df.filter(df.collaborative == 'true')
end = time.time()
f.write("\nQuery Filter:" +str(end-init))
print("Query Filter:", end-init)


print("\n\n\n")
# ------------------
init = time.time()
df.agg(avg(col("num_albums")))
end = time.time()
f.write("\nQuery Avg:" +str(end-init))
print("Query Avg:", end-init)


print("\n\n\n")
# ------------------
init = time.time()
df.select("tracks")
end = time.time()
f.write("\nQuery Select:" + str(end-init))
print("Query Select:", end-init)
