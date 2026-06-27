# 配置Logtail采集Docker事件-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/collect-docker-events

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

# 采集Docker事件

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Docker事件信息记录了容器、镜像、插件、网络、存储等所有交互事件。本文介绍如何通过日志服务控制台创建Logtail采集配置采集Docker事件。

## 前提条件

已在服务器上安装Linux Logtail 0.16.18及以上版本。具体操作，请参见[安装](products/sls/documents/install-logtail-on-a-linux-server.md)[Logtail（Linux](products/sls/documents/install-logtail-on-a-linux-server.md)[系统）](products/sls/documents/install-logtail-on-a-linux-server.md)。

## 限制说明

- 

Logtail可运行在容器模式或宿主机上，需具备访问Docker的权限（可以访问到/var/run/docker.sock）。

Logtail采集Kubernetes日志请参见[采集](products/sls/documents/overview-of-log-collection-from-containers.md)[Kubernetes](products/sls/documents/overview-of-log-collection-from-containers.md)[日志](products/sls/documents/overview-of-log-collection-from-containers.md)，采集标准容器日志请参见[采集](products/sls/documents/collect-docker-container-text-logs.md)[Docker](products/sls/documents/collect-docker-container-text-logs.md)[容器日志（标准输出/文件）](products/sls/documents/collect-docker-container-text-logs.md)。

- 

Logtail在重启或停止期间，无法采集容器事件。

## 应用场景

- 

监控所有容器的启停事件，当核心容器停止后立即告警。

- 

采集所有容器事件，用于审计、安全分析、问题排查。

- 

监控所有镜像的拉取事件，如果拉取非合法路径的镜像时立即告警。

## 操作步骤

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在接入数据区域，选择自定义数据插件。

- 选择目标Project和Logstore，单击下一步。

- 

在机器组配置页面，配置机器组。

- 

根据实际需求，选择使用场景和安装环境。

重要

无论是否已有机器组，都必须根据实际需求正确选择使用场景和安装环境，这将影响后续的页面配置。

- 

确认目标机器组已在应用机器组区域，单击下一步。

### 已有机器组

从源机器组列表选择目标机器组。

### 没有可用机器组

单击创建机器组，在创建机器组面板设置相关参数。机器组标识分为IP地址和用户自定义标识，更多信息请参见[创建用户自定义标识机器组（推荐）](products/sls/documents/create-a-user-defined-identity-machine-group.md)或[创建](products/sls/documents/create-an-ip-address-based-machine-group.md)[IP](products/sls/documents/create-an-ip-address-based-machine-group.md)[地址机器组](products/sls/documents/create-an-ip-address-based-machine-group.md)。

重要

创建机器组后立刻应用，可能因为连接未生效，导致心跳为FAIL，您可单击自动重试。如果还未解决，请参见[Logtail](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。

- 

在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。

- 

inputs为数据源配置，必选项。

重要

一个inputs中只允许配置一个类型的数据源。

- 

processors为处理配置，用于解析数据。可选项，您可以配置一种或多种处理方式。

如果当前的inputs配置无法满足日志解析需求，您可以在插件配置中添加processors配置，即添加Logtail插件处理数据。例如提取字段、提取日志时间、脱敏数据、过滤日志等。更多信息，请参见[使用](products/sls/documents/overview-22.md)[Logtail](products/sls/documents/overview-22.md)[插件处理数据](products/sls/documents/overview-22.md)。

{ "inputs": [ { "detail": {}, "type": "service_docker_event" } ] }

| 配置项 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 数据源类型，固定为 service_docker_event 。 |
| EventQueueSize | int | 否 | 事件缓冲队列大小。不配置时，默认为 10，无特殊需求请保持默认设置。 |


- 

创建索引和预览数据，然后单击下一步。日志服务默认开启全文索引。您也可以根据采集到的日志，手动创建字段索引，或者单击自动生成索引，日志服务将自动生成字段索引。更多信息，请参见[创建索引](products/sls/documents/create-indexes.md)。

重要

如果需要查询日志中的所有字段，建议使用全文索引。如果只需查询部分字段、建议使用字段索引，减少索引流量。如果需要对字段进行分析（SELECT语句），必须创建字段索引。

- 单击查询日志，系统将跳转至Logstore查询分析页面。

您需要等待1分钟左右，待索引生效后，才能在原始日志页签中，查看已采集到的日志。更多信息，请参见[查询与分析快速指引](products/sls/documents/quick-guide-to-query-and-analysis.md)。

## 问题排查

使用Logtail采集日志后，如果预览页面或查询页面无数据，您可以参见[Logtail](products/sls/documents/what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)[采集日志失败的排查思路](products/sls/documents/what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)进行排查。

## 日志样例

Docker事件样例如下所示。

- 

样例1：镜像拉取事件

__source__: 10.10.10.10 __tag__:__hostname__: logtail-ds-77brr __topic__: _action_: pull _id_: registry.cn-hangzhou.aliyuncs.com/ringtail/eventer:v1.6.1.3 _time_nano_: 1547910184047414271 _type_: image name: registry.cn-hangzhou.aliyuncs.com/ringtail/eventer

- 

样例2：Kubernetes中容器的销毁事件

__source__: 10.10.10.10 __tag__:__hostname__: logtail-ds-xnvz2 __topic__: _action_: destroy _id_: af61340b0ac19e6f5f32be672d81a33fc4d3d247bf7dbd4d3b2c030b8bec4a03 _time_nano_: 1547968139380572119 _type_: container annotation.kubernetes.io/config.seen: 2019-01-20T15:03:03.114145184+08:00 annotation.kubernetes.io/config.source: api annotation.scheduler.alpha.kubernetes.io/critical-pod: controller-revision-hash: 2630731929 image: registry-vpc.cn-hangzhou.aliyuncs.com/acs/pause-amd64:3.0 io.kubernetes.container.name: POD io.kubernetes.docker.type: podsandbox io.kubernetes.pod.name: logtail-ds-44jbg io.kubernetes.pod.namespace: kube-system io.kubernetes.pod.uid: 6ddcf598-1c81-11e9-9ddf-00163e0c7cbe k8s-app: logtail-ds kubernetes.io/cluster-service: true name: k8s_POD_logtail-ds-44jbg_kube-system_6ddcf598-1c81-11e9-9ddf-00163e0c7cbe_0 pod-template-generation: 9 version: v1.0

Docker事件的日志字段如下。更多信息，请参见[Docker](https://docs.docker.com/engine/reference/commandline/events/)[官方文档](https://docs.docker.com/engine/reference/commandline/events/)。

| 字段 | 说明 |
| --- | --- |
| _type_ | 资源类型，例如 container、image。 |
| _action_ | 操作类型，例如 destroy、status。 |
| _id_ | 事件唯一标识。 |
| _time_nano_ | 事件的时间戳。 |


[上一篇：采集Windows事件日志](products/sls/documents/collect-windows-event-logs.md)[下一篇：数据传输加密](products/sls/documents/data-encryption.md)

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
