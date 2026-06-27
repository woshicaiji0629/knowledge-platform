# 在Kubernetes中实现HTTPS安全访问
容器服务ACK集群支持多种应用访问的形式，最常见的形式如<SLB-Instance-IP>:<Port>、<NodeIP>:<NodePort>和域名访问等。ACK集群默认不支持HTTPS访问，如果您希望能够通过HTTPS进行应用的访问，容器服务ACK和阿里云负载均衡服务为您提供安全的HTTPS访问。本文通过实际案例演示的HTTPS访问配置，帮助您在容器服务ACK中配置自己的证书。
