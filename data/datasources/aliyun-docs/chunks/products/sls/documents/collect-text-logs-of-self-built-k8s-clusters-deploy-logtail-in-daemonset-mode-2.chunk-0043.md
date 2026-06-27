### 如何将ACK集群日志传输到另一个阿里云账号的Project？
通过在ACK集群中手动安装日志服务LoongCollector（Logtail）组件，并为其配置目标账号的主账号ID或访问凭证（AccessKey），即可实现将容器日志发送到另一个阿里云账号的日志服务Project中。
场景描述：当因为组织架构、权限隔离或统一监控等原因，需要将某个ACK集群的日志数据采集到另一个独立的阿里云账号的日志服务Project时，可通过手动安装 LoongCollector（Logtail）进行跨账号配置。
操作步骤：此处以手动安装LoongCollector为例，如需了解如何安装Logtail，请参考[Logtail](install-run-upgrade-and-uninstall-logtail.md)[安装与配置](install-run-upgrade-and-uninstall-logtail.md)。
连接Kubernetes集群，并根据地域选择对应命令，下载LoongCollector及其依赖组件：
中国地域：
wget https://aliyun-observability-release-cn-shanghai.oss-cn-shanghai.aliyuncs.com/loongcollector/k8s-custom-pkg/3.0.12/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh
海外地域：
wget https://aliyun-observability-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/loongcollector/k8s-custom-pkg/3.0.12/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh
进入loongcollector-custom-k8s-package目录，修改配置文件./loongcollector/values.yaml。
