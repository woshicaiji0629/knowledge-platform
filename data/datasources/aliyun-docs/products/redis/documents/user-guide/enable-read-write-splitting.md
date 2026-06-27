# 开启读写分离与管理只读节点-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/enable-read-write-splitting

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 开启读写分离

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）支持开关读写分离功能及自定义只读节点数量。[读写分离功能](products/redis/documents/product-overview/read-or-write-splitting-instances-1.md)采用星型复制架构，所有只读节点均从主节点同步数据，数据同步延迟低。

## 影响

- 

秒级连接闪断：开启或关闭读写分离操作会导致实例发生秒级连接闪断。请在业务低峰期执行，并确保实例写入流量较低且应用具备重连机制。

- 

命令限制增加：由于读写分离不支持部分命令，在实例开启读写分离时，请评估命令限制对业务的影响，更多信息，请参见[读写分离的命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。

## 前提条件

实例需同时满足以下条件：

- 

部署模式为云原生。经典实例可[转为云原生](products/redis/documents/user-guide/change-to-the-cloud-native-deployment-mode.md)后，再执行本操作。

- 

实例为Redis开源版或Tair（企业版）内存型、持久内存型。

- 

实例规格为1 GB及以上。

- 

实例类型为高可用。

- 

集群架构实例必须为代理模式。标准架构无此要求。

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏，单击节点管理。

- 

打开读写分离开关。

- 

在弹出的面板中，确认实例配置信息以及订单费用。单击去支付。

说明

新创建的只读节点规格与主节点（源实例）一致。

- 

根据提示完成支付流程。

支付成功后，实例状态将变为变配中。请等待1~5分钟，实例状态改为运行中即表示变配完成，您可以在实例详情页中查看进展。

说明

若实例为双可用区，实例提供主、备可用区的连接地址（两个地址均支持读、写操作）。您需要主动区分主、备可用区连接地址，并将备可用区的请求指向备可用区连接地址，以实现就近访问和负载均衡。

- 

（可选）更多管理操作。

- 

调整只读节点数量：在节点管理页面，单击操作列下的修改。标准架构支持的只读节点范围为1~9个，集群架构为每分片1~4个。

- 

关闭读写分离功能：关闭读写分离开关。

## 常见问题

### 开启读写分离时报错The primary availability zone requires at least one read-only node？

因为当前实例为多可用区、标准架构（主可用区1个主节点、备可用区1个备节点），而读写分离的最低要求是主可用区必须具备1个主节点和1个只读节点。

请您先为主可用区增加1个备节点，确保主可用区有2个节点，再开启读写分离。

[上一篇：调整集群分片数](products/redis/documents/user-guide/adjust-the-number-of-cluster-shards.md)[下一篇：增删备节点](products/redis/documents/user-guide/node-management.md)

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
