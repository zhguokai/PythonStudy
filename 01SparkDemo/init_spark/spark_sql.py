# coding: utf-8
from pyspark import Row
from pyspark.sql.context import SQLContext

from common import spark_context as sc

sql_context = SQLContext(sc)


def load_data_from_mysql():
    df = sql_context.load(source="jdbc", url="jdbc:mysql://localhost:3306/mysql?user=root&&password=123456",
                          dbtable="user")
    df.printSchema()
    df.select('User').show()
    df.select(df.Host, df.Password).show()
    df.filter(df.Host == 'localhost').show()
    df.groupBy("User").count().show()
    df.show()


def load_data_sql():
    # DataFrames
    df = sql_context.load(source="jdbc", url="jdbc:mysql://localhost:3306/mysql?user=root&&password=123456",
                          dbtable="user")
    df.toJSON().saveAsTextFile("df1.json")
    df.saveAsParquetFile('df1.parquet')

    # 生成Table数据
    users = df.map(lambda row: Row(name=row.User, password=row.Password))
    # 注入Table
    schema_users = sql_context.createDataFrame(data=users)
    # schema_users = sql_context.inferSchema(users)
    schema_users.registerAsTable("user")

    # RDDS
    sql_result = sql_context.sql("select name,password from user")
    user_names = sql_result.map(lambda p: ("Name:" + p.name, "password:" + p.password))
    print u"测试".encode('utf8')

    df.save("namesAndAges.parquet")
    for user_name, password in user_names.collect():
        print(user_name, password)


if __name__ == "__main__":
    # load_data_from_mysql()
    load_data_sql()
