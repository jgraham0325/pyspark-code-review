# Databricks notebook source
# MAGIC %md # Load new data from loan risks files into table in Databricks

table_name = 'default.loan_risks_upload'
source_data = '/databricks-datasets/learning-spark-v2/loans/'
source_format = 'PARQUET'

spark.sql("DROP TABLE IF EXISTS " + table_name)

spark.sql("CREATE TABLE " + table_name + " (" \
  "loan_id BIGINT, " + \
  "funded_amnt INT, " + \
  "paid_amnt DOUBLE, " + \
  "addr_state STRING)"
)

spark.sql("COPY INTO " + table_name + \
  " FROM '" + source_data + "'" + \
  " FILEFORMAT = " + source_format
)

loan_risks_upload_data = spark.sql("SELECT * FROM " + table_name)

display(loan_risks_upload_data)

'''
Result:
+---------+-------------+-----------+------------+
| loan_id | funded_amnt | paid_amnt | addr_state |
+=========+=============+===========+============+
| 0       | 1000        | 182.22    | CA         |
+---------+-------------+-----------+------------+
| 1       | 1000        | 361.19    | WA         |
+---------+-------------+-----------+------------+
| 2       | 1000        | 176.26    | TX         |
+---------+-------------+-----------+------------+
...
'''