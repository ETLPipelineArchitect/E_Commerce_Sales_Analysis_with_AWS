from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("ECommerceSalesAnalysis").getOrCreate()

# Load Processed Data
orders_df = spark.read.parquet("s3://your-bucket/ecommerce_data/processed/orders.parquet")

# Data Analysis
orders_df.createOrReplaceTempView("orders")

top_products = spark.sql("SELECT product_category_name, COUNT(*) AS total_sales FROM orders GROUP BY product_category_name ORDER BY total_sales DESC LIMIT 10")
top_products.show()

# Save Query Results
result_path = "s3://your-bucket/ecommerce_data/output/top_products.csv"
top_products.write.csv(result_path, mode='overwrite')
