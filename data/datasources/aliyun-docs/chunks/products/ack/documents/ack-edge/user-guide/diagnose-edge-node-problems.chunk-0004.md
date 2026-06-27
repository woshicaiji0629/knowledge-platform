## 如何处理边缘节点升级失败的问题？
[升级边缘节点池](upgrade-ack-edge-cluster.md)时，若未返回升级成功结果This node has been upgraded successfully，请参考以下内容排查处理。

| 升级失败信息 | 可能原因 | 处理建议 |
| --- | --- | --- |
| edgeadm version xxxx does not match cluster version | 升级工具版本与集群版本不匹配。 | 检查集群控制面是否已经完成升级。 检查 TARGET_CLUSTER_VERSION 参数是否填写正确。 |
| node has already been upgraded to xxx | 节点已经是升级后的目标版本。 | 如果确认节点上还有组件没有完成升级，请保留日志并 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |
| kubelet target version xxxx does not match cluster version xxxx | 指定的 kubelet 升级的版本与集群控制面版本不匹配。 | 如果指定了 kubelet-version 参数，请检查该参数是否填写正确（与集群控制面版本一致）。 如果没有指定该参数，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |
| Parameter currentVersion cann't null | 使用了老版本的 edgeadm。 | 请检查 edgeadm 版本是否为最新版本。 当前支持的集群升级范围为 1.18 升级到 1.20 版本、1.20 升级到 1.22 版本。 |
| upgrade kubelet failed at phase install, recover to previous state. error run phase upgrade: xxxx | 升级失败，且已自动回滚到之前的状态，节点状态不受影响。 | 请保留日志并 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |
| upgrade kubelet failed at phase install, recover to previous state recover kubelet failed, err: xxx error run phase upgrade: xxxx | 升级失败，且自动回滚失败，节点状态会受到影响。 | 请保留日志并 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 处理。 |
