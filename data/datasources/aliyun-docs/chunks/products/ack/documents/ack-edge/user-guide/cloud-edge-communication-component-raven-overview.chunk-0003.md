### 功能说明
创建ACK Edge集群时，您需要选择并且购买至少1台云上ECS节点，将该节点作为云上网关节点。
如果边缘侧主机采用公网方式与云上ACK Edge控制面进行交互，则需要购买一个传统型负载均衡（CLB）实例、访问控制列表（ACL）实例和弹性公网IP（EIP）实例，用于不同节点池的网关节点之间构建加密的网络隧道。
Raven组件提供两种模式跨域通信，代理模式和隧道模式。
代理模式主要支持APIServer、MetricsServer 和 Prometheus等服务的跨域主机网络通信，例如kubectl logs/exec/attach/top等原生命令。
隧道模式仅支持节点间网络互通的节点池，主要提供云边容器网络通信，例如Prometheus的容器Metrics数据监控。
Raven组件支持多地域（多网络域）设备主机IP冲突场景下的网络通信。
