# 什么是ACK One GitOps-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/gitops-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/product-overview.md)

- [快速入门](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/getting-started.md)

- [操作指南](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide.md)

- [实践教程](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases.md)

- [开发参考](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/developer-reference.md)

- [服务支持](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/support.md)

[首页](https://help.aliyun.com/zh)

# GitOps概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

GitOps是将Git仓库作为Kubernetes集群中部署应用的唯一来源，通过自动化配置基础设施实现应用的持续部署。Fleet实例托管了ArgoCD，并集成多集群能力，实现多集群的GitOps持续交付，满足应用的高可用部署、系统组件多集群分发等需求。本文介绍GitOps和ACK One GitOps的详细信息。

## GitOps介绍

[GitOps](https://about.gitlab.com/topics/gitops/#what-is-git-ops)将Git仓库作为应用部署的唯一来源，不断调整Kubernetes集群上应用的状态，使集群应用的状态最终与Git仓库中期望的状态保持一致。

### GitOps优势

- 

简单易学：Git易于被开发者接受，易于集成，无需额外学习成本。

- 

可靠性强：Git仓库提供版本控制、快速回滚和审计能力。

- 

安全性高：开发者使用GitOps无需任何Kubernetes集群权限，仅需要Git仓库权限，保证集群安全可靠。

- 

应用持续部署：Kubernetes集群和Git仓库中的应用状态自动同步，保持一致，实现应用持续部署。

### GitOps原理图

## ACK One GitOps介绍

ACK One舰队托管了开源[ArgoCD](https://argo-cd.readthedocs.io/)实现应用的GitOps持续交付。ArgoCD作为控制器运行在Kubernetes集群中，可以持续监控应用的实际状态，并与Git仓库中声明的期望状态保持同步。

### ACK One GitOps优势

- 

开箱即用，免运维。

- 

托管ArgoCD，提供原生的CLI和UI体验。

- 

集成阿里云RAM账号SSO登录，支持阿里云RAM的多租权限设置。

- 

多集群分发，ACK One关联集群自动加入ArgoCD，成为应用分发GitOps的目标集群。

- 

支持ArgoCD ApplicationSet，提升多集群应用分发体验。

- 

完整的可观测性能力：Argo CD的监控和告警配置，便于掌握实时运行情况；Argo CD 日志采集和控制台查看，提升可审计能力。

- 

支持阿里云 Codeup（包括配置WebHook）。

### ACK One GitOps原理图

## 相关功能

- 

- 

| 功能 | 描述 | 相关文档 |
| --- | --- | --- |
| GitOps 使用快速入门 | 介绍如何在 ACK One 舰队的 Fleet 实例中开启 GitOps 实现多集群应用发布的流程，帮助您快速上手 GitOps。 | [GitOps](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/work-with-gitops.md) [快速入门](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/work-with-gitops.md) |
| GitOps 用户管理 | 介绍 ACK One GitOps 支持的用户类型，以及如何为用户授权。 | [用户管理](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-users-based-on-gitops.md) |
| 登录 GitOps 系统 | 介绍 ACK One GitOps 用户如何登录 GitOps 系统。 | [登录](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/log-on-to-the-gitops-system.md) [GitOps](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/log-on-to-the-gitops-system.md) [系统](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/log-on-to-the-gitops-system.md) |
| 管理 Git 源仓库 | 介绍如何在 GitOps 系统中添加、查看及删除 Git 源仓库。 | [仓库管理](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-git-repositories.md) |
| 使用 GitOps 管理集群 | 介绍如何在 GitOps 系统中管理 ACK 集群。 | [使用](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-gitops-to-manage-ack-clusters.md) [GitOps](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-gitops-to-manage-ack-clusters.md) [管理集群](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-gitops-to-manage-ack-clusters.md) |
| GitOps 应用管理 | 介绍如何使用 GitOps 系统管理应用。 | [Application](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-gitops-to-manage-applications.md) [管理](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-gitops-to-manage-applications.md) [使用](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-an-applicationset-to-create-multiple-applications.md) [ApplicationSet](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-an-applicationset-to-create-multiple-applications.md) [创建多个应用](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-an-applicationset-to-create-multiple-applications.md) |
| GitOps 中多租权限管理 | 介绍如何配置 Local User 或者 RAM 用户/角色的 Argo CD RBAC 权限。 | [为用户配置](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-users-based-on-gitops.md) [ArgoCD RBAC](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/manage-users-based-on-gitops.md) |
| 自定义 GitOps 操作关联集群的 RBAC 权限 | 介绍如何为关联集群添加 GitOps 可下发资源的 RBAC 权限。 | [自定义](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/custom-gitops-operations-associated-with-the-cluster-s-rbac-permissions.md) [GitOps](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/custom-gitops-operations-associated-with-the-cluster-s-rbac-permissions.md) [操作关联集群的](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/custom-gitops-operations-associated-with-the-cluster-s-rbac-permissions.md) [RBAC](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/custom-gitops-operations-associated-with-the-cluster-s-rbac-permissions.md) [权限](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/custom-gitops-operations-associated-with-the-cluster-s-rbac-permissions.md) |
| Argo CD 监控的开启关闭 | 介绍如何开启或关闭舰队和 Argo CD 监控。 | [舰队监控](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/fleet-monitoring.md) |
| 配置 Argo CD 告警 | 介绍如何配置 Argo CD 告警。 | [配置](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/configure-ack-one-argocd-alarm.md) [ACK One ArgoCD](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/configure-ack-one-argocd-alarm.md) [告警](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/configure-ack-one-argocd-alarm.md) |
| GitOps 日志的开启和关闭 | 介绍如何开启或关闭 GitOps 日志。 | [开启](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/enable-the-collection-of-the-control-plane-logs-and-audit-logs-of-gitops.md) [GitOps](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/enable-the-collection-of-the-control-plane-logs-and-audit-logs-of-gitops.md) [控制面日志与审计日志](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/enable-the-collection-of-the-control-plane-logs-and-audit-logs-of-gitops.md) |
| GitOps 中敏感数据管理 | 介绍如何在 GitOps 中管理 Secret 信息。 | [Secret](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/secret-management.md) [管理](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/secret-management.md) |
| 使用钉钉机器人通知 GitOps 应用变更 | 介绍如何配置钉钉机器人接收应用变更通知。 | [使用钉钉机器人通知](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/notify-gitops-of-application-changes-using-dingtalk-bots.md) [GitOps](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/notify-gitops-of-application-changes-using-dingtalk-bots.md) [应用变更](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/notify-gitops-of-application-changes-using-dingtalk-bots.md) |
| GitOps 中 HPA 的使用 | 介绍如何处理 GitOps 和 HPA 对应用副本数的冲突。 | [应用使用](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/applications-using-hpa.md) [HPA](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/applications-using-hpa.md) |
| 自建 ArgoCD 无损迁移至 ACK One GitOps | 介绍如何将自建 ArgoCD 无损迁移至 ACK One GitOps。 | [自建](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/migrate-self-built-argocd-to-ack-one-gitops.md) [ArgoCD](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/migrate-self-built-argocd-to-ack-one-gitops.md) [迁移至](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/migrate-self-built-argocd-to-ack-one-gitops.md) [ACK One GitOps](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/migrate-self-built-argocd-to-ack-one-gitops.md) |
| 配置自定义域名访问 GitOps 控制台 | 介绍如何为 GitOps 控制台配置自定义域名。 | [自定义域名访问](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/access-the-gitops-console-through-a-custom-domain-name.md) [GitOps](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/access-the-gitops-console-through-a-custom-domain-name.md) [控制台](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/access-the-gitops-console-through-a-custom-domain-name.md) |


[上一篇：GitOps](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/gitops.md)[下一篇：GitOps快速入门](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/work-with-gitops.md)

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
