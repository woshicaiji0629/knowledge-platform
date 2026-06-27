## 部署建议
您可以从以下维度考虑如何启动并使用云服务器ECS：
地域和可用区
地域指阿里云数据中心的地理区域，地域和可用区决定了ECS实例所在的物理位置。一旦成功创建实例后，其元数据（仅[专有网络](https://www.aliyun.com/getting-started/what-is/what-is-vpc)[VPC](https://www.aliyun.com/getting-started/what-is/what-is-vpc)类型ECS实例支持获取元数据）将确定下来，并无法更换地域。您可以根据用户地理位置、阿里云产品发布情况、应用可用性以及是否需要内网通信等因素选择地域和可用区。例如，如果您需要通过阿里云内网使用[云数据库](https://www.aliyun.com/getting-started/what-is/what-is-cloud-database)RDS，RDS实例和ECS实例必须处于同一地域中。更多详情，请参见[地域和可用区](https://help.aliyun.com/zh/document_detail/40654.html#concept-2459516)。
高可用性
为保证业务处理的正确性和服务不中断，建议您通过快照实现[数据备份](https://www.aliyun.com/getting-started/what-is/what-is-data-backup)，通过跨可用区、部署集、[负载均衡](https://www.aliyun.com/getting-started/what-is/what-is-load-balance)（Server Load Balancer）等实现应用容灾。
网络规划
阿里云推荐您使用专有网络VPC，可自行规划私网IP，全面支持新功能和新型实例规格。此外，专有网络VPC支持多业务系统隔离和多地域部署系统的使用场景。更多详情，请参见[专有网络（Virtual Private Cloud）](../../../vpc/documents/what-is-vpc.md)。
安全方案
您可以免费使用云服务器ECS的安全组，控制ECS实例的出入网访问策略以及端口监听状态。更多信息，请参见[安全组概述](overview-44.md)。
对于部署在云服务器ECS上的应用，阿里云为您提供了免费的DDoS基础防护和基础安全服务。更多信息，请参见[DDoS](anti-ddos-origin-basic.md)[基础防护](anti-ddos-origin-basic.md)和[基础安全服务](basic-security-services.md)。
DDoS基础防护默认开启无需购买，为您提供不超过5 Gbps的DDoS基础防护能力。如果您需要更高的防护能力来确保云服务器ECS业务的安全
