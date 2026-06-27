# 通过AliyunPipelineConfig CRD在Kubernetes集群中采集容器标准输出和文件日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 通过Kubernetes CRD采集集群容器日志（标准输出/文件）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

为了统一管理阿里云容器服务ACK集群或自建 Kubernetes 集群在多环境、多集群场景下的日志采集配置，避免因手动配置导致的不一致、效率低下及变更不可追溯等问题，可采用Kubernetes 的自定义资源（CRD）方式定义采集配置。通过该方式，无论是 ACK 集群还是自建 Kubernetes 集群，均可使用kubectl或 CI/CD 流水线实现配置的版本化管理、环境差异化部署和自动化发布。结合 LoongCollector 的热加载能力，配置变更后可立即生效，无需重启采集组件，提升运维效率与系统的可维护性。

旧版CRD-AliyunLogConfig的配置方式已停止维护，请使用新版AliyunPipelineConfig，新旧版的能力对比请参见[CRD](products/sls/documents/use-crd-to-manage-collection-configurations.md)[类型](products/sls/documents/use-crd-to-manage-collection-configurations.md)。

重要

对于通过自定义资源（CRD）创建的采集配置，只能通过更新对应的CRD进行修改。在日志服务控制台上所做的更改不会同步至CRD，也不会生效。

## 适用范围

- 

运行环境：

- 

支持阿里云容器服务ACK（托管与专有版）和自建Kubernetes 集群。

- 

Kubernetes为1.16.0及以上版本且支持Mount propagation: HostToContainer。

- 

容器运行时（仅支持Docker与Containerd）

- 

Docker：

- 

需具备访问docker.sock的权限。

- 

标准输出采集仅支持JSON类型的日志驱动。

- 

存储驱动仅支持overlay、overlay2两种存储驱动（其他类型需手动挂载日志目录）。

- 

Containerd：需具备访问containerd.sock的权限。

- 

资源要求：LoongCollector（Logtail）以system-cluster-critical高优先级运行，集群资源不足时请勿部署，否则可能驱逐节点上原有的Pod。

- 

CPU：至少预留0.1 Core。

- 

内存：采集组件至少150MB，控制器组件至少100MB。

- 

实际使用量与采集速率、监控目录和文件数量、发送阻塞程度有关，请保证实际使用率低于限制值的80%。

- 

权限要求：部署使用的阿里云主账号或子账号需具备AliyunLogFullAccess权限。

如需自定义权限策略，请参考[AliyunCSManagedLogRolePolicy](products/ram/documents/developer-reference/aliyuncsmanagedlogrolepolicy.md)系统策略，将其包含的权限内容复制并赋予目标 RAM 用户或角色，以实现精细化的权限配置。

## 采集配置创建流程

- 

[安装](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[LoongCollector](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)：通过DaemonSet模式部署LoongCollector，确保集群中每个节点均运行一个采集容器，统一采集该节点上所有容器的日志。

- 

[创建](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)[LogStore](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)：LogStore是日志数据的存储单元，用于存储日志。一个 Project 内可创建多个 LogStore。

- 

创建采集配置YAML文件：[使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[连接集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)，您可以通过以下两种方式创建采集配置文件：

- 

方式一：使用采集配置生成器

通过日志服务控制台的[采集配置生成器](https://sls.console.aliyun.com/lognext/crd-generator)，可视化填写参数，自动生成标准YAML文件。

- 

方式二：手动编写YAML

结合本文档提供的典型场景示例与配置流程，根据实际业务需求手动编写 YAML 文件。建议按本文结构逐步构建配置：从极简配置起步 → 添加处理逻辑 → 启用高级功能。

对于本文未覆盖的复杂场景或需要深度定制的字段，可进一步参考[AliyunPipelineConfig](products/sls/documents/kubernetes-cr-parameter-description.md)[参数说明](products/sls/documents/kubernetes-cr-parameter-description.md)，获取完整字段列表、取值规则及插件能力详情。

一个完整的采集配置通常包含以下部分：

- 

- 

- 

- 

- 

- 

- 

| [极简配置（必选）](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md) ：构建从集群到日志服务的数据通道。包含两部分： 输入 （inputs） ：定义日志的来源。容器内日志包含以下两种日志源，如需采集其他类型日志（如 MySQL 查询结果）请参考 [输入插件](products/sls/documents/developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) 。 容器标准输出（stdout 与 stderr）：容器程序打印到控制台的日志内容。 文本日志文件：容器内部写入指定路径下的日志文件。 输出 （flushers） ：定义日志发送目标，将采集的日志发送至指定的 LogStore。 若目标 Project 或 LogStore 不存在，系统将自动创建。您也可以选择提前手动创建 [Project](products/sls/documents/manage-a-project.md) 和 [LogStore](products/sls/documents/manage-a-logstore.md) 。 [常用处理配置（可选）](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md) ：通过定义 processors 字段，对原始日志进行结构化解析（如正则解析、分隔符解析）或脱敏、过滤处理等。 本文仅介绍原生处理插件，覆盖常见日志处理场景，如需更多功能，请参考 [扩展处理插件](products/sls/documents/developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) 。 [其他高级配置（可选）](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md) ：实现多行文本日志的采集、日志标签富化等，满足更精细化的采集需求。 | 结构示例： apiVersion: telemetry.alibabacloud.com/v1alpha1 # 使用默认值，无需修改。 kind: ClusterAliyunPipelineConfig # 使用默认值，无需修改。 metadata: name: test-config # 设置资源名，在当前 Kubernetes 集群内唯一。 spec: project: # 设置目标 Project 名称。 name: k8s-your-project config: # 设置 Logtail 采集配置。 inputs: # 设置 Logtail 采集配置里的输入插件 ... processors: # 设置 Logtail 采集配置的处理插件 ... flushers: # 设置 Logtail 采集配置里的输出插件 ... |
| --- | --- |


- 

应用配置

kubectl apply -f <your_yaml>

## 安装LoongCollector（Logtail）

LoongCollector 是阿里云日志服务（SLS）推出的新一代日志采集 Agent，是 Logtail 的升级版，二者不能同时存在，如需安装Logtail，请参考[Logtail](products/sls/documents/install-run-upgrade-and-uninstall-logtail.md)[安装与配置](products/sls/documents/install-run-upgrade-and-uninstall-logtail.md)。

本文仅介绍LoongCollector的基础安装步骤，如需了解详细参数请参考[安装配置](products/sls/documents/loongcollector-installation-kubernetes-1.md)。如果您已安装LoongCollector或Logtail，可跳过此步骤，直接创建存储采集日志的[LogStore](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)。

## ACK集群

通过容器服务控制台安装LoongCollector，默认将日志发送到当前阿里云账号的日志服务Project中。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，进入集群详情页。

- 

在左侧导航栏，单击组件管理。

- 

在日志与监控页签中，找到loongcollector，单击安装。

说明

对于新建集群，在组件配置页面，勾选使用日志服务，支持创建新 Project或使用已有 Project。

安装完成后，日志服务会自动在ACK所属地域下创建相关资源，您可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | k8s-log-${cluster_id} | 资源管理单元，隔离不同业务日志。 如需自行创建 Project 以实现更灵活的日志资源管理，请参考 [创建](products/sls/documents/manage-a-project.md) [Project](products/sls/documents/manage-a-project.md) 。 |
| 机器组 | k8s-group-${cluster_id} | 日志采集节点集合。 |


重要

LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。

## 自建集群

- 

连接Kubernetes集群，并根据地域选择对应命令，下载LoongCollector及其依赖组件：

中国地域：

wget https://aliyun-observability-release-cn-shanghai.oss-cn-shanghai.aliyuncs.com/loongcollector/k8s-custom-pkg/3.0.12/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh

海外地域：

wget https://aliyun-observability-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/loongcollector/k8s-custom-pkg/3.0.12/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh

- 

进入loongcollector-custom-k8s-package目录，修改配置文件./loongcollector/values.yaml。

# ===================== 必需要补充的内容 ===================== # 管理采集日志的Project名，例如 k8s-log-custom-sd89ehdq。 projectName: "" # Project所属地域，例如上海：cn-shanghai region: "" # Project所属主账号uid，请用引号包围，例如"123456789" aliUid: "" # 使用网络，可选参数：公网Internet，内网Intranet，默认使用公网 net: Internet # 主账号或者子账号的AK，SK，需具备AliyunLogFullAccess系统策略权限 accessKeyID: "" accessKeySecret: "" # 自定义集群ID，命名只支持大小写，数字，短划线(-)。 clusterID: ""

- 

在loongcollector-custom-k8s-package目录下执行如下命令，安装LoongCollector及其他依赖组件：

bash k8s-custom-install.sh install

- 

安装完成后，查看组件运行状态。

若Pod未成功启动，请确认values.yaml配置是否正确，相关镜像拉取是否成功。

# 检查Pod状态 kubectl get po -n kube-system | grep loongcollector-ds

同时，日志服务会自动创建如下资源，可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | values.yaml 文件中自定义的 projectName 的值 | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | 日志采集节点集合。 |


重要

LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。

## 创建LogStore

若您已提前创建好LogStore，可直接跳过此步骤，进行[采集配置](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，单击目标Project名称。

- 

在左侧导航栏，选择日志存储，单击+。

- 

在创建LogStore页面，完成以下核心配置：

- 

Logstore名称：设置一个在Project内唯一的名称。该名称创建后不可修改。

- 

Logstore类型：根据规格对比选择标准型或查询型。

- 

计费模式：

- 

按使用功能计费：按存储、索引、读写次数等各项资源独立计费。适合小规模或功能使用不确定的场景。

- 

按写入数据量计费：仅按原始写入数据量计费，并提供30天的免费存储周期及免费的数据加工、投递等功能。成本模型简单，适合存储周期接近30天或数据处理链路复杂的场景。

- 

数据保存时间：设置日志的保留天数，取值范围为1~3650天（3650天表示永久保存）。默认为30天。

- 

其他配置保持默认，单击确定。如需了解其他配置信息，请参考[管理](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)。

## 极简配置

在[spec.config](products/sls/documents/kubernetes-cr-parameter-description.md)中，通过配置输入(inputs)与输出（flushers）插件，定义日志采集的核心路径：从哪里采集日志，以及日志要发送到哪里。

## 容器标准输出-新版

用途：采集直接打印到控制台的容器标准输出日志（stdout/stderr）。

- 

- 

- 

- 

- 

- 

- 

## 

- 

- 

- 

- 

| inputs 输入插件 采集配置的起点，定义日志来源。目前只允许配置 1 个输入插件。 Type String （必选） 插件类型，固定为 input_container_stdio 。 IgnoringStderr boolean （可选） 是否忽略标准错误流（stderr），默认为 false ： true ：不采集 stderr false ：采集 stderr IgnoringStdout boolean （可选） 是否忽略标准输出流（stdout），默认为 false ： true ：不采集 stdout false ：采集 stdout | 示例 apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: # 设置资源名，在当前 Kubernetes 集群内唯一，也是创建出的 Logtail 采集配置名。 name: new-stdio-config spec: project: name: test-not-exist logstores: - name: new-stdio-logstore # 定义 LoongCollector(Logtail)采集与处理配置。 config: # --- 输入插件：定义从哪里采集日志 --- inputs: # 使用 input_file 插件采集容器内文本日志 - Type: input_container_stdio IgnoringStderr: false IgnoringStdout: false # --- 处理插件（可选）：定义如何解析和处理日志 --- processors: [] # --- 输出插件：定义将日志发送到哪里 --- flushers: # 如无多目标发送需求，填写一个 flusher 即可 - Type: flusher_sls # 指定使用 SLS 输出插件 Logstore: new-stdio-logstore1 - Type: flusher_sls # 指定使用 SLS 输出插件 Logstore: new-stdio-logstore2 |
| --- | --- |
| flushers 输出插件 通过配置 flusher_sls 插件，将采集到的日志发送至指定 Project 下的 LogStore。最多配置 5 个输出插件。 Type String （必选） 插件类型，固定为 flusher_sls 。 LogStore String （必选） 目标 Logstrore 名称，决定日志的实际存储位置。 说明 指定 LogStore 必须存在或已在 [spec.LogStores](products/sls/documents/kubernetes-cr-parameter-description.md) 中声明。 配置多个输出目标后，该采集配置将不再显示在当前 LogStore 的采集配置列表中。如需查看、修改或删除多目标分发配置，请参考 [如何管理多目标分发配置？](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md) 。 |  |


## 采集容器内文本文件

用途：采集写入到容器内特定文件路径的日志，如传统的access.log或app.log。

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

## 

- 

- 

- 

- 

| inputs 输入插件 采集配置的起点，定义日志来源。目前只允许配置 1 个输入插件。 Type String （必选） 插件类型，固定为 input_file 。 FilePaths String （必选） 待采集的日志文件路径列表。 目前仅支持配置 1 个路径。 支持通配符： * ：匹配单层目录中的文件名 ** ：递归匹配多级子目录（仅能出现一次，且必须位于文件名前） MaxDirSearchDepth integer （可选） 当路径中包含 ** 时，指定通最大目录深度，默认为 0 ，取值范围：0～1000。 FileEncoding String （可选） 文件编码格式，默认为 utf8 。可选值： utf8 gbk EnableContainerDiscovery boolean （可选） 是否启用容器发现功能，默认为 true 。 说明 仅当 LoongCollector（Logtail）以 Daemonset 模式运行，且采集文件路径为容器内路径时有效。 | 示例 apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: name: easy-row-config spec: # 指定日志要发送到的目标 Project。 project: name: test-not-exist logstores: - name: easy-row-logstore # 定义 LoongCollector(Logtail)采集与处理配置。 config: # 日志样例（可不填写） sample: '' # --- 输入插件：定义从哪里采集日志 --- inputs: # 使用 input_file 插件采集容器内文本日志 - Type: input_file # ... 此处为输入插件的具体配置 ... # 容器内的文件路径 FilePaths: - /var/log/text1.log # 最大目录监控深度 MaxDirSearchDepth: 0 FileEncoding: utf8 # 启用容器发现功能。 EnableContainerDiscovery: true # --- 处理插件（可选）：定义如何解析和处理日志 --- processors: [] # --- 输出插件：定义将日志发送到哪里 --- flushers: # 如无多目标发送需求，填写一个 flusher 即可 - Type: flusher_sls # 指定使用 SLS 输出插件 Logstore: easy-row-logstore1 - Type: flusher_sls # 指定使用 SLS 输出插件 Logstore: easy-row-logstore2 |
| --- | --- |
| flushers 输出插件 通过 flusher_sls 插件，将采集到的日志发送至指定 Project 下的 LogStore。最多配置 5 个输出插件。 Type String （必选） 插件类型，固定为 flusher_sls 。 LogStore String （必选） 目标 LogStore 名称，决定日志的实际存储位置。 说明 指定 LogStore 必须存在或已在 [spec.LogStores](products/sls/documents/kubernetes-cr-parameter-description.md) 中声明。 配置多个输出目标后，该采集配置将不再显示在当前 LogStore 的采集配置列表中。如需查看、修改或删除多目标分发配置，请参考 [如何管理多目标分发配置？](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md) 。 |  |


## 常用处理配置

在完成[极简配置](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)后，您可以通过添加processors插件进行处理配置，将原始日志进行结构化解析或脱敏、过滤处理。

核心配置：在[spec.config](products/sls/documents/kubernetes-cr-parameter-description.md)中添加processors，配置处理插件，支持同时启用多个插件。

此处仅介绍原生处理插件，覆盖常见日志处理场景，如需更多功能，请参考[扩展处理插件](products/sls/documents/developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md)。

重要

对于Logtail 2.0及以上版本以及LoongCollector组件，推荐遵循以下插件组合规则：

- 

优先使用原生插件。

- 

当原生插件无法满足需求时，可在原生插件后配置扩展插件。

- 

原生插件只能在扩展插件之前使用。

### 结构化配置

## 正则解析

通过正则表达式提取日志字段，并将日志解析为键值对形式。

| 关键字段 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定为 processor_parse_regex_native 。 | # ...在 spec.config 下... processors: # 使用正则表达式解析插件解析日志内容 - Type: processor_parse_regex_native # 指定原始日志字段来源，通常为 content SourceKey: content # 正则表达式用于匹配并提取日志字段 Regex: >- (\S+)\s-\s(\S+)\s$$([^]]+)$$\s" (\w+)\s(\S+)\s([^"]+)" \s(\d+)\s(\d+)\s" ([^"]+)"\s" ([^"]+).* # 提取字段列表，按正则分组顺序对应 Keys: - remote_addr - remote_user - time_local - request_method - request_uri - request_protocol - status - body_bytes_sent - http_referer - http_user_agent # 解析失败时是否保留原始字段 KeepingSourceWhenParseFail: true # 解析成功时是否保留原始字段 KeepingSourceWhenParseSucceed: true # 如果保留原始字段，可以指定重命名后的字段名 RenamedSourceKey: fail |
| SourceKey String （必选） 源字段名。 |  |
| Regex String （必选） 匹配日志的正则表达式。 |  |
| Keys String （必选） 提取的字段列表。 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时，是否保留源字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时，是否保留源字段，默认为 false 。 |  |
| RenamedSourceKey String （可选） 保留源字段时，用于存储源字段的字段名，默认不改名。 |  |


## 分隔符解析

通过分隔符将日志内容结构化，解析为多个键值对形式。支持单字符分隔符和多字符分隔符。

- 

- 

- 

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_parse_delimiter_native 。 | # ...在 spec.config 下... processors: # 分隔符解析插件配置 - Type: processor_parse_delimiter_native # 原始字段来源，通常为 content SourceKey: content Separator: ',' Quote: '"' # 按顺序定义提取后的字段名 Keys: - time - ip - request - status - size - user_agent |
| SourceKey String （必选） 源字段名。 |  |
| Separator String （必选） 字段分隔符，例如 CSV 使用逗号 (,)。 |  |
| Keys [String] （必选） 提取的字段列表。 |  |
| Quote String （可选） 引用符，用于包裹包含特殊字符（如逗号）的字段内容。 |  |
| AllowingShortenedFields boolean （可选） 是否允许提取的字段数量小于 Keys 的数量，默认为 true 。若不允许，则此情景会被视为解析失败。 |  |
| OverflowedFieldsTreatment String （可选） 当提取的字段数量大于 Keys 的数量时的行为，默认为 extend 。可选值包括： extend ：保留多余的字段，且每个多余的字段都作为单独的一个字段加入日志，多余字段的字段名为 _column$i_ ，其中 $i 代表额外字段序号，从 0 开始计数。 keep ：保留多余的字段，但将多余内容作为一个整体字段加入日志，字段名为 _column0_ 。 discard ：丢弃多余的字段。 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时，是否保留源字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时，是否保留源字段，默认为 false 。 |  |
| RenamedSourceKey String （可选） 保留源字段时，用于存储源字段的字段名，默认不改名。 |  |


## 标准JSON解析

将Object类型的JSON日志结构化，解析为键值对形式。

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值为 processor_parse_json_native 。 | # ...在 spec.config 下... processors: # JSON 解析插件配置 - Type: processor_parse_json_native # 原始日志字段来源 SourceKey: content |
| SourceKey String （必选） 源字段名。 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时，是否保留源字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时，是否保留源字段，默认为 false 。 |  |
| RenamedSourceKey String （可选） 保留源字段时，用于存储源字段的字段名，默认不改名。 |  |


## 嵌套JSON解析

通过指定展开深度，将嵌套的JSON日志解析为键值对形式。

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

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_json 。 | # ...在 spec.config 下... processors: # 配置 JSON 字段展开插件 - Type: processor_json # 指定需要解析的原始字段名 SourceKey: content ExpandDepth: 0 ExpandConnector: '_' Prefix: expand IgnoreFirstConnector: false # 是否展开数组元素为独立字段 ExpandArray: false # 是否保留原始字段内容 KeepSource: true # 当原始字段缺失时是否报错 NoKeyError: true # 是否将原始字段名作为展开字段名的前缀 UseSourceKeyAsPrefix: false # 如果 JSON 解析失败，是否保留原始日志数据 KeepSourceIfParseError: true |
| SourceKey String （必选） 源字段名。 |  |
| ExpandDepth integer （可选） JSON 展开深度，默认值为 0。 0：表示展开到能解析成功的最深层级； 1：表示仅展开当前层级，以此类推。 |  |
| ExpandConnector String （可选） JSON 展开时字段名的连接符，默认为下划线（_）。 |  |
| Prefix String （可选） 指定 JSON 展开后字段名的前缀。 |  |
| IgnoreFirstConnector String （可选） 是否忽略第一个连接符，即是否在顶级字段前添加连接符，默认为 false 。 |  |
| ExpandArray boolean （可选） 是否展开数组类型，默认为 false 。 false（默认值）：不展开。 true：展开。例如 {"k":["1","2"]} 展开为 {"k[0]":"1","k[1]":"2"} 。 说明 Logtail 1.8.0 及以上版本支持该参数。 |  |
| KeepSource boolean （可选） 被解析后的日志中是否保留原始字段，默认为 true 。 true：保留 false：丢弃 |  |
| NoKeyError boolean （可选） 原始日志中没有指定的原始字段时，系统是否报错，默认为 true 。 true：报错 false：不报错 |  |
| UseSourceKeyAsPrefix boolean （可选） 是否将原始字段名作为所有 JSON 展开字段名的前缀。 |  |
| KeepSourceIfParseError boolean （可选） 解析日志失败时，是否保留原始日志，默认为 true 。 true：保留 false：丢弃 |  |


## JSON数组解析

使用json_extract函数，从JSON数组中提取JSON对象，更多json函数请参考[JSON](products/sls/documents/json-functions.md)[函数](products/sls/documents/json-functions.md)。

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，SPL 插件类型为 processor_spl 。 | # ...在 spec.config 下... processors: # 使用 SPL 脚本处理日志字段 - Type: processor_spl # 脚本超时时间（单位：毫秒） TimeoutMilliSeconds: 1000 # SPL 脚本内容，用于从 content 字段中提取 JSON 数组中的元素 Script: >- * | extend json1 = json_extract(content, '$[0]'), json2 = json_extract(content, '$[1]') |
| Script String （必选） SPL 脚本内容，用于从 content 字段中提取 JSON 数组中的元素。 |  |
| TimeoutMilliSeconds integer （可选） 脚本超时时间，取值范围 0~10000，单位为毫秒，默认 1000。 |  |


## Nginx日志解析

根据log_format中的定义将日志内容结构化，解析为多个键值对形式。如默认内容不符合您的需求，可使用自定义格式。

- 

- 

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，Nginx 日志解析的插件类型为 processor_parse_regex_native 。 | # ...在 spec.config 下... processors: # NGINX 日志解析插件配置 - Type: processor_parse_regex_native # 原始日志字段来源 SourceKey: content # 正则表达式解析规则 Regex: >- (\S*)\s*-\s*(\S*)\s*\[ (\d+/\S+/\d+:\d+:\d+:\d+)\s+\S+\] \s*"(\S+)\s+(\S+)\s+\S+" \s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*) \s*"([^"]*)"\s*"([^"]*)".* # 提取字段映射 Keys: - remote_addr - remote_user - time_local - request_method - request_uri - request_time - request_length - status - body_bytes_sent - http_referer - http_user_agent # NGINX 特定配置 Extra: Format: >- log_format main '$remote_addr - $remote_user [$time_local] "$request" ''$request_time $request_length ''$status $body_bytes_sent "$http_referer" ''"$http_user_agent"'; LogType: NGINX |
| SourceKey String （必选） 源字段名。 |  |
| Regex integer （必选） 正则表达式。 |  |
| Keys String （必选） 提取的字段列表。 |  |
| Extra Format String （必选） Nginx 配置文件中的日志配置部分，以 log_format 开头。 生产环境中，此处的 log_format 必须与 Nginx 配置文件（通常位于 /etc/nginx/nginx.conf 文件中）中的定义保持一致。 LogType String （必选） 解析日志类型，固定值为 NGINX 。 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时是否保留原始字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时是否保留原始字段，默认为 false 。 |  |
| RenamedSourceKey String （可选） 保留原始字段时，用于存储原始的字段名，默认不改名。 |  |


## Apache日志解析

根据Apache日志配置文件中的定义将日志内容结构化，解析为多个键值对形式。

- 

- 

- 

- 

- 

- 

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值为 processor_parse_regex_native 。 | # ...在 spec.config 下... processors: # 配置 Apache Combined 日志解析插件（基于正则表达式） - Type: processor_parse_regex_native # 原始日志字段来源，通常为 content SourceKey: content # 正则表达式用于匹配并提取 Apache combined 格式日志 Regex: >- ([0-9.-]+)\s # remote_addr ([\w.-]+)\s # remote_ident ([\w.-]+)\s # remote_user (\[[^\[\]]+\]|-)\s # time_local "((?:[^"]|\")+)"\s # request_method + request_uri + request_protocol "((?:[^"]|\")+)"\s # request_uri（重复捕获？需注意逻辑） "((?:[^"]|\")+)"\s # request_protocol (\d{3}|-)\s # status (\d+|-)\s # response_size_bytes "((?:[^"]|\")+)"\s # http_referer "((?:[^"]|\"|')+)" # http_user_agent # 提取字段列表，按正则分组顺序对应 Keys: - remote_addr - remote_ident - remote_user - time_local - request_method - request_uri - request_protocol - status - response_size_bytes - http_referer - http_user_agent # 插件附加信息（非必须，用于说明日志格式） Extra: Format: >- LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined LogType: Apache SubType: combined |
| SourceKey String （必选） 源字段名。 |  |
| Regex integer （必选） 正则表达式。 |  |
| Keys String （必选） 提取的字段列表。 |  |
| Extra Format String （必选） Apache 配置文件中的日志配置部分，通常以 LogFormat 开头。 LogType String （必选） 解析日志类型，固定值为 Apache 。 SubType String （必选） 日志格式。 common combined 自定义 |  |
| KeepingSourceWhenParseFail boolean （可选） 解析失败时是否保留原始字段，默认为 false 。 |  |
| KeepingSourceWhenParseSucceed boolean （可选） 解析成功时是否保留原始字段，默认为 false 。 |  |
| RenamedSourceKey String （可选） 保留原始字段时，用于存储原始的字段名，默认不改名。 |  |


### 数据脱敏

使用processor_desensitize_native插件对日志中的敏感数据进行脱敏处理。

- 

- 

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_desensitize_native 。 | # ...在 spec.config 下... processors: # 配置原生日志脱敏插件 - Type: processor_desensitize_native # 原始字段名 SourceKey: content # 脱敏方式：const 表示用固定字符串替换敏感内容 Method: const # 替换敏感内容的目标字符串 ReplacingString: '********' # 被替换内容前的内容表达式 ContentPatternBeforeReplacedString: 'password'':''' # 敏感内容本身的正则表达式，匹配要被替换的内容 ReplacedContentPattern: '[^'']*' # 是否替换所有匹配项，默认为 true ReplacingAll: true |
| SourceKey String （必选） 源字段名。 |  |
| Method String （必选） 脱敏方式。可选值包括： const ：用常量替换敏感内容。 md5 ：用敏感内容的 MD5 值替换相应内容。 |  |
| ReplacingString String （可选） 用于替换敏感内容的常量字符串。当 Method 取值为 const 时必选。 |  |
| ContentPatternBeforeReplacedString String （必选） 敏感内容的前缀正则表达式。 |  |
| ReplacedContentPattern String （必选） 敏感内容的正则表达式。 |  |
| ReplacingAll boolean （可选） 解析成功时是否保留原始字段，默认为 true 。 |  |


### 内容过滤

通过配置processor_filter_regex_native插件，基于正则表达式匹配日志字段值，仅保留满足条件的日志。

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_filter_regex_native 。 | # ...在 spec.config 下... processors: # 配置正则表达式过滤插件（可用于日志脱敏或敏感词过滤） - Type: processor_filter_regex_native # 定义正则表达式列表，用于匹配日志字段的内容 FilterRegex: # 示例：匹配日志字段值中包含 "WARNING" 或 "ERROR" 的内容 - WARNING|ERROR # 指定需要匹配的日志字段名，示例为对 level 字段进行过滤 FilterKey: - level |
| FilterRegex String （必选） 匹配日志字段的正则表达式。 |  |
| FilterKey String （必选） 匹配的日志字段名。 |  |


### 时间解析

配置 processor_parse_timestamp_native 插件对日志中的时间字段进行解析，并将解析结果设置为日志的__time__字段。

- 

- 

| 关键字段详解 | 示例 |
| --- | --- |
| Type String （必选） 插件类型，固定值 processor_parse_timestamp_native 。 | # ...在 spec.config 下... processors: # 配置原生时间解析插件 - Type: processor_parse_timestamp_native # 原始日志字段来源，通常为 content SourceKey: content # 时间格式定义，需与日志中的时间字段格式完全匹配 SourceFormat: '%Y-%m-%d %H:%M:%S' SourceTimezone: 'GMT+00:00' |
| SourceKey String （必选） 源字段名。 |  |
| SourceFormat String （必选） [时间格式](products/sls/documents/time-parsing.md) ，需与日志中的时间字段格式完全匹配。 |  |
| SourceTimezone String （可选） 日志时间所属时区，默认使用机器时区，即 LoongCollector 进程所在环境的时区。 格式： GMT+HH:MM ：东区 GMT-HH:MM ：西区 |  |


## 其他高级配置

在完成[极简配置](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)后，您可以参考下述操作采集多行日志、配置日志主题类型等，以满足更精细化的日志采集需求。以下是常见高级配置及其功能：

- 

配置多行日志采集：当一条日志内容（如异常堆栈信息）占用多行时，需启用多行模式，并配置行首正则表达式以匹配日志的起始行，将占用多行的日志作为一条日志采集并存储到日志服务的LogStore中。

- 

配置日志主题类型：为不同的日志流设置不同的主题（Topic），可用于组织和分类日志数据，更好地管理和检索相关日志。

- 

指定容器采集（过滤与黑名单）：指定特定容器与路径采集，包括白名单与黑名单配置。

- 

日志标签富化：将环境变量、Pod标签相关的元信息添加到日志中，作为日志的扩展字段。

### 配置多行日志采集

日志服务默认为单行模式，按行进行日志的切分与存储，导致含堆栈信息的多行日志被逐行切分，每一行作为独立日志存储和展示，不利于分析。

针对上述问题，可通过开启多行模式来改变日志服务的切分方式，并通过配置正则表达式匹配日志起始行，从而将原始日志按照起始行规则进行切分和存储。

核心配置：在[spec.config.inputs](products/sls/documents/kubernetes-cr-parameter-description.md)配置中添加Multiline参数。

- 

- 

- 

- 

| 关键字段详解 | 示例 |
| --- | --- |
| Multiline 开启多行日志采集功能。 Mode 模式选择，默认值为 custom 。 custom ：表示自定义正则表达式匹配行首。 JSON ：多行 JSON。 StartPattern 行首正则表达式，Mode 取值为 custom 时必填 。 | # ...在 spec.config 下... inputs: - Type: input_file # 开启多行日志采集功能 Multiline: # 模式选择：custom 表示自定义正则表达式匹配行首 Mode: custom # 正则表达式匹配每条日志的起始行（即新日志开始的标志） StartPattern: '\d+-\d+-\d+\s\d+:\d+:\d+' |


### 配置日志主题类型

核心配置：在[spec.config](products/sls/documents/kubernetes-cr-parameter-description.md)中增加global参数以设置Topic。

- 

- 

- 

## 

## 

## 

| 关键字段详解 | 示例 |
| --- | --- |
| TopicType topic 类型，可选值： machine_group_topic ：机器组 topic，用于区分来自不同机器组的日志。 filepath ：文件路径提取，用于区分不同用户或应用产生的日志数据。 custom ：自定义，使用自定义的静态日志主题。 | 机器组 Topic spec: config: global: #将应用该配置的机器组 Topic 作为 Topic TopicType: machine_group_topic 文件路径提取 spec: config: global: TopicType: filepath # Topic 格式。当 TopicType 取值为 filepath 或 custom 时必填。 # 提取结果为__topic__: userA，__topic__: userB，__topic__: userC TopicFormat: \/data\/logs\/(.*)\/serviceA\/.* 自定义 spec: config: global: TopicType: custom # Topic 格式。当 TopicType 取值为 filepath 或 custom 时必填。 TopicFormat: customized:// + 自定义主题名 |
| TopicFormat Topic 格式。当 TopicType 取值为 filepath 或 custom 时必填。 |  |


### 指定容器采集（过滤与黑名单）

## 过滤

只采集符合条件的容器，多个条件之间为“且”的关系，任意条件为空表示忽略该条件；条件支持使用正则表达式。

核心配置：在[spec.config.inputs](products/sls/documents/kubernetes-cr-parameter-description.md)中配置ContainerFilters容器过滤相关参数。

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

| 关键字段详解 | 示例 |
| --- | --- |
| ContainerFilters 容器过滤 Pod 标签黑/白名单 IncludeK8sLabel K8s Pod 标签白名单，指定需要采集日志的容器。 ExcludeK8sLabel K8s Pod 标签黑名单：排除符合特定条件的容器日志采集。 环境变量黑白名单 IncludeEnv 环境变量白名单 ExcludeInv 环境变量黑名单 Pod/Namespace/容器名称正则匹配 K8sNamespaceRegex Namespace 正则匹配 K8sPodRegex Pod 名称正则匹配 K8sContainerRegex 容器名称正则匹配 所有正则匹配均基于 Go 语言的 RE2 正则引擎，功能较 PCRE 等引擎有所限制，请遵循 [附录：正则表达式使用限制（容器过滤）](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md) 编写正则表达式。 | # ...在 spec.config 下... inputs: - Type: input_file # 或 input_container_stdio # 当输入插件类型为 input_file 时，需配置：启用容器发现功能为 true。 EnableContainerDiscovery: true # 容器过滤 ContainerFilters: # K8s Pod 标签白名单：指定需要采集日志的容器 IncludeK8sLabel: # 示例：匹配所有包含 app 标签且标签值为 nginx 或 redis 的 Pod。 app: ^(nginx|redis)$ # K8s Pod 标签黑名单：排除符合特定条件的容器日志采集 ExcludeK8sLabel: # 示例：排除所有包含 app:test 标签的 Pod app: test # 环境变量白名单 IncludeEnv: # 匹配所有包含 NGINX_SERVICE_PORT=80 或 NGINX_SERVICE_PORT=6379 的容器。 NGINX_SERVICE_PORT: ^(80|6379)$ # 环境变量黑名单 ExcludeEnv: # 排除所有 ENVIRONMENT=test 的容器。 ENVIRONMENT: test # Namespace 正则匹配，示例为匹配 default 和 nginx 命名空间下的所有容器。 K8sNamespaceRegex: ^(default|nginx)$ # Pod 名称正则匹配，示例为匹配所有以 nginx-log-demo 开头的 Pod 下的容器。 K8sPodRegex: ^(nginx-log-demo.*)$ # 容器名称正则匹配，示例为匹配所有名为 container-test 的容器 K8sContainerRegex: ^(container-test)$ |


## 黑名单

排除指定条件的文件。需要在YAML的config.inputs下按需使用如下参数：

## 

| 关键字段详解 | 示例 # ...在 spec.config 下... inputs: - Type: input_file # 文件路径黑名单，排除指定条件的文件。路径必须为绝对路径，支持使用 * 通配符。 ExcludeFilePaths: - /var/log/*.log # 文件名黑名单，排除指定条件的文件。支持使用 * 通配符。 ExcludeFiles: - test # 目录黑名单，排除指定条件的文件。路径必须为绝对路径，支持使用 * 通配符。 ExcludeDirs: - /var/log/backup* |
| --- | --- |
| ExcludeFilePaths 文件路径黑名单，排除指定条件的文件。路径必须为绝对路径，支持使用 * 通配符。 |  |
| ExcludeFiles 文件名黑名单，排除指定条件的文件。支持使用 * 通配符。 |  |
| ExcludeDirs 目录黑名单，排除指定条件的文件。路径必须为绝对路径，支持使用 * 通配符。 |  |


### 日志标签富化

核心配置：通过在[spec.config.inputs](products/sls/documents/kubernetes-cr-parameter-description.md)中配置ExternalEnvTag和ExternalK8sLabelTag，向日志中添加与容器环境变量、Pod标签相关的tag。

| 关键字段详解 | 示例 |
| --- | --- |
| ExternalEnvTag 将指定的环境变量值映射为 tag 字段，格式为： <环境变量名>: <tag 名> 。 | # ...在 spec.config 下... inputs: - Type: input_file # 或 input_container_stdio ExternalEnvTag: <环境变量名>: <tag 名> ExternalK8sLabelTag: <Pod 标签名>: <tag 名> |
| ExternalK8sLabelTag 将 Kubernetes Pod 的标签值映射为 tag 字段，格式为： <Pod 标签名>: <tag 名> 。 |  |


## 常见场景完整配置示例

### 场景一：采集Nginx Access log并解析为结构化字段

解析Nginx日志，根据log_format中的定义将日志内容结构化，解析为多个键值对形式。

完整YAML示例

apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: name: nginx-config spec: config: aggregators: [] global: {} inputs: - Type: input_file FilePaths: - /root/log/text1.log MaxDirSearchDepth: 0 FileEncoding: utf8 EnableContainerDiscovery: true processors: - Type: processor_parse_regex_native SourceKey: content Regex: >- (\S*)\s*-\s*(\S*)\s*\[(\d+/\S+/\d+:\d+:\d+:\d+)\s+\S+\]\s*"(\S+)\s+(\S+)\s+\S+"\s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*"([^"]*)"\s*"([^"]*)".* Keys: - remote_addr - remote_user - time_local - request_method - request_uri - request_time - request_length - status - body_bytes_sent - http_referer - http_user_agent Extra: Format: >- log_format main '$remote_addr - $remote_user [$time_local] "$request" ''$request_time $request_length ''$status $body_bytes_sent "$http_referer" ''"$http_user_agent"'; LogType: NGINX flushers: - Type: flusher_sls Logstore: my-log-logstore sample: >- 192.168.*.* - - [15/Apr/2025:16:40:00 +0800] "GET /nginx-logo.png HTTP/1.1" 0.000 514 200 368 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.*.* Safari/537.36" project: name: my-log-project logstores: - name: my-log-logstore

### 场景二：采集并处理多行日志

日志服务默认为单行模式，按行进行日志的切分与存储，导致含堆栈信息的多行日志被逐行切分，每一行作为独立日志存储和展示，不利于分析。

针对上述问题，可通过开启多行模式来改变日志服务的切分方式，并通过配置正则表达式匹配日志起始行，从而将原始日志按照起始行规则进行切分和存储。示例如下：

完整YAML示例

apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: name: multiline-config spec: config: aggregators: [] global: {} inputs: - Type: input_file FilePaths: - /root/log/text1.log MaxDirSearchDepth: 0 FileEncoding: utf8 Multiline: StartPattern: '\[\d+-\d+-\w+:\d+:\d+,\d+]\s\[\w+]\s.*' Mode: custom UnmatchedContentTreatment: single_line EnableContainerDiscovery: true processors: [] flushers: - Type: flusher_sls Logstore: my-log-logstore sample: |- [2023-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened at TestPrintStackTrace.f(TestPrintStackTrace.java:3) at TestPrintStackTrace.g(TestPrintStackTrace.java:7) at TestPrintStackTrace.main(TestPrintStackTrace.java:16) project: name: my-log-project logstores: - name: my-log-logstore

## 常见问题

### 如何管理多目标分发配置？

由于多目标分发配置关联了多个日志库，这类配置需要通过 Project 级别的管理页面进行维护：

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)，单击目标Project名称。

- 

在目标Project页面，单击左侧导航栏资源>配置管理。

说明

此页面集中管理Project下的所有采集配置，包括那些因日志库被误删而残留的配置。

### 如何将ACK集群日志传输到另一个阿里云账号的Project？

通过在ACK集群中手动安装日志服务LoongCollector（Logtail）组件，并为其配置目标账号的主账号ID或访问凭证（AccessKey），即可实现将容器日志发送到另一个阿里云账号的日志服务Project中。

场景描述：当因为组织架构、权限隔离或统一监控等原因，需要将某个ACK集群的日志数据采集到另一个独立的阿里云账号的日志服务Project时，可通过手动安装 LoongCollector（Logtail）进行跨账号配置。

操作步骤：此处以手动安装LoongCollector为例，如需了解如何安装Logtail，请参考[Logtail](products/sls/documents/install-run-upgrade-and-uninstall-logtail.md)[安装与配置](products/sls/documents/install-run-upgrade-and-uninstall-logtail.md)。

- 

连接Kubernetes集群，并根据地域选择对应命令，下载LoongCollector及其依赖组件：

中国地域：

wget https://aliyun-observability-release-cn-shanghai.oss-cn-shanghai.aliyuncs.com/loongcollector/k8s-custom-pkg/3.0.12/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh

海外地域：

wget https://aliyun-observability-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/loongcollector/k8s-custom-pkg/3.0.12/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh

- 

进入loongcollector-custom-k8s-package目录，修改配置文件./loongcollector/values.yaml。

# ===================== 必需要补充的内容 ===================== # 管理采集日志的Project名，例如 k8s-log-custom-sd89ehdq。 projectName: "" # Project所属地域，例如上海：cn-shanghai region: "" # Project所属主账号uid，请用引号包围，例如"123456789" aliUid: "" # 使用网络，可选参数：公网Internet，内网Intranet，默认使用公网 net: Internet # 主账号或者子账号的AK，SK，需具备AliyunLogFullAccess系统策略权限 accessKeyID: "" accessKeySecret: "" # 自定义集群ID，命名只支持大小写，数字，短划线(-)。 clusterID: ""

- 

在loongcollector-custom-k8s-package目录下执行如下命令，安装LoongCollector及其他依赖组件：

bash k8s-custom-install.sh install

- 

安装完成后，查看组件运行状态。

若Pod未成功启动，请确认values.yaml配置是否正确，相关镜像拉取是否成功。

# 检查Pod状态 kubectl get po -n kube-system | grep loongcollector-ds

同时，日志服务会自动创建如下资源，可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | values.yaml 文件中自定义的 projectName 的值 | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | 日志采集节点集合。 |


重要

LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。

### 如何让同一个日志文件或容器标准输出被多个采集配置同时采集？

默认情况下，日志服务为了防止数据重复，限制了每个日志源只能被一个采集配置采集：

- 

一个 文本日志文件只能匹配一个 Logtail 采集配置；

- 

一个 容器的标准输出（stdout） 也只能被一个标准输出采集配置采集。

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)，进入目标Project。

- 

在左侧导航选择日志库，找到目标LogStore。

- 

单击其名称前的展开LogStore。

- 

单击Logtail配置，在配置列表中，找到目标Logtail配置，单击操作列的管理Logtail配置。

- 

在Logtail配置页面，单击编辑，下滑至输入配置区域：

- 

采集文本文件日志：开启允许文件多次采集。

- 

采集容器标准输出：开启允许标准输出多次采集。

## 附录：正则表达式使用限制（容器过滤）

容器过滤时所使用的正则表达式基于Go语言的RE2引擎，与PCRE等其他引擎相比存在部分语法限制。请在编写正则表达式时注意以下事项：

1. 命名分组语法差异

Go语言使用(?P<name>...)语法定义命名分组，不支持 PCRE中的(?<name>...)语法。

- 

正确示例：(?P<year>\d{4})

- 

错误写法：(?<year>\d{4})

2. 不支持的正则特性

以下常见但复杂的正则功能在RE2中不可用，请避免使用：

- 

断言：(?=...)、(?!...)、(?<=...)、（?<!...)

- 

条件表达式：(?(condition)true|false)

- 

递归匹配：(?R)、(?0)

- 

子程序引用：(?&name)、(?P>name)

- 

原子组：(?>...)

3. 使用建议

推荐使用[Regex101](https://regex101.com/)等工具调试正则表达式时，选择 Golang (RE2) 模式进行验证，以确保兼容性。若使用了上述不支持的语法，插件将无法正确解析或匹配。

[上一篇：通过控制台采集集群容器日志（标准输出/文件）](products/sls/documents/collect-kubernetes-cluster-text-logs-daemonset.md)[下一篇：AliyunPipelineConfig参数说明](products/sls/documents/kubernetes-cr-parameter-description.md)

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
