### 注册集群相关
通过[容器服务管理控制台](https://cs.console.aliyun.com)的注册集群功能接入外部Kubernetes集群时，请确保外部集群与阿里云之间的网络稳定性。
容器服务ACK提供外部Kubernetes集群的注册接入，但无法管控外部集群自身的稳定性以及不当操作。因此当您通过注册集群配置外部集群节点的Label、Annotation、Tag等信息时，可能导致应用运行异常，请谨慎操作。
