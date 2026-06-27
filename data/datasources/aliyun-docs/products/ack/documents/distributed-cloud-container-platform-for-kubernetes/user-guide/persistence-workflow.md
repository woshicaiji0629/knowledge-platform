# 配置工作流以持久化存储到RDS MySQL数据库-容器服务Kubernetes版ACK-阿里云

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/persistence-workflow

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/product-overview.md)

- [快速入门](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/getting-started.md)

- [操作指南](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide.md)

- [实践教程](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/use-cases.md)

- [开发参考](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/developer-reference.md)

- [服务支持](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/support.md)

[首页](https://help.aliyun.com/zh)

# 持久化工作流

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

工作流的相关资源在工作流集群中会被定期清理，如果您想对工作流的运行过程进行分析和回溯，可以通过配置持久化策略将工作流持久化存储到数据库中。这样即使工作流被删除或者工作流运行的Pod被删除，您也可以查看到工作流的日志。本文以阿里云RDS MySQL数据库为例，为您介绍如何配置工作流持久化到数据库的策略。

## 配置使用RDS

- 

创建阿里云RDS MySQL实例。具体操作，请参见[快速创建](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[实例](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)。

重要

设置网络时，选择的VPC和工作流集群所使用的VPC要保持一致，设置白名单时需放开该VPC网段。

- 

创建数据库和账号。具体操作，请参见[创建数据库和账号](products/rds/documents/create-databases-and-accounts-for-an-apsaradb-rds-for-mysql-instance.md)。

- 

将下方YAML模板保存到argo-mysql-config.yaml，然后执行kubectl create -f argo-mysql-config.yaml，在工作流集群中创建一个名为argo-mysql-config的Secret，用于保存数据库的账号和密码。

username和password需要分别替换为您上一步骤实际创建的数据库账号和密码。apiVersion: v1 stringData: username: database-username password: database-password kind: Secret metadata: name: argo-mysql-config namespace: default type: Opaque

- 

编辑workflow-controller-configmap，增加持久化配置。

说明

- 

workflow-controller-configmap文件位于以集群ID命名的命名空间中。

- 

host为RDS实例地址RDS MySQL实例的地址。

- 

database为数据库的名称。

- 

archive需要设置为true。

- 

archiveTTL为持久化的保存时间，本示例设置为30d，表示工作流持久化到数据库中可以保存30天。该参数取值大小无限制。

persistence: | connectionPool: maxIdleConns: 100 maxOpenConns: 0 connMaxLifetime: 0s # 0 means connections don't have a max lifetime. archiveTTL: 30d archive: true mysql: host: rm-xxx.mysql.cn-beijing.rds.aliyuncs.com port: 3306 database: argo-workflow tableName: argo_workflows userNameSecret: name: argo-mysql-config key: username passwordSecret: name: argo-mysql-config key: password

## 相关文档

如果工作流已持久化到数据库中，即使工作流被删除，您也可以通过Argo CLI查看工作流的日志。具体信息，请参见[使用日志服务](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/configure-log-service.md)。

[上一篇：使用存储卷](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-volumes.md)[下一篇：配置Artifacts](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/configure-artifacts.md)

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
