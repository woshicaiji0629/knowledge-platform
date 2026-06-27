# 自定义集群API Server证书的SAN字段-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/customize-the-san-of-the-api-server-certificate-when-you-create-an-ack-cluster

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

# 自定义集群API Server证书的SAN字段

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK集群的API Server服务端证书中SAN（Subject Alternative Name）字段默认包括集群本地域名、API Server负载均衡的内网IP、API Server服务本地IP和公网EIP等字段。如果您有特殊的代理访问或跨域访问需求，可以通过控制台为新建集群或已有集群自定义SAN字段。

## 前提条件

已创建ACK托管集群、ACK专有集群或ACK Serverless集群。具体操作，请参见[创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)、[创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-dedicated-cluster.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-dedicated-cluster.md)[专有集群（已停止新建）](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-dedicated-cluster.md)或[创建集群](products/ack/documents/serverless-kubernetes/user-guide/create-an-ask-cluster-2.md)。

重要

- 

ACK Serverless集群不支持在新建集群时自定义SAN字段，仅支持在已有集群中更新SAN字段。

- 

ACK专有集群仅支持在新建集群时自定义SAN字段，不支持在已有集群中更新SAN字段。

## SAN介绍

SAN是一项对X.509标准的扩展，它允许在SSL安全证书中使用subjectAltName字段将多种值（包括IP地址、域名、URI和电子邮件等）与证书关联。

## 自定义集群API Server证书的SAN字段

## 新建集群

本小节以创建ACK托管集群为例，说明如何在新建集群过程中自定义API Server证书的SAN字段。其他集群类型的操作类似。

在创建集群的集群配置，单击显示高级选项。在自定义证书 SAN配置项中输入配置字段。具体操作，请参见[创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。

说明

自定义证书 SAN字段的配置，支持输入符合规范的自定义IP、域名和URI，多个字段以英文逗号（,）分隔。

自定义证书 SAN字段中可包含域名和IP。

## 已有集群

重要

更新或修改自定义证书SAN会触发集群API Server短暂重启。请在业务低峰期操作。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。

- 

在集群信息页面单击基本信息页签，然后在网络区域单击自定义证书 SAN右侧的编辑。

- 

在更新自定义证书 SAN对话框，配置自定义证书 SAN字段，参数配置完成后，单击确定。

## 相关文档

API Server的审计日志可以帮助您记录或追溯不同用户的日常操作。更多信息，请参见[使用集群](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)[API Server](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)[审计功能](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/work-with-cluster-auditing.md)。

[上一篇：为Pod动态配置阿里云产品白名单](products/ack/documents/ack-edge/security-and-compliance/dynamically-add-the-ip-addresses-of-pods-to-the-whitelists-of-alibaba-cloud-services.md)[下一篇：【已弃用】使用Pod安全策略](products/ack/documents/ack-edge/security-and-compliance/use-pod-security-policies.md)

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
