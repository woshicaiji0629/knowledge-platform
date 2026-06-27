## NetworkPolicy支持
Terway独占ENI节点池不支持NetworkPolicy。
Terway共享ENI节点池支持Kubernetes原生的NetworkPolicy功能，它通过用户定义的规则来控制Pod之间的网络流量。
在创建集群时，如果网络插件选择Terway后，勾选NetworkPolicy 支持选项，即可使集群支持NetworkPolicy。详细信息，请参见[在](use-network-policies.md)[ACK](use-network-policies.md)[集群使用网络策略](use-network-policies.md)。
说明
通过控制台管理NetworkPolicy的功能正在公测中，如果您希望使用，请在[配额平台](https://quotas.console.aliyun.com/white-list-products/csk/quotas)提交申请。
