from pyspark.sql import SparkSession
import time

my_spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .getOrCreate()

df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

print("\n\n\n")
# -----------------
init = time.time()
q_count = df.count()
end = time.time()
print("Query Count:", end-init)



print("\n\n\n")
# ------------------
init = time.time()
df.filter(lambda row: row['collaborative'] == 'true')
end = time.time()
print("Query Filter:", end-init)
#plays_coll = df.filter(df.collaborative == 'true')



print("\n\n\n")
# ------------------
from pyspark.sql.functions import avg, col, size, length
init = time.time()
df.agg(avg(col("num_albums")))
end = time.time()
print("Query Avg:", end-init)
#df.agg(avg(size("tracks")))
#df.agg(avg(length(col("name"))))



print("\n\n\n")
# ------------------
from pyspark.sql.functions import avg, col, size, length
init = time.time()
df.select("tracks")
end = time.time()
print("Query Select:", end-init)
