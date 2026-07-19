import sys

from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql.functions import (
    col,
    trim,
    to_date,
    current_timestamp
)

# ----------------------------------------------------
# Initialize Spark & Glue
# ----------------------------------------------------

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init("enterprise-ai-etl-job", {})

# ----------------------------------------------------
# Read CSV from S3 Raw Zone
# ----------------------------------------------------

df = spark.read.csv(
    "s3://ayushi-enterprise-ai-data-lakehouse/raw/global_supply_chain_risk_2026.csv",
    header=True,
    inferSchema=True
)

print("========== RAW SCHEMA ==========")
df.printSchema()

print("========== SAMPLE DATA ==========")
df.show(5, truncate=False)

# ----------------------------------------------------
# Remove Duplicate Rows
# ----------------------------------------------------

df = df.dropDuplicates()

# ----------------------------------------------------
# Remove rows where Shipment_ID is missing
# ----------------------------------------------------

df = df.na.drop(subset=["Shipment_ID"])

# ----------------------------------------------------
# Trim spaces from string columns
# ----------------------------------------------------

string_columns = [
    "Origin_Port",
    "Destination_Port",
    "Transport_Mode",
    "Product_Category",
    "Weather_Condition"
]

for column_name in string_columns:
    if column_name in df.columns:
        df = df.withColumn(column_name, trim(col(column_name)))

# ----------------------------------------------------
# Convert Date column
# ----------------------------------------------------

if "Date" in df.columns:
    df = df.withColumn(
        "Date",
        to_date(col("Date"))
    )

# ----------------------------------------------------
# Add ETL Timestamp
# ----------------------------------------------------

df = df.withColumn(
    "etl_processed_timestamp",
    current_timestamp()
)

print("========== CLEANED SCHEMA ==========")
df.printSchema()

print("========== CLEANED DATA ==========")
df.show(5, truncate=False)

# ----------------------------------------------------
# Write Parquet to Processed Zone
# ----------------------------------------------------

df.write \
    .mode("overwrite") \
    .parquet("s3://ayushi-enterprise-ai-data-lakehouse/processed/")

job.commit()