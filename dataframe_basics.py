from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.master("local[*]").appName("df-basics").getOrCreate()

# 2. Read the Parquet file and explore it
df = spark.read.parquet("data/yellow_tripdata_2026-01.parquet")
df.printSchema()
print("Rows:", df.count())
df.show(5, truncate=False)

# 3a. select: keep only the columns you need
trips = df.select(
    "tpep_pickup_datetime", "tpep_dropoff_datetime",
    "passenger_count", "trip_distance", "fare_amount",
)

# 3b. filter: drop bad rows
trips = trips.filter((F.col("fare_amount") > 0) & (F.col("trip_distance") > 0))

# 3c. withColumn: add trip duration in minutes
trips = trips.withColumn(
    "duration_min",
    (F.unix_timestamp("tpep_dropoff_datetime") - F.unix_timestamp("tpep_pickup_datetime")) / 60,
)
trips.show(5)

# 3d. groupBy + agg + orderBy: average fare per passenger count
summary = (
    trips.groupBy("passenger_count")
    .agg(
        F.count("*").alias("trips"),
        F.round(F.avg("fare_amount"), 2).alias("avg_fare"),
        F.round(F.avg("duration_min"), 1).alias("avg_duration_min"),
    )
    .orderBy("passenger_count")
)
summary.show()

spark.stop()