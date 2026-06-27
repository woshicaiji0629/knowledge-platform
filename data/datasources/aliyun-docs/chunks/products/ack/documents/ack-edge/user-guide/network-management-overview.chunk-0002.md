## 云边运维通信组件
ACK Edge集群采用了中心云管理IDC或边缘设备的架构，由于计算设备通常分散在多个地域及不同的网络域中，因此中心云与边缘侧无法直接通信。
为满足中心云对边缘侧运维、监控的需求，可以采用以下两种解决方案：
专线通信：通过专线的方案连接中心云VPC以及边缘侧的IDC或边缘设备，实现云边通过专线进行私网通信。
公网隧道：通过云边运维通信组件Raven在云边之间的公网上构建反向隧道，通过反向隧道实现运维监控流量通信。要求边缘侧IDC或设备具有访问公网的能力。更多详细信息，请参见[跨域运维通信组件](cloud-edge-communication-component-raven-overview.md)[Raven](cloud-edge-communication-component-raven-overview.md)。
