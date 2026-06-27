## 测试环境

| 测试环境信息 | 说明 |
| --- | --- |
| 地域和可用区域 | 所有测试均在华东 1（杭州）地域的可用区 I 中完成。 |
| Redis 实例架构 | 标准版（双副本）架构，详情请参见 [标准架构](../product-overview/standard-master-replica-instances.md) 。 |
| 部署压测工具的机器 | [云服务器](../../../ecs/documents/user-guide/what-is-ecs.md) [ECS](../../../ecs/documents/user-guide/what-is-ecs.md) 实例，规格为 ecs.g6e.13xlarge，规格详情请参见 [实例规格族](../../../ecs/documents/user-guide/overview-of-instance-families.md) 。 |
| 磁盘（ESSD）型实例规格 | tair.essd.standard.xlarge tair.essd.standard.2xlarge tair.essd.standard.4xlarge tair.essd.standard.8xlarge tair.essd.standard.13xlarge |

测试主要针对下述两种场景进行：
内存大于数据场景：绝大部分数据可以在内存中访问到，此场景下内存与数据的比例约为7:1。
数据大于内存场景：只有部分数据缓存在内存，部分访问请求需要读取硬盘中的数据，根据负载不同，需要访问磁盘的比例也不一样，此场景下内存与数据的比例约为1:4。
