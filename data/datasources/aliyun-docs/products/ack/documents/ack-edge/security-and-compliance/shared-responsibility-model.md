# 安全责任划分与共担模型-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/shared-responsibility-model

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

# 安全责任共担模型

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

安全合规在ACK集群托管架构下遵循责任共担原则，其中容器服务ACK负责集群控制面组件（包括Kubernetes控制平面组件和etcd）以及集群服务相关阿里云基础设施的默认安全性。本文介绍阿里云容器服务ACK的安全责任共担模型。

## 阿里云负责

首先在管控面侧，阿里云会通过完备的平台安全能力负责管控侧基础设施（包括计算、存储、网络等云服务资源）的安全性；同时基于阿里云OS安全加固等业务通用的安全标准基线，对ACK集群管控面组件配置和镜像进行符合标准定义的安全加固。针对集群节点OS或K8s组件层面的安全漏洞，阿里云会负责及时提供相关公告并发布对应的漏洞补丁或版本更新能力。同时阿里云会面向企业云原生应用生命周期中安全防护的典型场景，提供必要的[安全防护功能](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/security-system-overview.md)和[最佳实践指导](https://help.aliyun.com/zh/document_detail/347684.html#task-2134590)。

## 客户负责

客户的安全管理运维人员需要负责部署在云上的业务应用安全防护以及对云上资源的安全配置和更新，包含以下内容：

- 

基于阿里云公告和提供的补丁或版本升级方式及时进行OS、集群侧系统组件、运行时等漏洞的修复和版本更新。

- 

遵循安全原则进行ACK集群、节点池和网络等参数配置，避免因为不当的参数或权限配置给攻击者可乘之机。

- 

基于使用需求，遵循权限最小化原则进行应用或账号、角色的授权，凭据的管理，相关安全策略的部署实施以及应用自身参数配置安全。

- 

负责应用制品的供应链安全。

- 

负责应用敏感数据和应用运行时刻的安全。

- 

对于离职员工或非受信人员，删除RAM用户或RAM角色并不会同步删除该用户或角色拥有的集群KubeConfig中的RBAC权限。因此，在删除RAM用户或RAM角色之前，请吊销离职员工或非受信用户的KubeConfig权限。具体操作，请参见[吊销集群的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential.md)[KubeConfig](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential.md)[凭证](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential.md)。

- 

针对容器服务ACK Edge集群，负责边缘节点稳定性和OS层面安全漏洞的修复和版本更新。

## 理解责任共担模型

在您设计和部署企业应用系统之前，请您充分理解企业自身和阿里云的安全责任边界。

ACK托管架构下集群安全的责任共担模型如下图所示。

当您选择使用ACK Serverless集群或在ACK托管集群中部署虚拟节点组件（ack-virtual-node）时，除了集群控制面和基础设施安全外，阿里云还将负责Pod底层[弹性容器实例（ECI）运行时](https://help.aliyun.com/zh/eci/product-overview/what-is-elastic-container-instance)的安全，由客户负责重建应用Pod以使修复生效。下图为Serverless架构下使用ACK Serverless集群或在ACK托管集群中部署虚拟节点组件（ack-virtual-node）时的安全责任共担模型。

对于使用[托管节点池](products/ack/documents/overview-of-managed-node-pools.md)的ACK集群，阿里云会负责根据客户对于托管节点池的配置尝试自动化的修复节点OS漏洞和Kubelet版本升级，其中，节点OS漏洞的修复补丁由[云安全中心](https://help.aliyun.com/zh/security-center/user-guide/purchase-security-center#task-lxj-3bc-zdb)提供。如果集群节点使用的是自定义OS镜像，仍需要由客户负责节点漏洞的修复更新。下图为托管架构下ACK集群使用托管节点池时的安全责任共担模型。

针对容器服务ACK Edge集群，阿里云负责集群控制面，对数据面[边缘节点池](products/ack/documents/ack-edge/user-guide/overview-of-cell-based-management-at-the-edge.md)提供K8s相关公告并发布对应的漏洞补丁或版本更新能力，客户需要基于阿里云公告以及提供的补丁或版本升级方式及时进行集群侧系统组件、运行时等漏洞的修复和版本更新。此外，客户需要负责边缘节点自身的稳定性、OS层面安全漏洞的修复和版本更新。

[上一篇：安全体系概述](products/ack/documents/ack-edge/security-and-compliance/security-system-overview.md)[下一篇：安全概览](products/ack/documents/ack-edge/security-and-compliance/security-overview.md)

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
