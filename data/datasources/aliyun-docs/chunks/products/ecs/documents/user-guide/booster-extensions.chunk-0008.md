### 配置Spark性能加速扩展
在Spark的Master节点和所有Worker节点配置Spark性能加速扩展的详细步骤如下：
在Spark的Master节点和所有Worker节点安装Spark性能加速扩展。
在实例详情页，选择定时与自动化任务>安装 / 卸载扩展程序，单击安装扩展程序。
在安装扩展程序对话框中，公共扩展选择Spark性能加速扩展，配置如下参数，然后单击下一步，按照界面提示完成操作。
worker_number：指Spark集群中Worker节点的数量。
worker_type：指Worker节点的实例规格，当前仅支持ecs.g8y.8xlarge及以上规格和ecs.r8y.8xlarge及以上规格。
在Spark所有Worker节点配置ZSTD。
替换jar包。
for jar in $SPARK_HOME/jars/zstd-*.jar; do sudo mv "$jar" "${jar}.bak"; done sudo cp /opt/keentune/compress/zstd-*.jar $SPARK_HOME/jars/
修改/opt/keentune/spark.conf配置。
如配置parquet文件写入过程的压缩方式，请修改以下参数：
spark.sql.parquet.compression.codec zstd spark.hadoop.parquet.compression.codec.zstd.level 1
重要
如果您的Parquet为1.13以下版本，建议您参考以下步骤升级到1.13及以上版本，以默认启用ZSTD的buffer pool。关于ZSTD JNI BufferPool的说明，请参见[Support ZSTD JNI BufferPool](https://github.com/apache/parquet-java/commit/279255df0c050aa95b5f5eb5963cf7eae5b8d180)。
wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-column/1.13.1/parquet-column-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-common/1.13.1/parquet-common-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-encoding/1.13.1/parquet-encoding-1.13.1.jar wget https://repo1.maven.org/maven
