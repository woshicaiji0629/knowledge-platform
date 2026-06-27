# 配置API Server的访问控制策略
ACK集群创建时会为API Server自动创建一个私网CLB实例，作为集群API Server的内网连接端点，通过为该私网CLB实例绑定EIP，即可创建公网端点，实现对API Server的公网访问。为避免API Server受到非法访问，您可以对该私网CLB实例的6443端口监听（Listener）配置访问控制规则，即设置访问白名单或者黑名单。
重要
由于公网端点和内网端点共享同一个私网CLB实例，因此对该CLB实例配置的访问控制规则将同时应用于公网端点和内网端点。
负载均衡提供监听级别的访问控制。您可以在创建监听时配置访问控制，也可以在监听创建后修改或重新配置访问控制。更多信息，请参见[访问控制](../../../../slb/documents/classic-load-balancer/user-guide/access-control.md)。
