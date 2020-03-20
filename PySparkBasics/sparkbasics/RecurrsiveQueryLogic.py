from pyspark.sql import SparkSession

if(__name__ == '__main__'):
    spark = SparkSession.builder.getOrCreate()
    path = "C:/Users/Valan Aravind/Desktop/ws-data-spark-master/data/DataSample.csv"
    samplesetDF = spark.read.csv(path,header=True,inferSchema=True)
    samplesetDF.show(5,False)
    poiPath = "C:/Users/Valan Aravind/Desktop/ws-data-spark-master/data/POIList.csv"
    poiDF = spark.read.csv(poiPath,header=True,inferSchema=True)
    poiDF.show()