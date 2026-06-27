# 使用ALB实现gRPC协议的负载均衡
gRPC是一种高性能、开源的远程过程调用框架，当您使用gRPC进行后端服务通信时，您可使用应用型负载均衡ALB（Application Load Balancer）实现gRPC协议的负载均衡，统一流量入口。gRPC基于HTTP/2协议进行通信，目前ALB仅支持前端加密（通过HTTPS监听）和后端明文（服务器组后端协议为gRPC）的形态。
