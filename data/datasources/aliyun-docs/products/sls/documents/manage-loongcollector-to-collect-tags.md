# 管理LoongCollector采集Tag-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/manage-loongcollector-to-collect-tags

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

# 管理LoongCollector采集Tag

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Tag是日志服务中用于标识数据的字段，如来源IP、文件路径等。使用LoongCollector采集数据时，采集器会自动添加Tag。本文主要介绍了如何对这些 Tag 进行自定义操作，例如添加、删除、重命名。

## 使用限制

- 

本功能仅支持LoongCollector 3.0.10及以上版本。如使用Logtail或低版本LoongCollector，建议升级至LoongCollector最新版本。

- 

使用本功能会修改Tag的名称、存储位置。如在日志消费中依赖修改的Tag字段，可能造成不兼容问题。

## Tag分类

Tag字段类似于字段索引，包含key和value两部分。例如：__tag__:__inode__:263554，__tag__:__inode__为Tag名称（key），263554为Tag值（value）。

Tag根据来源主要分为两类：

- 

Agent相关：与采集 Agent 本身相关，不依赖插件。 如 IP、主机名称等。

- 

输入插件相关：依赖输入插件，由输入插件提供并富化相关信息到日志中。如文件 inode、读取偏移量、Pod 名称、Namespace、镜像名称等。

## 计费说明

Tag字段本身不收费，但若将其设置为索引字段，则会产生费用，具体收费标准详见[计费说明](products/sls/documents/create-indexes.md)。关于字段索引的设置与删除操作，可参考[创建索引](products/sls/documents/create-indexes.md)。

## 创建/修改 Tag名称

LoongCollector 对Tag进行了规范化，并实现了Tag处理功能。您可以配置高级参数，来控制 Tag 的添加、删除和重命名。

### Agent相关Tag

该类 Tag 不依赖任何输入插件，属于全局参数。您可以在创建采集配置或者修改采集配置时添加配置参数，本文以修改采集配置为例，创建采集配置请参见[创建采集配置](products/sls/documents/manage-logtail-configurations-for-log-collection.md)。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。在Project列表区域，单击目标Project。

- 

单击日志存储下您的Logstore，在Logtail配置中添加Logtail配置，单击立即接入，本例使用正则-文本日志，表示将以正则匹配的方式解析文本日志。

- 

在Logtail配置列表中，单击目标Logtail采集配置。

- 

在Logtail配置页面，单击编辑。

- 

在全局配置中单击其他全集配置，在高级参数后边单击，配置Agent自身相关Tag。

{ "PipelineMetaTagKey": { "HOST_NAME": "sourceName", "AGENT_TAG": "__default__", "HOST_ID": "__default__", "CLOUD_PROVIDER": "__default__" } }

- 

- 

- 

- 

| 参数名 | 类型 | 是否必填 | 默认值 | 样例 | 说明 |
| --- | --- | --- | --- | --- | --- |
| PipelineMetaTagKey | object | 否 | 空 | {"HOST_NAME":"__hostname__"} | key 为 Tag 参数名，value 为 Tag 在日志中的字段名。当 value 为__default__时，取默认值。当 value 为空字符串时，表示删除 Tag。 可配置 Tag 如下： HOST_NAME：主机名。默认添加，默认值为"__hostname__"。 AGENT_TAG：用户自定义标识。默认添加，默认值为"__user_defined_id__"。该参数仅适用于 [用户自定义标识机器组](products/sls/documents/machine-group-overview.md) ，而 [IP](products/sls/documents/machine-group-overview.md) [地址机器组](products/sls/documents/machine-group-overview.md) 不包含此参数。 HOST_ID：主机 ID。默认不添加，默认值为"__host_id__"。 CLOUD_PROVIDER：云厂商。默认不添加，默认值为"__cloud_provider__"。 |


### 输入插件相关Tag

该类Tag与输入插件强相关，它是输入插件配置的一部分，可通过输入配置的高级参数进行设置。您可以在创建采集配置或者修改采集配置时添加配置参数，本文以修改采集配置为例，创建采集配置请参见[创建采集配置](products/sls/documents/manage-logtail-configurations-for-log-collection.md)。

重要

目前，该功能仅适用于文件采集和新版标准输出采集插件。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。在Project列表区域，单击目标Project。

- 

单击日志存储下您的Logstore，在Logtail配置中添加Logtail配置，单击立即接入，本例使用正则-文本日志，表示将以正则匹配的方式解析文本日志。

- 

在Logtail配置列表中，单击目标Logtail采集配置。

- 

在Logtail配置页面，单击编辑。

- 

在输入配置中单击其他输入配置，在高级参数后边单击，配置输入插件相关Tag。

重要

- 

在输入配置设置FileOffsetKey，采集配置的自动生成索引会将该Tag字段（__file_offset__）设置成索引字段，收费标准请参见[计费说明](products/sls/documents/create-indexes.md)。如果无需对该某字段建立索引，可以删除该字段的索引，同时保留其 Tag 字段。具体操作，请参见[更新索引](products/sls/documents/create-indexes.md)。

- 

该Tag不会在查询分析页面的上层显示，具有独特的属性和功能，并且Tag名称为__file_offset__。

在查询分析页面中，__file_offset__字段显示在左侧显示字段列表和日志详情区域中，其值为文件读取偏移量（如1465）。

{ "Tags": { "FileInodeTagKey": "__default__", "FilePathTagKey": "__default__" }, "FileOffsetKey":"__default__" }

- 

- 

- 

- 

- 

- 

- 

- 

| 参数名 | 类型 | 是否必填 | 默认值 | 样例 | 说明 |
| --- | --- | --- | --- | --- | --- |
| Tags | object | 否 | 空 | {"FileInodeTagKey":"__inode__"} | key 为 Tag 参数名，value 为 Tag 在日志中的字段名。当 value 为__default__时，取默认值。当 value 为空字符串时，表示删除 Tag。 可配置 Tag 如下： FileInodeTagKey：文件 inode。 默认不添加，默认值为"__inode__"。 FilePathTagKey：文件路径。默认添加，默认值为"__path__"。 以下参数仅当 EnableContainerDiscovery 参数取值为 true 时有效。 K8sNamespaceTagKey：文件所在容器命名空间。默认添加，默认值为"_namespace_"。 K8sPodNameTagKey：文件所在 Pod 名。默认添加，默认值为"_pod_name_"。 K8sPodUidTagKey：文件所在 Pod UID。默认添加，默认值为"_pod_uid_"。 ContainerNameTagKey：文件所在容器名。默认添加，默认值为"_container_name_"。 ContainerIpTagKey：文件所在容器 IP。默认添加，默认值为"_container_ip_"。 ContainerImageNameTagKey：文件所在容器镜像。默认添加，默认值为"_image_name_"。 |
| FileOffsetKey | string | 否 | 空 | __file_offset__ | 日志在文件中的位置 Tag。默认不添加，默认值为__file_offset__。当 value 为__default__时，取默认值。当 value 为空字符串时，表示删除 Tag。 重要 当 EnableLogPositionMeta 参数与 Tags.FileInodeTagKey 或 FileOffsetKey 参数同时存在时，EnableLogPositionMeta 参数会被忽略。 |


## 删除Tag

在高级参数配置中将该Tag设置为空字符串，从而实现删除Tag目的。

以下示例中AGENT_TAG的value设置为空字符串，该Tag不会显示。具体操作，请参见[创建/修改 Tag](products/sls/documents/manage-loongcollector-to-collect-tags.md)[名称](products/sls/documents/manage-loongcollector-to-collect-tags.md)。

{ "PipelineMetaTagKey": { "HOST_NAME": "sourceName", "AGENT_TAG": "", "HOST_ID": "__default__", "CLOUD_PROVIDER": "__default__" } }

## 查看Tag

- 

在Project列表区域，单击目标Project。

- 

在对应的日志库右侧的图标，选择查询分析，查看当前LogStore的日志。

- 

Tag字段展示在日志页面的最上方一行。

- 

[Agent](products/sls/documents/manage-loongcollector-to-collect-tags.md)[相关](products/sls/documents/manage-loongcollector-to-collect-tags.md)[Tag](products/sls/documents/manage-loongcollector-to-collect-tags.md)

- 

__tag__:sourceName：设置的Tag key为PipelineMetaTagKey.HOST_NAME，默认value为__tag__:__hostname__,设置value为__tag__:sourceName，代表来源主机名称。

- 

__tag__:__host_id__：设置的Tag key为PipelineMetaTagKey.HOST_NAME。该参数value使用默认值__host_id__。

- 

__tag__:__cloud_provider__：设置的Tag key为PipelineMetaTagKey.CLOUD_PROVIDER。该参数value使用默认值__cloud_provider__。

- 

__tag__:__user_defined_id__：设置的Tag key为AGENT_TAG，即该参数仅适用于[用户自定义标识机器组](products/sls/documents/machine-group-overview.md)，而[IP](products/sls/documents/machine-group-overview.md)[地址机器组](products/sls/documents/machine-group-overview.md)不包含此参数。

- 

[输入插件相关](products/sls/documents/manage-loongcollector-to-collect-tags.md)[Tag](products/sls/documents/manage-loongcollector-to-collect-tags.md)

- 

__tag__:__inode__：设置的Tag key为Tags.FileInodeTagKey，该参数value使用默认值__inode__。

- 

__tag__:__path__：设置的Tag key为Tags.FilePathTagKey，该参数value使用默认值__path__。

- 

__file_offset__：设置的Tag key为FileOffsetKey，该参数value使用默认值__file_offset__。

重要

- 

在输入配置设置FileOffsetKey，采集配置的自动生成索引会将该Tag字段（__file_offset__）设置成索引字段，收费标准请参见[计费说明](products/sls/documents/create-indexes.md)。如果无需对该某字段建立索引，可以删除该字段的索引，同时保留其 Tag 字段。具体操作，请参见[更新索引](products/sls/documents/create-indexes.md)。

- 

该Tag不会在查询分析页面的上层显示，具有独特的属性和功能，并且Tag名称为__file_offset__。

在查询分析页面中，__file_offset__字段显示在左侧显示字段列表和日志详情区域中，其值为文件读取偏移量（如1465）。

## 修改Tag值

重要

目前，该功能仅适用于文件采集和新版标准输出采集插件。

通过SPL处理插件管理Tag字段，修改Tag的值。使用SPL处理Tag字段时，需要遵循以下规则：

- 

SPL将字段__tag__:作为 Tag 的标识，并在SPL处理过程中自动为所有Tag字段添加该前缀。因此，在编写SPL语句时，需确保字段名包含此前缀以正确引用 Tag 相关数据。

- 

在SPL输出中，所有以Tag为前缀的字段均会被识别为Tag，这种方法可用于增加Tag。

本文在[修改采集配置时添加](products/sls/documents/use-logtail-spl-to-parse-logs.md)[SPL](products/sls/documents/use-logtail-spl-to-parse-logs.md)，以__tag__ :sourceName为例，为了更便捷地查询日志，可通过在日志采集配置中将值修改为user_module，从而用应用名称区分不同日志。创建采集配置时添加SPL请参见[创建采集配置时添加](products/sls/documents/use-logtail-spl-to-parse-logs.md)[SPL](products/sls/documents/use-logtail-spl-to-parse-logs.md)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标日志库前面的>，依次选择数据接入>Logtail配置。

- 

在Logtail配置列表中，单击目标Logtail配置后操作列的管理Logtail配置。

- 

单击页面上方的编辑，在页面下方的处理配置区域，处理配置中处理模式选择SPL，然后单击保存。

SPL语句设置为：* | extend "__tag__:sourceName"='user_module'

- 

在对应的日志库右侧的图标，选择查询分析，查看当前LogStore的日志。

__tag__:sourceName的字段值为user_module。

## 相关文档

普通索引字段支持设置成Tag字段，Tag字段支持显示和隐藏。具体操作请参见[Tag](products/sls/documents/quick-analysis.md)[字段](products/sls/documents/quick-analysis.md)。

[上一篇：如何获取Docker容器的Label和环境变量](products/sls/documents/how-do-i-obtain-the-labels-and-environment-variables-of-a-container.md)[下一篇：如何在日志样例中设置不可见字符](products/sls/documents/how-do-i-configure-non-printable-characters-in-a-sample-log.md)

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
