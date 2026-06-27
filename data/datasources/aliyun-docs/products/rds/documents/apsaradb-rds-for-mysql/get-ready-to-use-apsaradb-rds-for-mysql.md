# 准备使用RDS-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/get-ready-to-use-apsaradb-rds-for-mysql

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mysql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

- [AI能力中心](products/rds/documents/apsaradb-rds-for-mysql/ai-capability-center.md)

- [自研内核AliSQL](products/rds/documents/apsaradb-rds-for-mysql/proprietary-alisql.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mysql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mysql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mysql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mysql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mysql/support.md)

[首页](https://help.aliyun.com/zh)

# 准备工作

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

一个RDS实例是一台数据库服务器，应用服务器可以连接到RDS实例，使数据存放在RDS实例。请先获取应用服务器的信息，然后再创建或连接RDS实例。

## 操作步骤

- 

确认您的应用是否已部署或将要部署在[阿里云](products/ecs/documents/user-guide/what-is-ecs.md)[ECS](products/ecs/documents/user-guide/what-is-ecs.md)或其它阿里云产品（本文以ECS为例）。

- 

如果是，进入步骤2。

- 

如果不是，且不迁移上云，本文操作结束。请前往创建RDS实例，后续通过外网连接RDS实例。

说明

外网访问的安全性、性能、稳定性都弱于内网访问。

- 

确认具体的ECS实例。

- 

打开[ECS](https://ecs.console.aliyun.com/server/region#/server/region/cn-hangzhou)[实例列表](https://ecs.console.aliyun.com/server/region#/server/region/cn-hangzhou)，在顶部选择地域。数字代表该地域有多少个ECS实例。

说明

如果未创建任何ECS实例，请参见[创建](products/ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)[ECS](products/ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)[实例](products/ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)。

- 

找到已部署或将要部署应用的ECS实例，即要连接RDS的ECS实例，例如ECS实例A。

- 

查看ECS实例的地域和网络类型。

在ECS实例列表中，地域显示在页面顶部的地域切换区域，网络类型显示在实例列表的网络类型列中。

说明

如果网络类型是经典网络，建议迁移至专有网络。具体操作参见[ECS](products/ecs/documents/user-guide/migrate-ecs-instances-from-the-classic-network-to-a-vpc.md)[实例从经典网络迁移到专有网络](products/ecs/documents/user-guide/migrate-ecs-instances-from-the-classic-network-to-a-vpc.md)。

- 

查看VPC。

如果网络类型是专有网络，您还需要单击实例ID，在实例详情页的配置信息区域查看专有网络ID和名称（VPC ID和名称）。

## 下一步

[快速创建](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[实例](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)

[上一篇：快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)[下一篇：第一步：创建RDS MySQL实例与配置数据库](products/rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)

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
