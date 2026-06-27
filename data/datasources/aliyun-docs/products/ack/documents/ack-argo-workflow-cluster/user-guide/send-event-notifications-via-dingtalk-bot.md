# 使用钉钉机器人发送事件通知-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/send-event-notifications-via-dingtalk-bot

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

# 使用钉钉机器人发送事件通知

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

运行工作流时，您可能需要在工作流运行结束或它的某个步骤完成时通知外部系统，例如邮件通知、即时消息（例如钉钉）、消息总线（例如Kafka）。本文以发送钉钉消息为例介绍如何在工作流运行中发送消息通知。

## 前提条件

已[创建](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)[Argo](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)[工作流集群](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)，且工作流集群所在VPC具有公网访问能力。

## 工作原理

- 

外部系统一般通过暴露HTTP Webhook接口的方式，接收消息输入。

- 

Argo工作流支持Exit Handler机制，可以在步骤中或在工作流本身定义exit-handler。

- 

Exit Handler以容器的方式运行。您可以在容器中运行curl命令向外部系统发送HTTP消息，从而实现事件通知。

## 步骤一：创建钉钉机器人

创建钉钉机器人后会生成专属的Webhook地址，通过Webhook地址可以关联到其他服务接收通知，例如Argo工作流。

- 

打开需要接收事件通知的钉钉群。

- 

进入机器人设置页面。

- 

单击钉钉群右上角的群设置图标，然后在群设置面板，单击智能群助手。

- 

在智能群助手面板，单击添加机器人，然后在群机器人对话框中的添加机器人区域，单击添加图标。

- 

在选择要添加的机器人区域，单击自定义，然后在机器人详情对话框，单击添加。按页面提示完成机器人设置。您必须至少选择一种安全设置，建议选择加签或IP地址（段）中的至少一种，以保证安全性。

重要

在工作流中通过钉钉发送消息，要求工作流集群的VPC网络具有公网访问能力。您可以为工作流集群VPC配置公网NAT网关，同时将公网NAT网关的EIP地址配置到机器人的IP地址（段）中，以确保安全性。

- 

设置完成后，复制并保存Webhook地址。

## 步骤二：在工作流中使用钉钉机器人

使用以下YAML示例创建工作流，并在工作流中使用钉钉机器人。其中messageUrl部分的https://argo.xxx.xxxxx.alicontainer.com:2746需替换为Argo控制台地址。关于创建工作流的具体操作，请参见[创建工作流](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow.md)。

apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: notification-demo- spec: entrypoint: say-hello onExit: exit-handler # 工作流运行完成后，运行exit-handler。 templates: - name: say-hello container: image: alpine:latest command: [sh, -c] args: ["echo hello"] - name: exit-handler container: image: curlimages/curl command: [sh, -c] # 运行curl发送钉钉消息，消息类型为链接类型，可以嵌入Argo工作流控制台链接，快速查看工作流详情。 # 可以引用变量包括：{{workflow.name}} {{workflow.status}} {{workflow.failures}} {{workflow.duration}}。 args: [ "curl -H 'Content-Type: application/json' -d '{ \"msgtype\": \"link\", \"link\": { \"title\":\"Argo workflow notification\", \"text\":\"WF {{workflow.name}} {{workflow.status}}\", \"messageUrl\":\"https://argo.xxx.xxxxx.alicontainer.com:2746/workflows/default/{{workflow.name}}?tab=workflow\" } }' https://oapi.dingtalk.com/robot/send?access_token=b97fb519129fdfce879baa4e3b905b14e6a64e8994f0ea3b11dda****" #Webhook地址，此处替换为您钉钉群的Webhook地址。 ]

发送的钉钉消息示例如下所示。

## 相关文档

关于钉钉自定义机器人接入的具体操作，请参见[自定义机器人接入](https://open.dingtalk.com/document/robots/custom-robot-access)。

[上一篇：使用镜像缓存加速ACS Pod启动](products/ack/documents/ack-argo-workflow-cluster/user-guide/use-imagecache-to-accelerate-acs-pod-startup.md)[下一篇：事件驱动](products/ack/documents/ack-argo-workflow-cluster/user-guide/event-driven.md)

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
