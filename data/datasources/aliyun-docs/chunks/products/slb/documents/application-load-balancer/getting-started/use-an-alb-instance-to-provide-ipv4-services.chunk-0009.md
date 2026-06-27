## 释放资源
清理ECS、安全组等资源：
删除ECS01实例及其安全组：
登录[云服务器](https://ecs.console.aliyun.com/server)[ECS](https://ecs.console.aliyun.com/server)[实例控制台](https://ecs.console.aliyun.com/server)，顶部选择实例所属地域，单击ECS01实例右侧的，弹出的窗口中选择释放，立即释放实例并确认。
登录[云服务器](https://ecs.console.aliyun.com/securityGroup)[ECS](https://ecs.console.aliyun.com/securityGroup)[安全组控制台](https://ecs.console.aliyun.com/securityGroup)，顶部选择实例所属地域，勾选ECS01自定义安全组并单击删除，删除安全组。
参照上述步骤，删除ECS02实例及对应安全组资源。
删除域名解析记录
删除域名解析记录，具体操作，请参见[删除域名解析记录](https://help.aliyun.com/zh/dns/delete-a-dns-record)。
清理ALB资源：
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。顶部选择实例所属地域，单击实例右侧的，弹出的窗口中选择释放并确认。
移除后端服务器，具体操作，请参见[创建和管理服务器组](../user-guide/create-and-manage-a-server-group.md)。
删除服务器组，具体操作，请参见[创建和管理服务器组](../user-guide/create-and-manage-a-server-group.md)。
清理VPC资源：
登录[专有网络](https://vpc.console.aliyun.com/vpc)[VPC](https://vpc.console.aliyun.com/vpc)[控制台](https://vpc.console.aliyun.com/vpc)，顶部选择实例所属地域。
单击实例右侧删除，系统将校验是否存在未删除的云产品资源或关联资源。如有依赖资源时，您需要完全释放资源后，才可删除专有网络和交换机。
