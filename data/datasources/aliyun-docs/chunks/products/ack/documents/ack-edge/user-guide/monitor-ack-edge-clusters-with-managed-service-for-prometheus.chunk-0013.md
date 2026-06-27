### ACK Edge集群如何实现监控数据的获取？
在边缘计算场景中，边缘节点处在相对封闭的线下IDC环境中，云上VPC和边缘侧处于不同的网络平面内。部署在云上的Prometheus Agent无法直接通过Endpoint访问到边缘侧的Node Exporter、GPU Exporter，从而获取相应的监控指标。从ack-arms-prometheus 1.1.4版本开始，借助ACK Edge集群内置的[云边运维通信组件](cloud-edge-tunneling.md)[Tunnel](cloud-edge-tunneling.md)，ack-arms-prometheus可以自动打通云边之间的监控数据采集链路。
