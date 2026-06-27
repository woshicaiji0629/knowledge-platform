## 前提条件
支持ACK集群版本及类型。
说明
支持在版本≥1.16.9的托管版、专有版，≥1.26.3的ACK Edge集群和ACK Serverless集群、ACK灵骏集群和容器计算服务ACS上使用加速镜像。且创建集群时操作系统为Alibaba Cloud Linux 2.1903、Alibaba Cloud Linux 3.2104、Alibaba Cloud Linux 3.2104 LTS 64 bit ARM edition、Alibaba Cloud Linux UEFI 2.1903、CentOS 7.9。
已创建企业版实例，更多信息，请参见[创建企业版实例](https://help.aliyun.com/zh/acr/user-guide/create-a-container-registry-enterprise-edition-instance#task488)。
重要
在镜像加速中，两种模式支持的企业版实例规格有所不同：
完整模式：支持的企业版实例为标准版或高级版。
仅索引模式：支持的企业版实例为基础版、标准版或高级版。
已在企业版实例中配置ACK或ACK Serverless集群对应的专有网络。加速镜像需要在专有网络中使用，更多信息，请参见[配置专有网络的访问控制](https://help.aliyun.com/zh/acr/user-guide/configure-access-over-vpcs#task1305)。
