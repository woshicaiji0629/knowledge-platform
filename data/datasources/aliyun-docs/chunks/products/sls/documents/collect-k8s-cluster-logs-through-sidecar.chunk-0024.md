### 5. 输出配置
默认采集所有日志发送到当前日志库，压缩方式为lz4。如需将同一来源的日志分发到不同日志库，请参考如下步骤进行配置：
多目标动态分发
重要
多目标发送仅适用于LoongCollector 3.0.0及以上版本，Logtail不支持。
输出目标最多可配置5个。
配置多个输出目标后，该采集配置将不再显示在当前 LogStore 的采集配置列表中。如需查看、修改或删除多目标分发配置，请参考[如何管理多目标分发配置？](collect-k8s-cluster-logs-through-sidecar.md)。
配置步骤：在Logtail配置页面的输出配置区域。
单击展开输出配置。
单击添加输出目标，完成如下配置：
日志库：选择目标日志库。
压缩方式：支持lz4和zstd。
路由配置：根据日志的Tag字段路由分发，满足路由配置的日志会被上传到目标日志库，路由配置为空时表示采集到的所有日志都会被上传到目标日志库。
Tag名称：用于路由的Tag字段名称，直接填写字段名（如__path__），无需__tag__:前缀。Tag字段分为如下两类：
关于Tag的详细信息请参考[管理](manage-loongcollector-to-collect-tags.md)[LoongCollector](manage-loongcollector-to-collect-tags.md)[采集](manage-loongcollector-to-collect-tags.md)[Tag](manage-loongcollector-to-collect-tags.md)。
Agent相关：与采集 Agent 本身相关，不依赖插件。 如__hostname__、__user_defined_id__等。
输入插件相关：依赖输入插件，由输入插件提供并富化相关信息到日志中。如文件采集的__path__；K8s采集的_pod_name_、_container_name_等。
Tag值：日志的Tag字段值与此匹配时，发送到该目标日志库。
是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。
