## 获取edgeadm运维工具
执行以下命令获取离线运维工具：
export REGION="" INTERCONNECT_MODE="" CLUSTER_VERSION=""; export ARCH=$(uname -m | awk '{print ($1 == "x86_64") ? "amd64" : (($1 == "aarch64") ? "arm64" : "amd64")}') INTERNAL=$( [ "$INTERCONNECT_MODE" = "private" ] && echo "-internal" || echo "" ); wget http://aliacs-k8s-${REGION}.oss-${REGION}${INTERNAL}.aliyuncs.com/public/pkg/run/attach/${CLUSTER_VERSION}/${ARCH}/edgeadm -O edgeadm; chmod u+x edgeadm;
参数说明如下：

| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| CLUSTER_VERSION | ACK Edge 集群 发布的版本和具体版本号，请参见 [版本发布说明](release-notes-for-kubernetes-versions-supported-by-ack-edge.md) 。 | 1.26.3-aliyun.1 |
| REGION | ACK Edge 集群 支持的地域及其 Region ID，请参见 [开服地域](../../product-overview/supported-regions.md) 。 | cn-hangzhou |
| INTERCONNECT_MODE | 指定节点接入的网络类型。 basic：公网接入。 private：专线接入。 | basic |
