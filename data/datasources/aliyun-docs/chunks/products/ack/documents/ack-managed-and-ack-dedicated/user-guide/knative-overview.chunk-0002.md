### 核心组件
Knative包括以下核心组件，分别执行不同的功能。
Knative Serving：管理Serverless工作负载，提供了应用部署、多版本管理、基于请求的自动弹性、灰度发布等能力，而且在没有业务流量时可以将应用实例缩容至零。
Knative Eventing：提供了事件源的接入、事件注册和订阅、以及事件过滤等一整套事件管理的能力。事件模型可以有效地解耦生产者和消费者的依赖关系。
Knative Functions: 提供了一个简单的方式来创建、构建和部署Knative服务。您无需深入了解底层技术栈（例如Kubernetes、容器、Knative），通过使用Knative Functions，即可将无状态、事件驱动的函数作为Knative服务部署到Kubernetes集群中。
