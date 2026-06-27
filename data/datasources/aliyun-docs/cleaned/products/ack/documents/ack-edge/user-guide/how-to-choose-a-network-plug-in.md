# 容器网络插件功能与场景对比-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/how-to-choose-a-network-plug-in

# 如何选择网络插件Terway Edge与Flannel
容器服务 Edge 版支持两种容器网络插件，需要您在创建集群之前完成容器网络插件的选型，集群创建完成后不可以更改。本文介绍两种网络插件信息对比。
## 插件功能对比
ACK Edge集群支持以下两种容器网络插件：
Flannel：采用了VXLAN模式，是一种Overlay的容器网络插件。详细信息，请参见[Flannel](flannel-network-plugin.md)[网络插件](flannel-network-plugin.md)。
Terway Edge：是一种Underlay的网络插件。详细信息，请参见[Terway Edge](terway-edge-network-plug-in-introduction.md)[网络插件](terway-edge-network-plug-in-introduction.md)。
| 对比项 | Terway Edge 版 | Flannel VXLAN |
| --- | --- | --- |
| 插件来源 | 阿里云自研的网络插件。 | Flannel 社区提供的网络插件。 |
| 适用场景 | 管理自建 IDC、ENS 实例等。 适用于规模较大、网络效率要求高等场景。 | 管理边缘设备，其他云厂商计算实例。 适用于规模小，设备分散等场景。 |
| Pod 网段 | 云端支持 Pod 网段扩容，Pod 网段可以直接使用 VPC 网段。 边缘不支持 Pod 网段扩容，需在创建集群时指定 Pod 网段。 | 不支持 Pod 网段扩容，需在创建集群时指定 Pod 网段。 |
| 网络性能 | 网络性能高，相比于 VXLAN 封包性能提升约 20%。 | 网络性能适中，有 VXLAN 封包。 |
| 云产品对接 | 无缝对接云产品，例如 CLB、ALB、NLB、ECI 等。 | 有限对接云产品，部分能力不可用。 |
| 容器互访 | 支持集群外客户端直接访问容器 IP。 | 不支持集群外客户端直接访问容器 IP。 |
| 网络插件模式 | Underlay 模式，容器与计算资源在同一个网络平面。 | Overlay 模式，容器和计算资源不在同一个网络平面。 |
| 跨网络域容器通信条件 | 若您需要实现容器间跨局域网通信（例如云边容器通信、多个局域网之间容器通信），则需要满足如下条件：（1）节点与云端 VPC 有专线打通；（2）节点交换机需要支持 BGP 协议以接受路由发布。 | 若您需要实现容器间跨局域网通信，则需要节点间三层网络互通。 |
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
