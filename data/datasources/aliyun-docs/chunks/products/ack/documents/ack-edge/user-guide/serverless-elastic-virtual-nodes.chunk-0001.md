### 虚拟节点是什么
在ACK集群中，节点是运行工作负载的基本单位，提供实际的计算和存储资源。通常，您的ACK集群会有至少一组ECS节点池，创建Pod时，kubelet会将Pod调度到ECS节点上运行。这种架构能很好地应对流量稳定的业务。如果您的业务有不易提前预测的瞬时波峰，尽管ACK支持弹性伸缩，但ECS节点池扩容时，ECS实例的创建和启动本身会有一定的额外耗时。借助虚拟节点，您可以直接调度Pod到[阿里云弹性容器实例](https://cn.aliyun.com/product/eci)[ECI（Elastic Container Instance）](https://cn.aliyun.com/product/eci)上运行，降低节点运维操作负担，同时避免产生闲置节点资源，降低成本。
重要
相较于ECS节点，虚拟节点本身不支持自定义Label、Annotation、Taint。
虚拟节点通过[ack-virtual-node](../../product-overview/ack-virtual-node.md)[组件](../../product-overview/ack-virtual-node.md)封装计算资源，无需管理底层基础设施即可直接部署工作负载，ack-virtual-node会自动将应用Pod调度到ECI上运行。ECI是Serverless容器运行服务，一个ECI实例相当于一个Pod。使用ECI部署容器应用时，您只需要提供打包好的容器镜像，即可运行容器，并仅为容器实际运行消耗的资源付费。
