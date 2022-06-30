# GLUE import
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.transforms import Relationalize
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from awsglue.transforms import *
# SPARK import
from pyspark.context import SparkContext
from pyspark.sql.functions import col
from pyspark.sql.functions import struct
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
# Standard import
from datetime import datetime

# Create glue context
glueContext = GlueContext(SparkContext.getOrCreate())

# Create dynamic frame
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database = "workshopdb",
    table_name = "origin",
    transformation_ctx="datasource0")

# User Define Function
def calc_age(invoiceDatetime: str, birthday: str):
    invoice_datetime = datetime.strptime(invoiceDatetime, "%m/%d/%Y %H:%M:%S")
    birthday_datetime = datetime.strptime(birthday, "%m/%d/%Y")
    age = invoice_datetime.year - birthday_datetime.year
    if invoice_datetime.strftime('%m%d') < birthday_datetime.strftime('%m%d'):
        age -= 1
    return age
ageUDF = udf(lambda x,y: calc_age(x,y),IntegerType())

# dynamicframe to dataframe
df = datasource0.toDF()

# add a new column
df = df.withColumn("customer",
    struct(
        col("customer.*"),
        ageUDF(df.invoiceDatetime, df.customer.birthday).alias("age")
    )
)

# create dynamicframe based on dataframe
frame = DynamicFrame.fromDF(df, glueContext, "order")

# store to s3
sink0 = glueContext.write_dynamic_frame_from_options(
    frame=frame,
    connection_type="s3",
    connection_options={
        "path": "s3://wsscc2021-analytics-workshop/data/parquet/"
    },
    format="parquet",
    transformation_ctx="datatarget0"
)