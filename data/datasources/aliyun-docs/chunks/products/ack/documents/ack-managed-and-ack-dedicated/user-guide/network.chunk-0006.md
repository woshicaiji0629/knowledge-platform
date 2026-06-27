## 服务发现DNS
ACK使用DNS来实现应用的服务发现能力，例如客户端应用可以通过Service的服务名解析出它的ClusterIP访问，再通过Service访问后端Pod。采用DNS服务发现的能力让集群中应用间的调用与IP地址和部署环境解耦。关于集群DNS组件的详细信息，请参见[服务发现](service-discovery-dns-1.md)[DNS](service-discovery-dns-1.md)。
