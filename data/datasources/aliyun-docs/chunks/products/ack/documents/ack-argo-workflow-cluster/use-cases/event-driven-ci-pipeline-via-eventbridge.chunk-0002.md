## 工作原理
基于事件驱动的自动化CI Pipeline，包含2部分：
基于Git事件的触发，代码提交到Git仓库时，触发相应的事件。
CI系统运行构建前的测试，构建Docker镜像，并推送至镜像仓库。
镜像构建成功后，可使用CD系统（如[ACK One GitOps](../../distributed-cloud-container-platform-for-kubernetes/user-guide/gitops-overview.md)）将新的Image Tag同步到Kubernetes集群中。
在本实践中，事件驱动方案采用了在可用性、易用性、安全性、可扩展性等多方面具有[优势](https://help.aliyun.com/zh/eventbridge/product-overview/benefits#section-hf0-60r-chs)的[事件总线](https://help.aliyun.com/zh/eventbridge/product-overview/what-is-eventbridge)[EventBridge](https://help.aliyun.com/zh/eventbridge/product-overview/what-is-eventbridge)，CI部分基于CNCF毕业项目Argo Workflows来构建。工作流集群全托管Argo Workflows，可提升稳定性和可观测性，提供运维能力，帮助您实现更大规模、具有更快的运行速度和更低成本的CI Pipeline。
用户向Git仓库提交代码。
EventBridge根据配置的规则，捕获Git事件并将其传递给ACK One工作流集群，从而触发CI工作流的执行。
[基于](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[ACK One](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[工作流集群的](../../distributed-cloud-container-platform-for-kubernetes/use-cases/building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)[CI](../../distrib
