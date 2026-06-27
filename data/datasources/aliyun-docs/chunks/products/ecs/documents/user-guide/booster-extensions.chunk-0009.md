-common-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-encoding/1.13.1/parquet-encoding-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-format-structures/1.13.1/parquet-format-structures-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.13.1/parquet-hadoop-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-jackson/1.13.1/parquet-jackson-1.13.1.jar for file in $SPARK_HOME/jars/parquet-*.jar; do sudo mv "$file" "$file.bak"; done sudo cp -rf parquet-*.jar $SPARK_HOME/jars
如配置shuffle过程的数据压缩方式，请修改以下参数：
spark.io.compression.zstd.level 1 spark.io.compression.codec zstd
使用Spark存算分离时，需要配置OSS的Endpoint和AccessKey。
使用OSS存储时，必须在/opt/keentune/spark.conf文件中配置s3a相关参数。
spark.hadoop.fs.s3a.endpoint <OSS的Endpoint> spark.hadoop.fs.s3a.access.key <AccessKey ID> spark.hadoop.fs.s3a.secret.key <AccessKey Secret>
在Spark的Master节点使用新的配置启动Spark集群。
您可以使用以下两种方式来启动Spark集群：
直接使用/opt/keentune/spark.conf来重启Spark。
