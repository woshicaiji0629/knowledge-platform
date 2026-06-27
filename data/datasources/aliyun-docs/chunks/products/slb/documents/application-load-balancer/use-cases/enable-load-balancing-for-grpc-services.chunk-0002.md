## 场景示例
某公司在华东1（杭州）地域的专有网络VPC（Virtual Private Cloud）内部署了gRPC服务，在VPC中创建了ALB实例和支持gRPC协议的后端服务器组，ALB配置了HTTPS监听并打开HTTP2.0开关，同时后端服务器组配置了gRPC协议的健康检查。
客户端需要通过ALB实例来访问VPC中部署的gRPC服务。
