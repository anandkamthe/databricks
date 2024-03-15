# Databricks notebook source
# Import the required libraries
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Get the list of schemas
schemas = spark.catalog.listDatabases()

# Print the list of schemas
for schema in schemas:
    print(schema.name)
