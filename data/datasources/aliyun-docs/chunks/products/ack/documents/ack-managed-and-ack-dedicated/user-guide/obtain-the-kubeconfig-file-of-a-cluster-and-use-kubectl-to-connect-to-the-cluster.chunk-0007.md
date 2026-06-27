em cat ./kubeconfig |grep client-key-data | awk -F ' ' '{print $2}' |base64 -d > ./client-key.pem APISERVER=`cat ./kubeconfig |grep server | awk -F ' ' '{print $2}'`请按实际情况修改kubeconfig路径。默认情况下，kubectl使用$HOME/.kube/config来连接集群。也可通过设置KUBECONFIG环境变量或设置--kubeconfig参数来指定其他KubeConfig文件。
如何解决通过kubectl连接集群时提示certificate is valid for错误的问题？
当为集群API Server的SLB绑定了新的IP，然后使用kubectl访问这个新的IP时，执行kubectl命令可能会失败并提示Error while proxying request: x509: certificate is valid for xxx或Unable to connect to the server: x509: certificate is valid for xxx错误。
ACK托管集群：将新的IP加入到API Server证书SAN中，请参见[自定义集群](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md)[API Server](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md)[证书](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md)[SAN](../security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster.md)。
ACK专有集群：配置kubectl，使用insecure-skip-tls-verify配置忽略此错误。
重要
此方式将导致客户端不再校验API Server证书，不建议在生产环境中使用。建议[热迁移](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clust
