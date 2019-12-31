from pyspark.sql import SparkSession

if(__name__ == '__main__'):
    spark = SparkSession.builder.getOrCreate()
    path = "C:/Users/Valan Aravind/Desktop/Scala/R/Data/SparkCSV.csv"
    sparkDF = spark.read.csv(path,header=True)
    print("Please order by Sl_no")
    sparkDF.show()
    print("Spark dataframe is succesfully displayed")
