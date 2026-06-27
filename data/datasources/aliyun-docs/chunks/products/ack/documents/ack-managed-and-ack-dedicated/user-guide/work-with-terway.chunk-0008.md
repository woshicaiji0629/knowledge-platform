### 查看节点支持的最大容器网络Pod数量
方式一：创建节点池时，在实例规格区域，通过Terway兼容性（可支持 Pod 数量）查看某一实例规格支持的Pod数量。
方式二：先参考下列方式获取计算数据，然后手动计算ECS规格支持的Pod数量。
通过[实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md)文档查询ECS实例支持的弹性网卡数量。
通过[OpenAPI](https://next.api.aliyun.com/api/Ecs/2014-05-26/DescribeInstanceTypes?lang=JAVA&params=%7B%22InstanceTypes%22:%5B%22ecs.c1.large%22%5D%7D&tab=DOC)进行查询，通过指定已有节点的实例规格InstanceTypes，单击发起调用，返回值中EniQuantity表示实例规格支持的弹性网卡上限，EniPrivateIpAddressQuantity表示单个弹性网卡支持的私有IP数量。EniTotalQuantity表明实例规格支持的总网卡数量。
