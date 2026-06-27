### 资源编排ROS
资源编排服务ROS（Resource Orchestration Service）是阿里云提供的一项简化云计算资源管理的服务。开发者和管理员可以编写模板，在模板中定义所需的阿里云资源（例如：ECS 实例、RDS 数据库实例）、资源间的依赖关系等。ROS 的编排引擎将根据模板自动完成所有资源的创建和配置，实现自动化部署及运维。更多详情，请参见[什么是资源编排服务](https://help.aliyun.com/zh/ros/product-overview/what-is-ros)。
快速使用资源编排ROS编排CDN，请参见[资源编排](resource-orchestration-ros-integration-example.md)[ROS](resource-orchestration-ros-integration-example.md)[集成示例](resource-orchestration-ros-integration-example.md)。
支持使用资源编排服务ROS调用CDN。编排的部分资源包括普通资源和数据资源。
普通资源：
[ALIYUN::CDN::Domain](https://help.aliyun.com/zh/ros/developer-reference/aliyun-cdn-domain)：用于添加加速域名。
[ALIYUN::CDN::DomainConfig](https://help.aliyun.com/zh/ros/developer-reference/aliyun-cdn-domainconfig)：用于批量配置域名。
数据资源：
[DATASOURCE::CDN::Domains](https://help.aliyun.com/zh/ros/developer-reference/datasource-cdn-domains)：用于查询已创建加速域名的基础信息。
