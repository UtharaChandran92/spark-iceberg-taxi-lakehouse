# Spark + Iceberg lakehouse on NYC Yellow Taxi data
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
## Step 2: DataFrame basics
- Read one month (Jan 2026) of NYC Yellow Taxi Parquet with PySpark.
- Used select, filter and withColumn to clean trips and add duration in minutes.
- Learned that transformations are lazy, so nothing runs until an action like show() or count().