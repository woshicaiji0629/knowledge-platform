# 云上云下节点资源管理运维-ACK Edge-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/node-management-overview

# ACK Edge节点管理概述
ACK Edge集群支持管理云上云下丰富的节点资源类型，针对边缘节点复杂的网络环境，ACK Edge提供了强大的边缘自治和离线运维的能力保障业务的持续稳定运行。本文介绍如何使用ACK Edge节点管理的相关能力。
## 支持管理的节点类型
### 云端节点类型
当业务需要混合云形态部署时，您可以通过ACK Edge集群的云端节点池管理云上的ECS节点，充分利用云上弹性、存储、网络的能力。ACK Edge集群云端节点提供了与ACK托管集群Pro版一致的节点管理能力。更多信息，请参见[节点管理](https://help.aliyun.com/zh/document_detail/476587.html)。
### 边缘节点类型
ENS实例：ACK Edge集群支持通过边缘节点池管理阿里云ENS实例，实现地理上的就近接入。更多信息，请参见[ENS](ens-management-overview.md)[管理](ens-management-overview.md)。
跨地域ECS节点：ACK Edge集群的云端节点池与ACK托管集群Pro版一样只能管理同VPC下的ECS节点，除此之外，ACK Edge集群还支持通过边缘节点池管理分散在不同地域的ECS节点。
其他边缘节点：ACK Edge集群支持通过边缘节点池管理非阿里云的IaaS资源（如IDC节点、其他厂商云节点、楼宇、场馆、工厂、门店、车、船等）。
## 支持的节点管理操作
### 云端节点管理操作
对于云上节点，ACK Edge集群支持的节点管理操作与ACK托管集群Pro版一致。详细信息，请参见[节点管理](../../node-18.md)。
### 边缘节点的管理操作
您可以对边缘节点执行一些基础的管理操作。
将边缘节点添加到ACK Edge集群的指定节点池中。具体操作，请参见[添加边缘节点](add-an-edge-node.md)。
升级边缘节点对应的集群版本。具体操作，请参见[升级边缘节点](upgrade-edge-node.md)。
将节点移除ACK Edge集群。具体操作，请参见[移除边缘节点](remove-edge-nodes.md)。
ACK Edge集群为边缘节点提供了两种网络接入类型，公网型和专线型。与VPC内的网络相比，边缘节点面临不稳定的网络环境带来的挑战。针对边缘节点复杂的网络环境，ACK Edge提供了强大的边缘自治和离线运维的能力保障业务的持续稳定运行。
ACK Edge集群支持开启边缘节点自治。当边缘与云端网络断连时，边缘节点上的业务应用能够持续稳定地运行，无需担心被驱逐或迁移至其他边缘节点。详细信息，请参见[设置边缘节点自治](configure-node-autonomy.md)。
在断网状态下，ACK Edge集群支持边缘节点离线运维，在不依赖云端控制面的情况下完成集群变更。详细信息，请参见[边缘节点离线运维](edge-node-offline-operation-and-maintenance-tool.md)。
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
