# 如何在工作流集群中开启和访问日志服务-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/configure-log-service

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-argo-workflow-cluster/product-overview.md)

- [服务支持](products/ack/documents/ack-argo-workflow-cluster/support.md)

- [实践教程](products/ack/documents/ack-argo-workflow-cluster/use-cases.md)

- [操作指南](products/ack/documents/ack-argo-workflow-cluster/user-guide.md)

[首页](https://help.aliyun.com/zh)

# 使用日志服务

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

工作流完成时，一般需要配置工作流和Pod的回收策略清理相应的资源，以避免集群控制面和工作流控制器资源的线性增长。当工作流出现问题或需要进行流程分析时，查看工作流日志是一个必不可少的能力。由于原生的集群在Pod清理后就不能查看Pod或工作流日志，因此，工作流集群集成了阿里云日志服务SLS，收集工作流运行过程中Pod产生的日志，上报到您账号下的SLS服务中，并且支持通过Argo CLI或Argo UI便捷地查看工作流的日志。

## 使用说明

- 

日志收集后，如果工作流还在集群中，无论Pod是否被删除，您都可以通过[Argo CLI](products/ack/documents/ack-argo-workflow-cluster/user-guide/configure-log-service.md)和[Argo UI](products/ack/documents/ack-argo-workflow-cluster/user-guide/configure-log-service.md)查看工作流相关的Pod日志。

- 

如果工作流在集群中被删除，但是已经 持久化 到数据库中，您可以通过Argo CLI[下载工作流日志的](products/ack/documents/ack-argo-workflow-cluster/user-guide/configure-log-service.md)[ZIP](products/ack/documents/ack-argo-workflow-cluster/user-guide/configure-log-service.md)[包](products/ack/documents/ack-argo-workflow-cluster/user-guide/configure-log-service.md)或者直接访问[日志服务控制台](https://sls.console.aliyun.com/)查看日志。

关于如何将工作流持久化到数据库中，请参见[持久化工作流](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/persistence-workflow.md)。

## 注意事项

- 

如果工作流集群开启oss-artifact-repository，同时设置archiveLogs: true，即工作流集群已配置使用oss-artifact-repository存储日志，则SLS日志收集不生效。

- 

相比oss-artifact-repository收集，SLS日志收集具有自动的日志生命周期管理（可配置日志保留的天数），强大的查询能力。如需通过SLS收集日志，可以将archiveLogs: true删除。

## 前提条件

若您选择使用Argo CLI方式开启日志服务和获取日志，您需要提前完成以下操作：

- 

下载并安装v3.4.12或以上版本的阿里云Argo CLI。具体操作，请参见[阿里云](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow.md)[Argo CLI](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow.md)。

- 

若您使用的账号为RAM用户，则需要为RAM用户授予日志服务SLS的只读权限，系统权限策略为AliyunLogReadOnlyAccess。具体授权操作，请参见[创建](products/sls/documents/create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)[RAM](products/sls/documents/create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)[用户及授权](products/sls/documents/create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)。

## 开启日志服务

工作流集群创建后，系统会自动创建一个名为k8s-log-<clusterid>的Project，用来收集工作流集群日志。如果日志服务Project不存在，请自行创建名为k8s-log-<clusterid>的Project。关于创建Project的具体操作，请参见[创建](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)。

您可以通过阿里云 Argo CLI或者通过直接创建日志服务CR两种方式开启日志服务。

### 通过阿里云Argo CLI开启

阿里云Argo CLI完全兼容开源Argo CLI，增强了日志能力，可以获取工作流已删除Pod的日志。

执行以下命令，配置日志服务参数。

argo config sls Please input log retention days. Default is 7 days. 10

预期输出：

Start to config SLS for your cluster. Created AliyunLogConfig CR workflow-sls-config in default namespace. Created SLS logstore workflow-logstore in SLS project k8s-log-<clusterid>, log retention days is 10 days

预期输出表明，日志服务配置成功。所有工作流日志将被收集到名为workflow-logstore的日志库（Logstore）中。

您可以登录[日志服务控制台](https://sls.console.aliyun.com/)，查找名为k8s-log-<clusterid>的Project，然后查看对应的workflow-logstore。

### 通过创建日志服务CR开启

执行以下命令，创建阿里云日志配置CR。日志服务控制器会自动创建一个名为k8s-log-<clusterid>的Project和一个名为workflow-logstore的日志库（Logstore）。

cat << EOF | kubectl apply -f - apiVersion: log.alibabacloud.com/v1alpha1 kind: AliyunLogConfig metadata: name: workflow-sls-config namespace: default spec: # log will store for 5 days lifeCycle: 5 logstore: workflow-logstore logtailConfig: inputType: plugin configName: workflow-sls-config inputDetail: plugin: inputs: - detail: Stderr: true Stdout: true type: service_docker_stdout EOF

## 通过Argo CLI访问日志服务

## 访问集群中的工作流日志

通过Argo CLI可以访问在集群中现存的工作流的日志，包括已存在的Pod和删除的Pod。

在集群中存在的Pod可以通过原生kubectl logs <pod-name>访问，默认最多显示2000行日志，若该方式显示的日志数量不够或者需要访问已经删除的Pod，可以通过以下两种方式访问SLS的日志。

### 通过Argo CLI直接访问SLS（推荐）

- 

执行以下命令，配置访问权限。

argo config init #按照提示配置相关信息,包括ak、sk等。

- 

执行以下命令获取对应Pod的日志。

argo logs <workflow-name> <pod-name> --sls # 获取对应Pod日志。 argo logs <workflow-name> --sls # 获取对应workflow日志ZIP包。

### 通过访问Argo Server访问SLS

如需通过Argo CLI访问已删除Pod的日志，则需要先开启Argo Server并配置相关参数。

说明

通过日志服务获取工作流日志，必须指定<pod-name>。

若需要访问其他Namespace的Workflow/Pod，则获取KUBE_TOKEN时，需要使用对应Namespace。

- 

执行以下命令，开启Argo Server并配置参数。

export ARGO_SERVER=argo.<cluster id>.<region>.alicontainer.com:2746 export KUBE_TOKEN=$(k create token default -n default --duration 24h) export ARGO_TOKEN="Bearer $KUBE_TOKEN" export ARGO_INSECURE_SKIP_VERIFY=true

- 

执行以下命令，获取工作流Pod的日志。

argo logs <workflow-name> <pod-name>

## 访问持久化到数据库的工作流日志

您可以配置[持久化工作流](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/persistence-workflow.md)，将工作流持久化保存到数据库中，即使工作流在集群中被删除，也可以通过Agro CLI方式下载工作流日志。

- 

执行以下命令，配置访问权限。

argo config init #按照提示配置相关信息,包括ak、sk等。

- 

执行以下命令查询工作流的UID。

# argo archive list NAMESPACE NAME STATUS AGE DURATION PRIORITY MESSAGE P/R/C PARAMETERS UID default hello-world-l6c2r Succeeded 3d 1m 0 0/0/0 179eaef0-fde3-496f-946d-549e8f******

- 

下载工作流日志。

# argo archive logs 179eaef0-fde3-496f-946d-549e8f****** # ls hello-world-l6c2r.zip

## 通过Argo UI访问日志服务

无论工作流Pod是否被删除，您都可以通过Argo UI访问Pod的日志。如果Pod被删除，则访问SLS获取日志并显示到Argo UI。

在 Argo Workflows 的Logs页面中，选择目标工作流（如hello-world）及对应容器后，即可查看 Pod 的运行日志。若暂未获取到日志数据，页面底部会提示尝试通过 Artifacts 获取日志。

## 关闭日志服务

- 

执行以下命令，删除AliyunLogConfig CR。

kubectl delete aliyunlogconfigs.log.alibabacloud.com workflow-sls-config -n default

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)，将名为workflow-logstore的日志库删除。

[上一篇：使用Prometheus监控服务](products/ack/documents/ack-argo-workflow-cluster/user-guide/monitoring-services-with-prometheus.md)[下一篇：在Argo UI配置SLS日志链接](products/ack/documents/ack-argo-workflow-cluster/user-guide/configure-sls-log-links-in-argo-ui.md)

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
