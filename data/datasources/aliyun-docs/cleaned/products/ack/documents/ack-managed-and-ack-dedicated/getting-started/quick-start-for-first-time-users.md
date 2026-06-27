# 快速创建ACK托管集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/getting-started/quick-start-for-first-time-users

# 快速创建ACK托管集群
首次使用阿里云容器服务 Kubernetes 版 ACK（Container Service for Kubernetes），您需要为阿里云账号赋予系统角色权限，才能正常创建集群、保存日志并访问ECS、OSS、NAS、SLB等云服务。本文将指导您完成授权、免费开通相关云产品，并快速创建一个ACK托管集群。
## 1. 开通容器服务并为角色授权
在创建ACK集群之前，您需要免费开通相应服务。如果您在创建ACK集群前没有开通容器服务ACK，可能会导致集群无法创建或创建失败。建议按照以下操作开通容器服务，并为容器服务默认角色授权。
开通容器服务ACK
首次开通容器服务ACK时，您需要登录[容器服务](https://common-buy.aliyun.com/?spm=5176.2020520152.0.0.75a361b1SJ9jQT&commodityCode=csk_propayasgo_public_cn)[ACK](https://common-buy.aliyun.com/?spm=5176.2020520152.0.0.75a361b1SJ9jQT&commodityCode=csk_propayasgo_public_cn)[开通页面](https://common-buy.aliyun.com/?spm=5176.2020520152.0.0.75a361b1SJ9jQT&commodityCode=csk_propayasgo_public_cn)，阅读并选中容器服务ACK服务协议，单击立即开通。
在集群类型区域选择ACK Pro版或ACK 基础版，选择ACK Pro版将同时开通ACK Pro版和ACK基础版。
角色授权
首次登录容器服务ACK时，为了您账号的ACK集群云资源的访问安全，您需要授权阿里云账号创建容器服务默认角色，授权该默认角色是为了确保ACK能够正常调用相关的云服务资源，从而实现集群的创建、管理和维护等功能。角色授权操作步骤如下。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，然后单击前往RAM进行授权进入[访问控制快速授权](https://ram.console.aliyun.com/role/authorize?request=%7B%22ReturnUrl%22%3A%22https%3A%2F%2Fcs.console.aliyun.com%2F%22%2C%22Services%22%3A%5B%7B%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCSManagedLogRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedLogRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedCmsRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedCmsRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedCsiRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedCsiRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedCsiProvisionerRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedCsiProvisionerRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedCsiPluginRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedCsiPluginRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSServerlessKubernetesRole%22%2C%22TemplateId%22%3A%22ServerlessKubernetes%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSKubernetesAuditRole%22%2C%22TemplateId%22%3A%22KubernetesAudit%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedNetworkRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedNetworkRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSDefaultRole%22%2C%22TemplateId%22%3A%22Default%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedKubernetesRole%22%2C%22TemplateId%22%3A%22ManagedKubernetes%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedArmsRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedArmsRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCISDefaultRole%22%2C%22TemplateId%22%3A%22AliyunCISDefaultRole%22%7D%5D%2C%22Service%22%3A%22CS%22%7D%5D%7D)页面，然后单击确认授权。完成以上授权后，刷新控制台即可使用。
如果您需要了解更多服务角色的资源操作权限，请参见[容器服务](../user-guide/ack-default-roles.md)[ACK](../user-guide/ack-default-roles.md)[服务角色](../user-guide/ack-default-roles.md)。
## 2. 开通集群相关云产品
为了您能够快速体验创建、使用和管理ACK集群等功能，您可以使用阿里云账号，单击开通链接按需开通与功能相关联的云资源服务。只有阿里云账号才能开通云产品，RAM用户暂不支持开通云产品操作。如果您想为RAM用户授权，用于管理已开通的云产品，详细操作，请参见[授权管理](../user-guide/faq-about-authorization-management.md)[FAQ](../user-guide/faq-about-authorization-management.md)。
必选项：使用ACK集群的强依赖服务，必须开通。
展开查看相关产品。
| 产品名称 | 开通链接 | 产品说明 |
| --- | --- | --- |
| 专有网络 VPC | [专有网络 VPC](https://www.aliyun.com/product/vpc) | 用于构建集群网络环境和路由规则。 |
| 负载均衡 SLB | [负载均衡 SLB](https://www.aliyun.com/product/slb) | 用于为集群创建负载均衡，对流量进行按需分发的服务，通过将流量分发到不同的后端服务器来扩展应用系统的吞吐能力，并且可以消除系统中的单点故障，提升应用系统的可用性。 |
| 弹性伸缩服务 ESS | [弹性伸缩](https://www.aliyun.com/product/ess) | 用于为集群创建 Worker 节点和实现自动伸缩。 |
建议项：集群创建和应用管理中常见的依赖服务，建议开通。
展开查看相关产品。
| 产品名称 | 开通链接 | 产品说明 |
| --- | --- | --- |
| NAT 网关服务 | [NAT](https://www.aliyun.com/product/nat) [网关](https://www.aliyun.com/product/nat) | 用于为集群开启公网访问和公网镜像拉取。 |
| 文件存储 NAS | [文件存储 NAS](https://www.aliyun.com/product/nas) | 基于 NAS 实现集群应用数据的共享访问、弹性扩展、高可靠以及高性能持久化文件存储方案。 |
| 日志服务 SLS | [日志服务 SLS](https://www.aliyun.com/product/sls) | 用于 ACK 集群组件和应用的日志采集和检索。 |
| 阿里云可观测监控 Prometheus 版 | [可观测监控 Prometheus 版](https://www.aliyun.com/product/developerservices/prometheus) | 基于 Prometheus 实现对 ACK 集群的监控和告警。 |
| 容器镜像服务 ACR | [容器镜像服务 ACR](https://www.aliyun.com/product/acr) | 用于镜像的安全托管和全生命周期管理。 |
| 弹性容器实例 ECI | [弹性容器实例](https://www.aliyun.com/product/eci) | 使用虚拟节点运行 Serverless 弹性容器实例。 |
| 服务网格 ASM | [服务网格 ASM](https://www.aliyun.com/product/servicemesh) | 基于 服务网格 实现多个 ACK 集群应用的统一流量管理。 |
| 云监控服务 CMS | [云监控](https://www.aliyun.com/product/jiankong) | 用于监控集群节点和应用运行状态。 |
可选项：根据业务架构和运维需求选择性开通。
展开查看相关产品。
| 产品名称 | 开通链接 | 产品说明 |
| --- | --- | --- |
| 云安全中心 SAS | [云安全中心](https://www.aliyun.com/product/sas) | 用于监控集群应用运行时的安全事件和告警。 |
| 对象存储 OSS | [对象存储 OSS](https://www.aliyun.com/product/oss) | 基于 OSS 实现集群应用数据安全、低成本的对象存储方案。 |
| 密钥管理服务 KMS | [密钥管理服务](https://www.aliyun.com/product/kms) | 用于集群应用密钥的管理以及 Pro 集群开启密钥的落盘加密能力。 |
| 云解析 PrivateZone 服务 | [云解析 PrivateZone](https://www.aliyun.com/product/pvtz) | 基于阿里云专有网络 VPC（Virtual Private Cloud）环境的私有 DNS 服务。该服务允许您在自定义的一个或多个 VPC 中将私有域名映射到 IP 地址。旨在为企业提供一个稳定、安全且高效的内网 DNS 解决方案，满足从简单到复杂的各种网络架构需求。 |
| 云备份 Cloud Backup | [云备份 Cloud Backup](https://www.aliyun.com/product/hbr?spm=a2c4g.11186623.0.0.4a2921afpp2aYy) | 提供备份、容灾保护以及策略化归档管理。 |
## 3. 快速创建集群
创建ACK托管集群时，您可以选择开启智能托管模式。开启后，您仅需进行简单的规划配置，即可一键创建符合最佳实践的ACK集群。该集群会默认创建一个智能托管节点池，其中的节点生命周期将由ACK进行托管和运维。更多信息，请参见[创建](../user-guide/create-ack-managed-clusters-in-auto-mode.md)[ACK Auto Mode 集群](../user-guide/create-ack-managed-clusters-in-auto-mode.md)。
说明
如果您需要对集群进行详细自定义配置，可参见[创建](../user-guide/create-an-ack-managed-cluster-2.md)[ACK](../user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../user-guide/create-an-ack-managed-cluster-2.md)的完整流程来完成集群创建。
登录[容器服务管理控制台](https://cs.console.aliyun.com)。在集群列表页面，单击创建集群。
在上方选择ACK 托管集群页签，单击开启智能托管，如果您有公网访问集群能力的需求，您可以在个人测试集群勾选使用 EIP 暴露 API server获得该能力，方便您的后续连接和管理集群。然后单击确认配置，检查所选配置后单击创建集群。
快速创建模式下，默认网络插件为Terway（已勾选 Trunk ENI），服务网段为192.168.0.0/16，专有网络自动创建并已勾选为专有网络配置 SNAT，安全组为自动创建企业级安全组。
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
