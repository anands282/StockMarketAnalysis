from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("Read JSON files from S3") \
    .getOrCreate()

# S3 bucket path where the JSON files are stored
bucket_path = "s3://stock-market-project-store/*.json"

# Read JSON files into a DataFrame
df = spark.read.json(bucket_path)

df.printSchema()
df.show()
spark.stop()
