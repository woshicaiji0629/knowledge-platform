# 通过CRD管理采集配置的两种方式AliyunPipelineConfig与AliyunLogConfig-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/use-crd-to-manage-collection-configurations

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 使用CR实例管理采集配置

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

CRD（[CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)）允许用户定义自定义资源类型，日志服务利用CRD定义了自己的资源类型，您可以通过创建CR（CustomResource）实例来管理采集配置。本文主要介绍日志服务的两类CRD（AliyunPipelineConfig和AliyunLogConfig）的区别和优势。

## 背景信息

CRD全称为“[CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)”，是Kubernetes（k8s）的一种API对象，允许用户定义自定义资源类型。通过CRD，用户可以扩展Kubernetes原生的API，以满足特定的应用场景需求。CR即“CustomResource”，是基于CRD定义的资源类型创建的具体的实例。

日志服务定义了自己的CRD，并支持通过CR来管理Logtail采集配置。您需要连接Kubernetes集群，并额外使用Kubernetes鉴权。然后向kube-apiserver提交YAML配置文件来创建资源，从而创建相应的Logtail采集配置。

警告

通过CR创建的配置，在控制台上对其修改不会同步到CR中。因此，如需修改由CR创建的配置内容，只能修改CR实例，禁止直接在控制台操作，避免配置不一致。

通过CR管理Logtail采集配置的工作原理

- 

日志服务通过Deployment部署了一个控制器alibaba-log-controller，该控制器负责监听AliyunLogConfig资源的变化。

- 

当用户通过kubectl或其他Kubernetes管理工具创建、更新或删除AliyunLogConfig资源时，alibaba-log-controller会监测到这些变化，然后根据资源配置文件中的内容和服务端Logtail采集配置的状态，自动向日志服务提交各种请求，如采集配置变更等。

## CRD类型

警告

使用AliyunPipelineConfig，需要日志组件版本最低为0.5.1。

为了便于通过云原生方式管理Logtail采集配置，日志服务定义了两类CRD，它们的能力与区别见下表：

| 类型 | AliyunPipelineConfig（推荐使用） | AliyunLogConfig |
| --- | --- | --- |
| ApiGroup | telemetry.alibabacloud.com/v1alpha1 | log.alibabacloud.com/v1alpha1 |
| CRD 资源名 | ClusterAliyunPipelineConfig | AliyunLogConfig |
| 作用域 | 集群 | 命名空间 |
| 采集配置格式 | 基本等价于日志服务 API 中的 [LogtailPipelineConfig](products/sls/documents/developer-reference/api-sls-2020-12-30-struct-logtailpipelineconfig.md) | 基本等价于日志服务 API 中的 [LogtailConfig](products/sls/documents/developer-reference/api-sls-2020-12-30-struct-logtailconfig.md) |
| 跨地域能力 | 支持 | 支持 |
| 跨账号能力 | 支持 | 支持 |
| Webhook 校验参数 | 支持 | 不支持 |
| 配置冲突检测 | 支持 | 日志组件 0.5 以上版本支持 |
| 配置难度 | 较低 | 较高 |
| 配置可观测性 | Status 包含错误详情、更新时间、上次应用成功配置、上次应用成功时间等信息 | Status 包含错误码与错误信息 |


[上一篇：采集配置生成器](products/sls/documents/collection-configuration-generator.md)[下一篇：【推荐】使用AliyunPipelineConfig管理采集配置](products/sls/documents/recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md)

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
