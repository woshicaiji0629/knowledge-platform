# 创建和管理边缘节点池-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/edge-node-pool-management

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

# 创建和管理边缘节点池

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ACK支持通过控制台对边缘节点池进行统一管理操作，包括创建、编辑、删除等。

## 操作入口

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏单击集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。

## 创建边缘节点池

- 

在节点池页面，单击创建边缘节点池。

- 

在创建边缘节点池页面，根据[边缘节点池属性](products/ack/documents/ack-edge/user-guide/edge-node-pool-management.md)完成配置，然后单击提交。

## 查看边缘节点池

在节点池页面，单击对应节点池名称，可查看以下信息。

- 

单击基本信息页签，查看节点池ID、容器运行时、云边网络连接、节点间网络互通、Pod网络模式、节点标签、污点信息。

- 

单击监控页签，查看节点监控信息。

## 编辑边缘节点池

- 

在节点池页面，找到对应节点池，单击右侧编辑，打开节点池编辑页面。

- 

在边缘节点池编辑页面，修改可编辑的属性，修改完成后，单击提交。

说明

目前仅支持编辑节点池名称，节点标签和污点。相关信息，请参见[边缘节点池属性](products/ack/documents/ack-edge/user-guide/edge-node-pool-management.md)。

## 删除边缘节点池

- 

在节点池页面，找到对应节点池，单击右侧的>删除，打开节点池删除页面。

- 

在节点池删除页面，仔细阅读删除节点池的注意事项，确认无误后单击确定。

说明

如果边缘节点池内仍存在边缘节点，请先[移除边缘节点](products/ack/documents/ack-edge/user-guide/remove-edge-nodes.md)，然后再删除该节点池，否则将无法删除边缘节点池。

## 边缘节点池属性

| 属性 | 创建后能否修改 | 描述 |
| --- | --- | --- |
| 节点池名称 |  | 长度为 1~63 个字符，可包含数字、下划线（_）或中划线（-），需以英文大小写字母、中文或数字开头。 |
| 容器运行时 |  | ACK Edge 集群 1.24 及更高版本仅支持 containerd 运行时。 |
| 云边网络连接 |  | 公网 ：节点池内的节点通过公网与云端节点进行交互，节点池内应用不能直接访问云端 VPC 内网。当边缘业务对云端的依赖性不强，且对云边通信以及安全性保障无要求，可选择该类型。 专用网络 ：节点池内的节点通过专线、VPN 或 CEN 等方式实现云上与云下网络打通，拥有更高的云边通信质量，提供更有效的安全保障。当业务对云边交互有强需求，且对云边网络的质量以及安全性有较强的要求，建议选择该类型。同时需要提前自行架设好节点与云端的专线基础设施。 |
| 节点间网络互通 |  | 互通 ：该节点池内的所有节点之间三层网络互通。 说明 适用场景：一个标准 IDC 或 VPC 为一个节点池，该节点池内主机之间内网互通。 不互通 ：该节点池内的所有主机之间三层网络不互通。 说明 适用场景：分散的一批边缘设备位于同一节点池，主机之间无网络通信需求。 |
| Pod 网络模式 |  | 容器网络 ：Pod 拥有独立的网络栈，不占用主机网络端口。需要安装 Flannel、kube-proxy、CoreDNS 等组件。 适合精细化容器网络控制场景。 主机网络 ：Pod 直接使用主机的网络栈，与主机共享 IP 地址和端口。主机网络模式的节点池内的节点默认不安装 Flannel、kube-proxy、CoreDNS 等组件，支持更大的集群规模。适合轻量化业务，以及业务间无需通信等场景。 |
| 节点标签（Labels） |  | 给节点池内所有节点添加标签。 |
| 污点 |  | 给节点池内所有节点添加污点。 |


[上一篇：管理节点池OS参数](products/ack/documents/ack-edge/user-guide/custom-node-pool-os-parameters.md)[下一篇：节点管理](products/ack/documents/ack-edge/user-guide/node-management-overview.md)

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
