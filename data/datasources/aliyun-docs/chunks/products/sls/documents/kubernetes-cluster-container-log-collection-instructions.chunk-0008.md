## 核心概念
Kubernetes：Kubernetes (K8s) 是一个开源的容器编排平台，用于自动化部署、扩展和管理容器化应用程序，是现代化云原生应用开发和运维的核心基础设施。
标准输出、标准错误与文本文件日志：标准输出（stdout）是程序正常运行时打印的信息（例如：业务日志、操作记录），默认输出到终端并被容器引擎捕获存储；标准错误（stderr）是程序错误或警告信息（例如：异常堆栈、启动失败原因），同样被容器引擎捕获存储，可与stdout混合输出；文本文件日志是应用主动写入文件的日志（例如：Nginx的access.log、自定义日志文件），直接写入容器内部文件系统，随容器销毁而销毁，可通过Volumn持久化。
checkpoint机制：checkpoint用于记录日志服务当前采集到文件的具体位置，默认在/tmp/logtail_checkpoint中保存。用于保障LoongCollector重启或节点宕机等异常情况下日志采集的可靠性。
LoongCollector（Logtail）：阿里云自研的高性能日志采集器，支持DaemonSet和Sidecar的Kubernetes部署模式。其中LoongCollector是Logtail的升级版，兼容Logtail的所有功能。
Kubernetes CRD：CRD是Kubernetes 的一种机制，允许用户自定义资源并创建实例进行配置，日志服务提供的自定义资源类型为[AliyunPipelineConfig](recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)。
采集配置：用于定义采集日志的类型，采集路径、有效日志的筛选，日志内容的解析、存储到日志服务的位置等规则，详情可参考[什么是采集配置](machine-group-and-collection-configuration-association-guide.md)。
解析插件：在采集配置的[处理插件配置](processing-plug-ins.md)中使用，日志服务提供了众多用于结构化、切分、过滤、脱敏日志内容的处理单元，支持正则、分隔符、JSON、多行等多种处理模式。
