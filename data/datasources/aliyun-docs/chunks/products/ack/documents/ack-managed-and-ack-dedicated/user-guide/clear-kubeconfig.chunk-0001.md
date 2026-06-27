## KubeConfig介绍
KubeConfig用于在客户端配置集群的访问凭据，您可以通过[容器服务管理控制台](https://cs.console.aliyun.com)、[获取集群](../developer-reference/api-query-the-kubeconfig-file-of-a-cluster.md)[KubeConfig](../developer-reference/api-query-the-kubeconfig-file-of-a-cluster.md)[接口](../developer-reference/api-query-the-kubeconfig-file-of-a-cluster.md)等方式获取。请妥善管理集群的KubeConfig凭据，避免KubeConfig泄露带来的数据泄露等安全风险。
重要
获取的KubeConfig具备特定的生效时间，到期之后将自动失效。关于KubeConfig有效期时间查询，请参见[如何获取](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[所使用的证书的过期时间？](obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)
