# 使用 PrivateLink 私网访问 VPC OpenAPI-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/use-privatelink-to-access-vpc-openapi-over-private-network

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

# 使用 PrivateLink 私网访问 VPC OpenAPI

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以通过[PrivateLink](https://help.aliyun.com/zh/privatelink/what-is-a-private-network-connection)提供的接口终端节点在您的 VPC 和阿里云 VPC OpenAPI 和 VPC对等连接 OpenAPI 之间建立私网连接。PrivateLink 支持通过阿里云内网安全、稳定地访问 VPC OpenAPI 和 VPC对等连接 OpenAPI，就像访问您 VPC 内的其他资源一样，无需经过公网，简化网络架构，有效规避安全风险。VPC 中的实例无需公网 IP 地址即可调用 API。

有关更多信息，请参阅[通过 PrivateLink 访问阿里云服务](https://help.aliyun.com/zh/privatelink/create-and-manage-endpoints/)。

## 创建接口终端节点

- 

VPC OpenAPI 的终端节点服务名称格式为com.aliyuncs.privatelink.{RegionId}.vpc，需申请服务白名单授权。

北京地域无需申请。

- 

VPC对等连接 OpenAPI 的终端节点服务名称格式为com.aliyuncs.privatelink.{RegionId}.vpcpeer。

- 

确保[已开通私网连接服务](https://common-buy.aliyun.com/?spm=5176.11182174.content.4.6df84882i4nDoy&commodityCode=privatelink_postpay_public_cn)，且已在目标地域创建[VPC、交换机](products/vpc/documents/vpc-and-vswitch.md)和[安全组](products/ecs/documents/user-guide/manage-security-groups.md)。

### 控制台

- 

前往[终端节点 - 创建终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/endpoints/new)页面。

- 

配置接口终端节点：

- 

基础配置：

- 

所属地域：选择访问阿里云服务入口所在地域。

- 

名称与描述：统一标识云资源。

- 

类型：选择阿里云服务。

- 

可用的服务：依据终端节点服务名称选择访问的阿里云服务。

可用：阿里云服务已在所属地域部署，且服务使用方具备连接到对应阿里云服务的权限。

- 

VPC OpenAPI：com.aliyuncs.privatelink.{RegionId}.vpc

- 

VPC对等连接 OpenAPI：com.aliyuncs.privatelink.{RegionId}.vpcpeer

- 

网络配置：

- 

为确保服务高可用，建议至少选择2个可用区下的交换机。可以为终端节点可用区的弹性网卡指定交换机内的 IP 地址，如不指定，将由系统默认分配。

不允许为弹性网卡指定交换机的[系统保留地址](products/vpc/documents/vpc-and-vswitch.md)。

- 

IP版本：VPC OpenAPI 和 VPC对等连接 OpenAPI 的终端节点服务暂不支持双栈，客户端仅可以使用IPv4地址访问服务。

- 

安全组：与接口终端节点关联，管控全部终端节点可用区的弹性网卡的入方向流量。

- 

高级配置：

- 

是否开启自定义服务域名：服务使用方开启后，可使用自定义域名访问阿里云服务。

- 

VPC OpenAPI：vpc-vpc.cn-beijing.aliyuncs.com（以北京地域为例）

- 

VPC对等连接 OpenAPI：vpcpeer.vpc-proxy.aliyuncs.com

- 

终端节点策略：保持默认终端节点策略，即允许完全访问。

- 

创建完成后，可使用同 VPC 的 ECS 执行以下命令测试是否连通。

ping <终端节点可用区的弹性网卡的IP> # 可在实例详情页的可用区与网卡页签下，查看弹性网卡的 IP 地址 # 如为 HTTP/HTTPS 服务，建议直接访问服务端口 curl -sI http://<终端节点域名> # 可在实例列表页查看终端节点域名 # 安全组入方向需开放HTTP（80）和HTTPS（443）端口，用于终端节点所在的VPC通过HTTP协议或者HTTPS协议访问服务。 # 是否可使用HTTPS协议访问，由对应的服务决定。

### API

调用[CreateVpcEndpoint](https://help.aliyun.com/zh/privatelink/developer-reference/api-privatelink-2020-04-15-createvpcendpoint)创建接口终端节点。

[上一篇：监控与日志](products/vpc/documents/monitoring-and-logging.md)[下一篇：服务支持](products/vpc/documents/support.md)

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
