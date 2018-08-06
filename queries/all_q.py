from pyspark.sql import SparkSession
import time

my_spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/recsys.playlists") \
    .config('spark.cores.max', '1') \
    .config('spark.driver.memory','2g') \
    .getOrCreate()

df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

f = open("vertical_small.txt", "w")


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
#df.filter(lambda row: row['collaborative'] == 'true')
end = time.time()
f.write("\nQuery Filter:" +str(end-init))
print("Query Filter:", end-init)



print("\n\n\n")
# ------------------
from pyspark.sql.functions import avg, col, size, length
init = time.time()
df.agg(avg(col("num_albums")))
end = time.time()
f.write("\nQuery Avg:" +str(end-init))
print("Query Avg:", end-init)
#df.agg(avg(size("tracks")))
#df.agg(avg(length(col("name"))))



print("\n\n\n")
# ------------------
from pyspark.sql.functions import avg, col, size, length
init = time.time()
df.select("tracks")
end = time.time()
f.write("\nQuery Select:" +str(end-init))
print("Query Select:", end-init)
