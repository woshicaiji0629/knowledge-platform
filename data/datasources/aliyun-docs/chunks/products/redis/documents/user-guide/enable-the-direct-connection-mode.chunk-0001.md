## 前提条件
重要
本功能公测中，如需使用请填写[表单](https://page.aliyun.com/form/act213201526/index.htm)申请使用。
实例需满足下述条件：
实例架构为集群架构。
部署模式为经典。
说明
云原生集群架构直连模式默认提供直连地址，无需额外开通。
云原生集群架构代理模式不支持开通直连模式。
兼容Redis版本为5.0，且[升级至最新小版本](update-the-minor-version.md)。
实例的TLS（SSL）加密功能需处于关闭状态，详情请参见[TLS](enable-tls-encryption.md)[加密](enable-tls-encryption.md)。
实例所属的交换机需具备充足的可分配的IP地址数，详情请参见[查询实例所属交换机可分配的](obtain-the-number-of-available-ip-addresses-in-the-vswitch-to-which-an-apsaradb-for-redis-instance-is-connected.md)[IP](obtain-the-number-of-available-ip-addresses-in-the-vswitch-to-which-an-apsaradb-for-redis-instance-is-connected.md)[地址数](obtain-the-number-of-available-ip-addresses-in-the-vswitch-to-which-an-apsaradb-for-redis-instance-is-connected.md)。
说明
例如实例的分片数为8，申请直连地址会为每个分片的主节点分配一个IP地址，同时直连地址本身需占用一个IP地址，那么实例所属的交换机中可分配的IP地址须大于等于9。
