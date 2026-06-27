# 保障集群主机安全的配置与实践-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/host-security

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

# 主机安全

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器运行所依赖的宿主机的安全保证容器的运行，建议您定期运行基线检查以验证集群是否符合阿里云OS安全加固（简称“阿里云OS加固”）标准、使用阿里云云安全中心安全防范能力、最小化对节点的访问权限以及遵循ECS安全最佳实践。

## 定期运行基线检查以验证集群是否符合阿里云OS加固和等保加固标准

### 阿里云OS加固

对于集群节点宿主机OS系统，阿里云OS加固功能提供了对应的加固标准，提供的操作系统包括Alibaba Cloud Linux、CentOS、Ubuntu等。Alibaba Cloud Linux 3不仅是阿里云官方操作系统镜像，也是ACK的首选默认系统镜像。更多信息，请参见[Alibaba Cloud Linux 3](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-alibaba-cloud-linux-3.md)。

### 等保加固

阿里云根据《GB/T22239-2019信息安全技术网络安全等级保护基本要求》中对操作系统提出的一些等级保护要求，基于云原生操作系统Alibaba Cloud Linux提供了等保加固功能，检查项包括身份鉴别、访问控制、安全审计、入侵防范、恶意代码防范等。更多信息，请参见[ACK](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/ack-reinforcement-based-on-classified-protection.md)[等保加固使用说明](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/ack-reinforcement-based-on-classified-protection.md)。

## 使用阿里云云安全中心安全防范能力

阿里云云安全中心支持对ACK集群节点的默认安全提供全方位保护，包括：

- 

漏洞修复：支持对主流漏洞类型进行检测并提供一键修复功能。您可以在漏洞修复页面查看服务器当前存在的漏洞风险，并手动执行一键扫描，帮助您更全面地了解您资产中的漏洞和风险情况。

- 

基线检查：基线检查功能针对服务器操作系统、数据库、软件和容器的配置进行安全检测，并提供检测结果说明和加固建议。基线检查功能可以帮助您进行系统安全加固，降低入侵风险并满足安全合规要求。

- 

云平台配置检查：云平台配置检查从身份认证及权限、网络访问控制、数据安全、日志审计、监控告警、基础安全防护六个维度为您提供云产品安全配置的检查，帮助您及时发现您的云产品配置风险并提供相应的修复方案。

- 

镜像安全扫描：支持对镜像中存在的高危系统漏洞、应用漏洞、恶意样本、配置风险和敏感数据进行检测和识别，并提供漏洞修复方案，为您提供一站式漏洞管理能力，让镜像漏洞修复更简单。

## 最小化对节点的访问权限

当您想要对节点进行远程访问时，可以通过登录[容器服务管理控制台](https://cs.console.aliyun.com)，通过Workbench或者VNC进行内网访问。如果没有业务需要，不为节点挂载公网EIP。若要公网访问，应该在ACK的安全组中配置ACK访问策略，限制访问来源。并且需要在ACK安全组中控制对节点各个端口的暴露，对于需要公网暴露的端口，必须限制访问来源。

## 遵循ECS安全最佳实践

ACK默认使用Alibaba Cloud Linux 3创建ECS实例作为ACK的节点。关于在阿里云ECS实例使用过程中提高安全性，请参见[云服务器](products/ecs/documents/user-guide/best-security-practices.md)[ECS](products/ecs/documents/user-guide/best-security-practices.md)[安全性](products/ecs/documents/user-guide/best-security-practices.md)。

## 相关文档

- 

如果您想了解如何为ACK集群开启等保加固、配置基线检查策略，请参见[ACK](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/ack-reinforcement-based-on-classified-protection.md)[等保加固使用说明](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/ack-reinforcement-based-on-classified-protection.md)。

- 

容器服务 Kubernetes 版已全面支持阿里云新一代操作系统Alibaba Cloud Linux 3的节点创建，并结合Alibaba Cloud Linux 3的高内核特性提供了多场景优化。更多信息，请参见[Alibaba Cloud Linux 3](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-alibaba-cloud-linux-3.md)。

- 

云安全中心漏洞管理支持发现和识别操作系统、Web内容管理系统、应用程序中的安全漏洞，可对漏洞进行优先级和风险评估，并支持一键修复部分漏洞，帮助您缩小系统的攻击面。更多信息，请参见[什么是漏洞管理](https://help.aliyun.com/zh/security-center/user-guide/overview-4)。

[上一篇：多租户安全](products/ack/documents/ack-edge/security-and-compliance/multi-tenancy-security.md)[下一篇：容器安全FAQ](products/ack/documents/ack-edge/security-and-compliance/faq-about-container-security.md)

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
