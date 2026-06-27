## 采集配置创建流程
[安装](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[LoongCollector](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)：通过DaemonSet模式部署LoongCollector，确保集群中每个节点均运行一个采集容器，统一采集该节点上所有容器的日志。
[创建](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[LogStore](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)：LogStore是日志数据的存储单元，用于存储日志。一个 Project 内可创建多个 LogStore。
创建采集配置YAML文件：[使用](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[连接集群](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)，您可以通过以下两种方式创建采集配置文件：
方式一：使用采集配置生成器
通过日志服务控制台的[采集配置生成器](https://sls.console.aliyun.com/lognext/crd-generator)，可视化填写参数，自动生成标准YAML文件。
方式二：手动编写YAML
结合本文档提供的典型场景示例与配置流程，根据实际业务需求手动编写 YAML 文件。建议按本文结构逐步构建配置：从极简配置起步 → 添加处理逻辑 → 启用高级
