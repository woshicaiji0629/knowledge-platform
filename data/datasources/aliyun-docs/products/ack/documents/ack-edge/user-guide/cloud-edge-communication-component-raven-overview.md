# 云边跨网络域运维通信-跨域运维通信组件Raven-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/cloud-edge-communication-component-raven-overview

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

# 跨域运维通信组件Raven概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在ACK Edge集群中，跨域运维通信组件Raven提供了强大的跨网络域通信功能，支持多地域高效云边运维，本文介绍Raven组件的概念、工作原理以及功能说明。

## 背景信息

ACK Edge集群采用了中心云管理边缘IDC以及边缘设备的云边协同架构。在云上搭建Kubernetes控制面，可以使分散在边缘侧的IDC，以及边缘基础设施通过多种网络形态与云上控制面进行交互，从而以云原生的方式实现对大规模边缘设备的高效管理。

在边缘云场景中，计算设备通常分散在多个地域并处于不同的网络域，这也是边缘云场景的典型特征。因此，边缘设备在集群中通常按照分组进行管理，不同分组的节点之间没有网络连接，应用之间相对独立。如图所示，本地的数据中心或边缘设备通常通过公用网络与阿里云的控制面公网端点建立连接，数据中心、边缘设备之间以及云上的VPC都处于不同的网络平面。

## 组件介绍

ACK Edge支持节点池级别的多地域分布管理，不同节点池中的节点位于不同的网络域，无法直接通信，并且可能存在节点IP冲突的问题。为了在这种场景下实现中心化监控运维，在ACK Edge集群1.26.3及以上版本中提供了Raven Agent组件支持主机、容器级别的监控运维。

### 工作原理

- 

在每个网络域中选择一个集群内节点作为网关节点；独立的边缘设备本身就是自己的网关。

- 

Raven Agent组件将以DaemonSet的形式部署在集群内的所有节点上，并且采用主机网络模式，在网关节点之间构建加密隧道。

- 

云上组件例如APIServer、MetricsServer、Prometheus等会通过网关节点与其他网络域主机、容器、服务进行通信。

### 功能说明

- 

创建ACK Edge集群时，您需要选择并且购买至少1台云上ECS节点，将该节点作为云上网关节点。

- 

如果边缘侧主机采用公网方式与云上ACK Edge控制面进行交互，则需要购买一个传统型负载均衡（CLB）实例、访问控制列表（ACL）实例和弹性公网IP（EIP）实例，用于不同节点池的网关节点之间构建加密的网络隧道。

- 

Raven组件提供两种模式跨域通信，代理模式和隧道模式。

- 

代理模式主要支持APIServer、MetricsServer 和 Prometheus等服务的跨域主机网络通信，例如kubectl logs/exec/attach/top等原生命令。

- 

隧道模式仅支持节点间网络互通的节点池，主要提供云边容器网络通信，例如Prometheus的容器Metrics数据监控。

- 

Raven组件支持多地域（多网络域）设备主机IP冲突场景下的网络通信。

## 组件架构

Raven组件包含控制面组件ack-edge-yurt-manager和数据面组件raven-agent-ds。Raven组件需要一个自定义集群资源Gateway来记录节点信息和配置信息，详情请参见[使用跨域运维通信组件](products/ack/documents/ack-edge/user-guide/using-the-cloud-side-communication-raven-component.md)[Raven](products/ack/documents/ack-edge/user-guide/using-the-cloud-side-communication-raven-component.md)。

- 

ack-edge-yurt-manager组件会在节点池维度划分网络域并且创建Gateway资源。

- 

raven-agent-ds组件会以DaemonSet的方式部署在集群的每一个节点上，它负责代理构建网关节点间的隧道以及路由配置等。

Raven组件支持两种云边通信模式。

- 

代理模式：构建反向代理通道，实现跨域主机网络通信，网关节点代理跨域的NodeName+Port的七层网络请求。

- 

隧道模式：构建VPN隧道，实现跨域容器网络通信，网关节点转发跨网络域的容器网络链路。

### 代理模式

- 

被选举的边缘网关节点会主动与云上网关节点建立加密的反向通道。

- 

对于单独的节点（Solo Node），其本身就为网关节点，与云上网关节点构建通道。

- 

云上的跨域请求会通过云上网关节点转发到边缘侧网关节点，由该节点代理访问本网络域内的目标服务。

### 隧道模式

- 

仅支持节点间网络互通的节点池。

- 

边缘侧被选举的网关节点会主动与云上网关节点构建IPSec加密的VPN隧道。

- 

Raven Agent在本网络域内构建 VXLAN网络，将跨域容器网络请求转发到网关节点。

- 

本网络域内的容器间通信通过Flannel VXLAN进行通信。

- 

跨网络域的请求将被拦截，并通过Raven VXLAN传送到网关节点，通过VPN隧道实现通信。

重要

由于跨域通信通过公网传输，可能存在数据丢失风险，请勿传输重要业务数据。如在使用过程中遇到问题或有相关产品建议，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)联系容器服务团队。

## 相关文档

- 

如您需要更改通信模式、配置访问控制白名单或使用自定义资源Gateway进行特殊配置，请参见[使用跨域运维通信组件](products/ack/documents/ack-edge/user-guide/using-the-cloud-side-communication-raven-component.md)[Raven](products/ack/documents/ack-edge/user-guide/using-the-cloud-side-communication-raven-component.md)。

- 

raven-agent-ds组件会不断迭代，详细的变更记录，请参见[raven-agent-ds](products/ack/documents/product-overview/raven-agent-ds.md)。

[上一篇：云边通信组件](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-components.md)[下一篇：使用跨域运维通信组件Raven](products/ack/documents/ack-edge/user-guide/using-the-cloud-side-communication-raven-component.md)

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
