## 功能特点
日志服务在Kubernetes容器日志采集中提供以下核心能力：
多源日志支持
[日志类型](kubernetes-cluster-container-log-collection-instructions.md)：标准输出信息（stdout）、标准错误信息（stderr）与容器文本文件日志。
精细化容器过滤
通过Namespace名称、Pod名称、容器名称、容器Label或环境变量来指定/排除采集的容器。
复杂日志处理能力
采集[多行日志](kubernetes-cluster-container-log-collection-instructions.md)：允许将跨越多行的日志条目（如Java异常堆栈信息）识别为单个完整日志事件进行采集，避免因换行符导致日志被错误分割。
日志预处理：例如使用[过滤插件](filtration-treatment.md)在采集端过滤无效数据，使用[日志脱敏](desensitization-treatment.md)、[字段提取](extract-content-from-log-fields.md)插件避免原始日志流出。
结构化解析字段：通过[正则](regular-parsing.md)、[JSON](json-parsing.md)、[分隔符](separator-pattern-resolution.md)等解析插件解析原始日志后存储。
智能元数据关联
上报容器日志时[自动关联](kubernetes-cluster-container-log-collection-instructions.md)[Meta](kubernetes-cluster-container-log-collection-instructions.md)[信息](kubernetes-cluster-container-log-collection-instructions.md)（例如容器名、镜像、Pod、Namespace、环境变量等）。
可靠性保障
[checkpoint](kubernetes-cluster-container-log-collection-instructions.md)机制通过记录当前采集位置确保日志完整性。
[容器停止时的日志处理](kubernetes-cluster-container-log-collection-instructions.md)：对不同运行时提供不同的容器停止处理策略。
