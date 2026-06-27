# AliyunPipelineConfig CR的YAML结构与字段详解-日志服务-阿里云-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/kubernetes-cr-parameter-description

# AliyunPipelineConfig参数说明
当您使用[ClusterAliyunPipelineConfig](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)创建日志采集配置时，需要通过一个结构化的YAML文件定义采集规则。本文介绍该YAML文件的整体结构及各字段的含义。
重要
CRD创建的采集配置内容请以CR为准，禁止在控制台修改，若在控制台进行修改，改动内容会被CR覆盖，可能导致数据格式异常或丢失。
## 工作原理
创建CR资源：用户通过 kubectl 提交ClusterAliyunPipelineConfigYAML 文件，定义采集规则。
控制器监听变化：loongcollector-operator 持续监听集群中CR资源的变更。
同步配置：当检测到 CR 变化时，operator 将其转换为具体配置，并提交到指定Project。
采集器拉取最新配置：loongcollector-ds定时向日志服务发送心跳获取配置更新，拉取最新的采集配置并热加载。
开始采集与上报：loongcollector-ds 根据最新配置采集日志，并通过配置的接入点发送到 SLS。
## 基础字段
定义API版本与资源类型，所有配置都必须以此开头：
apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig
## 结构示例
apiVersion: telemetry.alibabacloud.com/v1alpha1 # 使用默认值，无需修改。 kind: ClusterAliyunPipelineConfig # 使用默认值，无需修改。 metadata: name: test-config # 设置资源名，在当前Kubernetes集群内唯一。 spec: project: # 设置目标Project名称。 name: k8s-your-project config: # 设置Logtail采集配置。 inputs: # 设置Logtail采集配置里的输入插件 ... flushers: # 设置Logtail采集配置里的输出插件 ...
## 核心参数说明
### metadata.name
采集配置名称，必填，在Project内唯一，创建后不可修改。
| 命名规则： 只能包含：小写字母、数字、-和_。 必须以小写字母或数字开头和结尾。 长度限制：2~128 字符。 | 示例： metadata: name: nginx-access-log |
| --- | --- |
### spec.projecct
目标Project信息。
说明
project字段在CR创建后不允许更改，如需切换project请创建新的CR。
| 参数 | 数据类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 目标 Project 的名称，若不存在会自动创建。 |
| description | string | 否 | Project 的描述（仅在创建时生效）。 |
| endpoint | string | 否 | Project 所在地域的 [服务入口](developer-reference/service-entrance.md) ，默认值为集群所在的地域。 该参数仅控制采集配置的创建地域，不控制采集器数据投递目标。 如需跨地域采集，请配置 [config_server_address](logtail-configuration-files-and-record-files.md) [和](logtail-configuration-files-and-record-files.md) [data_server_list](logtail-configuration-files-and-record-files.md) 。 |
| uid | string | 否 | 目标 Project 所属的阿里云主账号的 uid。默认值为当前集群所属的主账号 uid。 该参数仅控制采集配置创建到哪个账号下。 如需跨账号采集日志，请同步配置 alibaba-log-controller 组件的环境变量： ALICLOUD_LOG_ACCOUNT_INFOS={"<uid>":{"accessKeyID":"<your_access_key_id>","accessKeySecret":"<your_access_key_secret>"}} 。 |
### spec.config
采集配置主体，定义具体的输入、处理、输出插件。
| 子字段 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| sample | string | 否 | 日志样例，支持多条日志，总长度不超过 1500 字节。 |
| global | object | 否 | [全局配置](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) 。 |
| inputs | object 列表 | 是 | [输入插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) 列表，目前只允许配置 1 个输入插件。 |
| processors | object 列表 | 否 | 处理插件列表： [原生插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) [扩展插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) |
| flushers | object 列表 | 是 | [输出插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md) 列表，目前只允许存在 1 个 flusher_sls 插件。 |
### spec.LogStores
可选配置，用于声明需要创建的LogStore，其作用如下：
仅在创建时生效：所有参数（除name外）都只在 LogStore 首次创建时有效。如果 LogStore 已存在，这些配置将被忽略，不会影响已有 LogStore 的属性。
不决定数据发送目标：此列表不控制日志发送到哪个 LogStore。真正的发送目标由config.flushers中的输出插件（如flusher_sls）决定。
可选配置：如果目标 LogStore 已经存在，可以不用在此处定义。
仅支持增删，不支持修改：可以向列表中添加新的 LogStore 或删除某项，但无法通过更新此配置来修改已创建的 LogStore 属性（如 TTL、Shard 数量等）。如需修改，请通过控制台或 API 操作。
| 参数 | 数据类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 需要创建的 LogStore 名称。 |
| queryMode | string | 否 | [LogStore](manage-a-logstore.md) [规格对比](manage-a-logstore.md) 。默认值为 standard ，可选值： query ：查询型 LogStore。 standard ：标准型 LogStore。 |
| ttl | int | 否 | [数据保留天数](manage-a-logstore.md) （1~3650）默认 30，3650 表示永久。 |
| hotTtl | int | 否 | [热数据存储时间](data-tiered-storage-overview.md) （以天为单位）。默认 0，需要小于 ttl 且大于等于 7。 |
| infrequentAccessTTL | int | 否 | 目标 LogStore 的 [低频存储时间](data-tiered-storage-overview.md) （以天为单位）。默认值为 0，需要 hotTtl 存在、小于 ttl 且大于等于 30，如果 hotTtl+infrequentAccessTTL 不等于 ttl，还需要 ttl-(hotTtl+infrequentAccessTTL)>=60 。该参数需要 loongcollector-operator 组件版本号大于等于 1.0.6 有效。 |
| shardCount | int | 否 | Shard 数量。默认值为 2，取值范围为 1~100。 |
| maxSplitShard | int | 否 | 最大自动分裂 Shard 数量。默认值为 64，取值范围为 1~256。 |
| autoSplit | bool | 否 | 是否开启自动分裂 Shard。默认值为 true。 |
| telemetryType | string | 否 | 可观测数据类型。默认值为 None，可选值： None ：日志数据。 Metrics ：时序数据。 |
| appendMeta | bool | 否 | 是否记录外网 IP 地址和日志接收时间。默认值为 true。 true ：开启记录外网 IP 和日志接收时间功能，开启后日志服务自动把日志来源设备的公网 IP 地址和日志到达服务端的时间添加到日志的 Tag 字段中。 false ：不开启记录外网 IP 和日志接收时间功能。 |
| enableTracking | bool | 否 | 是否启用 WebTracking 功能。默认值为 false。 |
| encryptConf | object | 否 | [加密配置数据结构](developer-reference/api-sls-2020-12-30-struct-encryptconf.md) ，包含参数 enable 、 encrypt_type 、 user_cmk_info 。默认值为空。 |
| meteringMode | string | 否 | [计费模式](billing-methods.md) 。更多信息，请参见 [管理](manage-a-logstore.md) [LogStore](manage-a-logstore.md) 。默认值为空，可选值： ChargeByFunction ：按功能计费 ChargeByDataIngest ：按写入量计费。 说明 如果 LogStore 的 queryMode 为 query，只支持按功能计费。 如果账号未开通写入量计费，无法配置为 ChargeByDataIngest。 |
| index | object | 否 | 指定索引（仅限 LogStore 创建时生效），格式参考通用数据格式 [index](developer-reference/api-sls-2020-12-30-struct-index.md) 。该参数需要 loongcollector-operator 组件版本号大于等于 1.0.6 有效。 |
### spec.machineGroups
指定哪些机器组可以应用此采集配置。
默认行为：安装LoongCollector时，系统会自动创建的名为k8s-group-${clusterId}的机器组。若未显式设置machineGroups，将默认关联该机器组。
同步机制：loongcollector-operator会确保采集配置所关联的机器组严格等于machineGroups中定义的列表。任何不在该列表中的机器组都会被自动解除关联。
自动创建支持：如果指定的机器组不存在，系统会自动创建同名的[标识型机器组](create-a-user-defined-identity-machine-group.md)，并将其与当前采集配置绑定。
| 参数 | 数据类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 否 | 要关联的机器组名称。 |
### spec.enableUpgradeOverride
可选，是否允许覆盖旧配置。用于解决新旧版采集配置之间的冲突问题，默认为false。
true：loongcollector-operator会对已有的AliyunLogConfig定义的采集配置进行覆盖升级。
false：采集配置存在冲突，AliyunPipelineConfig应用失败。
使用场景：当集群中存在AliyunLogConfig定义的采集配置、且与当前的AliyunPipelineConfig指向同一个采集配置时，就会发生冲突。
同一个采集配置的定义：
Project 相同
AliyunLogConfig：使用集群默认 Project 或spec.project
AliyunPipelineConfig：使用spec.project.name
采集配置名称相同
AliyunLogConfig：spec.logtailConfig.configName
AliyunPipelineConfig：metadata.name
覆盖升级过程：
新配置生效
ClusterAliyunPipelineConfig被应用，更新采集配置。
旧配置清理
如果更新成功，控制器会自动删除集群中对应的AliyunLogConfig资源。
完成迁移
完成从旧方式到新方式的平滑过渡。
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
