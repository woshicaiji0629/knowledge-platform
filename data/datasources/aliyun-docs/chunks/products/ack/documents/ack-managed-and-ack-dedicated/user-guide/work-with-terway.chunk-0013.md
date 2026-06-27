### 共享ENI模式与独占ENI模式
为Pod分配IP地址时，Terway有两种模式：共享ENI模式和独占ENI模式。
重要
在Terway v1.11.0及之后的版本中，Terway在单个集群中支持为单个节点池选择共享ENI或独占ENI模式，在创建集群时不再支持勾选。
节点上的主弹性网卡被分配给节点OS，其余弹性网卡会被Terway托管用于配置Pod网络，因此请勿手动配置这些弹性网卡。如果您需要自行管理部分弹性网卡，请参见[为弹性网卡（ENI）配置白名单](configure-a-whitelist-for-an-eni.md)。
