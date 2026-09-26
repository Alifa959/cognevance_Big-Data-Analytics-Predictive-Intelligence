from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, countDistinct

spark = SparkSession.builder.appName("EcommerceBigDataAnalytics").getOrCreate()

df = spark.read.option("header", True).option("inferSchema", True).csv(
    "data/raw/orders.csv"
)

df = df.dropDuplicates()

if "revenue" in df.columns:
    df.groupBy("category").agg(
        spark_sum("revenue").alias("total_revenue"),
        countDistinct("order_id").alias("orders")
    ).orderBy(col("total_revenue").desc()).show(20)

df.write.mode("overwrite").parquet("data/processed/spark_orders.parquet")

spark.stop()
