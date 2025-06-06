from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("creatingfromcsv").getOrCreate()
df = spark.read.csv("C:\\Users\\dell\\PycharmProjects\\practise\\text.csv", header=True,inferSchema=True)
df.show()
df.printSchema()
