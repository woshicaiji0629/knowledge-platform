## 更新Worker节点已过期的证书
以Root权限登录任意Master节点并执行以下命令，获取集群RootCA私钥。
cat /etc/kubernetes/pki/ca.key
执行以下命令，获取base64编码后集群的根私钥。
若获取的集群RootCA私钥中有一行空行，执行以下命令：
sed '1d' /etc/kubernetes/pki/ca.key| base64 -w 0
若获取的集群RootCA私钥中无空行，执行以下命令：
cat /etc/kubernetes/pki/ca.key | base64 -w 0
以Root权限登录Worker节点并执行如下命令，更新Worker节点的证书。
docker run -it --privileged=true -v /:/alicoud-k8s-host --pid host --net host \ registry.cn-hangzhou.aliyuncs.com/acs/cert-rotate:v1.0.0 /renew/upgrade-k8s.sh --role node --rootkey ${base64CAKey}
说明
${base64CAKey}为[步骤](update-expired-certificates-of-a-kubernetes-cluster.md)[2](update-expired-certificates-of-a-kubernetes-cluster.md)获取的通过base64编码后的集群根私钥。
在集群的每个Worker节点重复此步骤，完成所有Worker节点的证书更新。
该文章对您有帮助吗？
反馈
