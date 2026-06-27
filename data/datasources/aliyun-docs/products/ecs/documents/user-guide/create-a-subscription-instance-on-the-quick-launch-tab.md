# 快速购买ECS实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/create-a-subscription-instance-on-the-quick-launch-tab

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 快速购买ECS实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

快速购买提供了四种配置多种套餐的实例规格。您可以在几分钟内，以最简单的方式购买一个ECS实例，提高配置效率。本文介绍如何快速购买ECS实例。

重要

如果您刚接触ECS不久，想要快速上手购买并使用ECS实例，我们为您准备了一个较简单的示例，请参见[控制台购买 Windows 实例并搭建 IIS Web](products/ecs/documents/user-guide/quickly-purchase-a-windows-instance-and-build-an-iis-service.md)[服务](products/ecs/documents/user-guide/quickly-purchase-a-windows-instance-and-build-an-iis-service.md)，它将帮助您更直观地理解整个流程。在初步了解ECS后，您可以通过阅读本文，了解快速购买实例时更加详细的配置说明。

## 前提条件

- 

注册中国站阿里云账号，并完成实名认证。具体操作，请参见[阿里云账号注册流程](https://help.aliyun.com/zh/account/ali-cloud-account-registration-process)。

- 

开通按量付费ECS资源时，您的阿里云账户余额（即现金余额）和代金券的总值不得小于100.00元人民币。具体充值操作，请参见[在线充值](https://help.aliyun.com/zh/user-center/use-alipay-online-banking-to-recharge-online)。

## 默认配置

快速购买ECS实例时，为了减少配置参数时间，部分参数由系统自动分配。默认分配的参数如下表所示。

| 参数 | 默认配置 |
| --- | --- |
| 可用区 | 系统随机分配，不能修改。 |
| 网络类型 | 默认专有网络，不能修改。更多信息，请参见 [默认专有网络和交换机](products/vpc/documents/user-guide/default-vpcs-and-default-vswitches.md) 。 |
| 安全组 | 默认安全组，实例创建后可修改，具体操作，请参见 [为实例（主网卡）关联安全组](products/ecs/documents/user-guide/manage-ecs-instances-in-security-groups.md) 。 |
| 专有网络 | 默认专有网络交换机，更多信息，请参见 [默认专有网络和交换机](products/vpc/documents/user-guide/default-vpcs-and-default-vswitches.md) 。 |
| 密码 | 无密码，您需要在实例创建成功后重置密码，具体操作，请参见 [重置实例登录密码](products/ecs/documents/user-guide/reset-the-logon-password-of-an-instance.md) 。 |
| 实例名称 | 系统命名，实例创建后可修改。 |


## 操作步骤

- 

前往[实例购买页](https://ecs-buy.aliyun.com/wizard/#/)。

- 

在实例创建页，单击左上角的快速购买页签。

- 

根据界面提示，配置ECS实例参数。

- 

- 

- 

- 

- 

- 

- 

| 参数 | 说明 | 示例 |
| --- | --- | --- |
| 实例规格 | 实例规格包括 CPU 型号、核数和内存大小，以套餐的形式提供，包含基础配置、标准配置、专业配置和增强配置四个套餐。 | 基础配置（2vCPU 2GiB） |
| 镜像 | 纯净的操作系统镜像，提供了运行实例所需的信息，快速购买支持 Alibaba Cloud Linux、CentOS、Windows Server、Ubuntu 四种操作系统。快速购买不支持选择自定义镜像或云市场镜像，如需更多镜像，可前往 [自定义购买](https://ecs-buy.aliyun.com/ecs#/custom/prepay/) 。 已购买的实例可以通过 [更换操作系统（更换系统盘）](products/ecs/documents/user-guide/replace-the-operating-system-of-an-instance.md) 的方式更换为目标镜像。 | Alibaba Cloud Linux 3.2104 LTS 64 位 |
| 预装应用 | 支持基于不同的操作系统，安装预装应用。实例启动后，安装预装应用需耗时 3-5 分钟。 | 按需选择 |
| 付费类型 | 包年包月 ：先付费再使用，适用于长期稳定的业务，例如 Web 服务。 按量付费 ：先使用再付费，适用于有大幅波动的场景，例如临时扩展、临时测试、科学计算。 重要 当您不再使用按量付费实例时，请尽快释放实例，否则 ECS 资源会持续扣费。 | 包年包月 |
| 地域 | 选择距离近的地域可以降低网络时延，实例创建完成后不支持更改地域和可用区。更多信息，请参见 [地域和可用区](https://help.aliyun.com/zh/document_detail/40654.html) 。 | 华东 1（杭州） |
| 公网 IP | 如果实例需要进行公网通信，必须分配公网 IP。 | 选中分配公网 IPv4 地址 |
| 带宽计费模式 | 按固定带宽 ：按您选择的带宽值计费，实际的出网带宽不会高于指定的带宽值，适用于对网络带宽有稳定要求的场景。 按使用流量 ：按实际使用的流量计费，适用于对网络带宽要求变化大的场景。为避免产生高额的带宽流量费，可先设置出网带宽峰值。 （可选）： 选中 升级至 CDT 计费 。CDT 以灵活计费、提供免费流量、阶梯价格优惠及多产品统一计费等优势，为公网带宽费用管理提供高效经济的解决方案。相对于按量付费，有一定的折扣优惠。更多信息，请参见 [什么是云数据传输](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt) [CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt) 。 重要 自 2024 年 12 月 12 日 0 时起，您无需额外操作即可直接使用云数据传输（CDT），享受高效服务。 升级为 CDT 计费后，所有存量和新增的按流量计费实例将通过 CDT 统一计费和出账，按带宽计费的实例继续在原来的云产品上统计费用和出账。您可以前往费用与成本，在账单详情页面查看 CDT 的账单情况。 开通 CDT 即可获得 220 GB/月公网流量免费额度， 其中 20 GB/月可用于 中国内地地域 ，200 GB/月可用于 非中国内地地域 。 | 按固定带宽 |
| 带宽值/带宽峰值 | 选择 按固定带宽 的 带宽值 或 按使用流量 的 带宽峰值 ，实际的出网带宽不会高于指定的 带宽值/带宽峰值 。 | 1 Mbps |
| 购买实例数量 | 购买实例的数量。 | 1 |
| 购买时长 | 购买实例的使用时长。 付费类型 为 包年包月 时，需配置此参数。 | 1 个月 |
| 自动续费 | 自动续费可以减少手动续费的管理成本，避免因忘记手动续费而导致 ECS 实例服务中断。 付费类型 为 包年包月 时，才能选择此参数。 | 选中启用自动续费 |


- 

在页面右侧的配置概要面板，确认选择的实例配置，并阅读页面底部的《产品服务协议》和《服务等级协议》，如无疑问，单击确认下单。

## 后续步骤

快速购买不支持设置实例登录凭证，创建实例成功后，您可以在ECS管理控制台重置密码。具体操作，请参见[重置实例登录密码](products/ecs/documents/user-guide/reset-the-logon-password-of-an-instance.md)。

[上一篇：一图教您如何购买云服务器ECS](products/ecs/documents/user-guide/a-picture-is-to-teach-you-how-to-buy-cloud-server-ecs.md)[下一篇：自定义购买实例](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)

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
