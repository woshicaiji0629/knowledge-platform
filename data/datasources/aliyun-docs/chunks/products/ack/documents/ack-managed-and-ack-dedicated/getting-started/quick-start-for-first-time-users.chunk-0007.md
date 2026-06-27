## 3. 快速创建集群
创建ACK托管集群时，您可以选择开启智能托管模式。开启后，您仅需进行简单的规划配置，即可一键创建符合最佳实践的ACK集群。该集群会默认创建一个智能托管节点池，其中的节点生命周期将由ACK进行托管和运维。更多信息，请参见[创建](../user-guide/create-ack-managed-clusters-in-auto-mode.md)[ACK Auto Mode 集群](../user-guide/create-ack-managed-clusters-in-auto-mode.md)。
说明
如果您需要对集群进行详细自定义配置，可参见[创建](../user-guide/create-an-ack-managed-cluster-2.md)[ACK](../user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../user-guide/create-an-ack-managed-cluster-2.md)的完整流程来完成集群创建。
登录[容器服务管理控制台](https://cs.console.aliyun.com)。在集群列表页面，单击创建集群。
在上方选择ACK 托管集群页签，单击开启智能托管，如果您有公网访问集群能力的需求，您可以在个人测试集群勾选使用 EIP 暴露 API server获得该能力，方便您的后续连接和管理集群。然后单击确认配置，检查所选配置后单击创建集群。
快速创建模式下，默认网络插件为Terway（已勾选 Trunk ENI），服务网段为192.168.0.0/16，专有网络自动创建并已勾选为专有网络配置 SNAT，安全组为自动创建企业级安全组。
该文章对您有帮助吗？
反馈
