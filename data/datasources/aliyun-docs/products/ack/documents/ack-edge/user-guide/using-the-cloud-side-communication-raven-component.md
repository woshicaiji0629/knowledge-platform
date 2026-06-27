# 使用跨域运维通信组件Raven-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/using-the-cloud-side-communication-raven-component

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

# 使用跨域运维通信组件Raven

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在ACK Edge集群中，跨网络域通信组件Raven提供了基础的多地域网络通信能力，以实现云边运维能力。您可以配置Raven组件，选择云边通信模式（代理模式、隧道模式），也可以增删访问控制白名单条目，放行边缘网关节点以使其与云上构建隧道。

说明

如果您的集群采用专线打通云边网络通信，您可以卸载Raven组件。

## 前提条件

- 

已创建ACK Edge集群，且集群版本为v1.26.3及以上。具体操作，请参见[创建集群](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)。

- 

如开启代理模式，边缘侧安全策略请勿阻挡TCP[10280,10285)区间的端口。

- 

如开启隧道模式，边缘侧安全策略请勿阻挡UDP 4500，云端安全组放开UDP 8472端口。

- 

由于边缘侧需要与云上构建反向通道，因此边缘侧安全策略请勿阻挡Raven组件挂载的EIP地址。

如何查看Raven挂载的EIP地址，请参见[云资源信息](products/ack/documents/ack-edge/user-guide/using-the-cloud-side-communication-raven-component.md)。

## 注意事项

- 

Raven组件的跨域通信能力依赖弹性公网IP、传统型负载均衡CLB、访问控制ACL等云资源。

- 

托管组件Edge-Controller-Manager（ECM）会根据您是否开启Raven的跨域通信能力来购买CLB、EIP、ACL等云产品资源；关闭或卸载Raven跨域能力则会释放相关云产品资源。您可以根据实际需求变配云产品的资源规格。

以上云资源的命名方式为k8s/raven-agent-ds/kube-system/{CLUSTER_ID}，请勿修改资源名称，否则可能导致ECM组件无法识别该资源，进而导致资源泄露问题。

请勿擅自删除以上资源导致Raven能力不可用。

- 

云资源信息记录在集群资源configmap kube-system/raven-cfg中，请勿手动删除。

展开查看raven-cfg的示例代码

apiVersion: v1 kind: ConfigMap metadata: name: raven-cfg namespace: kube-system data: acl-id: acl-xxx acl-entry: "" eip-id: eip-xxx eip-ip: 47.XX.XX.47 enable-l3-tunnel: "false" enable-l7-proxy: "true" loadbalancer-id: lb-xxx loadbalancer-ip: 192.XX.XX.1

## 基于raven-agent-ds配置通信模式和访问控制白名单

ACK Edge集群安装时，会自动安装raven-agent-ds组件，并默认启动代理模式。您可以自行同步配置通信模式（代理模式、隧道模式）并设置边缘网关节点的访问控制白名单。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。

- 

搜索并定位raven-agent-ds，在目标卡片区域，单击配置，然后完成相关参数配置。

- 

- 

| 配置项 | 说明 |
| --- | --- |
| controller | Raven 组件是否开启代理模式 （推荐配置）：代理模式，构建反向代理通道，实现跨域主机网络通信。 Raven 组件是否开启隧道模式 ：隧道模式仅支持节点间网络互通的节点池。通过构建 VPN 隧道，实现跨域容器网络通信，主要支持云边容器 Metrics 监控。 重要 由于跨域通信通过公网传输，可能存在数据丢失风险，请勿传输重要业务数据。如在使用过程中遇到问题或有相关产品建议，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 联系容器服务团队。 关于两种通信模式的更多信息，请参见 [跨域运维通信组件](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md) [Raven](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md) 。 |
| accessControlListEntry | 访问控制白名单条目。放行的边缘网关节点可以与云上构建隧道，增强网络安全性。 采用 CIDR 标准格式，固定 IP 地址以“ /32 ”为掩码，多个地址之间使用英文半角逗号（,）分隔。不填写时，表示所有源地址均可被负载均衡放行访问云上服务。 如果您添加 ACL 条目，请放行 CLB 健康检查 IP 地址段 100.64.0.0/10 。 |


## 通过Label自定义网关节点

Raven组件会通过在网关节点之间构建通道实现跨域通信的目的，默认会在节点池中随机选择一些网关节点，建议您指定一些固定的节点作为网关节点用于构建稳定运维通道，您可以使用以下命令选择：

kubectl label node node-xxx raven.openyurt.io/gateway-node=true

## 相关文档

- 

如需了解Raven组件的更多信息，例如组件构成、支持的通信模式等，请参见[跨域运维通信组件](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md)[Raven](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md)[概述](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md)。

- 

ACK Edge集群会不断迭代raven-agent-ds组件，详细的变更记录请参见[raven-agent-ds](products/ack/documents/product-overview/raven-agent-ds.md)。

[上一篇：跨域运维通信组件Raven](products/ack/documents/ack-edge/user-guide/cloud-edge-communication-component-raven-overview.md)[下一篇：云边运维通信组件Tunnel](products/ack/documents/ack-edge/user-guide/cloud-edge-tunneling.md)

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
