## 迁移Batch批处理系统到Argo工作流
评估与规划
评估现有Batch批处理作业，包括依赖关系、资源需求、参数配置等。了解Argo Workflows的特性和最佳实践，并根据本文选择Argo Workflows的功能以替代Batch批处理作业。另外，由于容器Argo工作流集群的ACS能力，您可以跳过规划Compute Environment和管理优先级队列。
创建容器Argo工作流集群
具体操作，请参见[工作流集群快速入门](../../distributed-cloud-container-platform-for-kubernetes/user-guide/workflow-cluster-quickstart.md)。
转换作业定义
根据Batch批量计算到Argo工作流的功能映射，重写Batch批量计算作业为Argo工作流，也可以通过调用Argo工作流[SDK](https://argoproj.github.io/argo-workflows/client-libraries/)，以自动化方式创建工作流，并接入业务系统。
数据存储
确保容器Argo工作流集群可以访问工作流运行所需要的数据，工作流集群可以挂载访问阿里云OSS、NAS、CPFS、云盘等存储资源。更多信息，请参见[使用存储卷](../../distributed-cloud-container-platform-for-kubernetes/user-guide/use-volumes.md)。
测试验证
验证工作流运行正常、数据访问、结果输出正常、资源用量符合预期。
运维：监控和日志
开启容器Argo工作流集群[可观测能力](../../distributed-cloud-container-platform-for-kubernetes/user-guide/observability.md)，查看工作流运行状态和日志。
