## 使用curl命令操作Kubernetes API
执行以下命令查看当前集群中所有Namespaces。
curl --cert ./client-cert.pem --key ./client-key.pem -k $APISERVER/api/v1/namespaces
通过curl命令管理Pod和Deployment常见示例操作如下。
