# 采集ACK集群容器日志（DaemonSet方式部署日志采集）-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 采集ACK集群容器日志（DaemonSet方式部署日志采集）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK集群与阿里云日志服务SLS深入集成，通过提供日志采集组件来简化容器日志的收集和管理。本文介绍如何安装日志采集组件并完成日志采集配置，包括日志的自动采集、查询和分析，以提升运维效率，降低管理成本。

## 场景指引

日志采集组件可通过以下两种方式来采集容器日志。

- 

DaemonSet：适用于日志分类明确、功能较单一的集群。可参见本文了解。

- 

Sidecar：适用于大型、混合型集群。详情请参见[通过](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)[Sidecar](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)[方式采集](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)[Kubernetes](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)[容器文本日志](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)。

关于两种方式的差异，请参见[采集方式](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/log-management-2.md)，关于日志服务计费详情，请参见[计费概述](products/sls/documents/billing-overview.md)。

## 索引

- 

- 

- 

- 

- 

- 

| 操作步骤 | 操作链接 |
| --- | --- |
| 步骤一：安装日志采集组件 | 在以下两个日志采集组件中选择一个进行安装。 [安装](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [LoongCollector（推荐）](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) LoongCollector 是 SLS 推出的新一代采集 Agent，是 Logtail 的升级版。 [安装](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [Logtail](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) Logtail 组件是用于采集 Kubernetes 日志的 Agent，支持多种日志类型及标准容器和 Kubernetes 集群的日志数据采集。 |
| 步骤二：创建采集配置 | 根据采集需求选择文本日志或标准输出。 [采集文本日志](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) 文本日志是由容器内的程序生成并保存到指定目录下的日志文件，适用于需要对指定目录下的日志文件长期分析或故障排查等场景。 [采集标准输出](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) 标准输出（stdout）是容器内程序在运行时生成的实时日志，适用于程序调试和快速定位问题等场景。 |
| 步骤三：查询分析日志 | 通过控制台进行日志查询与分析。 [查询分析日志](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [日志默认字段](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) |


## 步骤一：安装日志采集组件

## 安装LoongCollector（推荐）

重要

LoongCollector目前支持在公有云的所有地域安装，但金融云和政务云暂不支持。

[LoongCollector（原](products/sls/documents/loongcollector-collection.md)[Logtail）](products/sls/documents/loongcollector-collection.md)：Logtail是日志服务提供的日志采集Agent，用于采集阿里云ECS、自建IDC或其他云厂商等服务器上的日志。Logtail基于日志文件采集，无需修改应用程序代码，且采集日志不会影响应用程序运行。LoongCollector是日志服务推出的新一代采集Agent，是Logtail的升级版，兼容Logtail的同时性能更佳。

### 为已有ACK托管集群安装

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。

- 

在日志与监控页签中，找到loongcollector，单击安装。

- 

安装完成后，日志服务会自动在ACK所属地域下创建如下资源，您可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | k8s-log-${cluster_id} | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | loongcollector-ds 的机器组，主要用于日志采集场景。 |
| k8s-group-${cluster_id}-cluster | loongcollector-cluster 的机器组，主要用于指标采集场景。 |  |
| k8s-group-${cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 |  |


重要

LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。

## 安装Logtail

[Logtail](products/sls/documents/logtail-collection.md)[采集](products/sls/documents/logtail-collection.md)：Logtail是日志服务提供的日志采集Agent，用于采集阿里云ECS、自建IDC或其他云厂商等服务器上的日志。Logtail基于日志文件，无侵入式采集日志。您无需修改应用程序代码，且采集日志不会影响您的应用程序运行。

### 已有的ACK集群中安装Logtail组件

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。

- 

在日志与监控页签中，找到logtail-ds，然后单击安装。如未找到logtail-ds组件，请[安装](products/sls/documents/collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md)[LoongCollector](products/sls/documents/collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md)[组件](products/sls/documents/collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md)。

LoongCollector组件为logtail-ds组件的升级版，两个组件不能同时存在，推荐使用LoongCollector组件。

### 新建ACK集群时安装Logtail组件

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

单击创建集群，在组件配置页面，选中使用日志服务。

本文只描述日志服务相关配置，关于更多配置项说明，请参见[创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。

当选中使用日志服务后，会出现创建项目（Project）的提示。

- 

使用已有Project

可选择一个已有的Project来管理采集到的容器日志。

- 

创建新Project

日志服务自动创建一个Project来管理采集到的容器日志。其中ClusterID为新建的Kubernetes集群的唯一标识。

重要

在组件配置页中，默认开启控制面组件日志，开启此配置会在Project中自动配置并采集集群控制面组件日志并遵循按量计费，因此请根据自身情况选择是否需要开启，相关信息请参考[管理控制面组件日志](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-control-plane-component-logs-of-ack-managed-cluster.md)。

安装完成后，自动生成名为k8s-log-<YOUR_CLUSTER_ID>的Project，并在该Project下生成如下资源，可登录[日志服务控制台](https://sls.console.aliyun.com)查看资源。

| 资源类型 | 资源名称 | 作用 | 示例 |
| --- | --- | --- | --- |
| 机器组 | k8s-group- <YOUR_CLUSTER_ID> | logtail-daemonset 的机器组，主要用于日志采集场景。 | k8s-group-my-cluster-123 |
| k8s-group- <YOUR_CLUSTER_ID> -statefulset | logtail-statefulset 的机器组，主要用于指标采集场景。 | k8s-group-my-cluster-123-statefulset |  |
| k8s-group- <YOUR_CLUSTER_ID> -singleton | 单实例机器组，主要用于部分单实例采集配置。 | k8s-group-my-cluster-123-singleton |  |
| Logstore | config-operation-log | 用于存储 Logtail 组件中的 alibaba-log-controller 日志。建议不要在此 Logstore 下创建采集配置。该 Logstore 可以删除，删除后不会再采集 alibaba-log-controller 的运行日志。该 Logstore 的收费标准和普通的 Logstore 收费标准是一致的，具体请参见 [按写入数据量计费模式计费项](products/sls/documents/billing-items-in-the-pay-per-data-write-mode.md) 。 | 无 |


## 步骤二：创建采集配置

### 采集文本日志

以下为四种采集配置方式。建议只使用一种方法管理日志采集配置：

- 

- 

| 配置方式 | 配置说明 | 场景适用 |
| --- | --- | --- |
| （推荐）CRD-AliyunPipelineConfig | 通过 K8s CRD 管理日志采集配置。 | 适用于需要复杂采集和处理需求以及在 ACK 集群中确保日志与应用版本一致性的场景。 |
| CRD-AliyunLogConfig | 旧版 CRD 管理方式。 | 支持已知场景的旧版管理方式。 需要逐渐迁移到新版本 CRD-AliyunPipelineConfig 以享受更好的扩展性和稳定性。两类 CRD 采集方式对比请参见 [CRD](products/sls/documents/use-crd-to-manage-collection-configurations.md) [类型](products/sls/documents/use-crd-to-manage-collection-configurations.md) 。 |
| 日志服务控制台 | 图形化界面直接管理，快速部署配置。 | 适合少量采集配置的创建和管理，部分高级功能和自定义需求无法通过实现。 |
| 环境变量 | 通过环境变量快速配置日志参数。 | 进行简单配置调整，不支持复杂处理逻辑，仅支持单行文本日志。可满足以下定制需求： 将多个应用数据采集到同一 Logstore。 将不同应用数据采集到不同的 Project。 |


说明

当使用（推荐）CRD-AliyunPipelineConfig配置方式时，需要logtail-ds组件版本高于1.8.10。升级详情请参见[升级](products/sls/documents/install-logtail-components-in-a-kubernetes-cluster.md)[Logtail latest](products/sls/documents/install-logtail-components-in-a-kubernetes-cluster.md)[版本](products/sls/documents/install-logtail-components-in-a-kubernetes-cluster.md)。对于LoongCollector组件，则无版本限制。

CRD-AliyunPipelineConfig（推荐）

您只需要创建AliyunPipelineConfig自定义资源即可创建采集配置，资源创建完成后自动生效。

重要

对于通过自定义资源创建的采集配置，其修改只能通过更新相应的自定义资源来实现，在日志服务控制台上对采集配置的修改不会同步到自定义资源中。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>自定义资源。

- 

在自定义资源页面，单击资源定义（CustomResourceDefinition）页签，然后单击使用YAML创建资源。

- 

根据实际情况修改以下示例YAML的参数，将其复制并粘贴到模板中，然后单击创建完成操作。

该示例YAML以多行文本模式采集default命名空间下，标签为app: ^(.*test.*)$的Pod中/data/logs/app_1路径下的test.LOG文件内容，并将其发送到名为k8s-log-<YOUR_CLUSTER_ID>的Project中的名为k8s-file（自动创建）的Logstore。您需根据实际情况修改YAML中的以下参数：

- 

project，示例：k8s-log-<YOUR_CLUSTER_ID>。

登录[日志服务控制台](https://sls.console.aliyun.com)，确定您安装的日志采集组件生成的Project的名称。

- 

IncludeK8sLabel，示例：app: ^(.*test.*)$。用于筛选目标Pod的标签，当前条件指定标签键为app，值中包含test的Pod会被采集。

说明

如果需要采集集群中名称包含test的所有Pod，可以将IncludeK8sLabel替换为K8sContainerRegex，并使用通配符配置值，如：K8sContainerRegex: ^(.test.)$。

- 

FilePaths，示例：/data/logs/app_1/**/test.LOG（**：递归匹配多级子目录，仅能出现一次，且必须位于文件名前）。更多详情请参见[采集容器内文本文件](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)。

- 

Endpoint（[访问域名](products/sls/documents/developer-reference/api-sls-2020-12-30-endpoint.md)）和Region（地域ID），示例：cn-hangzhou.log.aliyuncs.com和cn-hangzhou。

有关YAML文件中config项的详情，包括支持的输入、输出、处理插件类型和容器过滤方式，请参见[PipelineConfig](products/sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)。完整的YAML参数详情请参见[CR](products/sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)[参数说明](products/sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)。

apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: # 设置资源名，在当前Kubernetes集群内唯一。该名称也是创建出的采集配置名，如果名称重复则不会生效。 name: example-k8s-file spec: # 指定目标Project project: name: k8s-log-<YOUR_CLUSTER_ID> logstores: # 创建名为 k8s-file的Logstore - name: k8s-file # 定义采集配置 config: # 日志样例（可不填写） sample: | 2024-06-19 16:35:00 INFO test log line-1 line-2 end # 定义输入插件 inputs: # 使用input_file插件采集容器内多行文本日志 - Type: input_file # 容器内的文件路径 FilePaths: - /data/logs/app_1/**/test.LOG # 启用容器发现功能。 EnableContainerDiscovery: true # 添加容器信息过滤条件，多个选项之间为“且”的关系。 CollectingContainersMeta: true ContainerFilters: # 指定待采集容器所在 Pod 所属的命名空间，支持正则匹配。 K8sNamespaceRegex: default # 指定待采集容器的名称，支持正则匹配。 IncludeK8sLabel: app: ^(.*app.*)$ # 开启多行日志采集，单行日志采集请删除该配置 Multiline: # 选择自定义行首正则表达式模式 Mode: custom # 配置行首正则表达式 StartPattern: '\d+-\d+-\d+\s\d+:\d+:\d+' # 定义处理插件 processors: # 使用正则解析插件解析日志 - Type: processor_parse_regex_native # 源字段名 SourceKey: content # 解析用的正则表达式，用捕获组"()"捕获待提取的字段 Regex: (\d+-\d+-\d+\s\S+)(.*) # 提取的字段列表 Keys: ["time", "detail"] # 定义输出插件 flushers: # 使用flusher_sls插件输出到指定Logstore。 - Type: flusher_sls # 需要确保该 Logstore 存在 Logstore: k8s-file # 需要确保 endpoint 正确 Endpoint: cn-beijing.log.aliyuncs.com Region: cn-beijing TelemetryType: logs

CRD-AliyunLogConfig

您只需要创建AliyunLogConfig自定义资源即可创建采集配置，创建完成后自动生效。

重要

对于通过自定义资源创建的采集配置，其修改只能通过更新相应的自定义资源来实现，在日志服务控制台上对采集配置的修改不会同步到自定义资源中。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>自定义资源。

- 

在自定义资源页面，单击资源定义（CustomResourceDefinition）页签，然后单击使用YAML创建资源。

- 

根据实际情况修改以下示例YAML的参数，将其复制并粘贴到模板中，然后单击创建完成操作。

该示例YAML将创建名为example-k8s-file的采集配置，并对集群内名称开头为app的所有容器，以极简文本模式采集/data/logs/app_1路径下的test.LOG文件内容，发送到名为k8s-log-<YOUR_CLUSTER_ID>的Project中的名为k8s-file（自动创建）的Logstore。

您需根据实际情况修改示例中容器内文件路径，更多详情请参见[容器文件路径映射](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md)。

- 

logPath：采集日志路径。示例：/data/logs/app_1。

- 

filePattern：采集日志文件名称。示例：test.LOG。

有关YAML文件中的Config项提供的配置详情，如支持的输入，输出，处理插件类型与容器过滤方式等，请参见[AliyunLogConfigDetail](products/sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)，完整的YAML参数详情请参见[CR](products/sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)[参数说明](products/sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)。

apiVersion: log.alibabacloud.com/v1alpha1 kind: AliyunLogConfig metadata: # 设置资源名，在当前Kubernetes集群内唯一。 name: example-k8s-file # 设置资源所在命名空间。 namespace: kube-system spec: # 设置目标project名称（可不填写，默认为k8s-log-<your_cluster_id>） # project: k8s-log-test # 设置Logstore名称。如果您所指定的Logstore不存在，日志服务会自动创建。 logstore: k8s-file # 设置采集配置。 logtailConfig: # 设置采集的数据源类型。采集文本日志时，需设置为file。 inputType: file # 设置采集配置的名称，必须与metadata.name一致。 configName: example-k8s-file inputDetail: # 指定通过极简模式采集文本日志。 logType: common_reg_log # 设置日志文件所在路径。 logPath: /data/logs/app_1 # 设置日志文件的名称。支持通配符星号（*）和半角问号（?），例如log_*.log。 filePattern: test.LOG # 采集容器的文本日志时，需设置dockerFile为true。 dockerFile: true # 开启多行日志采集。单行日志采集删除该配置 # 行首正则表达式，以该正则表示一行日志的开始。 logBeginRegex: \d+-\d+-\d+.* #设置容器过滤条件。 advanced: k8s: K8sPodRegex: '^(app.*)$'

日志服务控制台

说明

此方式适合少量采集配置的创建和管理，无需登录Kubernetes集群，操作步骤简单但无法批量配置。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

选择Project列表中您在安装日志采集组件时所使用的Project，如k8s-log-<YOUR_CLUSTER_ID>。在Project页面中单击目标Logstore的Logtail配置，添加采集配置，并单击Kubernetes-文件的立即接入。

- 

在机器组配置页面K8s场景的ACK Daemonset方式下勾选k8s-group-${your_k8s_cluster_id}机器组并单击添加到应用机器组，单击下一步。

- 

创建采集配置，按下文填写必须配置后单击下一步即可，采集配置生效大概需要1分钟，请耐心等待。此处仅介绍主要配置，详细配置请参见[Logtail](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md)[采集配置](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md)。

- 

全局配置

在全局配置中输入配置名称。

- 

输入配置

- 

Logtail部署模式：选择Daemonset。

- 

文件路径类型：选择待采集的文件路径是容器内路径或宿主机路径。对于通过hostPath方式挂载数据卷的容器，如果您希望直接采集其在宿主机上映射的日志文件，请选择宿主机路径，其余情况请选择容器内路径。

- 

文件路径：代表日志采集的路径，日志路径必须以正斜线（/）开头，例如下图/data/wwwlogs/main/**/*.Log表示/data/wwwlogs/main目录下后缀名为.Log的文件。如果需要设置日志目录被监控的最大深度，即文件路径中通配符**匹配的最大目录深度。可以修改最大目录监控深度的取值，0代表只监控本层目录。

- 

创建索引和预览数据：日志服务默认开启全文索引，此时查询会索引日志中所有字段。您也可以根据采集到的日志，手动创建字段索引，或者单击自动生成索引，日志服务将生成字段索引，通过此索引针对特定字段进行精确查询，从而减少索引费用和提高查询效率。更多信息请参见[创建索引](products/sls/documents/create-indexes.md)。

环境变量

说明

此方式仅支持单行文本，如果要配置多行文本或其他日志格式，必须使用自定义资源方式或在日志服务控制台配置。

- 

创建应用时配置日志服务。

通过容器控制台配置

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com/)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>无状态。

- 

在无状态页面，单击使用镜像创建。

- 

在应用基本信息页签，设置应用名称，单击下一步，进入容器配置页面，设置镜像名称。

以下仅介绍日志服务相关的配置。关于其他的应用配置，请参见[创建无状态工作负载](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)[Deployment](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)。

- 

在日志配置区域，配置日志相关信息。

- 

设置采集配置。

单击采集配置创建新的采集配置，每个采集配置由日志库和容器内日志路径（可设置为stdout）两项构成。

- 

日志库：配置Logstore名称，用于指定所采集的日志存储于该Logstore。如果该Logstore不存在，ACK将会自动为集群关联的日志服务Project下创建相应的Logstore。

说明

新创建的Logstore中的日志默认保存时间为90天。

- 

容器内日志路径（可设置为stdout）：指定希望采集的日志所在的路径，例如使用/usr/local/tomcat/logs/catalina.*.log来采集Tomcat的文本日志。

每一项采集配置都会被自动创建为对应Logstore的一个采集配置，默认采用极简模式（按行）进行采集。

- 

设置自定义Tag。

单击自定义Tag创建新的自定义Tag，每一个自定义Tag都是一个键值对，会拼接到所采集到的日志中，可使用它来为容器的日志数据进行标记，例如版本号。

通过YAML模板

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>无状态。

- 

在无状态页面上方的命名空间下拉框中设置命名空间，然后单击页面右上角的使用YAML创建资源。

- 

配置YAML文件。

YAML模板的语法同Kubernetes语法，但是为了给容器指定采集配置，需要使用env来为容器增加采集配置和自定义Tag，并根据采集配置，创建对应的volumeMounts和volumes。以下是一个简单的Pod示例：

apiVersion: v1 kind: Pod metadata: name: my-demo spec: containers: - name: my-demo-app image: 'registry.cn-hangzhou.aliyuncs.com/log-service/docker-log-test:latest' env: # 配置环境变量 - name: aliyun_logs_log-varlog value: /var/log/*.log - name: aliyun_logs_mytag1_tags value: tag1=v1 # 配置volume mount volumeMounts: - name: volumn-sls-mydemo mountPath: /var/log # 如果Pod不断重启，启动参数可以添加sleep command: ["sh", "-c"] # 使用 shell 来运行命令 args: ["sleep 3600"] # 设置休眠时间为 1 小时（3600 秒） volumes: - name: volumn-sls-mydemo emptyDir: {}

- 

通过环境变量来创建采集配置和自定义Tag，所有与配置相关的环境变量都采用aliyun_logs_作为前缀。

- 

创建采集配置的规则如下：

- name: aliyun_logs_log-varlog value: /var/log/*.log

示例中创建了一个采集配置，格式为aliyun_logs_{key}，对应的{key}为log-varlog。

- 

aliyun_logs_log-varlog：该env表示创建一个Logstore名为log-varlog，日志采集路径为/var/log/*.log的配置，对应的日志服务采集配置名称也是log-varlog，目的是将容器的/var/log/*.log文件内容采集到log-varlog这个Logstore中。

- 

创建自定义Tag的规则如下：

- name: aliyun_logs_mytag1_tags value: tag1=v1

配置Tag后，当采集到该容器的日志时，会自动附加对应的字段到日志服务。其中mytag1为任意不包含'_'的名称。

- 

如果采集配置中指定了非stdout的采集路径，需要在此部分创建相应的volumeMounts。

示例中采集配置添加了对/var/log/*.log的采集，因此相应地添加了/var/log的volumeMounts。

- 

当YAML编写完成后，单击创建，即可将相应的配置交由Kubernetes集群执行。

- 

配置环境变量的高级参数。

通过容器环境变量配置采集支持多种配置参数。您可以根据实际需求设置高级参数，以满足日志采集的特殊需求。

重要

通过容器环境变量配置采集日志的方式不适用于边缘场景。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 字段 | 说明 | 示例 | 注意事项 |
| --- | --- | --- | --- |
| aliyun_logs_{key} | 必选项。{key}只能包含小写字母、数字和-。 若不存在 aliyun_logs_{key}_logstore，则默认创建并采集到名为{key}的 logstore。 当值为 stdout 时表示采集容器的标准输出；其他值为容器内的日志路径。 | - name: aliyun_logs_catalina value: stdout - name: aliyun_logs_access-log value: /var/log/nginx/access.log | 默认采集方式为极简模式。如需解析日志内容，建议使用日志服务控制台，或者 CRD 进行配置。 {key}表示日志服务中 LoongCollector 采集配置的名称，需保持在 K8s 集群内唯一。 |
| aliyun_logs_{key}_tags | 可选。值为{tag-key}={tag-value}类型，用于对日志进行标识。 | - name: aliyun_logs_catalina_tags value: app=catalina | 不涉及。 |
| aliyun_logs_{key}_project | 可选。值为指定的日志服务 Project。当不存在该环境变量时，为您安装时所选的 Project。 | - name: aliyun_logs_catalina_project value: my-k8s-project | Project 需与您的 LoongCollector 工作所在的 Region 一致。 |
| aliyun_logs_{key}_logstore | 可选。值为指定的日志服务 Logstore。当不存在该环境变量时，Logstore 和{key}一致。 | - name: aliyun_logs_catalina_logstore value: my-logstore | 不涉及。 |
| aliyun_logs_{key}_shard | 可选。值为创建 Logstore 时的 shard 数，取值范围为[1 , 10]。当不存在该环境变量时，值为 2。 说明 若 logstore 已经存在，则该参数不生效。 | - name: aliyun_logs_catalina_shard value: '4' | 不涉及。 |
| aliyun_logs_{key}_ttl | 可选。值为指定的日志保存时间，取值范围为[1 , 3650]。 当取值为 3650 时，指定日志的保存时间为永久保存。 当不存在该环境变量时，默认指定日志的保存时间为 90 天。 说明 若 Logstore 已经存在，则该参数不生效。 | - name: aliyun_logs_catalina_ttl value: '3650' | 不涉及。 |
| aliyun_logs_{key}_machinegroup | 可选。值为应用的机器组。当不存在该环境变量时与安装 LoongCollector 的默认机器组一致。关于该参数的详细使用方法，请参见下文的 [采集](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [集群容器日志](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) 。 | - name: aliyun_logs_catalina_machinegroup value: my-machine-group | 不涉及。 |
| aliyun_logs_{key}_logstoremode | 可选。值为指定的日志服务 Logstore 的类型，不指定该参数的话，默认值为 standard ，取值： 说明 若 Logstore 已经存在，则该参数不生效。 standard ：支持日志服务一站式数据分析功能，适用于实时监控、交互式分析以及构建完整的可观测性系统等场景。 query ：支持高性能查询，索引流量费用约为 standard 的一半，但不支持 SQL 分析，适用于数据量大、存储周期长（周、月级别以上）、无日志分析的场景。 | - name: aliyun_logs_catalina_logstoremode value: standard - name: aliyun_logs_catalina_logstoremode value: query | 不涉及。 |


- 定制需求1：将多个应用数据采集到同一Logstore

如果需要将多个应用数据采集到同一Logstore，可以设置aliyun_logs_{key}_logstore参数，例如以下配置将2个应用的stdout采集到stdout-logstore中。

示例中应用1的{key}为app1-stdout，应用2的{key}为app2-stdout。

应用1设置的环境变量为：

# 配置环境变量 - name: aliyun_logs_app1-stdout value: stdout - name: aliyun_logs_app1-stdout_logstore value: stdout-logstore

应用2设置的环境变量为：

# 配置环境变量 - name: aliyun_logs_app2-stdout value: stdout - name: aliyun_logs_app2-stdout_logstore value: stdout-logstore

- 定制需求2：将不同应用数据采集到不同的Project

如果需要将不同应用的数据采集到多个Project中，需要进行以下操作：

- 

在每个Project中创建一个机器组，选择自定义标识，标识名为k8s-group-{cluster-id}，其中{cluster-id}为集群ID，机器组名称可以自定义配置。

- 

在每个应用的环境变量中配置project、logstore、machinegroup信息，其中机器组名称为上一步创建的机器组名称。

如下示例中应用1的{key}为app1-stdout，应用2的{key}为app2-stdout。其中如果两个应用在同一个K8s集群中，对应的machinegroup可以使用同一个machinegroup。

应用1设置的环境变量为：

# 配置环境变量 - name: aliyun_logs_app1-stdout value: stdout - name: aliyun_logs_app1-stdout_project value: app1-project - name: aliyun_logs_app1-stdout_logstore value: app1-logstore - name: aliyun_logs_app1-stdout_machinegroup value: app1-machine-group

应用2设置的环境变量为：

# 应用2 配置环境变量 - name: aliyun_logs_app2-stdout value: stdout - name: aliyun_logs_app2-stdout_project value: app2-project - name: aliyun_logs_app2-stdout_logstore value: app2-logstore - name: aliyun_logs_app2-stdout_machinegroup value: app1-machine-group

### 采集标准输出

以下为四种采集配置方式。建议只使用一种方法管理日志采集配置：

- 

- 

| 配置方式 | 配置说明 | 场景适用 |
| --- | --- | --- |
| （推荐）CRD-AliyunPipelineConfig | 通过 K8s CRD 管理日志采集配置。 | 适用于需要复杂采集和处理需求以及在 ACK 集群中确保日志与应用版本一致性的场景。 |
| CRD-AliyunLogConfig | 旧版 CRD 管理方式。 | 支持已知场景的旧版管理方式。 需要逐渐迁移到新版本 CRD-AliyunPipelineConfig 以享受更好的扩展性和稳定性。两类 CRD 采集方式对比请参见 [CRD](products/sls/documents/use-crd-to-manage-collection-configurations.md) [类型](products/sls/documents/use-crd-to-manage-collection-configurations.md) 。 |
| 日志服务控制台 | 图形化界面直接管理，快速部署配置。 | 适合少量采集配置的创建和管理，部分高级功能和自定义需求无法通过实现。 |
| 环境变量 | 通过环境变量快速配置日志参数。 | 进行简单配置调整，不支持复杂处理逻辑，仅支持单行文本日志。可满足以下定制需求： 将多个应用数据采集到同一 Logstore。 将不同应用数据采集到不同的 Project。 |


说明

当使用（推荐）CRD-AliyunPipelineConfig时，需要logtail-ds组件版本高于1.8.10。升级详情请参见[升级](products/sls/documents/install-logtail-components-in-a-kubernetes-cluster.md)[Logtail latest](products/sls/documents/install-logtail-components-in-a-kubernetes-cluster.md)[版本](products/sls/documents/install-logtail-components-in-a-kubernetes-cluster.md)。对于LoongCollector组件，则无版本限制。

CRD-AliyunPipelineConfig（推荐）

您只需要创建AliyunPipelineConfig自定义资源即可创建采集配置，资源创建完成后自动生效。

重要

对于通过自定义资源创建的采集配置，其修改只能通过更新相应的自定义资源来实现，在日志服务控制台上对采集配置的修改不会同步到自定义资源中。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>自定义资源。

- 

在自定义资源页面，单击资源定义（CustomResourceDefinition）页签，然后单击使用YAML创建资源。

- 

根据实际情况修改以下示例YAML的参数，将其复制并粘贴到模板中，然后单击创建完成操作。

说明

您可用[采集配置生成器](products/sls/documents/collection-configuration-generator.md)生成目标场景YAML脚本，该工具可帮您快速完成配置，减少手动操作。

以下示例YAML文件以多行文本模式采集default命名空间下，标签为app: ^(.*test.*)$的Pod中的标准输出，并将其发送到名为k8s-log-<YOUR_CLUSTER_ID>的Project中的名为k8s-stdout（自动创建）的Logstore。您需根据实际情况修改YAML中的以下参数：

- 

project，示例：k8s-log-<YOUR_CLUSTER_ID>。

登录[日志服务控制台](https://sls.console.aliyun.com)，确定您安装的日志采集组件生成的Project的名称。

- 

IncludeK8sLabel，示例：app: ^(.*test.*)$。用于筛选目标Pod的标签，当前条件指定标签键为app，值中包含test的Pod会被采集。

- 

Endpoint和Region，示例：cn-hangzhou.log.aliyuncs.com和cn-hangzhou。

有关YAML文件中config项的详情，包括支持的输入、输出、处理插件类型和容器过滤方式，请参见[PipelineConfig](products/sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)。完整的YAML参数详情请参见[CR](products/sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)[参数说明](products/sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)。

apiVersion: telemetry.alibabacloud.com/v1alpha1 # 创建一个 ClusterAliyunPipelineConfig kind: ClusterAliyunPipelineConfig metadata: # 设置资源名，在当前Kubernetes集群内唯一。该名称也是创建出的日志采集配置名。如果名称重复则不会生效。 name: example-k8s-stdout spec: # 指定目标project project: name: k8s-log-<YOUR_CLUSTER_ID> # 创建用于存储日志的 Logstore logstores: - name: k8s-stdout # 定义日志采集配置 config: # 日志样例（可不填写） sample: | 2024-06-19 16:35:00 INFO test log line-1 line-2 end # 定义输入插件 inputs: # 使用service_docker_stdout插件采集容器内文本日志 - Type: service_docker_stdout Stdout: true Stderr: true # 配置容器信息过滤条件，多个选项之间为“且”的关系。 # 指定待采集容器所在 Pod 所属的命名空间，支持正则匹配。 K8sNamespaceRegex: "^(default)$" # 启用容器元数据预览 CollectContainersFlag: true # 采集Pod标签符合条件的容器。多个条目之间为或的关系 IncludeK8sLabel: app: ^(.*test.*)$ # 配置多行切分配置，单行日志采集无效配置 # 配置行首正则表达式 BeginLineRegex: \d+-\d+-\d+.* # 定义输出插件 flushers: # 使用flusher_sls插件输出到指定Logstore。 - Type: flusher_sls # 需要确保该 Logstore 存在 Logstore: k8s-stdout # 需要确保 endpoint 正确 Endpoint: cn-hangzhou.log.aliyuncs.com Region: cn-hangzhou TelemetryType: logs

CRD-AliyunLogConfig

您只需要创建AliyunLogConfig自定义资源即可创建采集配置，创建完成后自动生效。

重要

对于通过自定义资源创建的采集配置，其修改只能通过更新相应的自定义资源来实现，在日志服务控制台上对采集配置的修改不会同步到自定义资源中。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>自定义资源。

- 

在自定义资源页面，单击资源定义（CustomResourceDefinition）页签，然后单击使用YAML创建资源。

- 

根据实际情况修改以下示例YAML的参数，将其复制并粘贴到模板中，然后单击创建完成操作。

该YAML脚本将创建名为simple-stdout-example的采集配置，并对集群内名称开头为app的所有容器，以多行模式采集标准输出，发送到名为k8s-log-<YOUR_CLUSTER_ID>的Project中的名为k8s-stdout的Logstore。

有关YAML文件中的logtailConfig项提供的详情，如支持的输入，输出，处理插件类型与容器过滤方式等，请参见[AliyunLogConfigDetail](products/sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)，完整的YAML参数详情请参见[CR](products/sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)[参数说明](products/sls/documents/use-aliyunlogconfig-to-manage-collection-configurations.md)。

# 标准输出配置 apiVersion: log.alibabacloud.com/v1alpha1 kind: AliyunLogConfig metadata: # 设置资源名，在当前Kubernetes集群内唯一。 name: simple-stdout-example spec: # 设置目标project名称（可不填写，默认为k8s-log-<your_cluster_id>） # project: k8s-log-test # 设置Logstore名称。如果您所指定的Logstore不存在，日志服务会自动创建。 logstore: k8s-stdout # 设置日志采集配置。 logtailConfig: # 设置采集的数据源类型。采集标准输出时，需设置为plugin。 inputType: plugin # 设置Logtail采集配置的名称，必须与资源名(metadata.name)相同。 configName: simple-stdout-example inputDetail: plugin: inputs: - type: service_docker_stdout detail: # 指定采集stdout和stderr。 Stdout: true Stderr: true # 指定待采集容器所在 Pod 所属的命名空间，支持正则匹配。 K8sNamespaceRegex: "^(default)$" # 指定待采集容器的名称，支持正则匹配。 K8sContainerRegex: "^(app.*)$" # 配置多行切分配置 # 配置行首正则表达式 BeginLineRegex: \d+-\d+-\d+.*

日志服务控制台

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

选择Project列表中您在安装日志采集组件时所使用的Project，如k8s-log-<YOUR_CLUSTER_ID>。在Project页面中点击目标Logstore的Logtail配置，添加采集配置，并单击K8S-标准输出-旧版的立即接入。

- 

由于上一步骤中已为ACK集群安装日志采集组件，请单击使用现有机器组。

- 

在机器组配置页面K8s场景的ACK Daemonset方式下勾选k8s-group-${your_k8s_cluster_id}机器组并单击>添加到应用机器组中，点击下一步。

- 

创建Logtail采集配置，按下文填写必须配置后点击下一步即可，Logtail采集配置生效大概需要1分钟，请耐心等待。

此处仅介绍必须配置，详细配置请参见[Logtail](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md)[采集配置](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md)。

- 

全局配置

在全局配置中输入配置名称。

- 

创建索引和预览数据：日志服务默认开启全文索引，此时查询会索引日志中所有字段。您也可以根据采集到的日志，手动创建字段索引，或者单击自动生成索引，日志服务将生成字段索引，通过此索引针对特定字段进行精确查询，从而减少索引费用和提高查询效率。更多信息请参见[创建索引](products/sls/documents/create-indexes.md)。

环境变量

- 

创建应用时配置日志服务。

通过控制台配置

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com/)，在左侧导航栏单击集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>无状态。

- 

在无状态页面上方的命名空间下拉框中设置命名空间，然后单击页面右上角的使用镜像创建。

- 

在应用基本信息页签，设置应用名称，单击下一步，进入容器配置页面。

以下仅介绍日志服务相关的配置。关于其他的应用配置，请参见[创建无状态工作负载](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)[Deployment](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)。

- 

在日志配置区域，配置日志相关信息。

- 

设置采集配置。

单击采集配置创建新的采集配置，每个采集配置由日志库和容器内日志路径（可设置为stdout）两项构成。

- 

日志库：配置Logstore名称，用于指定所采集的日志存储于该Logstore。如果该Logstore不存在，ACK将会自动为您在集群关联的日志服务Project下创建相应的Logstore。

说明

新创建的Logstore中的日志默认保存时间为90天。

- 

容器内日志路径（可设置为stdout）：指定为stdout时，表示采集容器的标准输出和标准错误输出。

每一项采集配置都会被自动创建为对应Logstore的一个采集配置，默认采用极简模式（按行）进行采集。

- 

设置自定义Tag。

单击自定义Tag创建新的自定义Tag，每一个自定义Tag都是一个键值对，会拼接到所采集到的日志中，您可以使用它来为容器的日志数据进行标记，例如版本号。

- 

当完成所有配置后，可单击右上角的下一步进入后续流程。

后续操作，可参见[创建无状态工作负载](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)[Deployment](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)。

通过YAML模板

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>无状态。

- 

在无状态页面上方的命名空间下拉框中设置命名空间，然后单击页面右上角的使用YAML创建资源。

- 

配置YAML文件。

YAML模板的语法同Kubernetes语法，但是为了给容器指定采集配置，需要使用env来为容器增加采集配置和自定义Tag，并根据采集配置，创建对应的volumeMounts和volumes。以下是一个简单的Pod示例：

apiVersion: apps/v1 kind: Deployment metadata: annotations: deployment.kubernetes.io/revision: '1' labels: app: deployment-stdout cluster_label: CLUSTER-LABEL-A name: deployment-stdout namespace: default spec: progressDeadlineSeconds: 600 replicas: 1 revisionHistoryLimit: 10 selector: matchLabels: app: deployment-stdout strategy: rollingUpdate: maxSurge: 25% maxUnavailable: 25% type: RollingUpdate template: metadata: labels: app: deployment-stdout cluster_label: CLUSTER-LABEL-A spec: containers: - args: - >- while true; do date '+%Y-%m-%d %H:%M:%S'; echo 1; echo 2; echo 3; echo 4; echo 5; echo 6; echo 7; echo 8; echo 9; sleep 10; done command: - /bin/sh - '-c' - '--' env: - name: cluster_id value: CLUSTER-A - name: aliyun_logs_log-stdout value: stdout image: 'mirrors-ssl.aliyuncs.com/busybox:latest' imagePullPolicy: IfNotPresent name: timestamp-test resources: {} terminationMessagePath: /dev/termination-log terminationMessagePolicy: File dnsPolicy: ClusterFirst restartPolicy: Always schedulerName: default-scheduler securityContext: {} terminationGracePeriodSeconds: 30

- 

通过环境变量来创建您的采集配置和自定义Tag，所有与配置相关的环境变量都采用aliyun_logs_作为前缀。

- 

创建采集配置的规则如下：

- name: aliyun_logs_log-varlog value: /var/log/*.log

示例中创建了一个采集配置，格式为aliyun_logs_{key}，对应的{key}为log-varlog。

- 

aliyun_logs_log-varlog：该env表示创建一个Logstore名为log-varlog，日志采集路径为/var/log/*.log的配置，对应的日志服务采集配置名称也是log-varlog，目的是将容器的/var/log/*.log文件内容采集到log-varlog这个Logstore中。

- 

创建自定义Tag的规则如下：

- name: aliyun_logs_mytag1_tags value: tag1=v1

配置Tag后，当采集到该容器的日志时，会自动附加对应的字段到日志服务。其中mytag1为任意不包含'_'的名称。

- 

如果您的采集配置中指定了非stdout的采集路径，需要在此部分创建相应的volumeMounts。

示例中采集配置添加了对/var/log/*.log的采集，因此相应地添加了/var/log的volumeMounts。

- 

当YAML编写完成后，单击创建，即可将相应的配置交由Kubernetes集群执行。

- 

配置环境变量的高级参数。

通过容器环境变量配置采集支持多种配置参数。您可以根据实际需求设置高级参数，以满足日志采集的特殊需求。

重要

通过容器环境变量配置采集日志的方式不适用于边缘场景。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 字段 | 说明 | 示例 | 注意事项 |
| --- | --- | --- | --- |
| aliyun_logs_{key} | 必选项。{key}只能包含小写字母、数字和-。 若不存在 aliyun_logs_{key}_logstore，则默认创建并采集到名为{key}的 logstore。 当值为 stdout 时表示采集容器的标准输出；其他值为容器内的日志路径。 | - name: aliyun_logs_catalina value: stdout - name: aliyun_logs_access-log value: /var/log/nginx/access.log | 默认采集方式为极简模式。如需解析日志内容，建议使用日志服务控制台，并参见 [通过](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md) [DaemonSet](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md) [方式采集](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md) [Kubernetes](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md) [容器文本日志](products/sls/documents/collect-container-text-logs-through-the-daemonset-console.md) 或 [通过](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md) [DaemonSet](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md) [方式采集](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md) [Kubernetes](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md) [容器标准输出（旧版）](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md) 进行配置。 {key}表示日志服务中日志采集配置的名称，需保持在 K8s 集群内唯一。 |
| aliyun_logs_{key}_tags | 可选。值为{tag-key}={tag-value}类型，用于对日志进行标识。 | - name: aliyun_logs_catalina_tags value: app=catalina | 不涉及。 |
| aliyun_logs_{key}_project | 可选。值为指定的日志服务 Project。当不存在该环境变量时，为您安装时所选的 Project。 | - name: aliyun_logs_catalina_project value: my-k8s-project | Project 需与您的日志采集组件工作所在的 Region 一致。 |
| aliyun_logs_{key}_logstore | 可选。值为指定的日志服务 Logstore。当不存在该环境变量时，Logstore 和{key}一致。 | - name: aliyun_logs_catalina_logstore value: my-logstore | 不涉及。 |
| aliyun_logs_{key}_shard | 可选。值为创建 Logstore 时的 shard 数，取值范围为[1 , 10]。当不存在该环境变量时，值为 2。 说明 若 logstore 已经存在，则该参数不生效。 | - name: aliyun_logs_catalina_shard value: '4' | 不涉及。 |
| aliyun_logs_{key}_ttl | 可选。值为指定的日志保存时间，取值范围为[1 , 3650]。 当取值为 3650 时，指定日志的保存时间为永久保存。 当不存在该环境变量时，默认指定日志的保存时间为 90 天。 说明 若 Logstore 已经存在，则该参数不生效。 | - name: aliyun_logs_catalina_ttl value: '3650' | 不涉及。 |
| aliyun_logs_{key}_machinegroup | 可选。值为应用的机器组。当不存在该环境变量时与安装日志采集组件的默认机器组一致。关于该参数的详细使用方法，请参见下文的 [采集](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) [集群容器日志](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md) 。 | - name: aliyun_logs_catalina_machinegroup value: my-machine-group | 不涉及。 |
| aliyun_logs_{key}_logstoremode | 可选。值为指定的日志服务 Logstore 的类型，不指定该参数的话，默认值为 standard ，取值： 说明 若 Logstore 已经存在，则该参数不生效。 standard ：支持日志服务一站式数据分析功能，适用于实时监控、交互式分析以及构建完整的可观测性系统等场景。 query ：支持高性能查询，索引流量费用约为 standard 的一半，但不支持 SQL 分析，适用于数据量大、存储周期长（周、月级别以上）、无日志分析的场景。 | - name: aliyun_logs_catalina_logstoremode value: standard - name: aliyun_logs_catalina_logstoremode value: query | 该参数需要 logtail-ds 镜像版本>=1.3.1。 |


- 定制需求1：将多个应用数据采集到同一Logstore

如果您需要将多个应用数据采集到同一Logstore，可以设置aliyun_logs_{key}_logstore参数，例如以下配置将2个应用的stdout采集到stdout-logstore中。

示例中应用1的{key}为app1-stdout，应用2的{key}为app2-stdout。

应用1设置的环境变量为：

# 配置环境变量 - name: aliyun_logs_app1-stdout value: stdout - name: aliyun_logs_app1-stdout_logstore value: stdout-logstore

应用2设置的环境变量为：

# 配置环境变量 - name: aliyun_logs_app2-stdout value: stdout - name: aliyun_logs_app2-stdout_logstore value: stdout-logstore

- 定制需求2：将不同应用数据采集到不同的Project

如果您需要将不同应用的数据采集到多个Project中，您需要进行以下操作：

- 

在每个Project中创建一个机器组，选择自定义标识，标识名为k8s-group-{cluster-id}，其中{cluster-id}为您的集群ID，机器组名称可以自定义配置。

- 

在每个应用的环境变量中配置project、logstore、machinegroup信息，其中机器组名称为您在上一步创建的机器组名。

如下示例中应用1的{key}为app1-stdout，应用2的{key}为app2-stdout。其中如果两个应用在同一个K8s集群中，对应的machinegroup可以使用同一个machinegroup。

应用1设置的环境变量为：

# 配置环境变量 - name: aliyun_logs_app1-stdout value: stdout - name: aliyun_logs_app1-stdout_project value: app1-project - name: aliyun_logs_app1-stdout_logstore value: app1-logstore - name: aliyun_logs_app1-stdout_machinegroup value: app1-machine-group

应用2设置的环境变量为：

# 应用2 配置环境变量 - name: aliyun_logs_app2-stdout value: stdout - name: aliyun_logs_app2-stdout_project value: app2-project - name: aliyun_logs_app2-stdout_logstore value: app2-logstore - name: aliyun_logs_app2-stdout_machinegroup value: app1-machine-group

## 步骤三：查询分析日志

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)。

- 

在Project列表中，单击目标Project，进入对应的Project详情页面。

- 

在对应的日志库右侧的图标，选择查询分析，查看Kubernetes集群输出的日志。

### 日志默认字段

## 文本日志

K8s每条容器文本日志默认包含的字段如下表所示。

| 字段名称 | 说明 |
| --- | --- |
| __tag__:__hostname__ | 容器宿主机的名称。 |
| __tag__:__path__ | 容器内日志文件的路径。 |
| __tag__:_container_ip_ | 容器的 IP 地址。 |
| __tag__:_image_name_ | 容器使用的镜像名称。 说明 若存在多个相同 Hash 但名称或 Tag 不同的镜像，采集配置将根据 Hash 选择其中一个名称进行采集，无法确保所选名称与 YAML 文件中定义的一致。 |
| __tag__:_pod_name_ | Pod 的名称。 |
| __tag__:_namespace_ | Pod 所属的命名空间。 |
| __tag__:_pod_uid_ | Pod 的唯一标识符（UID）。 |


## 标准输出

Kubernetes集群的每条日志默认上传的字段如下所示。

| 字段名称 | 说明 |
| --- | --- |
| _time_ | 日志采集时间。 |
| _source_ | 日志源类型，stdout 或 stderr。 |
| _image_name_ | 镜像名 |
| _container_name_ | 容器名 |
| _pod_name_ | Pod 名 |
| _namespace_ | Pod 所在的命名空间 |
| _pod_uid_ | Pod 的唯一标识 |


## 相关文档

- 

当完成日志内容的采集后，可在日志服务中使用查询与分析功能，来帮助了解日志情况，请参考[查询与分析快速指引](products/sls/documents/quick-guide-to-query-and-analysis.md)。

- 

当完成日志内容的采集后，可在日志服务中使用可视化功能， 来帮助直观地统计与了解日志情况，请参考[快速创建仪表盘](products/sls/documents/dashboard-overview.md)。

- 

当完成日志内容的采集后，可在日志服务中使用告警功能， 来自动提醒日志中的异常情况，请参考[告警设置快速入门](products/sls/documents/alarm-settings-quick-start.md)。

- 

日志服务仅采集增量日志，历史日志文件采集请参见[导入历史日志文件](products/sls/documents/import-historical-logs.md)。

- 

容器采集异常排查思路：

- 

[日志服务采集数据常见的错误类型](products/sls/documents/log-collection-error-type.md)。

- 

查看控制台是否有报错信息，具体操作，请参见[如何查看](products/sls/documents/user-guide/how-do-i-view-logtail-collection-errors.md)[Logtail](products/sls/documents/user-guide/how-do-i-view-logtail-collection-errors.md)[采集错误信息](products/sls/documents/user-guide/how-do-i-view-logtail-collection-errors.md)。

- 

如果控制台无报错信息，排查机器组心跳、Logtail采集配置等内容。具体操作，请参见[如何排查容器日志采集异常](products/sls/documents/what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)。

[上一篇：日志管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/log-management-2.md)[下一篇：通过控制台采集集群容器日志（标准输出/文件）](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-kubernetes-cluster-text-logs-daemonset.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
