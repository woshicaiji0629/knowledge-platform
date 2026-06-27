## 添加/移除后端服务器
添加后端服务器前，请确保服务器上已部署业务应用。
重要
ALB通过特定IP地址与后端服务器通信和健康检查，请确保后端服务器未屏蔽这些地址（包括iptables或安全策略软件）：
[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)使用所在交换机网段的私网地址（Local IP）通信，可在实例详情页查看。
升级前的ALB实例使用内网地址段100.64.0.0/10与后端服务器通信。
请确保后端服务器的配置不会导致转发路径形成[环路](../support/alb-exception-status-code-description.md)。
