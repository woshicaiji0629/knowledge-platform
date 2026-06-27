## 步骤一：准备OSS Bucket的数据
执行以下命令，下载测试数据到ECS实例中。
wget https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
将下载的测试数据上传到[阿里云](https://cn.aliyun.com/product/oss)[OSS](https://cn.aliyun.com/product/oss)对应的Bucket中。
重要
上传到OSS的步骤以Alibaba Cloud Linux 3.2104 LTS 64位的ECS实例为例。其他操作系统的具体操作，请参见[命令行工具](../../../../oss/documents/developer-reference/ossutil.md)[ossutil](../../../../oss/documents/developer-reference/ossutil.md)[快速入门](../../../../oss/documents/developer-reference/ossutil.md)和[命令行工具](../../../../oss/documents/developer-reference/overview-59.md)[ossutil 1.0](../../../../oss/documents/developer-reference/overview-59.md)。
[安装](../../../../oss/documents/developer-reference/install-ossutil.md)[ossutil](../../../../oss/documents/developer-reference/install-ossutil.md)。
创建名称为examplebucket的存储空间。
输入以下命令创建examplebucket。
ossutil mb oss://examplebucket
以下输出结果表明已成功创建examplebucket。
0.668238(s) elapsed
将下载的测试数据上传到新建的examplebucket中。
ossutil cp spark-3.0.1-bin-hadoop2.7.tgz oss://examplebucket
