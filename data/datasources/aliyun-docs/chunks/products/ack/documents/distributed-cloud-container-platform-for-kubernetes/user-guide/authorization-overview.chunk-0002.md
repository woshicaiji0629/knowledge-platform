## 服务角色
服务角色是云服务在特定情况下，为完成功能而获取其他云服务访问权限的RAM角色。
例如，ACK One上创建工作流集群后，需要创建弹性容器ECI实例运行工作流，因此需要拥有创建ECI实例的相应权限。
ACK One提供以下服务角色，具体的策略内容请参见[ACK One](manage-the-service-linked-role-for-ack-one.md)[服务角色策略内容](manage-the-service-linked-role-for-ack-one.md)。

| 角色名称 | 角色权限说明 |
| --- | --- |
| AliyunCSDefaultRole | ACK One 在集群管控操作中使用该角色访问您在 ECS、VPC、SLB、ROS、ESS 等服务中的资源。 必须授予该角色的权限，授权后才能正常使用 ACK One 功能。 |
| AliyunServiceRoleForAdcp | ACK One 在集群管控操作中使用该角色访问您在 ECS、VPC、SLB 等相关云服务中的资源。 必须授予该角色的权限，授权后才能正常使用 ACK One 功能。 |
| AliyunAdcpServerlessKubernetesRole | ACK One 多集群舰队和分布式工作流 Argo 集群需要使用该角色，访问 VPC、ECS、PrivateZone、ECI、SLS 等服务中的资源。 必须授予该角色的权限，授权后才能正常使用 ACK One 功能。 |
| AliyunAdcpManagedMseRole | ACK One 多集群舰队需要使用该角色访问 MSE 等服务中的资源。 该角色权限仅在使用 [多集群网关](manage-multi-cluster-gateways.md) 功能时需要授权，未授权不影响其他功能使用。 |
| AliyunCSManagedKubernetesRole | ACK One 多集群舰队需要使用该角色访问 ACK 服务的资源。 |
| AliyunCSManagedLogRole | ACK One 中日志组件使用此角色来访问您在其他云产品中的资源。 |
| AliyunCSManagedCmsRole | ACK One 中的 CMS 组件使用此角色来访问您在其他云产品中的资源。 |
| AliyunCSManagedArmsRole | ACK One 中的 Arms 插件使用此角色来访问您在其他云产品中的资源。 |
