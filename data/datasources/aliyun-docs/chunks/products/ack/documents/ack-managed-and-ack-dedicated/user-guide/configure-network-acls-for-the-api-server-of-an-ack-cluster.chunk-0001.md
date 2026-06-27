## 操作步骤
您可以针对不同的监听设置访问白名单或黑名单，只允许特定IP访问或限制某些特定IP访问。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。
在集群信息页面，单击基本信息页签，然后在网络区域，找到并单击内网端点右侧的设置访问控制。仔细阅读访问控制策略的放行提示后，单击确定。
在负载均衡控制台跳转的面板中，打开启用访问控制开关，选择访问控制方式和访问控制策略组之后，单击确定。
在此开启访问控制之前，您需要首先[访问控制](../../../../slb/documents/classic-load-balancer/user-guide/access-control.md)，并[访问控制](../../../../slb/documents/classic-load-balancer/user-guide/access-control.md)。更多CLB访问控制信息，请参见[访问控制](../../../../slb/documents/classic-load-balancer/user-guide/access-control.md)。
重要
配置访问控制策略时，除了确保用户侧指定的IP地址能够正常访问API Server外，集群控制面组件和控制台相关的IP地址段也要能够正常访问API Server。因此，请务必在访问控制策略的白名单中添加放行以下网段，切勿将其加入黑名单，以免影响集群功能和管理操作的正常运行。
容器服务 Kubernetes 版管控的网段100.104.0.0/16。
集群专有网络VPC的主网段及附加网段（如有），或集群节点所在的交换机vSwitch网段。
用户侧需访问API Server连接端点的客户端出口网段。
除放行以上网段之外，ACK Edge集群还需要放行边缘节点出口网段。
除放行以上网段之外，ACK灵骏集群还需要放行灵骏VPD网段。
该文章对您有帮助吗？
反馈
