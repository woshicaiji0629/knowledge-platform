## 前提条件
已[创建](create-an-ack-edge-cluster-1.md)[ACK Edge](create-an-ack-edge-cluster-1.md)[集群](create-an-ack-edge-cluster-1.md)，且版本为1.18.8-aliyunedge.1及以上。
确保ACK Edge集群已安装的ack-arms-prometheus版本为1.1.4及以上，如不满足，请及时[升级](monitor-ack-edge-clusters-with-managed-service-for-prometheus.md)[ack-arms-prometheus](monitor-ack-edge-clusters-with-managed-service-for-prometheus.md)[版本](monitor-ack-edge-clusters-with-managed-service-for-prometheus.md)。
如果集群版本小于1.26，需要检查确保集群kube-system/edge-tunnel-server-cfg的ConfigMap中，已经对Node Exporter的端口9100、GPU Exporter的端口9445开启了转发配置，具体配置信息如下：
http-proxy-ports: 9445 https-proxy-ports: 9100
