## ALB Ingress基本概念
阿里云容器服务ACK/ACK Serverless等Kubernetes产品，可以使用ALB Ingress，将集群外部流量路由到集群内部的Service，实现七层负载均衡功能。K8s集群中部署了ALB Ingress Controller组件，负责监听API Server中AlbConfig、Ingress、Service等资源的变化，并动态转换为ALB所需的配置。关于ALB Ingress Controller组件的介绍，请参见[ALB Ingress Controller](../../../../ack/documents/product-overview/alb-ingress-controller.md)。
