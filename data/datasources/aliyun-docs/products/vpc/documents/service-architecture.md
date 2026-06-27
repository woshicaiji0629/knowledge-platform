# 产品技术架构与核心功能组件-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/service-architecture

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

# VPC技术原理

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

专有网络 VPC 是云上构建的逻辑隔离的私有网络环境。基于软件定义网络（SDN）和 VXLAN 隧道技术，分离数据平面与控制平面，并为每个 VPC 分配唯一的 VXLAN 网络标识符（VNI），实现虚拟网络间的隔离。

## 产品架构

数据平面：数据包的转发路径

数据平面负责处理和转发网络流量，主要由分布式的虚拟交换机和网关集群组成。

- 

网络隔离：VPC 利用 VXLAN (Virtual eXtensible LAN) 隧道技术实现网络隔离。传统 VLAN 技术最多支持 4096 个虚拟网络，无法满足大规模云计算数据中心的需求。VXLAN 通过将二层以太网报文封装在三层 UDP 包中传输，突破了物理网络限制，可支持上百万个虚拟网络。

- 

通信流程：

- 

VPC 内通信：同一 VPC 内的云服务器实例间通信时，其发出的数据包会被封装，并标记上该 VPC 独有的 VNI。数据包在物理网络中传输，但只有同一 VPC 内的实例才能解析和接收。

- 

VPC 间隔离：不同 VPC 的实例因其 VNI 不同，分属于不同的逻辑路由平面，数据包无法互通，实现了网络隔离。

控制平面：网络的集中管理

控制平面是 VPC 的管理核心，由 SDN 控制器集群构成，负责网络的集中管理和策略下发。

- 

功能分离：SDN 技术将控制平面与数据平面解耦。通过控制台或 API 进行的网络配置（如定义路由、设置安全规则），由 SDN 控制器处理。管理员无需关心底层硬件细节，即可通过控制器动态调整网络行为。

- 

配置下发：控制器计算出转发表等配置信息，并通过自研协议下发至数据平面的交换机和网关，以指导流量转发。该分离架构使网络配置的变更无需操作底层物理硬件，提升了网络的灵活性和自动化水平。

高可用设计

VPC 架构设计中融入高可用与冗余机制，保障服务稳定性。

- 

分布式节点：使用分布式虚拟交换机，避免单点故障。

- 

集群化部署：网关和控制器均采用集群部署，并实现多机房（可用区）互备。

- 

链路冗余：所有物理链路均具备冗余容灾能力。

## 功能架构

VPC 提供丰富功能，支持构建满足特定业务需求的网络架构，同时具备精细化访问控制与监控运维能力。

- 

[交换机](products/vpc/documents/vpc-and-vswitch.md)：在 VPC 内划分地址空间以部署云资源。交换机是可用区级别的资源。

- 

[路由表](products/vpc/documents/vpc-route-table.md)：控制 VPC 内的流量走向。交换机与路由表绑定，由路由条目决定流经该交换机的数据包的下一跳。

- 

[IP](products/vpc/documents/ip-address-management-ipam.md)[地址管理（IPAM）](products/vpc/documents/ip-address-management-ipam.md)：作为 IP 地址管理工具，自动化分配与管理 IP 地址，简化网络管理流程并避免地址冲突。

- 

[IPv4](products/vpc/documents/ipv4-gateway-overview.md)[网关](products/vpc/documents/ipv4-gateway-overview.md)/[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)：结合路由表集中控制公网访问流量，降低分散接入带来的安全风险。

- 

[VPC](products/vpc/documents/vpc-peer-to-peer-connection.md)[对等连接](products/vpc/documents/vpc-peer-to-peer-connection.md)：支持同账号/跨账号、同地域/跨地域 VPC 互连。

- 

[网络](products/vpc/documents/network-acl-overview.md)[ACL](products/vpc/documents/network-acl-overview.md)：与交换机绑定，通过配置网络ACL规则，控制出入交换机的流量。

- 

[流日志](products/vpc/documents/vpc-flow-logs.md)：采集并记录弹性网卡的进出流量信息，可以监控网络性能、排查网络故障或优化流量成本。

- 

[流量镜像](products/vpc/documents/traffic-mirroring-overview.md)：作为旁路监控方案，在不影响业务流量的前提下，将符合筛选条件的流量复制并转发到安全分析设备，实现实时检测。

[上一篇：图说专有网络VPC](products/vpc/documents/figure-vpc.md)[下一篇：网络规划](products/vpc/documents/vpc-network-planning.md)

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
