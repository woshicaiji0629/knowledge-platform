## 为Pod配置固定IP、独立虚拟交换机与安全组
Terway独占ENI节点池默认支持为每个Pod配置固定IP、独立的虚拟交换机及安全组，能提供精细化流量管理、流量隔离、网络策略配置和IP管理能力。
Trunk ENI是Terway共享ENI节点池的一种选项。开启Trunk ENI后，可以为每个Pod配置固定IP、独立的虚拟交换机、安全组。
在创建集群时，网络插件选择Terway后，勾选Trunk ENI 支持选项。详细信息，请参见[为](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)[Pod](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)[配置固定](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)[IP](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)[及独立虚拟交换机、安全组](configure-a-static-ip-address-a-separate-vswitch-and-a-separate-security-group-for-each-pod.md)。
说明
ACK托管集群无需申请即可选择Trunk ENI选项。如果您希望在ACK专有集群中开启Trunk ENI，请先在[配额平台](https://quotas.console.aliyun.com/white-list-products/csk/quotas)提交申请。
从Kubernetes 1.31开始，新建的ACK托管集群会自动启用Trunk ENI功能，无需手动进行选择。
开启Trunk ENI模式后，会安装terway-eniip与terway-controlplane组件。
