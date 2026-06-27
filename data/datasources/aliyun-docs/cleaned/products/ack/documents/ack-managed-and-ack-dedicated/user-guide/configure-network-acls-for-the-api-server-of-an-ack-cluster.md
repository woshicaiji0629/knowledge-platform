# 配置API Server的访问控制策略-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/configure-network-acls-for-the-api-server-of-an-ack-cluster

# 配置API Server的访问控制策略
ACK集群创建时会为API Server自动创建一个私网CLB实例，作为集群API Server的内网连接端点，通过为该私网CLB实例绑定EIP，即可创建公网端点，实现对API Server的公网访问。为避免API Server受到非法访问，您可以对该私网CLB实例的6443端口监听（Listener）配置访问控制规则，即设置访问白名单或者黑名单。
重要
由于公网端点和内网端点共享同一个私网CLB实例，因此对该CLB实例配置的访问控制规则将同时应用于公网端点和内网端点。
负载均衡提供监听级别的访问控制。您可以在创建监听时配置访问控制，也可以在监听创建后修改或重新配置访问控制。更多信息，请参见[访问控制](../../../../slb/documents/classic-load-balancer/user-guide/access-control.md)。
## 操作步骤
您可以针对不同的监听设置访问白名单或黑名单，只允许特定IP访问或限制某些特定IP访问。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。
在集群信息页面，单击基本信息页签，然后在网络区域，找到并单击内网端点右侧的设置访问控制。仔细阅读访问控制策略的放行提示后，单击确定。
在负载均衡控制台跳转的面板中，打开启用访问控制开关，选择访问控制方式和访问控制策略组之后，单击确定。
在此开启访问控制之前，您需要首先[访问控制](../../../../slb/documents/classic-load-balancer/user-guide/access-control.md)，并[访问控制](../../../../slb/documents/classic-load-balancer/user-guide/access-control.md)。更多CLB访问控制信息，请参见[访问控制](../../../../slb/documents/classic-load-balancer/user-guide/access-control.md)。
重要
配置访问控制策略时，除了确保用户侧指定的IP地址能够正常访问API Server外，集群控制面组件和控制台相关的IP地址段也要能够正常访问API Server。因此，请务必在访问控制策略的白名单中添加放行以下网段，切勿将其加入黑名单，以免影响集群功能和管理操作的正常运行。
容器服务 Kubernetes 版管控的网段100.104.0.0/16。
集群专有网络VPC的主网段及附加网段（如有），或集群节点所在的交换机vSwitch网段。
用户侧需访问API Server连接端点的客户端出口网段。
除放行以上网段之外，ACK Edge集群还需要放行边缘节点出口网段。
除放行以上网段之外，ACK灵骏集群还需要放行灵骏VPD网段。
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
