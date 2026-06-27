### 选择后端协议与调度算法

| 后端协议 | 适用场景 |
| --- | --- |
| HTTP（默认） | 大多数 Web 应用场景。适用于 HTTP、HTTPS 和 QUIC 监听。 |
| HTTPS | ALB 到后端服务器之间需要加密通信。适用于 HTTPS 和 HTTP 监听。 |
| gRPC | 后端服务使用 gRPC 协议。需搭配 HTTPS 监听且启用 HTTP2.0。 |
| 调度算法 | 适用场景 |
| --- | --- |
| 加权轮询 | 通用场景。按权重比例均匀分配请求。轮询调度以每次请求为粒度进行分配，而非基于用户。 |
| 加权最小连接数 | 长连接或请求处理时间差异较大的场景。综合权重和实时连接数，优先分配给负载较低的服务器。 |
| 一致性哈希 | 需要请求亲和性的场景（如缓存命中优化）。根据源 IP 或 URL 参数将相同特征的请求固定到同一后端。 |

详细算法逻辑参见[负载均衡调度算法介绍](../../product-overview/introduction-to-load-balancing-scheduling-algorithm.md)。
各监听协议与后端协议、健康检查协议的完整适配关系如下：

| 监听协议 | 支持的后端协议 | 支持的服务器组类型 | 支持的健康检查协议 |
| --- | --- | --- | --- |
| HTTP | HTTP、HTTPS | 服务器类型、IP 类型、函数计算类型 函数计算类型服务器组无需配置后端协议和健康检查协议。 | HTTP、HTTPS、TCP、gRPC 基础版 ALB 实例不支持 HTTPS 健康检查协议。 |
| HTTPS | HTTP、HTTPS、gRPC gRPC 需搭配 HTTPS 监听且启用 HTTP2.0。 基础版 ALB 实例的 HTTPS 监听仅支持 HTTP 和 gRPC 后端协议。 |  |  |
| QUIC | HTTP |  |  |
