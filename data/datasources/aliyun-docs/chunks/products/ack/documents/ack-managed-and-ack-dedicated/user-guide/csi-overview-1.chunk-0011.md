## 通过控制台查看节点注释
在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，选择节点管理>节点。
在节点列表的操作列，单击详情，在基本信息页签下查看节点注释。
若存在volumes.kubernetes.io/controller-managed-attach-detach: true，表示存储插件为CSI；若不存在，则为Flexvolume。
