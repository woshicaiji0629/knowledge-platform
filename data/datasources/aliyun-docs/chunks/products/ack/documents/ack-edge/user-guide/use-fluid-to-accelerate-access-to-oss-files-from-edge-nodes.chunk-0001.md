## 前提条件
已创建ACK Edge集群，且集群版本为1.18及以上。具体操作，请参见[创建集群](create-an-ack-edge-cluster-1.md)。
已创建一个边缘节点池，并为其添加边缘节点，具体操作，请参见[创建边缘节点池](../../create-an-edge-node-pool-1.md)、[添加边缘节点](add-an-edge-node.md)。
已安装云原生AI套件并部署ack-fluid组件。
重要
若您已安装开源Fluid，请卸载后再部署ack-fluid组件。
未安装云原生AI套件：安装时开启Fluid数据加速。具体操作，请参见[部署](deploy-ai-suite-console.md)[AI](deploy-ai-suite-console.md)[套件控制台](deploy-ai-suite-console.md)。
已安装云原生AI套件：在[容器服务管理控制台](https://cs.console.aliyun.com)的云原生AI套件页面部署ack-fluid。
已通过kubectl连接Kubernetes集群。具体操作，请参见[通过](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
已开通阿里云对象存储OSS服务。具体操作，请参见[开通](../../../../oss/documents/getting-started/activate-oss.md)[OSS](../../../../oss/documents/getting-started/activate-oss.md)[服务](../../../../oss/documents/getting-started/activate-oss.md)。
