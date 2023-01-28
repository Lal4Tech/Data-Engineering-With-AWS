### 
# You might have noticed this code in the screencast.
#
# import findspark
# findspark.init('spark-2.3.2-bin-hadoop2.7')
#
# The findspark Python module makes it easier to install
# Spark in local mode on your computer. This is convenient
# for practicing Spark syntax locally. 
# However, the workspaces already have Spark installed and you do not
# need to use the findspark module
#
###

from pyspark.sql import SparkSession

# Because we aren't running on a spark cluster, the session is just for development
spark = SparkSession \
    .builder \
    .appName("Maps and Lazy Evaluation Example") \
    .getOrCreate()


# Starting off with a regular python list
log_of_songs = [
        "Despacito",
        "Nice for what",
        "No tears left to cry",
        "Despacito",
        "Havana",
        "In my feelings",
        "Nice for what",
        "despacito",
        "All the stars"
]

# parallelize the log_of_songs to use with Spark
# distributed_song_log_rdd is an RDD (Reslient Distributed Dataset)
distributed_song_log_rdd = spark.sparkContext.parallelize(log_of_songs)

# notice we DO NOT use the .collect() method. What is the difference between
# .collect() and .foreach() ? 
# .collect() forces all the data from the entire RDD on all nodes 
# to be collected from ALL the nodes, which kills productivity, and could crash
# .foreach() allows the data to stay on each of the independent nodes

print("Show the original input data is preserved")

distributed_song_log_rdd.foreach(print)

print("-" * 30)

def convert_song_to_lowercase(song):
    return song.lower()

print("Converting sample string 'Havana' to lowercase")
print(convert_song_to_lowercase("Havana"))

print("-" * 30)
 
print("Show the converted data")
lower_case_songs=distributed_song_log_rdd.map(convert_song_to_lowercase)
lower_case_songs.foreach(print)

print("-" * 30)

# Show the original input data is still mixed case
print("Show the original input data is still mixed case")
distributed_song_log_rdd.foreach(print)

print("-" * 30)

# Use lambda functions instead of named functions to do the same map operation
print("Using lambda function")
distributed_song_log_rdd.map(lambda song: song.lower()).foreach(print)
