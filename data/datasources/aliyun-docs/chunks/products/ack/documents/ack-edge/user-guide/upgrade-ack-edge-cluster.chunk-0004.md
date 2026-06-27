### 步骤一：升级控制面
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择运维管理>集群升级。
在集群升级页面选择可升级的目标版本，然后单击前置检查，提前扫描集群升级可能存在的潜在风险。
检查完成后，您可以在前置检查结果区域查看检查结果。
结果正常时，升级检查成功，请继续进行集群升级操作。
结果提示异常时，不影响当前集群的运行及集群状态。您可以参见推荐的解决方案进行修复。关于典型修复方案，请参见[集群检查项及修复方案](../../ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)。
说明
Kubernetes 1.20及以后版本的集群升级前检查时，会检查当前版本是否使用了废弃API，检查结果不会影响升级流程，仅作为提示信息。详细内容，请参见[废弃](../../ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)[API](../../ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)[说明](../../ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)。
前置检查通过后，单击立即升级，按照页面提示进行控制面的升级。
升级过程中，您可以在页面右上角查看升级历史。
升级完成后，请在集群列表查看集群版本，确认升级是否成功。新扩容节点的版本也将遵循控制面版本。
