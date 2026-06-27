# 使用集群的API Server审计功能实现集群安全运维-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/work-with-cluster-auditing

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# 使用集群的API Server审计功能实现集群安全运维

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

审计（Auditing）产生于API Server内部，用于记录对Kubernetes API的请求以及请求结果。ACK集群提供API Server的审计日志，帮助集群管理人员排查“什么人在什么时间对什么资源做了什么操作”，可用于追溯集群操作历史、排查集群故障等，降低集群安全运维压力。

## 使用说明

本文仅适用于ACK托管集群、ACK专有集群、ACK Serverless集群。

如果您想在注册集群中实现集群API Server审计功能，请参见[启用集群](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-cluster-auditing-in-registered-clusters.md)[API Server](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-cluster-auditing-in-registered-clusters.md)[审计功能](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-cluster-auditing-in-registered-clusters.md)。

## 计费说明

您可以在费用账单的账单总览页面，查看计费明细，包含审计日志的费用信息。具体操作，请参见[账单查询](products/ack/documents/ack-managed-and-ack-dedicated/product-overview/view-your-bills.md)。关于审计日志的计费方式，请参见[按使用功能计费](products/sls/documents/pay-as-you-go.md)。

## 步骤一：启用集群API Server审计功能

创建Kubernetes集群时会默认选中使用日志服务，开启集群API Server审计功能。若您未开通，请参见下方步骤开通。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>集群审计。

- 

在审计页面单击集群审计页签。

若您未开通集群日志或集群审计功能，请按照页面提示手动选择SLS Project并开启功能。

重要

请确保您账号下日志服务资源没有超出配额，否则会导致集群审计功能开启失败。

- 

可创建的日志Project数量配额。

- 

单个日志Project内可创建的日志库数量配额。

- 

单个日志Project内可创建的仪表盘数量配额。

关于SLS配额的说明和调整方式，请参见[调整资源配额](products/sls/documents/adjust-resource-quotas.md)。

## 步骤二：查看审计报表

重要

请勿修改审计报表。如果您有自定义审计报表的需求，请在[日志服务管理控制台](https://sls.console.aliyun.com/)创建新的报表。

ACK集群内置了4个审计日志报表，包括审计中心概览、资源操作概览、资源操作详细列表以及Kubernetes CVE安全风险。您可以在集群审计页面选择审计事件的筛选维度（例如命名空间、RAM用户等），并通过报表获取以下内容。

您也可以在获取结果后，单击目标区域右上角的图标，进行更多操作，例如查看指定区域全屏图、预览置顶区域对应的查询语句等。

### 审计中心概览

审计中心概览展示ACK集群中的事件整体概览以及重要事件（例如RAM用户操作、公网访问、命令执行、删除资源、访问保密字典、Kubernetes CVE安全风险等）的详细信息。

### 资源操作概览

资源操作概览展示Kubernetes集群中常见的计算资源、网络资源以及存储资源的操作统计信息。操作包括创建、更新、删除、访问。其中：

- 

计算资源：Deployment、StatefulSet、CronJob、DaemonSet、Job、Pod。

- 

网络资源：Service、Ingress。

- 

存储资源：ConfigMap、Secret、PersistentVolumeClaim。

- 

访问控制资源：Role、ClusterRole、RoleBinding、ClusterRoleBinding

页面顶部包含审计中心概览、资源操作概览、资源操作详细列表、Kubernetes CVE 安全风险四个Tab页签，支持按Namespace筛选和设置时间范围。各资源类型按操作类型分面板以环形图展示统计数据。

### 资源操作详细列表

该报表用于展示Kubernetes集群中某类资源的详细操作列表。您需要选择或输入指定的资源类型进行实时查询。该报表会显示：资源操作各类事件的总数、Namespace分布、成功率、时序趋势以及详细操作列表等。

说明

若您需要查看Kubernetes中注册的CRD（CustomResourceDefinition）资源或列表中没有列举的其他资源，可以手动输入资源名的复数形式。例如CRD资源为AliyunLogConfig，则输入AliyunLogConfigs。

### Kubernetes CVE安全风险

该报表用于展示当前集群中可能包含的Kubernetes CVE安全风险，您可以选择或输入子账号ID（即RAM用户账号）进行实时查询。该报表会显示当前账号下的Kubernetes CVE安全风险。关于CVE详情和解决方案，请参见[【CVE](products/ack/documents/product-overview/security-bulletins.md)[安全】漏洞修复公告](products/ack/documents/product-overview/security-bulletins.md)。

## （可选）步骤三：查看详细日志记录

如果您有自定义查询、分析审计日志的需求，可以进入日志服务管理控制台查看详细的日志记录。

说明

ACK托管集群集群的API Server审计日志在日志服务中对应的日志库数据默认保存时间为30天，ACK专有集群对应的默认保存时间为365天。如需修改日志的默认保存时间，请参见[管理](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。

- 

单击基本信息页签，单击日志服务 Project对应的Project ID，然后在Project列表区域，单击名为audit-${clustered}的日志库（Logstore）。

在集群创建过程中，指定的日志Project中会自动添加一个名为audit-${clustereid}的日志库。

重要

审计日志的Logstore默认已经配置好索引。请勿修改索引，以免报表失效。

- 

在输入框中输入查询和分析语句，并配置查询分析的时间范围，例如最近15分钟，然后单击查询/分析，查看查询分析结果。

常见的审计日志搜索方式如下：

- 

查询某一RAM用户的操作记录：输入RAM用户ID，单击查询/分析。

- 

查询某一资源的操作：输入集群计算、网络、存储、访问控制资源的名称，单击查询/分析。

- 

过滤掉系统组件的操作，输入NOT user.username: node NOT user.username: serviceaccount NOT user.username: apiserver NOT user.username: kube-scheduler NOT user.username: kube-controller-manager，然后单击查询/分析。

更多查询、统计方式，请参见[日志服务查询分析方法](products/sls/documents/log-search-overview.md)。

## （可选）步骤四：配置告警

若您需要对某些资源的操作进行实时告警，可以通过日志服务的告警功能实现。告警方式支持短信、钉钉机器人、邮件、自定义Webhook和通知中心。更多信息，请参见[告警设置快速入门](products/sls/documents/alarm-settings-quick-start.md)。

### 示例1：对容器执行命令时告警

某公司对于Kubernetes集群使用有严格限制，不允许用户登录容器或对容器执行命令。如果有用户执行命令时，告警需要立即被发送，并在告警信息中包含用户登录的具体容器、执行的命令、操作人、事件ID、时间、操作源IP等信息。

- 

查询语句为：

verb : create and objectRef.subresource:exec and stage: ResponseStarted | SELECT auditID as "事件ID", date_format(from_unixtime(__time__), '%Y-%m-%d %T' ) as "操作时间", regexp_extract("requestURI", '([^\?]*)/exec\?.*', 1)as "资源", regexp_extract("requestURI", '\?(.*)', 1)as "命令" ,"responseStatus.code" as "状态码", CASE WHEN "user.username" != 'kubernetes-admin' then "user.username" WHEN "user.username" = 'kubernetes-admin' and regexp_like("annotations.authorization.k8s.io/reason", 'RoleBinding') then regexp_extract("annotations.authorization.k8s.io/reason", ' to User "(\w+)"', 1) ELSE 'kubernetes-admin' END as "操作账号", CASE WHEN json_array_length(sourceIPs) = 1 then json_format(json_array_get(sourceIPs, 0)) ELSE sourceIPs END as "源地址" order by "操作时间" desc limit 10000

- 

条件表达式为：操作事件 =~ ".*"。

### 示例2：API Server公网访问失败告警

某集群开启了公网访问，为防止恶意攻击，需要监控公网访问的次数以及失败率。当访问次数达到一定阈值（10次）且失败率高于一定阈值（50%）时，告警需要立即被发送，并在告警信息中包含用户的IP所属区域、操作源IP、是否高危IP等信息。

- 

查询语句为：

* | select ip as "源地址", total as "访问次数", round(rate * 100, 2) as "失败率%", failCount as "非法访问次数", CASE when security_check_ip(ip) = 1 then 'yes' else 'no' end as "是否高危IP", ip_to_country(ip) as "国家", ip_to_province(ip) as "省", ip_to_city(ip) as "市", ip_to_provider(ip) as "运营商" from (select CASE WHEN json_array_length(sourceIPs) = 1 then json_format(json_array_get(sourceIPs, 0)) ELSE sourceIPs END as ip, count(1) as total, sum(CASE WHEN "responseStatus.code" < 400 then 0 ELSE 1 END) * 1.0 / count(1) as rate, count_if("responseStatus.code" = 403) as failCount from log group by ip limit 10000) where ip_to_domain(ip) != 'intranet' and ip not LIKE '%,%' ORDER by "访问次数" desc limit 10000

- 

条件表达式为：源地址 =~ ".*"。

## 相关操作

### 更换日志Project

如果您想将集群API Server审计日志数据迁移至另一个日志Project中，您可以使用集群审计中的更换日志 Project功能。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>集群审计。

- 

在审计页面单击集群审计页签，然后单击更换日志 Project，将集群审计日志的数据迁移至另一个SLS Project中。

### 关闭集群API Server审计功能

如果您不再需要集群API Server的审计功能，可以通过以下方法关闭审计功能。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>集群审计。

- 

在审计页面单击集群审计页签，然后单击关闭集群审计，关闭当前集群的审计功能。

### 在ACK专有集群中使用第三方日志解决方案

ACK推荐您使用阿里云日志服务SLS记录集群审计日志。但如果您需要使用第三方日志服务，您可以在部署集群时不使用阿里云SLS，根据需要对接其他的日志解决方案，完成相关审计日志的采集和检索。集群Master各节点的审计日志的源文件（文件为标准的JSON格式）可在/var/log/kubernetes/kubernetes.audit路径下获取。

## 参考信息：ACK专有集群API Server审计配置介绍

创建ACK专有集群集群配置集群组件时，控制台会默认选中使用日志服务，开启API Server审计功能，按审计策略采集事件数据，并将事件数据写入到后端。

说明

以下功能涉及kube-apiserver启动参数的更改，仅面向ACK专有集群。ACK托管集群和ACK Serverless集群集群控制面由ACK托管，不支持手动修改。

### 审计策略

审计策略定义了审计功能的配置和请求的采集规则。不同审计级别（Audit Level）的事件日志采集规则不同。Audit Level包括以下几种。

| Audit Level | 日志采集规则 |
| --- | --- |
| None | 符合规则的事件不予采集。 |
| Metadata | 采集请求的 Metadata，例如用户信息、时间戳等，但不采集请求体或返回体。 |
| Request | 采集请求的 Metadata 和请求体，但不采集返回体。不适用于非资源请求（Non-Resource Request）。 |
| RequestResponse | 采集请求的 Metadata、请求体和返回体。不适用于非资源请求（Non-Resource Request）。 |


您可以使用--audit-policy-file命令行标志（flag）将以下YAML示例文件保存为API Server的启动参数。登录Master节点后，您可以查看审计配置策略文件的目录，即/etc/kubernetes/audit-policy.yml。一个审计日志配置策略文件的YAML示例如下。

展开查看YAML示例文件

apiVersion: audit.k8s.io/v1 # 必填。v1.24及以上集群为audit.k8s.io/v1，v1.24以下集群为audit.k8s.io/v1beta1 kind: Policy # RequestReceived阶段（Stage）的请求无须生成审计事件。 omitStages: - "RequestReceived" rules: # 以下类型的请求十分频繁且潜在风险较低，建议设置为None，不做审计。 - level: None users: ["system:kube-proxy"] verbs: ["watch"] resources: - group: "" # core resources: ["endpoints", "services"] - level: None users: ["system:unsecured"] namespaces: ["kube-system"] verbs: ["get"] resources: - group: "" # core resources: ["configmaps"] - level: None users: ["kubelet"] # legacy kubelet identity verbs: ["get"] resources: - group: "" # core resources: ["nodes"] - level: None userGroups: ["system:nodes"] verbs: ["get"] resources: - group: "" # core resources: ["nodes"] - level: None users: - system:kube-controller-manager - system:kube-scheduler - system:serviceaccount:kube-system:endpoint-controller verbs: ["get", "update"] namespaces: ["kube-system"] resources: - group: "" # core resources: ["endpoints"] - level: None users: ["system:apiserver"] verbs: ["get"] resources: - group: "" # core resources: ["namespaces"] # 对只读URL，例如/healthz*，/version*及/swagger*，设置为None，不做审计。 - level: None nonResourceURLs: - /healthz* - /version - /swagger* # Event事件设置为None，不做审计。 - level: None resources: - group: "" # core resources: ["events"] # 对于可能包含敏感信息或二进制文件的Secrets，ConfigMaps，TokenReview接口，设置为Metadata。 - level: Metadata resources: - group: "" # core resources: ["secrets", "configmaps"] - group: authentication.k8s.io resources: ["tokenreviews"] # 请求可能会返回大量数据，设置为Request，不采集返回体。 - level: Request verbs: ["get", "list", "watch"] resources: - group: "" # core - group: "admissionregistration.k8s.io" - group: "apps" - group: "authentication.k8s.io" - group: "authorization.k8s.io" - group: "autoscaling" - group: "batch" - group: "certificates.k8s.io" - group: "extensions" - group: "networking.k8s.io" - group: "policy" - group: "rbac.authorization.k8s.io" - group: "settings.k8s.io" - group: "storage.k8s.io" # 已知的Kunernetes API默认设置为RequestResponse，返回请求体和响应体。 - level: RequestResponse resources: - group: "" # core - group: "admissionregistration.k8s.io" - group: "apps" - group: "authentication.k8s.io" - group: "authorization.k8s.io" - group: "autoscaling" - group: "batch" - group: "certificates.k8s.io" - group: "extensions" - group: "networking.k8s.io" - group: "policy" - group: "rbac.authorization.k8s.io" - group: "settings.k8s.io" - group: "storage.k8s.io" # 其余请求都默认设置为Metadata。 - level: Metadata

说明

在收到请求后，日志不立即开始记录，等待返回体Header发送后才开始记录。

对于大量冗余的kube-proxy watch请求、kubelet和system:nodes对节点的Get请求、kube组件在kube-system下对于endpoint的操作、以及API Server对Namespaces的Get请求等，系统不进行审计。

对于authentication、rbac、certificates、autoscaling、storage等敏感接口，系统根据读写记录相应的请求体和返回体。

### 审计后端

审计事件采集后，会被存储到Log后端日志文件系统，日志文件为标准的JSON格式。您可以配置并使用如下flag作为API Server的启动参数。

说明

登录到Master节点后，可通过/etc/kubernetes/manifests/kube-apiserver.yaml查看API Server的配置文件。

| 配置参数 | 说明 |
| --- | --- |
| --audit-log-maxbackup | 指定审计日志可分片存储的最大文件数量，为 10 个。 |
| --audit-log-maxsize | 指定单个审计日志的最大内存容量，为 100 MB。 |
| --audit-log-path | 指定审计日志的输出路径，为 /var/log/kubernetes/kubernetes.audit 。 |
| --audit-log-maxage | 指定审计日志最长的保存周期，为 7 天。 |
| --audit-policy-file | 配置审计日志策略的文件路径，为 /etc/kubernetes/audit-policy.yml 。 |


## 相关文档

- 

如您想使用容器内部的操作审计功能，即通过kubectl exec进入到容器内部执行的命令的审计，请参见[使用容器内部操作审计功能](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-container-auditing.md)。

- 

关于为企业安全管理运维人员提供使用集群的安全最佳实践，请参见[安全最佳实践](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/best-practices-for-security-1.md)。

- 

[容器安全](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/faq-about-container-security.md)[FAQ](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/faq-about-container-security.md)。

[上一篇：在Kubernetes中实现HTTPS安全访问](products/ack/documents/ack-edge/security-and-compliance/access-applications-in-an-ack-cluster-over-https.md)[下一篇：使用容器内部操作审计功能](products/ack/documents/ack-edge/security-and-compliance/use-container-auditing.md)

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
