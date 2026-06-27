# 通过参数设置禁用高风险命令-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/disable-high-risk-commands

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

# 禁用高风险命令

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以在控制台上通过设置#no_loose_disabled-commands参数来禁用一些可能影响云数据库 Tair（兼容 Redis）服务性能、危害数据安全的命令。

## 背景信息

在业务场景中，无限制地允许命令使用可能带来诸多问题。一些命令会直接清空大量甚至全部数据，例如FLUSHALL、FLUSHDB等；KEYS、HGETALL等命令的不当使用可能会阻塞云数据库 Tair（兼容 Redis）服务，影响服务性能。您可以结合实际情况，禁用特定的命令。

为保障实例稳定、高效率地运行，部分命令不支持被禁用，例如CONFIG等，具体命令请参见[不支持禁用的命令](products/redis/documents/user-guide/disable-high-risk-commands.md)。

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏中，单击参数设置。

- 

在参数列表中找到#no_loose_disabled-commands参数，单击其操作列的修改。

- 

在弹出的对话框中填写需禁用的命令。

重要

- 

命令以小写字母的形式填写，通过英文逗号（,）分隔多个命令，例如keys,flushdb。

- 

禁用命令后会同时禁用下级子命令，例如禁用script命令后会同时禁用SCRIPT EXISTS、SCRIPT LOAD等命令。但不支持单独禁用子命令。

- 

单击确定。

## 执行结果

通过[redis-cli](products/redis/documents/user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)连接实例并执行被禁用的命令FLUSHALL后，Tair将返回错误提示：ERR command 'FLUSHALL' not support for normal user或者NOPERM this user has no permissions to run the 'flushall' command。

## 不支持禁用的命令

CONFIG、MIGRATE、RESTORE-ASKING、LASTSAVE、BGREWRITEAOF、REPLICAOF、BGSAVE、PFDEBUG、PFSELFTEST、SLAVEOF以及ACL系列命令、MODULE系列命令和DEBUG系列命令。

## 相关API

| API 接口 | 说明 |
| --- | --- |
| [DescribeParameters](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describeparameters-redis.md) | 查询实例的配置参数和运行参数。 |
| [ModifyInstanceConfig](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-modifyinstanceconfig-redis.md) | 修改实例的参数配置。 |


[上一篇：查询参数修改历史](products/redis/documents/user-guide/view-the-parameter-modification-history.md)[下一篇：高可用](products/redis/documents/user-guide/master-replica-switchovers.md)

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
