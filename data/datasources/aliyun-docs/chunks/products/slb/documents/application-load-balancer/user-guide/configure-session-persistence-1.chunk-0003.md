## 前提条件
您已经创建了一个处于运行中状态的公网ALB实例。具体操作，请参见[创建和管理](create-and-manage-alb-instances.md)[ALB](create-and-manage-alb-instances.md)[实例](create-and-manage-alb-instances.md)。
您已经创建了服务器类型或IP类型的服务器组。具体操作，请参见[创建/删除服务器组](create-and-manage-a-server-group.md)。
您已经创建了后端服务器ECS01和ECS02，用于接收请求。ECS01和ECS02中部署了不同的后端服务，访问时需要有不同展示，例如访问ECS01时返回"Hello World ! This is ECS01."，返回ECS02时返回"Hello World ! This is ECS02."。注意安全组需要对相应服务端口放行。
您已将后端服务器ECS01与ECS02添加到服务器组中。具体操作，请参见[添加/移除后端服务器](create-and-manage-a-server-group.md)。
您已经为该实例配置了监听。具体操作，请参见[添加](../../add-an-http-listener.md)[HTTP](../../add-an-http-listener.md)[监听](../../add-an-http-listener.md)、[添加](add-an-https-listener.md)[HTTPS](add-an-https-listener.md)[监听](add-an-https-listener.md)或[添加](add-a-quic-listener.md)[QUIC](add-a-quic-listener.md)[监听](add-a-quic-listener.md)。
