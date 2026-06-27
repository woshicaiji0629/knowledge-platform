# 通过日志服务采集ACK Edge集群的容器日志-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/use-log-service-to-collect-log-data-from-containers-of-ack-edge-clusters

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

# 通过日志服务采集ACK Edge集群的容器日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云容器服务 Edge 版集成了日志服务，可以在创建ACK Edge集群时启用日志服务，快速采集ACK Edge集群的容器日志，包括容器的标准输出以及容器内的文本文件。本文介绍如何使用日志服务采集边缘容器的日志信息。

## 步骤一：启用日志服务组件Logtail

可以在创建ACK Edge集群时选中使用日志服务，启用Logtail组件；也可以为已有ACK Edge集群启用Logtail组件。

### 创建集群时启用Logtail

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面单击创建集群。

以下仅介绍开启日志服务的关键步骤。关于创建集群的具体操作，请参见[创建](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)[ACK Edge](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)[集群](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)。

- 

在组件配置配置向导中，选中使用日志服务。

当选中使用日志服务后，会出现创建项目（Project）的提示。关于日志服务管理日志的组织结构，请参见[项目（Project）](products/sls/documents/project.md)。有以下两种创建Project方式。

- 

单击使用已有 Project，选择一个现有的Project来管理采集的日志。

- 

单击创建新 Project，自动创建一个新的Project来管理采集的日志，Project会自动命名为k8s-log-{ClusterID}，ClusterID是新建的ACK Edge集群的唯一标识。 单击创建新 Project，将自动创建名称为k8s-log-{ClusterID}的 Project。

- 

配置完成后，单击右下角创建集群，在弹出的窗口中单击确认，完成创建。

完成创建后，可在集群列表页面看到开启了Logtail的ACK Edge集群。

### 为已有集群启用Logtail

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。

- 

在组件管理页面单击日志与监控页签，定位logtail-ds组件。

说明

- 

在ACK Edge ＞1.18.8-aliyunedge.1的版本中，日志组件统一合并为logtail-ds。

- 

在ACK Edge ≤ 1.18.8-aliyunedge.1的版本中，日志组件包含alibaba-log-controller和logtail-ds-docker两部分。

- 

在logtail-ds组件右侧，单击安装，并在安装组件对话框中单击确认。

如果已安装旧版本的日志服务组件，可以在组件右侧，单击升级。

## 步骤二：创建应用时配置日志服务

可以在创建应用的同时配置日志服务，从而对ACK Edge集群的日志进行采集。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>无状态。

- 

在无状态页面上方的命名空间下拉框中设置命名空间，然后单击页面右上角的使用镜像创建。

- 

在应用基本信息页签，设置应用名称、副本数量和类型，单击下一步，进入容器配置页面。

以下仅介绍日志服务相关的配置。关于其他的应用配置，请参见[创建无状态工作负载](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)[Deployment](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)。

- 

在日志配置区域，配置日志相关信息。

- 

设置采集配置。

重要

日志采集配置完成后，不支持修改。如需修改，请[通过](products/sls/documents/use-crds-to-collect-container-logs-in-daemonset-mode.md)[DaemonSet-CRD](products/sls/documents/use-crds-to-collect-container-logs-in-daemonset-mode.md)[方式采集容器日志](products/sls/documents/use-crds-to-collect-container-logs-in-daemonset-mode.md)。

单击采集配置，每个采集配置由日志库和容器内日志路径两项构成。

- 

日志库：配置Logstore名称，用于指定所采集的日志存储于该Logstore。如果该Logstore不存在，ACK将会自动在集群关联的日志服务Project下创建相应的Logstore。

说明

新创建的Logstore中的日志默认保存时间为180天。

- 

容器内日志路径：指定希望采集的日志所在的路径，例如使用/usr/local/tomcat/logs/catalina.*.log来采集Tomcat的文本日志。

说明

指定为stdout时，表示采集容器的标准输出和标准错误输出。

每一项采集配置都会被自动创建为对应Logstore的一个采集配置，默认采用极简模式（按行）进行采集。如果需要使用多行模式及更丰富的采集方式，请参见[通过](products/sls/documents/use-the-log-service-console-to-collect-container-text-logs-in-daemonset-mode.md)[DaemonSet-控制台方式采集容器文本日志](products/sls/documents/use-the-log-service-console-to-collect-container-text-logs-in-daemonset-mode.md)、[通过](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode.md)[DaemonSet-控制台方式采集容器标准输出](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode.md)。

配置前请确保集群已部署日志插件。例如，日志库分别填写为access和catalina。

- 

设置自定义Tag。

单击自定义Tag，每一个自定义Tag都是一个键值对，会拼接到所采集到的日志中，可以使用它来为容器的日志数据进行标记，例如版本号。

例如，将Tag名称设置为release，Tag值设置为1.0.0。

- 

当完成所有配置后，可单击右上角下一步进入后续流程。

后续操作，可参见[创建无状态工作负载](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)[Deployment](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)。

## 步骤三：查看日志

本例中查看通过控制台向导创建的tomcat应用的日志。完成配置后，tomcat应用的日志已被采集并存储到日志服务中，可以在日志服务控制台查看容器日志。操作步骤如下：

- 

安装成功后，进入[日志服务控制台](https://sls.console.aliyun.com/)。

- 

在进入控制台后，在Project列表区域选择Kubernetes集群对应的Project（默认为k8s-log-{Kubernetes集群ID}），进入日志库列表页签。

- 

在列表中找到相应的Logstore（采集配置中指定），将鼠标悬浮在相应的Logstore名称的右侧，单击图标，并单击查询分析。

本例中，在日志查询页面，可以查看Tomcat应用的标准输出日志和容器内文本日志，并可以发现自定义tag附加到日志字段中。

## 相关文档

- 

如需使用Sidecar采集容器文本日志，请参见[通过](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)[Sidecar](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)[方式采集](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)[Kubernetes](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)[容器文本日志](products/sls/documents/collect-container-text-logs-through-sidecar-console.md)。

- 

如需采集Kubernetes容器的标准输出，请参见[通过](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md)[DaemonSet](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md)[方式采集](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md)[Kubernetes](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md)[容器标准输出（旧版）](products/sls/documents/collect-container-stdout-and-stderr-in-daemonset-mode-1.md)。

- 

可以通过为日志添加告警规则，监控集群的运行状态，请参见[管理告警监控规则](products/sls/documents/manage-an-alert-monitoring-rule.md)。

- 

关于如何进行异常排查，请参见[Logtail](products/sls/documents/what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)[采集日志失败的排查思路](products/sls/documents/what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)。

- 

如需跨阿里云账号采集容器日志，请参见[通过](products/sls/documents/use-logtail-to-collect-container-logs-across-accounts.md)[Logtail](products/sls/documents/use-logtail-to-collect-container-logs-across-accounts.md)[跨阿里云账号采集容器日志](products/sls/documents/use-logtail-to-collect-container-logs-across-accounts.md)。

- 

如果在使用SLS Logstore时遇到问题，例如如何变更日志保存天数、关闭日志采集等，请参见[Logstore](products/sls/documents/logstore-related-issues.md)[相关问题](products/sls/documents/logstore-related-issues.md)排查。

[上一篇：通过阿里云Prometheus监控ACK Edge集群](products/ack/documents/ack-edge/user-guide/monitor-ack-edge-clusters-with-managed-service-for-prometheus.md)[下一篇：收集ACK Edge集群控制平面组件日志](products/ack/documents/ack-edge/user-guide/collect-ack-edge-cluster-control-plane-component-logs.md)

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
