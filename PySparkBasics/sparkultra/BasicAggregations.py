from pyspark.sql import SparkSession as ss, DataFrame
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *



if(__name__ == '__main__'):
    spark = ss.builder.getOrCreate()
    path = "C:/Users/Valan Aravind/Desktop/ws-data-spark-master/data"
    sparkDF = spark.read.csv(path + "/" +"DataSample.csv",header=True,inferSchema=True)\
        .sort("TimeSt","Latitude","Longitude")

    print("Data load complete")

    overCategory = Window.partitionBy("TimeSt","Latitude","Longitude")

    rankedDF = sparkDF.withColumn("row_num", row_number().over(overCategory.orderBy("ID")))
    rankedDF.show()
    filterDF = rankedDF.filter(col("row_num") == 1)
    finalDF = filterDF.drop(col("row_num"))
