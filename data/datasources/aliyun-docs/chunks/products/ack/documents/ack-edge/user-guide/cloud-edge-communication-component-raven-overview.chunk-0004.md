## 组件架构
Raven组件包含控制面组件ack-edge-yurt-manager和数据面组件raven-agent-ds。Raven组件需要一个自定义集群资源Gateway来记录节点信息和配置信息，详情请参见[使用跨域运维通信组件](using-the-cloud-side-communication-raven-component.md)[Raven](using-the-cloud-side-communication-raven-component.md)。
ack-edge-yurt-manager组件会在节点池维度划分网络域并且创建Gateway资源。
raven-agent-ds组件会以DaemonSet的方式部署在集群的每一个节点上，它负责代理构建网关节点间的隧道以及路由配置等。
Raven组件支持两种云边通信模式。
代理模式：构建反向代理通道，实现跨域主机网络通信，网关节点代理跨域的NodeName+Port的七层网络请求。
隧道模式：构建VPN隧道，实现跨域容器网络通信，网关节点转发跨网络域的容器网络链路。
