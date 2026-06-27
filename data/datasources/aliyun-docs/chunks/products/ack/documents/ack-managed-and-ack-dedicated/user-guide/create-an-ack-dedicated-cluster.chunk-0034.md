关于三者的详细对比，请参见[Ingress](ingress-management-2.md)[管理](ingress-management-2.md)。
服务发现
安装[NodeLocal DNSCache](configure-nodelocal-dnscache.md)，在节点上缓存DNS解析结果，以提升域名解析性能和稳定性，加速集群内部的服务间调用。
存储插件
基于[CSI](csi-overview-1.md)[存储插件](csi-overview-1.md)实现数据的持久化存储，可使用阿里云云盘、NAS、OSS、CPFS等存储卷资源。
选择默认创建[NAS](https://help.aliyun.com/zh/nas/product-overview/what-is-nas)和CNFS后，ACK会默认创建通用型NAS文件系统并使用[容器网络文件系统](cnfs-overview.md)[CNFS](cnfs-overview.md)进行管理。
如需后续创建CNFS，详见[通过](use-cnfs-to-manage-nas-file-systems.md)[CNFS](use-cnfs-to-manage-nas-file-systems.md)[管理](use-cnfs-to-manage-nas-file-systems.md)[NAS](use-cnfs-to-manage-nas-file-systems.md)[文件系统](use-cnfs-to-manage-nas-file-systems.md)。
云资源及计费说明：[NAS](https://help.aliyun.com/zh/nas/product-overview/overview-1)
容器监控
您可以使用阿里云Prometheus查看集群预先配置的监控大盘和监控性能指标。更多信息，请参见[阿里云](../../serverless-kubernetes/user-guide/enable-prometheus-service.md)[Prometheus](../../serverless-kubernetes/user-guide/enable-prometheus-service.md)[监控](../../serverless-kubernetes/user-guide/enable-prometheus-service.md)。
日志服务
使用已有SLS Project或新建一个SLS Project，用于收集集群应用日志。
同时将启用集群API Server审计功能，收集对Kubernetes API的请求以及请求结果。
如需后续启用，请参见[采集](collect-text-logs-from-ack-clusters-using-daemonset-de
