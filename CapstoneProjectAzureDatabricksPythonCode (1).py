#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Creating connection on top of the Azure Datalake Account 

serviceprincpleid="c5de8d16-a00e-4ee1-b50b-d5b8f383fd71"
serviceprincplekey=".E18Q~2d9qZALpRr4zuFwBcvcqf1jig6Dz5Smcsw"
configs = {
  "fs.azure.account.auth.type": "OAuth",
   "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
   "fs.azure.account.oauth2.client.id":serviceprincpleid,
   "fs.azure.account.oauth2.client.secret":serviceprincplekey,
   "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/16446715-0718-4581-af02-52ead6dc05d6/oauth2/token"}


# In[ ]:


#To create mount point on the Azure container , this code should be excecuted only for the first time.
dbutils.fs.mount(
source = "abfss://source@adlsprojectcontainer.dfs.core.windows.net/",
mount_point = "/mnt/mountadlsgen3",
extra_configs = configs)


# In[ ]:


# To know the mounted data path, in order to read the data later
get_ipython().run_line_magic('fs', '')
ls /mnt/mountadlsgen3


# In[ ]:


#To read from Azure blob 

df1=spark.read.option("header","true").csv("/mnt/mountadlsgen2/covid_data_1.csv")


# In[ ]:


#To display the dataframe records

display(df1)


# In[ ]:


#To show the schema of the file present in blob storage
df1.printSchema()


# In[ ]:


# Cleaning up column "iso_code", "continent" and "location" with Special characters
from pyspark.sql import functions as F

df_transformed1 = df1.withColumn('iso_code',F.trim(F.regexp_replace(F.col('iso_code'),'[^A-Z,a-z]','')))
df_transformed2 = df_transformed1.withColumn('continent',F.trim(F.regexp_replace(F.col('continent'),'[^A-Z,a-z]','')))
df_transformed7 = df_transformed2.withColumn('location',F.trim(F.regexp_replace(F.col('location'),'[^A-Z,a-z]','')))


# In[ ]:


display(df_transformed7)


# In[ ]:


# Selecting only required columns and Alaising the column names if required
df_transformed8 = df_transformed7.select(
                               F.col('iso_code').alias('iso_code'),
                               F.col('continent').alias('continent'),
                               F.col('location').alias('location'),
                               F.col('date').alias('date'),
                               F.col('total_cases').alias('total_cases_reported'),
                               F.col('new_cases').alias('new_cases_reported'),
                               F.col('total_deaths').alias('total_deaths_reported'),
                               F.col('new_deaths').alias('new_deaths_reported'),
							   F.col('total_cases_per_million').alias('total_cases_per_million'),
                               F.col('total_deaths_per_million').alias('total_deaths_per_million'))


display(df_transformed8)


# In[ ]:


# Drop Rows with NULL Values on Selected Columns

df_transformed_final = df_transformed8.na.drop(subset=["total_cases_reported","new_cases_reported","total_deaths_reported","new_deaths_reported","total_cases_per_million","total_deaths_per_million"])
display(df_transformed_final)


# In[ ]:


#Creating Azure SQL Database connection

jdbcHostname = "capstoneprojectsqlserver.database.windows.net"
jdbcPort = "1433"
jdbcDatabase = "capstoneprojectsqldb"
properties = {
        "user": "projectuser",
        "password": "ProJecT&198User"
    }

url = "jdbc:sqlserver://{0}:{1};database={2}".format(jdbcHostname, jdbcPort, jdbcDatabase)

df_transformed_final.write.format("jdbc")   .mode("overwrite")   .option("url", url)   .option("dbtable", "dbo.covid_data_analysis")   .option("user", "projectuser")   .option("password", "ProJecT&198User")   .save()


# In[ ]:


#To read from Azure SQL database
query_results = "(select * from dbo.covid_data_analysis) as covid_data_analysis"
df = spark.read.jdbc(url=url, table=query_results, properties=properties)

display(df)


# In[ ]:


#Creating a temp view on the dataframe we created in the above step
# Temporary representation of dataset to perform some transformation

temp_view_name ="v_covid_analysis"
df.createOrReplaceTempView(temp_view_name)


# In[ ]:


get_ipython().run_line_magic('sql', '')
Select * from v_covid_analysis


# In[ ]:


get_ipython().run_line_magic('sql', '')
Select iso_code,continent,location,date,total_cases_reported,new_cases_reported from v_covid_analysis


# In[ ]:





# In[ ]:




