## 通过Label自定义网关节点
Raven组件会通过在网关节点之间构建通道实现跨域通信的目的，默认会在节点池中随机选择一些网关节点，建议您指定一些固定的节点作为网关节点用于构建稳定运维通道，您可以使用以下命令选择：
kubectl label node node-xxx raven.openyurt.io/gateway-node=true
