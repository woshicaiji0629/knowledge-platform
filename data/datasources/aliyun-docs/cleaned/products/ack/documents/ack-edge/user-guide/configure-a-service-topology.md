# 如何配置Service流量拓扑-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/configure-a-service-topology

# 节点池服务拓扑管理
原生Kubernetes Service的后端端点扁平分布在集群中任意节点。因此，跨越不同分组节点的Service流量，会大概率出现访问不可达、或者访问效率低下的问题。Service流量拓扑支持边缘节点应用只能由相同节点池的节点访问，或者只能由本节点访问。本文介绍Service流量拓扑管理功能以及如何配置Service流量拓扑。
## 背景信息
在边缘计算场景下，边缘节点通常具备很强的区域性、地域性或者其他逻辑上的分组特性（比如具有相同的CPU架构、运营商或云提供商），不同分组的节点间往往存在网络不互通、资源不共享、资源异构、应用独立等明显的隔离属性。
## Service流量拓扑管理实现原理
为了解决上述问题，容器服务 Edge 版基于原生的Service，增加了Endpoint的拓扑管理功能，即通过简单配置来限制Service后端Endpoint的访问范围。例如，边缘节点应用只能由相同节点池的节点访问，或者只能由本节点访问。具体实现原理如下图所示。
Service1关联后端Pod2和Pod3两个实例，且Service1通过annotation："openyurt.io/topologyKeys: kubernetes.io/zone"配置了其拓扑节点池范围。
Pod2所在的节点2和Pod3所在的节点4分别属于两个不同的节点池A和节点池B。
因为Pod3和Pod1不在一个节点池，当Pod1访问Service1时，流量只会转发到Pod2上，访问Pod3的流量被限制。
## 注意事项
v1.26.3-aliyun.1以下版本：创建Service时，需要同步配置Service的流量拓扑注解，流量拓扑功能才能生效。如果Service创建完成后，再增加注解配置，流量拓扑功能无法生效，此时需要删除该Service，重新创建。
v1.26.3-aliyun.1及以上版本：Service拓扑注解支持创建后修改，修改后Service拓扑功能会立即生效。
### 注解说明
通过在原生的Service上添加Annotation实现流量的拓扑配置，相关参数如下所示。
| annotation Key | annotation Value | 说明 |
| --- | --- | --- |
| openyurt.io/topologyKeys | kubernetes.io/hostname | 限制 Service 只能被本节点访问。 |
| openyurt.io/topologyKeys | kubernetes.io/zone 或 openyurt.io/nodepool | 限制 Service 只能被本节点池的节点访问。 ACK Edge 集群 版本如果大于等于 1.18，推荐您使用 openyurt.io/nodepool。 |
| - | - | Service 不做任何拓扑限制。 |
## 配置Service流量拓扑
您可以通过控制台或命令行两种方式进行Service流量拓扑配置。
## 方式一：通过控制台配置Service流量拓扑
若您需要创建一个限制在本节点池内被访问的Service，只需要给Service添加注解即可。例如将名称配置为openyurt.io/topologyKeys，值配置为kubernetes.io/zone。关于创建服务的更多信息，请参见[Service](../../ack-managed-and-ack-dedicated/user-guide/service-management.md)[管理](../../ack-managed-and-ack-dedicated/user-guide/service-management.md)。
## 方式二：通过命令行配置Service流量拓扑
新建一个使用节点池拓扑域的Service，YAML样例如下。
apiVersion: v1 kind: Service metadata: annotations: openyurt.io/topologyKeys: kubernetes.io/zone name: my-service-nodepool namespace: default spec: ports: - port: 80 protocol: TCP targetPort: 8080 selector: app: nginx sessionAffinity: None type: ClusterIP
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
