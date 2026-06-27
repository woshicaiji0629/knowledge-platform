本较高。
高QPS场景
互联网业务往往具有高QPS的特点，比如预期内的大促活动和突发的热点事件。ALB Ingress支持自动弹性，高QPS时会自动弹出更多VIP，通过一个ALB实例即可支持百万QPS，因此ALB Ingress拥有比Nginx Ingress更低的延迟。同时Nginx Ingress依赖集群内的资源，在高QPS场景中更可能会遭遇性能瓶颈。
业务存在流量峰谷的场景
对于有波峰波谷的业务，比如电商和游戏，ALB Ingress拥有费用优势。ALB Ingress按量计费，流量波谷期间消耗较少的LCU，产生的费用更低，且因为自动弹性，用户无需关注和应对自身业务流量模型。而使用Nginx Ingress时则需要预留一部分集群资源，在波谷时会产生闲置成本，并且还需要手动设置与预留资源。
同城多活、异地多活容灾场景
对于业务连续性和可靠性有极高要求的行业和应用场景，比如社交网络平台和视频流媒体服务。您可以通过在分布式云容器平台ACK One创建[ALB](../../../../ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/alb-multi-cluster-gateway-overview.md)[多集群网关](../../../../ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/alb-multi-cluster-gateway-overview.md)，使用[ALB Ingress](../../../../ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-north-south-traffic.md)[来管理多集群流量](../../../../ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-north-south-traffic.md)，实现同城多活和异地多活的容灾方案。
