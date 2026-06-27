## 更新Master节点已过期的证书
以Root权限登录Master节点并执行以下命令，更新Master节点的证书。
docker run -it --privileged=true -v /:/alicoud-k8s-host --pid host --net host \ registry.cn-hangzhou.aliyuncs.com/acs/cert-rotate:v1.0.0 /renew/upgrade-k8s.sh --role master
说明
需在集群的每个Master节点，重复上述步骤，完成所有Master节点的证书更新。
