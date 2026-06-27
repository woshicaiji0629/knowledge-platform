## 步骤二：获取并使用KubeConfig
在控制台获取 KubeConfig 后，kubectl 可依据该文件连接并管理集群。
RAM用户连接集群前，除容器服务的系统权限外，还需要被授予集群操作的权限，请参见[为](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[RAM](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[用户授予](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[RBAC](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[权限](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)。
登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。
在集群信息页面，单击连接信息页签，选择公网访问或内网访问，然后复制KubeConfig。
内网访问：获取内网访问的KubeConfig，此时kubectl客户端机器必须与集群位于同一VPC。通过阿里云内网连接时，延迟更低，更安全。
公网访问：获取公网访问的KubeConfig，通过公网中的任意机器作为客户端来连接集群。依赖[EIP](../../../../eip/documents/product-overview/what-is-eip.md)连接 API Server，适用于本地开发或远程运维。
EIP 绑定后，相关费用请参见[按量付费](../../../../eip/documents/pay-as-you-go.md)。
将复制的KubeConfig内容粘贴至客户端的$HOME/.kube/config文件中，保存并退出。
如果$HOME/.kube/config文件不存在，可通过mkdir -p $HOME/.kube和touch $HOME/.kube/config来创建。
配置完成后，执行kubectl命令以验证集群连通性。
以查询命名空间为例。
kubectl get namespaces
预期输
