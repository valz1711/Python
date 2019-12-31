from pyspark.sql import SparkSession

if(__name__ == '__main__'):
    spark = SparkSession.builder.getOrCreate()
    path = "C:/Users/Valan Aravind/Desktop/Scala/R/Data/SparkCSV.csv"
    sparkDF = spark.read.csv(path,header=True)

    sparkDF.show()
    sparkDF.printSchema()
    orderedDF = sparkDF.withColumn("S_No",sparkDF["S_No"].cast("Int")).sort("S_No")
    orderedDF.show()
    orderedDF.printSchema()
    print("Spark dataframe is succesfully displayed")