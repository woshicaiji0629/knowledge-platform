### Knative介绍
[Knative](https://knative.dev/docs/)是一款基于Kubernetes集群的Serverless框架，提供云原生、跨平台的Serverless编排标准。Knative通过整合容器构建、工作负载管理以及事件模型来实现这一Serverless标准。优势如下。
更聚焦于业务逻辑：Knative通过简单的应用配置、自动扩缩容等手段让开发者聚焦于业务逻辑，降低运维负担、减少对底层资源的关注。
标准化：将业务代码部署到Serverless平台时，需要考虑源码的编译、部署和事件的管理。目前社区和云厂商提供的Serverless解决方案和FaaS方案标准不一。Knative提供了一个标准、通用的Serverless框架。
例如，如需在Knative中实现事件驱动，您可以编写对应的YAML文件（CR）并在集群中部署，无需与云产品做深度绑定，便于跨平台迁移。
使用门槛低：Knative支持将代码自动打包为容器镜像并发布为服务，也支持将函数快捷地部署到Kubernetes集群中，以容器的方式运行。
自动弹性及版本管理：Knative支持在没有流量时自动将实例数量缩容至零，从而节省资源，还提供版本管理、灰度发布等功能。
事件驱动：Knative提供了完整的事件模型，便于接入外部系统的事件，并将事件路由到适当的服务或函数进行处理。
关于Knative应用模型（Knative Service）的介绍，请参见[Knative](introduction-to-the-knative-service-model.md)[应用模型介绍](introduction-to-the-knative-service-model.md)。
