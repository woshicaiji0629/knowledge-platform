# 如何实现边缘节点自治-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/configure-node-autonomy

# 设置边缘节点自治
ACK Edge集群支持边缘节点自治，在边缘和云端网络断连状态下，保证边缘节点上的业务应用仍然可以持续稳定地运行，而不会被驱逐或者迁移到其他边缘节点。如果您将边缘节点设置为非自治，云边断连时节点上的应用在到达容忍时间之后将会被驱逐。本文介绍如何为边缘节点设置节点的自治属性。
## 前提条件
[已创建](create-an-ack-edge-cluster-1.md)[ACK Edge](create-an-ack-edge-cluster-1.md)[集群](create-an-ack-edge-cluster-1.md)
[已添加边缘节点](add-an-edge-node.md)
## 背景信息
设置边缘节点自治包括设置节点自治和节点非自治两种配置，边缘节点接入集群后默认为非自治状态。
当边缘节点被设置为自治状态时，如果边缘节点和云端管控断连，此时不仅系统能够保证节点上的应用不会被驱逐，而且节点上的应用也会自动恢复。设置节点自治适用于边缘计算的弱网络连接场景。
当边缘节点被设置为非自治状态时，如果边缘节点和云端管控断连，节点因不能正常地将心跳上报至管控端，而会被设置为不可用（not ready）状态，且节点上的应用在到达容忍时间之后将会被驱逐。
## 开启节点自治
## 通过控制台开启
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点。
在节点页面，选择目标节点操作列的更多>节点自治设置。
说明
仅当前节点是边缘节点时，才会显示节点自治设置按钮。
在弹出的节点自治设置对话框中，单击确定。
### 通过kubectl开启
给边缘节点添加如下注解，开启节点自治，该操作仅对边缘节点生效。
kubectl annotate node xxx node.beta.openyurt.io/autonomy=true --overwrite
此外，您还可以通过如下方式为边缘节点配置自治时间。
说明
仅支持1.28及以上的ACK Edge集群配置边缘节点自治时间，配置后，如果边缘节点与云端管控之间持续断网时间在自治时间内，则节点上的Pod持续运行，业务不受影响，不会触发驱逐行为，如果超过了配置的自治时间，则会驱逐边缘节点上的Pod。
kubectl annotate node xxx node.alibabacloud.com/autonomy-duration=500s --overwrite
## 查看节点自治状态
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点。
在节点页面，选择目标节点操作列的更多>详情。
在基本信息页面下方找到状态页签，查看类型为Autonomy对应状态是True表示自治开启成功。
## 配置缓存组件
当前EdgeHub会将节点上的组件所需要的相关数据进行缓存，在云边断网时确保这些组件可以正常运行，磁盘缓存目录为/etc/kubernetes/cache。
说明
缓存的数据指的是与API Server进行交互的数据，比如Pod、ConfigMap等资源信息，不包含业务数据。
如果您有组件需要在边缘节点断网的情况下依赖API Server的数据信息来正常运行，可以按照如下步骤进行配置。
获取您的开发人员提供的User-Agent，如果是社区组件，可以在社区内进行查询。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择配置管理>配置项。
切换命名空间为kube-system，找到名称为edge-hub-cfg的ConfigMap，在右侧单击YAML 编辑。
将您的User-Agent添加到cache_agents配置项中，然后单击确定。
您可以登录节点，进入/etc/kubernetes/cache目录，查看是否有名为您的User-Agent的目录。
配置完成后，对应的组件和API Server之间交互的数据都会保存到节点的磁盘里。如果您开启了节点自治，组件将会从本地磁盘获取数据，从而确保正常运行。
## 相关文档
如果您需要移除不使用的边缘节点，请参见[移除边缘节点](remove-edge-nodes.md)。
更多边缘节点问题，请参见[边缘节点](edge-node-faq.md)[FAQ](edge-node-faq.md)。
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
