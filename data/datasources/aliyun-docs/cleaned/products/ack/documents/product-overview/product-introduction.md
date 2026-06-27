# Kubernetes容器化应用生命周期管理-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/product-overview/product-introduction

# 什么是阿里云容器服务Kubernetes版
阿里云容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。本文介绍什么是容器服务 Kubernetes 版以及其下不同的集群类型。
## 产品介绍
容器服务ACK提供多种集群类型，包括ACK托管集群、ACK Serverless集群、ACK Edge集群等。
| 集群类型 | 说明 | 简介 | 计费 |
| --- | --- | --- | --- |
| 容器服务 Kubernetes 版 | 容器服务 Kubernetes 版 的 ACK 托管集群 提供 ACK 托管集群 Pro 版 和 ACK 托管集群基础版 。 ACK 托管集群 Pro 版 是在 ACK 托管集群基础版 的基础上发展而来的集群类型，继承了原托管版集群的所有优势，例如控制面托管、控制面高可用等，同时进一步增强了集群的可靠性、安全性和调度性，并且支持赔付标准的 SLA，适合生产环境下有着大规模业务，对稳定性和安全性有高要求的企业客户。 | [什么是容器服务 Kubernetes 版](../ack-managed-and-ack-dedicated/product-overview/what-is-ack.md) | [ACK](../ack-managed-and-ack-dedicated/product-overview/ack-pro-cluster-billing.md) [托管和专有集群计费说明](../ack-managed-and-ack-dedicated/product-overview/ack-pro-cluster-billing.md) |
| 容器服务 Serverless 版 | 无服务器 Kubernetes 容器服务。在 ACK Serverless 集群 中，您无需购买节点即可直接部署容器应用，无需对集群进行节点维护和容量规划，并且根据应用配置的 CPU 和内存资源量进行按需付费。 ACK Serverless 集群 提供完善的 Kubernetes 兼容能力，同时降低了 Kubernetes 使用门槛，让您更专注于应用程序，而不是管理底层基础设施。 | [什么是容器服务 Serverless 版](../serverless-kubernetes/product-overview/ask-overview.md) | [ACK Serverless](../serverless-kubernetes/product-overview/ack-serverless-cluster-billing-instructions.md) [集群计费说明](../serverless-kubernetes/product-overview/ack-serverless-cluster-billing-instructions.md) |
| 容器服务 Edge 版 | 容器服务 Edge 版 是针对边缘计算场景推出的云边一体化协同托管方案。在云端提供一个标准、安全、高可用的 Kubernetes 集群，整合阿里云虚拟化、存储、网络和安全等能力，并简化集群运维工作，让您专注于容器化应用的开发与管理。 | [什么是容器服务 Edge 版](../ack-edge/product-overview/ack-edge-overview.md) | [ACK Edge](../ack-edge/product-overview/billing-of-ack-edge-clusters.md) [集群计费说明](../ack-edge/product-overview/billing-of-ack-edge-clusters.md) |
| 容器服务灵骏版 | 容器服务灵骏版 是针对智能计算灵骏提供的集群类型，提供全托管和高可用控制面的标准 Kubernetes 集群服务，支持以灵骏计算节点作为 Kubernetes 集群的工作节点。 | [什么是容器服务灵骏版](../ack-lingjun-managed-clusters/product-overview/overview-14.md) | [ACK](../ack-lingjun-managed-clusters/product-overview/billingofacklingjun.md) [灵骏集群计费说明](../ack-lingjun-managed-clusters/product-overview/billingofacklingjun.md) |
| 云原生 AI 套件 | 以容器服务为底座的云原生 AI 技术和产品方案。 向下封装对各类异构资源的统一管理，向上提供标准 Kubernetes 集群环境和 API，以运行各核心组件，实现资源运维管理、AI 任务调度和弹性伸缩、数据访问加速、工作流编排、大数据服务集成、AI 作业生命周期管理、AI 制品管理、统一运维等功能。 向上针对 AI 生产流程中的主要环节，支持 AI 数据集管理，AI 模型开发、训练、评测，以及模型推理服务等。 | [云原生](../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-overview.md) [AI](../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-overview.md) [套件概述](../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-overview.md) | [云原生](../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-free-open-instructions.md) [AI](../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-free-open-instructions.md) [套件计费说明](../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-free-open-instructions.md) |
| 分布式云容器平台 | 面向混合云、多集群、分布式计算、容灾等场景推出的企业级云原生平台。支持连接并管理您任何地域、任何基础设施上的 Kubernetes 集群，从云端、到边缘、到 IDC。提供一致的管理和社区兼容的 API，支持对计算、网络、存储、安全、监控、日志、作业、应用、流量等进行统一运维管控。 | [ACK One](../distributed-cloud-container-platform-for-kubernetes/product-overview/ack-one-overview.md) [概述](../distributed-cloud-container-platform-for-kubernetes/product-overview/ack-one-overview.md) | [ACK One](../distributed-cloud-container-platform-for-kubernetes/product-overview/ack-one-billing.md) [计费说明](../distributed-cloud-container-platform-for-kubernetes/product-overview/ack-one-billing.md) |
## 产品优势
相较于自建的Kubernetes集群，容器服务 Kubernetes 版集群在应用、网络、存储、安全等多个方面均提供能力兼容与增强，无需您自行探索和开发，大大降低集群管理和运维成本。下表列举主要对比项。
| 对比项 | 自建 Kubernetes 集群 | 容器服务 Kubernetes 版集群 |
| --- | --- | --- |
| 集群管理 | 用户手动部署集群并自行开发。 用户自行探索和开发。 | 通过控制台一键创建集群，支持 GPU 实例和裸金属服务器，支持创建跨 AZ 高可用的集群。 提供容器优化的 OS 镜像，提供稳定测试和安全加固的 Kubernetes 和 Docker 版本。 支持多集群管理，支持跨 AZ 高可用集群，支持集群联邦管理。 |
| 应用管理 | 用户自行探索和开发。 | 支持灰度发布，支持蓝绿发布。 支持应用监控、应用弹性伸缩。 内置应用商店，支持 Helm 应用一键部署；支持服务目录，简化云服务集成。 |
| 网络管理 | 需要挑选社区网络插件进行适配。 用户自行探索和开发。 | 提供针对阿里云优化的高性能 VPC/ENI 网络插件，性能优于普通网络方案 20%。 支持容器访问策略和容器带宽限制。 |
| 存储管理 | 用户自行探索和开发。 | 支持阿里云云盘、本地盘、NAS、CPFS 和 OSS，提供标准的 CSI 驱动。 支持存储卷自动创建、迁移。 |
| 运维管理 | 手动运维控制面。 | 支持 Kubernetes 新版本一键升级，支持集群组件生命周期管理、支持集群手动和自动弹性伸缩。 提供高性能日志采集 Agent，提供大量日志 dashboard 看板 。 支持托管的 Prometheus 监控体系，默认内置多数大盘。 Pro 版集群提供多 AZ 高可用自动伸缩的托管的控制面，同时提供控制面可观测能力。 |
| 安全管理 | 自行构建安全能力。 | 支持镜像扫描/镜像签名。 支持容器运行时安全检测。 支持 Secret 数据落盘加密。 支持操作系统等保加固和 阿里云 OS 加固 。 |
| 服务保障 | 需要组建专门团队。 无 SLA 保障。 | 阿里云专业容器团队作为技术支持，为集群提供及时的稳定性和安全响应。 历经阿里大规模实践，是目前中国最大规模的公共云容器服务之一。 CNCF 白金会员，已通过一致性验证。 2019 年 Forrester 报告中国排名第一。2023 年入选 Gartner®容器管理魔力象限领导者象限，也是亚洲地区唯一入选该象限的云服务商。 ACK 托管集群 Pro 版 提供赔付保障的 SLA。 |
## 相关文档
[开服地域](supported-regions.md)
[使用须知及高危风险操作说明](before-you-start.md)
[配额与限制](limits.md)
[相关协议](../support/agreement.md)（容器服务 Kubernetes 版的服务条款和服务等级协议SLA说明）
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
