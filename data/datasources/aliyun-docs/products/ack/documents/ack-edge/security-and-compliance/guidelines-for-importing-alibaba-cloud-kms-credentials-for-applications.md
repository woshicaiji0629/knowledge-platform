# 应用安全获取KMS凭据的方案对比-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/guidelines-for-importing-alibaba-cloud-kms-credentials-for-applications

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

# 为应用导入阿里云KMS服务凭据

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以在应用Pod中以文件系统、Secret挂载或本地HTTP接口读取内存的形式，将存储在阿里云KMS凭据管家中的密文引入到应用程序中使用，避免应用开发构建时泄露敏感数据。若应用依赖文件系统读取密钥，与KMS 凭据管家集成时可能存在兼容性问题，可通过ack-secret-manager或csi-secrets-store-provider-alibabacloud解决；若期望应用可以直接从内存中获取敏感KMS凭据，避免敏感凭据落盘，可通过ack-kms-agent-webhook-injector实现更安全的凭据导入与管理。

## 组件介绍

- 

ack-secret-manager：支持以Kubernetes Secret的形式向集群导入或同步KMS凭据信息，确保集群内应用能够安全访问敏感数据。工作负载可通过文件系统挂载指定Secret实例，以使用凭据信息。

- 

csi-secrets-store-provider-alibabacloud：支持以Kubernetes Secret的形式向集群导入或同步KMS凭据信息，确保集群内应用能够安全访问敏感数据；还支持通过CSI Inline的形式将凭据密钥作为文件系统直接挂载到应用中，适用于通过文件系统接口（如读取文件）来获取敏感信息的应用。

- 

ack-kms-agent-webhook-injector：将[KMS Agent](products/kms/documents/key-management-service/developer-reference/kms-agent-overview.md)作为Sidecar容器注入Pod，使业务应用可通过本地HTTP接口，借助KMS Agent从KMS实例获取凭据并缓存于内存中，避免敏感信息硬编码，提升数据安全性。

## 使用场景

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 组件 | 适用的集群 | 使用说明 | 相关操作 |
| --- | --- | --- | --- |
| ack-secret-manager | ACK 托管集群 ACK 专有集群 ACK One 注册集群 ACK Serverless 集群 | 支持 Secret 同步和更新。 | [使用](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [ack-secret-manager](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [导入阿里云](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [KMS](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [服务凭据](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) |
| csi-secrets-store-provider-alibabacloud | 1.20 及以上版本的集群： ACK 托管集群 ACK 专有集群 ACK One 注册集群 | 支持 Secret 同步和更新。 支持通过 CSI Inline 的形式将凭据密钥作为文件系统直接挂载到应用程序中。 | [使用](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md) [csi-secrets-store-provider-alibabacloud](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md) [导入阿里云](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md) [KMS](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md) [服务凭据](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md) |
| ack-kms-agent-webhook-injector | 1.22 及以上版本的集群： ACK 托管集群 ACK 专有集群 | 支持 Secret 同步和更新。 支持通过本地 HTTP 接口，借助 KMS Agent 从 KMS 实例获取凭据并缓存在内存中。 | [使用](products/kms/documents/key-management-service/developer-reference/ack-rapid-integration-through-components.md) [ack-kms-agent-webhook-injector](products/kms/documents/key-management-service/developer-reference/ack-rapid-integration-through-components.md) [导入阿里云](products/kms/documents/key-management-service/developer-reference/ack-rapid-integration-through-components.md) [KMS](products/kms/documents/key-management-service/developer-reference/ack-rapid-integration-through-components.md) [服务凭据](products/kms/documents/key-management-service/developer-reference/ack-rapid-integration-through-components.md) |


## 相关计费

- 

ack-secret-manager和csi-secrets-store-provider-alibabacloud安装使用免费，但安装后将占用Worker节点资源。您可以在安装组件时配置各模块的资源申请量。

- 

使用KMS凭据管家会产生费用，请参见[产品计费](products/kms/documents/key-management-service/product-overview/kms-billing.md)。

[上一篇：使用阿里云KMS进行Secret的落盘加密](products/ack/documents/ack-edge/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-1.md)[下一篇：使用ack-secret-manager导入阿里云KMS服务凭据](products/ack/documents/ack-edge/security-and-compliance/use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)

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
