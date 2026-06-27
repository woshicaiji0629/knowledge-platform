## 不含Docker运行时迁移的升级
在待升级边缘节点池下的所有边缘节点上，依次执行如下命令，完成所有边缘节点的升级。
export REGION="" INTERCONNECT_MODE="" TARGET_CLUSTER_VERSION=""; export ARCH=$(uname -m | awk '{print ($1 == "x86_64") ? "amd64" : (($1 == "aarch64") ? "arm64" : "amd64")}') INTERNAL=$( [ "$INTERCONNECT_MODE" = "private" ] && echo "-internal" || echo "" ); wget http://aliacs-k8s-${REGION}.oss-${REGION}${INTERNAL}.aliyuncs.com/public/pkg/run/attach/${TARGET_CLUSTER_VERSION}/${ARCH}/edgeadm -O edgeadm; chmod u+x edgeadm;./edgeadm upgrade --interconnect-mode=${INTERCONNECT_MODE} --region=${REGION}
参数说明如下：

| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| TARGET_CLUSTER_VERSION | 指定要升级到的目标集群版本。 说明 升级的目标集群版本就是控制面升级完成后的版本。 | 1.24.6-aliyunedge.1 ACK Edge 集群 发布的版本和具体版本号，请参见 [版本发布说明](release-notes-for-kubernetes-versions-supported-by-ack-edge.md) 。 |
| REGION | 指定集群所在地域的 Region ID。 | cn-hangzhou ACK Edge 集群 支持的地域及其 Region ID，请参见 [开服地域](../../product-overview/supported-regions.md) 。 |
| INTERCONNECT_MODE | 指定节点接入的网络类型。 basic：公网接入。 private：专线接入。 | basic |

返回如下执行结果，则说明当前边缘节点升级成功。
