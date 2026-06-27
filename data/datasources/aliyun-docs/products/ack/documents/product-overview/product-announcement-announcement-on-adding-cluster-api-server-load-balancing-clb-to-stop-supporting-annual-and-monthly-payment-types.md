# 【产品公告】关于取消新建集群API Server负载均衡CLB包年包月付费的公告-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/product-overview/product-announcement-announcement-on-adding-cluster-api-server-load-balancing-clb-to-stop-supporting-annual-and-monthly-payment-types

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/product-overview.md)

- [操作指南](products/ack/documents/ack-user-guide.md)

- [服务支持](products/ack/documents/support.md)

[首页](https://help.aliyun.com/zh)

# 【产品公告】关于取消新建集群API Server负载均衡CLB包年包月付费的公告

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

自2024年11月25日起，容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）将逐步取消API Server所使用的负载均衡CLB实例包年包月付费选项。2024年12月1日起，将彻底取消该选项。

## 影响范围

本次变更涉及ACK托管集群、ACK专有集群、ACK Edge集群及ACK灵骏集群。

## 变更内容

在2024年12月1日完全停止支持后，在容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）中新建集群时，API Server负载均衡CLB的付费类型不再支持选择包年包月。

重要

存量包年包月类型负载均衡CLB不受影响，但建议您及时转换为按量付费类型。更多信息请参见[传统型负载均衡](products/slb/documents/product-overview/announcement-of-suspension-of-traditional-load-balancing-clb-package-year-and-month.md)[CLB](products/slb/documents/product-overview/announcement-of-suspension-of-traditional-load-balancing-clb-package-year-and-month.md)[包年包月停售公告](products/slb/documents/product-overview/announcement-of-suspension-of-traditional-load-balancing-clb-package-year-and-month.md)。

集群创建接口[CreateCluster - 创建集群](products/ack/documents/serverless-kubernetes/developer-reference/api-cs-2015-12-15-createcluster-serverless.md)中描述API Server负载均衡CLB的付费类型字段将会同步下线，将会下线的参数如下：

| 字段名称 | 说明 |
| --- | --- |
| charge_type | 付费类型 |
| period | 购买时长 |
| period_unit | 付费周期 |
| auto_renew | 是否自动续费 |
| auto_renew_period | 自动付费周期 |


[上一篇：【产品变更】关于ACK OpenAPI服务升级的公告](products/ack/documents/product-overview/announcement-on-ack-openapi-underlying-architecture-upgrade.md)[下一篇：【产品公告】关于集群创建接口CreateCluster参数行为变更的公告](products/ack/documents/product-overview/product-announcement-announcement-on-change-of-createcluster-parameter-behavior-of-cluster-creation-interface.md)

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
