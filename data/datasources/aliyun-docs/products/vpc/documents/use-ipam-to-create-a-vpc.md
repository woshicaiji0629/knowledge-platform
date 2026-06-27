# 通过IPAM地址池分配网段创建专有网络-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/use-ipam-to-create-a-vpc

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

# 结合IPAM规划并创建专有网络

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

创建VPC和交换机时，您需要指定VPC和交换机的网段，合理的网段规划需要避免网络冲突并保障网络的可扩展性，规划不当将会导致极高的重建成本。随着组网规模不断提升，网段规划的复杂度较高且难度较大。您可以使用阿里云的IPAM地址管理与规划功能，自动分配或跟踪IP地址并检测可能的IP地址冲突，提升网段规划效率。本文将介绍如何根据开发需求，使用IPAM管理地址空间，从IPAM地址池中分配资源以搭建IPv4专有网络。

## 场景示例

某企业的多个业务部门、每个业务部门的生产环境和测试环境，具备不同的安全和业务部署诉求，需要通过VPC进行严格隔离。网络管理员需要对企业的地址资源进行高效管理，满足当前业务需求和未来扩展需求。

企业选择使用IPAM进行地址规划与管理，自动分配或跟踪IP地址并检测可能的IP地址冲突。IPAM能够灵活地管理地址池，地址池的CIDR设计通过将IP地址段划分为多个层级（如区域级、部门级或业务线级），实现灵活高效的管理。

本文以下图中生产环境中VPC1的创建为例，介绍如何使用IPAM进行网络规划并搭建IPv4专有网络：

- 

创建IPAM和私网IPAM作用范围。

- 

依次创建顶级池、子地址池并预置CIDR。

为顶级池分配一个较大的CIDR块192.168.0.0/16，顶级池的子地址池-1192.168.0.0/20用于创建生产环境。

- 

创建VPC1时选择从生产环境地址池中分配。

## 操作步骤

### 步骤一：创建IPAM

- 

登录[IPAM](https://ipam.console.aliyun.com/ap-southeast-3/ipam)[管理控制台](https://ipam.console.aliyun.com/ap-southeast-3/ipam)。在顶部菜单栏，选择要创建IPAM的地域。

- 

在IPAM页面，单击创建IPAM。配置生效地域，其他参数可保持默认值或根据实际情况修改。

说明

- 

创建IPAM时至少设置一个生效的地域，且生效地域必须包含IPAM托管地域。

- 

托管地域即当前IPAM所在的地域，不支持删除。

### 步骤二：创建顶级池

- 

在左侧导航栏，单击IPAM地址池。

- 

在IPAM地址池页面，单击创建地址池，按下图进行配置，其他参数可保持默认值或根据实际情况修改。此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于参数的更多信息，请参见[创建和管理](products/vpc/documents/create-and-manage-address-pools.md)[IPAM](products/vpc/documents/create-and-manage-address-pools.md)[地址池](products/vpc/documents/create-and-manage-address-pools.md)。

- 

归属IPAM作用范围：只支持选择私网类型的IPAM作用范围。

- 

CIDR范围：选择IPAM，创建的当前地址池为顶级池。

- 

生效地域：IPAM地址池设置的生效地域需在所属IPAM生效地域的范围内，且一旦设置不允许修改。

- 

自动导入发现的资源：开启后，IPAM将通过资源发现能力持续查找VPC，将CIDR在当前地址池范围内且CIDR在IPAM中未分配的资源自动导入到IPAM中。

- 

预置CIDR：您可以单击添加CIDR，添加多个CIDR，只支持创建IPv4类型的CIDR。

- 

分配规则：设置地址池内分配给资源的最小网络掩码长度、默认网络掩码长度以及最大网络掩码长度。

### 步骤三：创建子地址池

按下图进行配置，顶级池的子地址池-1192.168.0.0/20用于创建生产环境。

此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于参数的更多信息，请参见[创建和管理](products/vpc/documents/create-and-manage-address-pools.md)[IPAM](products/vpc/documents/create-and-manage-address-pools.md)[地址池](products/vpc/documents/create-and-manage-address-pools.md)。

- 

归属IPAM作用范围：只支持选择私网类型的IPAM作用范围。

- 

CIDR范围：选择IPAM地址池，创建的当前地址池为源池的子地址池。

- 

源IPAM地址池：选择步骤二创建的顶级池。

- 

生效地域：源IPAM地址池设置生效地域时，子地址池无需设置生效地域，直接继承源地址池的生效地域。

- 

自动导入发现的资源：开启后，IPAM将通过资源发现能力持续查找VPC，将CIDR在当前地址池范围内且CIDR在IPAM中未分配的资源自动导入到IPAM中。

- 

预置CIDR：您可以单击添加CIDR，添加多个CIDR，只支持创建IPv4类型的CIDR。

- 

分配规则：设置地址池内分配给资源的最小网络掩码长度、默认网络掩码长度以及最大网络掩码长度。

创建完成后，池层次结构如下图所示。

### 步骤四：创建VPC1和交换机，选择从IPAM地址池分配CIDR

- 登录[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)。

- 

在顶部菜单栏处，选择专有网络的地域。本文选择IPAM地址池的生效地域。

- 

在专有网络页面，单击创建专有网络。根据以下信息配置专有网络和交换机，然后单击确定。

此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于参数的更多信息，请参见[创建和管理专有网络](products/vpc/documents/user-guide/create-and-manage-a-vpc.md)。

- 

IPv4网段：选择IPAM 分配的 IPv4 地址段。

- 

选择地址池：选择[步骤三](products/vpc/documents/use-ipam-to-create-a-vpc.md)中创建的地址池。

- 

IPv4地址掩码：当您设置网络掩码后，系统会默认分配指定掩码范围内第一个可用的CIDR，您也可以在地址池预置CIDR内，按需指定IPv4网段。

- 

交换机的IPv4网段：需要从属于IPAM分配的IPv4地址段。

- 

创建完成后，您可在[步骤三](products/vpc/documents/use-ipam-to-create-a-vpc.md)中创建地址池详情页的详细信息页签下，查看到该地址池中已有1.6%的地址资源被分配。

说明

子地址池预置CIDR为192.168.0.0/20，为该池提供4096个可用IP地址；设置网络掩码为/26，地址池中64个IP地址被分配给VPC1。因此，已有64/4096 = 1.6%的地址资源被分配给创建的VPC。

您可以在分配页签下，查看到相应的地址资源被分配给创建的VPC。

## 相关文档

- 

如果您需要了解IPAM的功能简介、应用场景、使用限制及计费等信息，请参见[IP](products/vpc/documents/ip-address-management-ipam.md)[地址管理（IPAM）](products/vpc/documents/ip-address-management-ipam.md)。

- 

如果您需要了解如何使用IPAM实现高效、可扩展以及安全的网络地址规划，请参见[地址规划](products/vpc/documents/address-planning.md)。

[上一篇：地址资源管理](products/vpc/documents/shared-resource-discovery-for-multi-account-address-resource-conflict-management.md)[下一篇：DHCP选项集与DNS主机名](products/vpc/documents/dhcp-option-set-and-dns-hostname.md)

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
