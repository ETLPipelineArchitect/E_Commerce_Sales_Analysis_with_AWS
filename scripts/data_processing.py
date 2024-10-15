from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, regexp_replace

# Initialize Spark Session
spark = SparkSession.builder.appName("ECommerceSalesAnalysis").getOrCreate()

# Read Data from S3
orders_df = spark.read.csv("s3://your-bucket/ecommerce_data/raw/orders.csv", header=True, inferSchema=True)

# Data Cleaning
orders_df = orders_df.dropna(subset=['order_id', 'customer_id'])

# Convert Data Types
orders_df = orders_df.withColumn('order_purchase_timestamp', to_date(col('order_purchase_timestamp'), 'yyyy-MM-dd HH:mm:ss'))

# Save Processed Data
orders_df.write.parquet("s3://your-bucket/ecommerce_data/processed/orders.parquet", mode='overwrite')
