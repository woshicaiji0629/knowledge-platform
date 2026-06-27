## 自建集群安装（DaemonSet模式）
适用场景
自建 IDC 机房中的 Kubernetes 集群
部署在其他云厂商的 Kubernetes 集群
跨账号或跨地域采集阿里云 ACK 集群容器日志
说明
请确保您的自建集群满足Kubernetes 1.6及以上版本。
操作指南
下载并解压安装包：在安装并配置了kubectl的机器上，根据集群所在地域选择命令下载LoongCollector及其他依赖组件。
#中国地域 wget https://aliyun-observability-release-cn-shanghai.oss-cn-shanghai.aliyuncs.com/loongcollector/k8s-custom-pkg/3.2.6/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh #海外地域 wget https://aliyun-observability-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/loongcollector/k8s-custom-pkg/3.2.6/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh
修改配置文件values.yaml：进入loongcollector-custom-k8s-package目录，修改配置文件./loongcollector/values.yaml。
