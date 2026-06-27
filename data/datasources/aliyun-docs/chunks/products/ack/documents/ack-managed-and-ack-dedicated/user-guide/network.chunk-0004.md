## 服务（Service）
由于云原生应用通常需要敏捷的迭代和快速的弹性，Pod在Kubernetes中被认为是临时性的、随时可替换的资源。当Pod被销毁、替换时，与其相关的网络资源也会发生变化，因此需要为Pod提供固定的访问方式。Kubernetes采用Service方式为一组拥有相同功能的容器提供固定的访问入口，并对这一组容器进行负载均衡。实现原理如下：
通过Selector关联一组容器，以将这个Service的IP地址和端口负载均衡到这一组容器IP和端口上。
在Pod发生变化时，Service会自动更新后端的转发规则，以保证通过Service能访问到最新的Pod。
ACK集群中的Service目前支持ClusterIP、NodePort、LoadBalancer、Headless Service、ExternalName模式，适用于集群内访问、集群外访问、公网访问等场景，详细信息请参见[Service](service-management.md)[管理](service-management.md)。
