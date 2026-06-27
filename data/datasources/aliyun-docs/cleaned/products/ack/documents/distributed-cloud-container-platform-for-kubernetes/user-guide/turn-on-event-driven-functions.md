# 开启事件驱动触发工作流自动运行-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/turn-on-event-driven-functions

# 开启事件驱动触发工作流自动运行
工作流集群支持事件驱动功能，可通过监控事件触发工作流自动运行，您可以使用该功能构建事件驱动的自动化系统。事件驱动支持各种事件源，包括阿里云对象存储OSS、阿里云轻量消息队列（原 MNS）、Git代码仓库，EventBrige等。
## 背景信息
事件驱动功能基于[开源](https://argoproj.github.io/argo-events/)[Argo Event](https://argoproj.github.io/argo-events/)[项目](https://argoproj.github.io/argo-events/)构建，完全符合开源事件驱动标准，方便您将开源事件驱动迁移到工作流集群。
重点模块说明：
Event Source
Argo Event自定义资源，针对不同的事件源创建不同的Event Source资源，并触发创建Event Source Pod获取事件。
当前工作流集群支持Git、阿里云对象存储OSS、阿里云轻量消息队列（原 MNS）作为事件源，如有其他需求，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
Event Bus
Event Source获取事件后，会缓存到Event Bus中。Event Bus支持以下两种类型：
NATS：基于[开源](https://nats.io)[NATS](https://nats.io)构建的使用ECI运行的本地消息系统。
轻量消息队列（原 MNS）：通过使用云上轻量消息队列（原 MNS）缓存事件，如果您已经使用轻量消息队列（原 MNS），可以创建一个轻量消息队列（原 MNS）作为Event Bus。
Event Sensor
从Event Bus中读取事件，按照定义的规则过滤事件，并触发工作流的运行。您可以参考[开源](https://argoproj.github.io/argo-events/sensors/trigger-conditions/)[Argo Event](https://argoproj.github.io/argo-events/sensors/trigger-conditions/)设置Sensor Trigger条件、转换、过滤器等。
Event Sensor仅支持触发创建Argo工作流，如果有其他需求，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
## 计费说明
以下资源创建会涉及ECI实例计费，具体计费信息，请参见[ECI](https://help.aliyun.com/zh/eci/product-overview/billing-overview#topic-1860085)[计费概述](https://help.aliyun.com/zh/eci/product-overview/billing-overview#topic-1860085)。
创建Event Source后，会触发创建一个Event Source Pod，并以ECI实例运行。
使用NATS方式创建Event Bus会创建一个Event Bus Pod，并以ECI实例运行。
创建Event Sensor后，会创建一个Event Sensor Pod，并以ECI实例运行。
## 前提条件
[创建工作流集群](create-a-workflow-cluster.md)
[为](https://help.aliyun.com/zh/document_detail/2252086.html)[RAM](https://help.aliyun.com/zh/document_detail/2252086.html)[用户授权](https://help.aliyun.com/zh/document_detail/2252086.html)
安装阿里云CLI 3.0.188或以上版本，并配置凭证。
具体操作，请参见[安装阿里云](https://help.aliyun.com/zh/cli/install-cli-on-windows)[CLI](https://help.aliyun.com/zh/cli/install-cli-on-windows)、[配置凭证](https://help.aliyun.com/zh/cli/configure-credentials/)。
## 操作步骤
获取工作流集群的ID。
通过命令行方式获取。
aliyun adcp DescribeHubClusters --Profile=XFlow
通过控制台方式获取。
登录[工作流集群控制台](https://cs.console.aliyun.com/one?spm=5176.26288914.J_2883378880.2.791c75b87xSv6P#/argowf/ccbe3ace8f2f54fbfa1c5b0005d456d5f/detail)，在工作流集群页面的基础信息页签中获取集群ID。
执行以下命令开启事件驱动功能。
aliyun adcp UpdateHubClusterFeature --ArgoEventsEnabled true --ClusterId ***
重要
请将ClusterId后的***替换为您在[步骤](turn-on-event-driven-functions.md)[1](turn-on-event-driven-functions.md)中实际获取的工作流集群ID。
等待一段时间后，执行以下命令查看集群的详细信息。
aliyun adcp DescribeHubClusterDetails --ClusterId ***
在返回结果中查看Condition类型为EnabledArgoEvents的状态为True，表示事件驱动功能开启成功。
预期结果如下：
{ "Message": "", "Reason": "", "Status": "True", "Type": "EnabledArgoEvents" }
## 后续操作
开启事件驱动工作流功能后，您可以使用OSS事件触发工作流，或者通过轻量消息队列（原 MNS）触发工作流。具体操作如下：
[通过轻量消息队列（原 MNS）触发工作流](use-mns-messages-to-trigger-workflows.md)
[通过向](trigger-a-workflow-by-uploading-a-file-to-oss.md)[OSS](trigger-a-workflow-by-uploading-a-file-to-oss.md)[上传文件触发工作流](trigger-a-workflow-by-uploading-a-file-to-oss.md)
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
