## 步骤一：为集群开启节点自动伸缩功能
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，单击节点伸缩后方的去配置。
首次使用节点自动伸缩功能时，按照页面提示，开通ESS服务并完成授权（如已开通并授权，请跳过）。
ACK托管集群：完成[AliyunCSManagedAutoScalerRole](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22CS%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCSManagedAutoScalerRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedAutoScalerRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fcs.console.aliyun.com%2F%22%7D)[角色授权](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22CS%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCSManagedAutoScalerRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedAutoScalerRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fcs.console.aliyun.com%2F%22%7D)。
ACK专有集群：完成KubernetesWorkerRole角色授权和AliyunCSManagedAutoScalerRolePolicy系统策略的授权。
在节点伸缩配置弹窗中，前置检查通过后，单击提示区域中的 RAM 角色链接（如KubernetesWorkerRole-xxxx）即可跳转到访问控制完成授权。
在节点伸缩配置页面，选择节点伸缩方案为自动伸缩，配置伸缩的配置项，然后单击确定。
节点伸缩方案选择后支持切换。如需切换，您可以在此处变更为[节点即时弹性](instant-elasticity.md)，仔细阅读页面提示并按照页面指引完成操作。
