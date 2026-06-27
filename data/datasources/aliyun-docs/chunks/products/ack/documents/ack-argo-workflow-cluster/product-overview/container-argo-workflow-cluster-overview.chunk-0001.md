## 适用场景
容器Argo工作流集群基于[开源](https://argoproj.github.io/argo-workflows/)[Argo Workflows](https://argoproj.github.io/argo-workflows/)[项目](https://argoproj.github.io/argo-workflows/)构建，完全符合开源工作流标准。Argo Workflows（Argo工作流）是一个强大的云原生工作流引擎，是CNCF毕业项目，毕业意味着该项目符合用户采用、安全、广泛度的最高标准。其使用场景主要包括批量数据处理、机器学习Pipeline、基础设施自动化、CI/CD等。在自动驾驶、科学计算、基因计算、金融量化、数字媒体等行业均有非常广泛的实践。
Argo Workflows拥有以下几大特性，使其在批量任务编排领域脱颖而出：
云原生：专为Kubernetes而设计，每个任务都是一个Pod，是Kubernetes上最受欢迎的工作流引擎。
轻量可扩展：轻量化，弹性可扩展，可并行启动数万个任务。
强大的编排能力：复杂DAG流程编排，同时可以集成编排各种类型任务，包括普通Job、Spark、Ray、Tensor Job等。
