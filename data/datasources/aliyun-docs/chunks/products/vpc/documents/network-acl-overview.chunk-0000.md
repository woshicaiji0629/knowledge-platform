### 作用范围
网络ACL仅对绑定交换机内的弹性网卡生效。
网络ACL会控制依赖弹性网卡实现网络通信的云资源的流量，例如ECS、ECI、NLB等实例。
由于RDS、CLB等实例不依赖弹性网卡，流量不会被网络ACL控制。RDS实例的访问控制由其[白名单](../../rds/documents/apsaradb-rds-for-mysql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)实现，CLB实例通过[访问控制策略](../../slb/documents/classic-load-balancer/user-guide/access-control.md)实现。网络ACL不会控制绑定了[网卡可见模式](../../eip/documents/associate-an-eip-with-a-secondary-eni-1.md)[EIP](../../eip/documents/associate-an-eip-with-a-secondary-eni-1.md)的辅助弹性网卡的流量。
通过私网连接PrivateLink的方式访问云服务时，流量经过终端节点网卡，会受网络ACL规则管控。
