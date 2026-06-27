# 审计容器内执行的命令并配置告警-容器服务Kubernetes版ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/use-container-auditing

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

# 使用容器内部操作审计功能

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器内部操作审计功能可以审计组织内成员或应用程序进入容器后执行的命令操作。本文介绍如何使用容器内部操作审计功能，以及如何通过日志服务收集分析审计日志，并根据需求为审计日志设置自定义的告警规则。

## 计费说明

容器内部操作审计功能可以免费使用。开通容器内部操作审计功能后，使用日志服务SLS的相关功能，会产生相关费用。日志服务相关计费信息，请参见[计费概述](products/sls/documents/billing-overview.md)。

该功能通过白名单开放中，如需使用，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)。

## 使用限制

- 

集群类型：仅支持ACK托管集群Pro版、ACK托管集群基础版、ACK专有集群。

- 

集群版本及操作系统限制：仅支持内核版本大于4.19的Alibaba Cloud Linux、Ubuntu、ContainerOS操作系统。

- 

Alibaba Cloud Linux：集群版本为1.18及以上。

- 

ContainerOS：集群版本为1.24及以上。

- 

Ubuntu：

- 

集群版本为1.30及以上。如需升级集群，请参见[手动升级集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。

- 

节点初始化时，会关闭操作系统自动升级。

- 

节点初始化时，把/etc/resolv.conf软连接指向到/run/systemd/resolve/stub-resolv.conf，将 DNS服务器指向 DHCP配置。

- 

目前不支持CPFS存储卷、镜像加速插件、安全加固等功能。

## 步骤一：启用容器内部操作审计功能

可通过以下步骤开启容器内部操作审计功能。启用此功能后，将安装以下两个组件。

- 

[日志采集组件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)：将审计日志收集到日志服务并创建默认的审计报表。

- 

ack-advanced-audit组件：实现容器内操作审计。

默认将在日志采集组件使用的日志Project中创建一个名为advaudit-${cluster_id}的日志库，用于保存审计日志。该日志库数据的保存时间为180天。如需修改日志保存时间，请参见[管理](products/sls/documents/manage-a-logstore.md)[Logstore](products/sls/documents/manage-a-logstore.md)。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>审计。

- 

在审计页面单击容器审计页签，然后单击开始安装。

## 步骤二：查看审计报表

在审计页面单击容器审计页签，然后单击容器内审计概览页签，查看审计报表内容。

- 

查看进入Pod容器的次数以及相关Pod信息。

- 

执行操作的Kubernetes操作账号信息、进入容器后执行的命令列表以及常见的高危列表。

## 步骤三：查看详细日志记录

可通过以下两种方式查看详细的日志记录。

- 

在审计报表页面查看：适用于查看最近的单个事件的日志记录。

- 

在日志库页面通过查询语句查看：适用于复杂场景，查看更多的历史信息以及历史事件。

## 在审计报表页面查看

在容器内审计概览报表页面，通过单击风险程序操作列表区域的traceId和eventId表格列的链接，查看对应审计日志的详细信息。

- 

单击traceId表格列的链接，可以查看单次进入容器后执行的所有操作命令的审计日志。

- 

单击eventId表格列的链接，可以查看执行的单个命令的详细信息。

## 在日志库页面通过查询语句查看

在容器内审计日志查询页面，通过查询语句查看详细的审计日志记录。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>审计。

- 

在审计页面单击容器审计页签，然后单击容器内审计日志查询页签。

- 

在输入框中输入查询和分析语句。

- 

查询进入某个Pod的容器后执行的命令操作审计日志：输入* and k8s.pod.namespace: <namespace> and k8s.pod.name: <pod_name>，将<namespace>替换为Pod所在的命名空间，<pod_name>替换为Pod的名称。

- 

查询执行指定程序的操作审计日志：输入* and process.name: <name>，将<name>替换为待查找的程序名称。

更多查询统计方式，请参见[日志服务查询分析方法](products/sls/documents/log-search-overview.md)。

- 

设置查询分析的时间范围，然后单击查询/分析，查看分析结果。

## （可选）步骤四：配置操作审计告警

通过日志服务的告警功能，您可以配置容器内部操作审计的实时告警，便于监控容器内关键的操作事件。告警方式支持短信、钉钉机器人、邮件、自定义Webhook和通知中心。本文以配置钉钉告警的方式，介绍如何配置容器内部操作审计告警。更多告警配置方式，请参见[告警](products/sls/documents/sls-alerting.md)。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

进入Webhook集成页面。

- 

在Project列表区域，单击目标Project。

- 

在左侧导航栏中，单击告警。

- 

在告警中心页面，单击通知对象页签，然后单击Webhook集成。

- 

创建Webhook。

- 

在Webhook集成页面，单击创建。

- 

在新建Webhook对话框中，配置如下配置项，然后单击确认。

| 配置项 | 描述 |
| --- | --- |
| 标识符 | Webhook 的唯一标识，不可重复。本示例配置为 ack-container-operation-audit-alert 。 |
| 名称 | Webhook 名称。本示例配置为 Kubernetes 容器内部操作审计告警 。 |
| 类型 | Webhook 类型。本示例选择 钉钉 。 |
| 请求地址 | Webhook URL 地址。 在钉钉侧创建自定义机器人，并获取 Webhook URL 地址。 更多信息，请参见 [自定义机器人接入](https://open.dingtalk.com/document/group/custom-robot-access) 。 |


- 

新建内容模板。

- 

在告警中心页面，单击通知策略页签，然后单击内容模板。

- 

在内容模板页面，单击创建。

- 

配置内容模板的标识符和名称，然后配置钉钉告警通知的标题和发送内容。

关于添加内容模板的更多信息，请参见[创建内容模板](products/sls/documents/create-an-alert-template.md)。本文需配置两个内容模板，具体配置内容如下。

| 标识符 | 名称 | 标题 | 发送内容 |
| --- | --- | --- | --- |
| ack-container-operation-audit-alert-enter | Kubernetes 进入容器告警 | KubernetesKubernetes 容器内部操作审计告警 | - 告警规则：${alert_name} - 触发时间：${alert_time} - 告警严重度：${severity} - 集群 ID：{{ alert.results[0].fire_result['clusterid'] }} 有账号通过 kubectl exec 或终端功能进入了容器，请检查是否存在异常。 操作次数：{{ alert.fire_results_count }} 次，下面是其中一次操作的具体信息： - 操作时间：{{ alert.results[0].fire_result['time'] }} {% if alert.results[0].fire_result['k8s.user.aliuid'] -%} - 操作账号：{{ alert.results[0].fire_result['k8s.user.aliuid'] }} {% else -%} - 操作账号：{{ alert.results[0].fire_result['k8s.user.username'] }} {% endif -%} - 命名空间：{{ alert.results[0].fire_result['k8s.pod.namespace'] }} - Pod：{{ alert.results[0].fire_result['k8s.pod.name'] }} - 容器：{{ alert.results[0].fire_result['kubeobject.operation.podexecoptions.container'] }} - 命令：{{ alert.results[0].fire_result['kubeobject.operation.podexecoptions.commandstr'] }} [[详情](${query_url})] [[设置](${alert_url})] |
| ack-container-operation-audit-alert-run-danger-cmd | Kubernetes 进入容器后执行风险程序告警 | Kubernetes 容器内部操作审计告警 | - 告警规则：${alert_name} - 触发时间：${alert_time} - 告警严重度：${severity} - 集群 ID：{{ alert.results[0].fire_result['clusterid'] }} 有账号通过 kubectl exec 或终端功能进入容器后执行了存在风险的程序命令，请检查是否存在异常。 操作次数：{{ alert.fire_results_count }} 次，下面是其中一次操作的具体信息： - 操作时间：{{ alert.results[0].fire_result['time'] }} {% if alert.results[0].fire_result['k8s.user.aliuid'] -%} - 操作账号：{{ alert.results[0].fire_result['k8s.user.aliuid'] }} {% else -%} - 操作账号：{{ alert.results[0].fire_result['k8s.user.username'] }} {% endif -%} - 命名空间：{{ alert.results[0].fire_result['k8s.pod.namespace'] }} - Pod：{{ alert.results[0].fire_result['k8s.pod.name'] }} - 容器：{{ alert.results[0].fire_result['k8s.container.name'] }} - 操作目录：{{ alert.results[0].fire_result['process.cwd'] }} - 执行的程序命令：{{ alert.results[0].fire_result['process.cmdline'] }} [[详情](${query_url})] [[设置](${alert_url})] |


- 

配置告警。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，选择集群使用的日志Project（k8s-log-${cluster_id}），单击名称进入日志Project页面。

- 

在页面左侧的图标栏单击仪表盘图标，选择仪表盘列表，然后单击Kubernetes容器内部操作审计。

- 

在Kubernetes容器内部操作审计报表页面，单击告警>创建告警。

- 

在告警监控规则页面，分别配置Kubernetes进入容器告警和Kubernetes进入容器后执行风险程序告警的告警规则。配置完成后，单击确定。

以下配置项均为示例值，请根据实际需求设置。

- 

Kubernetes进入容器告警

- 

- 

- 

- 

- 

- 

- 

- 

| 配置项 | 描述 |
| --- | --- |
| 规则名称 | Kubernetes 进入容器告警 |
| 检查频率 | 固定间隔 ：1 分钟。 |
| 查询统计 | 单击右侧 添加 ，然后单击 高级配置 页签，配置如下信息。配置完成后，单击 确认 。 日志库 ：搜索并选中 advaudit-${cluster_id} ，例如 advaudit-c76da730c08ca45adb90fad86fb****** 。 查询区间 ：本示例选中 1 分钟（相对） 。 查询 ：设置 日志库 后，会显示该字段。代码配置为： kind: Kubernetes and kubeObject.operation.kind: PodExec | select "clusterid", "time", "traceId", "eventId", "k8s.user.aliuid", "k8s.user.username", json_extract(k8s, '$.user.groups') as "k8s.user.groups", "host.hostip", "host.nodename", "k8s.pod.namespace", "k8s.pod.name", json_extract(k8s, '$.pod.labels') as "k8s.pod.labels", "kubeobject.operation.podexecoptions.container", json_extract(kubeobject, '$.operation.podExecOptions.command') as "kubeobject.operation.podexecoptions.command", "kubeobject.operation.podexecoptions.commandstr" from log |
| 触发条件 | 选择当 有数据 时，严重程度： 报告 。 |
| 输出目标 | 选择 SLS 通知 。 |
| 开启 | 打开开关。 |
| 告警策略 | 选择 极简模式 ，并配置如下信息。 渠道 ：选择 钉钉 。 选择 Webhook ：选择 Kubernetes 容器内部操作审计告警 。 提醒方式 ：选择 不提醒 。 内容模板 ：搜索并选择 Kubernetes 进入容器告警 。 发送时段 ：选择 任意 。 |


- 

Kubernetes进入容器后执行风险程序告警

- 

- 

- 

- 

- 

- 

- 

- 

| 配置项 | 描述 |
| --- | --- |
| 规则名称 | Kubernetes 进入容器后执行风险程序告警 |
| 检查频率 | 固定间隔 ：1 分钟。 |
| 查询统计 | 单击右侧 添加 ，然后单击 高级配置 页签，配置如下信息。配置完成后，单击 确认 。 日志库 ：搜索并选中 advaudit-${cluster_id} ，例如 advaudit-c76da730c08ca45adb90fad86fb74**** 。 查询区间 ：选中 1 分钟（相对） 。 查询 ：设置 日志库 后，才会显示该字段。代码配置为： kind: Command | select "clusterid", "time", "traceId", "eventId", "k8s.user.aliuid", "k8s.user.username", json_extract(k8s, '$.user.groups') as "k8s.user.groups", "host.hostip", "host.nodename", "k8s.pod.namespace", "k8s.pod.name", json_extract(k8s, '$.pod.labels') as "k8s.pod.labels", "k8s.container.name", "k8s.container.image", "process.cwd", "process.name", "process.cmdline", json_extract(process, '$.pid') as "process.pid", "process.user.uid", json_extract(process, '$.parentPid') as "process.parentpid", "process.parentname" from log where "process.name" in ('rm', 'sudo', 'su', 'nsenter', 'curl', 'wget', 'yum', 'apt-get', 'apt', 'apk', 'dpkg', 'nc', 'ncat', 'ssh', 'scp', 'nmap', 'docker', 'crictl', 'nerdctl', 'podman', 'kubectl', 'helm', 'mysql', 'redis', 'psql', 'redis-cli', 'pip', 'npm', 'gem') |
| 触发条件 | 当 有数据 时，严重程度： 中 。 |
| 输出目标 | 选择 SLS 通知 。 |
| 开启 | 打开开关。 |
| 告警策略 | 选择 极简模式 ，并配置如下信息。 渠道 ：选择 钉钉 。 选择 Webhook ：选择 Kubernetes 容器内部操作审计告警 。 提醒方式 ：选择 不提醒 。 内容模板 ：选择 Kubernetes 进入容器后执行风险程序告警 。 发送时段 ：选择 任意 。 |


- 

测试告警规则。

- 

通过kubectl exec -it <pod_name> -- bash命令进入容器，触发Kubernetes进入容器告警的告警规则。告警信息如下图所示。

- 

进入容器后，通过touch a.txt && rm a.txt命令，触发Kubernetes进入容器后执行风险程序告警的告警规则。告警信息如下图所示。

## 关闭容器内部操作审计功能

可通过卸载ack-advanced-audit组件关闭容器内部操作审计功能。

重要

关闭容器内部操作审计功能，不会删除自动创建的advaudit-${cluster_id}日志库，需要登录[日志服务控制台](https://sls.console.aliyun.com)手动删除该日志库，请参见[停止计费/删除](products/sls/documents/manage-a-logstore.md)[Logstore](products/sls/documents/manage-a-logstore.md)。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。

- 

在组件管理页面，搜索ack-advanced-audit组件，单击组件右下方的卸载，按照页面提示完成卸载。

## 相关文档

- 

关于ack-advanced-audit的发布记录及说明，请参见[ack-advanced-audit](products/ack/documents/product-overview/ack-advanced-audit.md)。

- 

API Server审计日志功能能够帮助集群管理人员排查“什么人在什么时间对什么资源做了什么操作”，请参见[使用集群](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)[API Server](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)[审计功能](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)。

[上一篇：使用集群API Server审计功能](products/ack/documents/ack-edge/security-and-compliance/work-with-cluster-auditing.md)[下一篇：使用ServiceAccount Token卷投影](products/ack/documents/ack-edge/security-and-compliance/enable-service-account-token-volume-projection.md)

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
