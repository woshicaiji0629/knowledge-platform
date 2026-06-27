## API
调用[CreateLoadBalancer](../developer-reference/api-alb-2020-06-16-createloadbalancer.md)创建应用型负载均衡实例。
后续操作
[创建服务器组](create-and-manage-a-server-group.md)：创建一组ALB实例转发请求的目标服务器。
添加监听：为ALB实例添加接收请求的入口，支持创建[HTTP](../../add-an-http-listener.md)、[HTTPS](add-an-https-listener.md)、[QUIC](add-a-quic-listener.md)监听。
[添加](configure-cname-resolution-for-alb.md)[CNAME](configure-cname-resolution-for-alb.md)[解析](configure-cname-resolution-for-alb.md)：[负载均衡域名已升级](../../product-overview/alb-and-nlb-domain-name-upgrade-announcement.md)，新建ALB实例不支持直接使用DNS名称访问。请使用自有域名，将其以CNAME形式解析到实例的DNS名称进行访问。
