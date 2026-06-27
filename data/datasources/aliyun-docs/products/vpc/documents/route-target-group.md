# 路由目标组-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/route-target-group

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

# 路由目标组

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当使用可用区级别的云产品（如网关型负载均衡终端节点GWLBe）作为路由下一跳时，若某可用区发生故障，传统方式需手动切换流量到备用实例。路由目标组支持通过主备模式配置两个下一跳实例，系统将自动检测实例的健康状态，当实例异常时，自动实现可用区级别的容灾切换，缩短故障恢复时间（RTO）。

## 工作原理

- 

主备模式：创建路由目标组时，需配置位于不同可用区、类型一致的主备实例。

- 

主实例：权重为100。正常情况下承载所有流量，在健康检查正常时生效。

- 

备实例：权重为0。主实例故障后接管流量，作为容灾备份。

- 

健康检查：路由目标组通过健康检查机制持续探测主备实例的可用性，以实现精确的故障发现和流量切换。

- 

故障发现：当健康检查连续3次探测目标实例失败时，系统判定该实例为不健康状态。如果主实例不健康，将自动触发向备实例的切换。

- 

故障恢复：当一个不健康的实例恢复后，健康检查需连续探测成功3次，才会将其判定为健康状态。

- 

主备切换

- 

自动切换：当健康检查发现主实例不可用时，系统会自动将路由的下一跳流量切换至备实例。

- 

手动回切：可用于计划内运维、容灾演练或在主实例恢复后手动回切。

- 

不支持自动回切：为避免因主实例网络抖动引发频繁的自动切换（业务震荡），路由目标组在故障恢复后不会自动将流量切回主实例。主实例恢复健康后，可以在业务低峰期手动回切。

| 切换场景 | 触发方式 | 切换时间 |
| --- | --- | --- |
| 故障切换 | 自动切换（健康检查触发） | < 30 秒 |
| 故障恢复回切 | 手动回切 | < 10 秒 |


## 适用范围

- 

支持的目标实例类型：当前仅支持网关型负载均衡终端节点（GWLBe）。

- 

实例部署要求：必须配置一个主实例和一个备实例，且二者必须属于同一个VPC、部署在不同可用区，以实现跨可用区容灾。

- 

配额限制：单个 VPC 内支持创建 10 个路由目标组。

## 配置路由容灾

将路由条目下一跳配置为路由目标组，流量将根据路由目标组当前生效的实例进行转发。当实例异常时，系统自动执行可用区级别的容灾切换。

- 

仅 IPv4 路由条目支持配置下一跳为路由目标组。

- 

路由目标组作为路由下一跳时，支持的路由操作与路由目标组成员所支持的路由操作保持一致。例如，网关路由表的系统路由支持将下一跳修改为网关型负载均衡终端节点，当网关型负载均衡终端节点作为路由目标组成员时，该路由目标组也可作为网关路由表系统路由的下一跳。

### 控制台

- 

创建路由目标组：前往[专有网络 - 路由目标组页面](https://vpc.console.aliyun.com/vpc/cn-hangzhou/routeTargetGroups)，单击创建路由目标组。

- 

专有网络：选择目标实例所属的 VPC。

- 

配置模式：目前，仅支持主备模式。

- 

目标成员类型：目前，仅支持网关型负载均衡终端节点。

- 

目标成员：选择部署在不同可用区的主实例和备实例。

配置完成后，可在路由目标组详情页选择编辑目标成员修改未启用的实例，启用中的实例不允许编辑。

- 

实例名称、所属资源组和标签：可结合使用，便于分类管理实例。

- 

配置路由条目指向路由目标组。

- 

前往[专有网络 - 路由表页面](https://vpc.console.aliyun.com/vpc/cn-hangzhou/route-tables)，选择目标路由表 ID。

- 

在自定义路由条目页签选择添加路由条目：

- 

目标网段：需要通过主备实例进行流量转发的目标网段。

- 

下一跳类型：选择路由目标组。

### API

- 

调用[CreateRouteTargetGroup](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createroutetargetgroup.md)创建路由目标组。

- 

调用[CreateRouteEntry](products/vpc/documents/developer-reference/api-vpc-2016-04-28-createrouteentry.md)创建自定义路由条目，配置NextHopType为RouteTargetGroup。

## 手动执行主备切换

- 

适用场景：

- 

手动触发主备实例之间的流量切换，可用于容灾演练或计划内维护。

- 

为避免因主实例网络抖动引发频繁的自动切换（业务震荡），路由目标组在故障恢复后不会自动将流量切回主实例。主实例恢复健康后，可以在业务低峰期手动回切。

- 

功能限制：未启用实例不健康时，不允许切换。

### 控制台

- 

前往[专有网络 - 路由目标组页面](https://vpc.console.aliyun.com/vpc/cn-hangzhou/routeTargetGroups)，单击路由目标组 ID。

- 

单击页面右上方的切换目标成员。

### API

调用[SwitchActiveRouteTarget](products/vpc/documents/developer-reference/api-vpc-2016-04-28-switchactiveroutetarget.md)执行路由目标组主备切换。

## 计费说明

路由目标组功能本身免费。

目标实例（当前仅支持网关型负载均衡终端节点）及其后端服务将收取费用，具体计费规则可参考[私网连接计费说明](https://help.aliyun.com/zh/privatelink/private-link-billing-description)与[GWLB](products/slb/documents/gateway-based-load-balancing-gwlb/product-overview/billing-products-template-simple-version.md)[计费规则](products/slb/documents/gateway-based-load-balancing-gwlb/product-overview/billing-products-template-simple-version.md)。

## 应用于生产环境

- 

连接中断风险：对于有状态的应用（如长连接防火墙、NAT会话），主备切换会导致现有连接中断，业务需要重新建立连接。需考虑重连机制，充分评估切换对业务的瞬时影响。

- 

容灾演练：在引入业务流量前，建议在业务低峰期或维护窗口手动执行主备切换，进行容灾演练，验证备用链路、安全组策略和后端服务的可用性，确保故障发生时备用路径能按预期工作。

[上一篇：使用网关路由表控制进入VPC的流量](products/vpc/documents/use-the-gateway-route-table-to-control-traffic-entering-the-vpc.md)[下一篇：前缀列表](products/vpc/documents/vpc-prefix-lists.md)

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
