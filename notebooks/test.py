# Databricks notebook source
# Import the necessary libraries
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.getOrCreate()

# List all the schemas
schemas = spark.catalog.listDatabases()

# Print the schema names
for schema in schemas:
    print(schema.name)
