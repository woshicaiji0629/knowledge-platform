## 安全策略组件对比
ACK提供两种安全策略组件形态：托管版与非托管版。集群在同一时间只能启用其中一种。两者详细对比如下。

| 差异项 | 托管版 | 非托管版 |
| --- | --- | --- |
| 部署模式 | 控制面托管：部署在集群控制面，由 ACK 全面托管 | 数据面部署：通过工作负载的形式部署在集群中，默认安装在 kube-system 命名空间下，会占用 Worker 节点的 Pod 资源 |
| 适用集群 | 1.30 及以上版本的 [Auto Mode](../user-guide/auto-mode-overview.md) [集群](../user-guide/auto-mode-overview.md) | 1.16 及以上版本的 ACK 托管集群 、 ACK 专有集群 |
| 启用参数配置 | 组件的启动参数由系统默认配置，不支持自定义 | 可自定义修改组件的启动参数 |
| 核心组件安装 | managed-gatekeeper managed-policy-template-controller 在 控制台的 组件管理 页面，托管版组件卡片将显示托管 。 | gatekeeper policy-template-controller 日志采集组件（logtail-ds 或 loongcollector） |
| 策略日志采集 | 通过 [采集](../user-guide/collect-control-plane-component-logs-of-ack-managed-cluster.md) [ACK](../user-guide/collect-control-plane-component-logs-of-ack-managed-cluster.md) [托管集群控制面组件日志](../user-guide/collect-control-plane-component-logs-of-ack-managed-cluster.md) 发送到指定的 SLS Project 中 | 通过在集群中安装日志采集组件以采集日志，并发送至指定的 SLS Project 中 |
| 策略规则库 | [容器安全策略规则库说明](predefined-security-policies-of-ack.md) 中的所有策略 | [容器安全策略规则库说明](predefined-security-policies-of-ack.md) 中的所有策略 云安全中心提供的 [容器主动防御](https://help.aliyun.com/zh/security-center/user-guide/use-the-feature-of-proactive-defense-for-containers#section-i5h-11v-pag) |
