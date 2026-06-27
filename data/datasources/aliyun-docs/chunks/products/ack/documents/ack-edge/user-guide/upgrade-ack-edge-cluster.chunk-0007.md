ch/${TARGET_CLUSTER_VERSION}/${ARCH}/edgeadm -O edgeadm; chmod u+x edgeadm;./edgeadm upgrade --interconnect-mode=${INTERCONNECT_MODE} --region=${REGION}
参数说明如下：

| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| TARGET_CLUSTER_VERSION | 指定要升级到的目标集群版本。 说明 升级的目标集群版本就是控制面升级完成后的版本。 | 1.24.6-aliyunedge.1 ACK Edge 集群 发布的版本和具体版本号，请参见 [版本发布说明](release-notes-for-kubernetes-versions-supported-by-ack-edge.md) 。 |
| REGION | 指定集群所在地域的 Region ID。 | cn-hangzhou ACK Edge 集群 支持的地域及其 Region ID，请参见 [开服地域](../../product-overview/supported-regions.md) 。 |
| INTERCONNECT_MODE | 指定节点接入的网络类型。 basic：公网接入。 private：专线接入。 | basic |

返回如下执行结果，则说明当前边缘节点升级成功。
