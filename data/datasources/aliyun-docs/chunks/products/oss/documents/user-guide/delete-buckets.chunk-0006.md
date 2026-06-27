## HDFS文件
通过OSS控制台的方式
在文件资源的状态列单击立即暂停，停止HDFS后台任务。
单击前往删除，进入HDFS页签。
逐个单击彻底删除，直至清空所有HDFS文件。
通过HDFS Shell命令的方式hdfs dfs -rm -r -skipTrash oss://examplebucket.cn-hangzhou.oss-dls.aliyuncs.com/*
更多信息，请参见[通过](connect-non-emr-clusters-to-oss-hdfs.md)[HDFS Shell](connect-non-emr-clusters-to-oss-hdfs.md)[命令执行](connect-non-emr-clusters-to-oss-hdfs.md)[OSS-HDFS](connect-non-emr-clusters-to-oss-hdfs.md)[服务快速入门常见操作。](connect-non-emr-clusters-to-oss-hdfs.md)
