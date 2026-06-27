### 管理多个地域分散的应用
在如下场景中，当有大量分散在不同地域的ECS需要统一管理或者部署相同的业务时，您可以创建一个ACK Edge集群来统一接入不同地域的ECS。具体操作，请参见下文[示例一：使用](manage-ecs-resources-in-multiple-regions.md)[ACK Edge](manage-ecs-resources-in-multiple-regions.md)[集群管理地域分散的应用](manage-ecs-resources-in-multiple-regions.md)。
安全防护场景
在分布式计算环境中，为防止系统被恶意攻击、数据泄露等问题，通常需要在分布式资源上部署网络安全的Agent来为系统提供安全保障，您可以使用ACK Edge集群完成安全Agent的统一部署和运维。
分布式压测、拨测场景
在大规模的业务压测场景中，压测工具从各个地域同时发起压测任务。因此，压测工具需要部署在地域分散的资源中，您可以使用ACK Edge集群来纳管这些资源，快速地向不同地域部署压测工具。
缓存加速场景
分布式缓存加速服务需要在各个地域部署缓存服务，以加速网络内容的传输速度，您可以使用ACK Edge集群实现对分布式缓存服务的统一部署和运维。
