# VPC互连-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/cross-vpc-interconnection-overview

# VPC互连
VPC之间网络默认隔离，但您可以使用[VPC](vpc-peer-to-peer-connection.md)[对等连接](vpc-peer-to-peer-connection.md)或[云企业网](../../cen/documents/getting-started/overview.md)，将VPC之间的网络进行私网打通，从而实现VPC中的实例互通。
## 选型
如何选择：
根据规模：若需互连2-3个VPC，推荐使用VPC对等连接；若需互连超过3个VPC，推荐使用云企业网。
根据功能：若需要[云上组播](../../cen/documents/user-guide/multicast-overview.md)、[服务链（Service Chaining）](../../cen/documents/use-cases/use-an-enterprise-edition-transit-router-to-enable-and-secure-network-communication.md)、[跨地域](../../cen/documents/user-guide/use-traffic-scheduling-to-limit-bandwidth-for-inter-region-connections.md)[Qos](../../cen/documents/user-guide/use-traffic-scheduling-to-limit-bandwidth-for-inter-region-connections.md)功能，或不希望手动配置路由，请使用云企业网。
根据成本：若互连的VPC属于相同地域，推荐您使用对等连接，同地域不计费。
根据带宽：若同地域VPC互连需要大带宽，推荐您使用对等连接，同地域不限制带宽。
两者差异：
| 对比项 | VPC 对等连接 | 云企业网 |
| --- | --- | --- |
| 组网连接方式 | Full Mesh 全连接方式，VPC 两两之间建立对等连接。 | Hub-Spoke 连接方式，VPC 以网络连接方式加入转发路由器。 |
| 互连 VPC 数量 | 一个 VPC 默认支持连接 10 个同地域 VPC，20 个跨地域 VPC。 | 一个 TR（转发路由器）默认可连接 1000 个 VPC。 |
| 路由配置 | 必须手动为每个 VPC 配置路由。 | 支持通过 [路由学习](../../cen/documents/user-guide/route-learning.md) 和 [路由同步](../../cen/documents/user-guide/route-synchronization.md) 功能自动配置路由。 |
| 网络扩展性 | 弱 单个 VPC 支持的对等连接数较少，且每次新增 VPC 时都需要两两建立连接并手动配置路由。 | 强 单个 TR 支持连接大量 VPC，且新增 VPC 时直接连接到 TR 即可，不必手动配置路由。 |
| 带宽限制 | 同地域：不限制。 跨地域：默认限制 1024 Mbps。 | 同地域：请查看 [网络实例连接支持的最大带宽](../../cen/documents/product-overview/limits.md) 。 跨地域：带宽分配方式若选择按流量付费，则按 [配额](../../cen/documents/user-guide/cen-quotas.md) 约束；若选择从带宽包分配，则最大带宽为 [带宽包](https://common-buy.aliyun.com/?spm=5176.10692594.0.0.64874ffcQgbWpq&commodityCode=cbn_bwp_pre&request=%7B%22cbn_id%22%3A%22%22%7D) 的带宽值。 |
| 计费 | 同地域不收费，跨地域统一由云数据传输 CDT（Cloud DataTransfer）收取 [出方向流量传输费](https://help.aliyun.com/zh/cdt/inter-region-data-transfers) 。 | 同地域收取连接费、流量处理费；跨地域收取连接费、流量处理费和跨地域带宽费。详情： [云企业网计费说明](../../cen/documents/product-overview/billing-rules.md) 。 |
## 示例
### 连通2个VPC内的ECS
如需连通2个位于不同VPC的ECS，建议[使用](vpc-peer-to-peer-connection.md)[VPC](vpc-peer-to-peer-connection.md)[对等连接](vpc-peer-to-peer-connection.md)。
相比于云企业网，同地域VPC互通免费。
### 连通多个VPC
使用对等连接连通3个以上的VPC时，因为需要在每个VPC之间两两建立连接并手动配置路由，操作较为繁琐。
此时推荐使用[云企业网](../../cen/documents/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts.md)，只需将每个VPC连接到地域内的TR，即可实现网络互通。
### 复杂组网降低成本
在复杂的网络架构中，单一的网络连接方案往往难以同时满足组网复杂性、高带宽需求以及成本控制的要求。因此，建议采用VPC对等连接与云企业网相结合的方式来解决这类复杂需求。
以下图为例，某公司在多个地域部署了多个VPC，这些VPC之间不仅需要实现互连互通，还要求具备路由策略控制能力并降低成本。
同地域VPC互连，可通过VPC对等连接相互打通，无任何费用。
跨地域VPC互连，可将VPC加入至云企业网，实现该地域VPC与其他地域VPC互连互通以及精细化的路由策略控制。
部分VPC之间需要跨域互联但需要独占带宽的场景，可通过跨地域VPC对等连接实现互通，例如 VPC A和 VPC F。
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
