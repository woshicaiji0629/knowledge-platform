# Redis String的CAS与CAD增强命令-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/cas-cad-command

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

# Redis String命令增强

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍Tair实例新增的String增强类命令，包括CAS和CAD。

## 前提条件

实例为Tair[内存型](products/redis/documents/product-overview/dram-based-instances.md)或[持久内存型](products/redis/documents/product-overview/persistent-memory-optimized-instances-1.md)（小版本为1.2.3及以上）。

说明

最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](products/redis/documents/user-guide/update-the-minor-version.md)。如果您的实例为集群实例或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。

## 注意事项

本文的操作对象为Redis String（即Redis原生String）。

说明

Tair实例中可同时设置Redis String和TairString，本文的命令无法对TairString使用。

## 命令列表

表 1.String增强命令

| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [CAS](products/redis/documents/developer-reference/cas-cad-command.md) | CAS key oldvalue newvalue [EX|PX|EXAT|PXAT time] | CAS（Compare And Set），查看指定的 oldvalue 是否与目标 Key 的 Value 相等，若相等则将 Value 修改成新的值（ newvalue ），不相等则不修改。 说明 该命令仅适用于操作 Redis String 类型的数据，如需对 TairString 做相同的操作，请使用 EXCAS。 |
| [CAD](products/redis/documents/developer-reference/cas-cad-command.md) | CAD key value | CAD（Compare And Delete），查看指定 Value 值是否与目标 Key 的 Value 相等，若相等则删除该 Key，不相等则不删除。 说明 该命令仅适用于操作 Redis String 类型的数据，如需对 TairString 做相同的操作，请使用 EXCAD。 |


说明

本文的命令语法定义如下：

- 

大写关键字：命令关键字。

- 

斜体：变量。

- 

[options]：可选参数，不在括号中的参数为必选。

- 

A|B：该组参数互斥，请进行二选一或多选一。

- 

...：前面的内容可重复。

## CAS

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | CAS key oldvalue newvalue [EX|PX|EXAT|PXAT time] |
| 时间复杂度 | O(1) |
| 命令描述 | CAS（Compare And Set），查看指定的 oldvalue 是否与目标 Key 的 Value 相等，若相等则将 Value 修改成新的值（ newvalue ），不相等则不修改。 说明 该命令仅适用于操作 Redis String 类型的数据，如需对 TairString 做相同的操作，请使用 EXCAS。 |
| 选项 | Key ：目标 Key，String 类型。 oldvalue ：原 Value 值，用于跟现有 Key 的 Value 进行比较。 newvalue ：当 oldvalue 与 Key 现有 Value 相等时，将 Value 修改为 newvalue。 EX ：指定 Key 的相对过期时间，单位为秒，为 0 表示马上过期，不传此参数表示不过期。 EXAT ：指定 Key 的绝对过期时间，单位为秒，为 0 表示马上过期，不传此参数表示不过期。 PX ：指定 Key 的相对过期时间，单位为毫秒，为 0 表示马上过期，不传此参数表示不过期。 PXAT ：指定 Key 的绝对过期时间，单位为毫秒 ，为 0 表示马上过期，不传此参数表示不过期。 说明 若原 String 已设置 TTL，在执行 CAS 命令时不加上 TTL，该 Key 将不过期。 |
| 返回值 | 执行成功：1 执行失败：0 若 Key 不存在：-1 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 SET foo bar 命令。 命令示例： CAS foo bar bzz EX 10 返回示例： (integer) 1 若此时执行 GET foo ，将返回 “bzz” 。 |


## CAD

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | CAD key value |
| 时间复杂度 | O(1) |
| 命令描述 | CAD（Compare And Delete），查看指定 Value 值是否与目标 Key 的 Value 相等，若相等则删除该 Key，不相等则不删除。 说明 该命令仅适用于操作 Redis String 类型的数据，如需对 TairString 做相同的操作，请使用 EXCAD。 |
| 选项 | Key ：目标 Key，String 类型。 value ：指定 Value，用于跟现有 Key 的 Value 进行比较。 |
| 返回值 | 执行成功：1 执行失败：0 若 Key 不存在：-1 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 SET foo bar 命令。 命令示例： CAD foo bar 返回示例： (integer) 1 执行成功，则 foo Key 被删除，若此时执行 GET foo ，将返回 (nil) 。 |


[上一篇：Tair扩展数据结构概览](products/redis/documents/developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md)[下一篇：exString](products/redis/documents/developer-reference/tairsting-command.md)

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
