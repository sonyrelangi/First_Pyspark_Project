from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
file_con = spark.read.csv("E:\PySpark_Projects\First_Pyspark_Project\Data\input.txt")
file_con.show()
