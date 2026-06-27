## 注意事项
如果您使用的是Flannel网络插件，则ALB Ingress后端Service服务仅支持NodePort和LoadBalancer类型。
AlbConfig、Namespace、Ingress和Service这些资源的名称不能以aliyun开头。
低版本Nginx Ingress Controller无法识别Ingress资源中的spec：ingressClassName字段。如果集群中同时存在Nginx Ingress和ALB Ingress，会存在ALB Ingress被低版本Nginx Ingress Controller调谐的风险。因此，请及时升级Nginx Ingress Controller版本，或通过Annotation注解项指定ALB Ingress对应的ingressClass。具体操作，请参见[升级](../../ack-managed-and-ack-dedicated/user-guide/update-the-nginx-ingress-controller.md)[Nginx Ingress Controller](../../ack-managed-and-ack-dedicated/user-guide/update-the-nginx-ingress-controller.md)[组件](../../ack-managed-and-ack-dedicated/user-guide/update-the-nginx-ingress-controller.md)或[ALB Ingress](advanced-alb-ingress-settings.md)[服务高级用法](advanced-alb-ingress-settings.md)。
