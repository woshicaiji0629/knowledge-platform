## 含Docker运行时迁移的升级
升级ACK Edge集群至1.24版本，若其中包含使用Docker运行时的节点时，您需要将容器运行时从Docker迁移到containerd，因为1.24版本的Kubernetes已经不支持Docker运行时。您可以通过以下任一方式完成升级操作。
（推荐）新建containerd节点池轮转迁移：新建一个节点池，运行时选择containerd，扩容节点。通过设置老节点池禁止调度或者更新应用负载指定节点池调度的方式（例如Label），逐步将应用全部迁移至新的节点池，再将旧节点池进行下线处理。关于如何创建节点池，请参见[边缘节点池管理](edge-node-pool-management.md)；关于如何将节点设置为不可调度，请参见[节点排水和调度状态](../../ack-managed-and-ack-dedicated/user-guide/overview-of-node-management.md)。
原地升级：直接将节点上的运行时从containerd切换到Docker，在升级前也要进行节点排水，另外升级会导致节点上所有容器重启。
节点排水。
在待升级边缘节点池下的所有边缘节点上，依次执行如下命令，完成所有边缘节点的升级。
export REGION="" INTERCONNECT_MODE="" TARGET_CLUSTER_VERSION=""; export ARCH=$(uname -m | awk '{print ($1 == "x86_64") ? "amd64" : (($1 == "aarch64") ? "arm64" : "amd64")}') INTERNAL=$( [ "$INTERCONNECT_MODE" = "private" ] && echo "-internal" || echo "" ); wget http://aliacs-k8s-${REGION}.oss-${REGION}${INTERNAL}.aliyuncs.com/public/pkg/run/attach/${TARGET_CLUSTER_VERSION}/${ARCH}/edgeadm -O edgeadm; chmod u+x edgeadm;./edgeadm upgrade --interconnect-mode=${INTERCONNECT_MODE} --region=${REGION}
参数说明如下：
