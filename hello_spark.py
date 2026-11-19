rom pyspark.sql import SparkSession
# Start a local Spark session that uses all your CPU cores
spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("hello")
    .getOrCreate()
)
print(f"Spark version: {spark.version}")
# A tiny three-row DataFrame
data = [
    (1, "Dublin", 12.5),
    (2, "Cork", 8.0),
    (3, "Galway", 15.25),
]
df = spark.createDataFrame(data, ["trip_id", "city", "fare"])
df.printSchema()
df.show()
spark.stop()
