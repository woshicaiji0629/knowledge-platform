# 什么是专有网络VPC-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/what-is-vpc

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/vpc/documents/vpc-user-guide.md)

- [开发参考](products/vpc/documents/developer-reference.md)

- [产品计费](products/vpc/documents/product-billing.md)

- [常见问题](products/vpc/documents/troubleshooting.md)

- [动态与公告](products/vpc/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 什么是专有网络VPC

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

专有网络VPC（Virtual Private Cloud）是云上安全隔离的虚拟网络环境，支持自定义网络配置、部署和访问云产品资源。

VPC提供了类似于传统数据中心的安全和可配置的私有网络空间，同时又具备云计算的弹性和可扩展性。用户能够完全掌控自己的专有网络，包括选择自己的IP地址范围、创建交换机、配置路由表和网关等。

## 使用场景

| 云上部署私网应用 在 VPC 内多个可用区分别部署私网应用程序，提供高可用服务能力。 | 对外提供公网服务 VPC 内应用程序基于 NAT 网关和负载均衡，统一公网流量出入口。 |
| --- | --- |
| 多地域业务连接 基于 VPC 构建多地域业务，使用云企业网 CEN 实现不同地域 VPC 互联。 | 构建混合云 基于 VPC 搭建云上数据中心并进行互联，通过专线与云下数据中心互通。 |


## 产品优势

- 

安全隔离：基于隧道技术保证不同VPC之间安全隔离。

- 

稳定可靠：支持网络多路径检测和切换，支持网络故障快速切换自愈，保障业务稳定。

- 

灵活易用：按需配置网络，可自定义IP地址范围与路由表安全策略。

- 

互联互通：混合云架构下轻松管理云上云下和公网出入口，满足业务不同的组网和通信需求。

## 基本概念

每个VPC至少由三部分组成：私网网段、交换机和路由表。

- 

私网网段：例如192.168.0.0/16、192.168.1.0/24，用于VPC和交换机IP地址分配，需要合理规划。

- 

交换机：部署云产品资源，为云上资源提供IP地址。可以通过创建多个交换机，为VPC划分多个子网。

- 

路由表：用于控制网络流量从实例资源流向其他目的地所采用的路径。创建VPC后，系统会自动创建一张系统路由表并添加系统路由。

## VPC入门

- 

新手入门：您可登录[专有网络控制台](https://vpc.console.aliyun.com/vpc/cn-hangzhou/vpcs)，单击创建专有网络，快速完成[一个基础的创建专有网络与交换机任务](products/vpc/documents/vpc-and-vswitch.md)，为在VPC内部署云服务做准备。

- 

网络规划：合理的网络规划需要避免网段冲突并保障网络的可扩展性，网络规划不当将会导致后期极高的重建成本。因此，建议在创建专有网络之前先进行[网络规划](products/vpc/documents/vpc-network-planning.md)。

[上一篇：开始使用](products/vpc/documents/get-started.md)[下一篇：图说专有网络VPC](products/vpc/documents/figure-vpc.md)

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
