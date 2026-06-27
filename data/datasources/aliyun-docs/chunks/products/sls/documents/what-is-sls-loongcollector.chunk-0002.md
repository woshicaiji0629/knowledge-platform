### 端上采集融合
LoongCollector支持所有的采集工作只用一个Agent实现，包括Logs、Metrics、Traces、Events、Profiles 的采集、处理、路由、发送等功能。且对于K8s，LoongCollector 基于标准 CRI API 与 Pod 的底层定义进行交互，让您无需变更容器配置，即可自动为采集的可观测性数据附加 K8s 元数据标签（如 Namespace、Pod、Container、Labels 等），实现数据与基础设施的精准关联。
