# 创建ACK Serverless集群
ACK Serverless集群是阿里云推出的无需购买节点即可部署工作负载的Kubernetes容器服务。ACK Serverless集群的秒级伸缩能力、根据应用配置的CPU和内存资源量按需、按量付费能力，降低业务的计算成本，尤其是有明显波峰波谷的业务。ACK Serverless集群提供完善的Kubernetes兼容能力，同时降低Kubernetes使用门槛，让您无需管理底层基础设施，更加专注于应用程序。本文介绍如何在容器服务管理控制台创建ACK Serverless集群。
重要
从2025年02月17日起，阿里云容器服务 Serverless 版将对尚未创建过集群的新用户关闭创建集群的入口。您可以通过容器计算服务 ACS（Container Compute Service）使用Serverless容器算力，ACS集群能够支持企业级K8s容器化应用的全生命周期管理，为您提供更强大的功能和更便捷的服务。关于ACS的详细介绍，请参见[ACS](https://help.aliyun.com/zh/cs/product-overview/product-introduction)[产品简介](https://help.aliyun.com/zh/cs/product-overview/product-introduction)。
对于尚未创建过ACK Serverless集群的新用户，我们已关闭新建ACK Serverless集群的入口。您可以通过以下方式使用Serverless容器算力：
创建ACS集群，并在其中使用Serverless容器算力。详细操作，请参见[创建](https://help.aliyun.com/zh/cs/user-guide/create-an-acs-cluster)[ACS](https://help.aliyun.com/zh/cs/user-guide/create-an-acs-cluster)[集群](https://help.aliyun.com/zh/cs/user-guide/create-an-acs-cluster)。
在ACK托管集群Pro版中按需弹性使用Serverless容器算力。详细操作，请参见[通过](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster)[ACK](https://help.aliyun.com/zh/cs/user-guide/access-acs-computing-power-in-an-ack-cluster)[托管集群](https://help.aliyun.com/zh/cs/user-guide/access-a
