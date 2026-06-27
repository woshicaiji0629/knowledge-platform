# 使用读写分离分担热点Key的大量读请求-云数据库Tair-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys

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

# 通过读写分离缓解热点Key问题

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

为缓解热点Key带来大量读请求的影响，您可以启用读写分离功能并增加只读节点，系统能够将读请求分散至各个节点。这将降低主节点的压力，并提升系统的整体吞吐量和稳定性。

## 功能概述

读写分离架构的所有只读节点通过异步复制主节点的数据（最终一致性），整体数据同步延迟低。这意味着在部分写入量较大的情况下，可能会发生数据同步延迟，此时应用程序能够容忍稍旧的数据。例如下述场景：

- 

缓存数据：网址首页的HTML缓存等，更新频率低。

- 

游戏排行榜：小时级别排行榜，其轻微的更新延迟对用户影响并不显著。

- 

天气预报数据：用户频繁查询天气，数据则按照预定时间进行更新。

增加只读节点的直接作用

- 

分担主节点负载：主节点仅负责100%写请求、1/N的读请求（N为总节点数，例如1个主节点、3个只读节点，即N为4）。这降低了主节点的CPU压力、网络压力，以及连接开销。

- 

提高系统吞吐量：每个只读节点可独立处理读请求，整体读性能呈线性扩展。在理想情况下，增加N个只读节点可提升N倍读性能。

- 

降低响应延迟：将读请求分散到多个节点后，可减少单个请求的排队等待时间。

不仅支持为标准（主从）架构开启读写分离，也支持为集群架构开启读写分离，可为集群的每个数据分片节点增加对应的只读节点，具体架构信息请参见[读写分离功能](products/redis/documents/product-overview/read-or-write-splitting-instances-1.md)。

## 如何开启

前提条件：

- 

部署模式为云原生。

- 

实例为Redis开源版或Tair（企业版）内存型、持久内存型。

- 

实例规格为1 GB及以上。

- 

实例类型为高可用。

开启方法：在实例详情页中，单击左侧导航栏的节点管理，并打开读写分离开关。具体操作请参见[开启读写分离](products/redis/documents/user-guide/enable-read-write-splitting.md)。

## 客户端连接

### 单可用区实例

通常情况下，读写分离架构实例仍提供一个连接地址，实例将通过[Proxy](products/redis/documents/product-overview/features-of-proxy-nodes.md)组件实现路由分发。您无需修改代码，开箱即用，更多信息请参见[客户端程序连接教程](products/redis/documents/user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)。

### 双可用区实例

在双可用区、读写分离架构实例，实例将分别提供主、备可用区连接地址。其中备可用区连接地址仅用于读请求，可实现就近访问，缩短读请求延迟。

例如实例为杭州I（主可用区）、杭州J（备可用区）。

- 

位于杭州I的客户端（ECS实例）可以连接实例的主可用区地址，并执行读写操作。代码如下：

import redis.clients.jedis.Jedis; import redis.clients.jedis.JedisPool; import redis.clients.jedis.JedisPoolConfig; public class MasterReadWrite { public static void main(String[] args) { JedisPoolConfig config = new JedisPoolConfig(); config.setMaxIdle(200); config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); // 配置主可用区连接地址、端口、账号密码信息。 String host = "r-bp1vtq8tnrquy****pd.redis.rds.aliyuncs.com"; int port = 6379; String password = "default:Passw***2"; JedisPool pool = new JedisPool(config, host, port, 3000, password); Jedis jedis = null; try { jedis = pool.getResource(); // 执行相关操作，示例如下。 jedis.set("foo", "bar"); System.out.println(jedis.get("foo")); } catch (Exception e) { // 超时或其他异常处理。 e.printStackTrace(); } finally { if (jedis != null) { jedis.close(); } } pool.destroy(); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。 } }

- 

位于杭州J的客户端（ECS实例）可以连接实例的备可用区地址，并仅执行读操作（如需执行写操作，仍需连接主可用区地址）。代码如下：

import redis.clients.jedis.Jedis; import redis.clients.jedis.JedisPool; import redis.clients.jedis.JedisPoolConfig; public class ReplicaRead { public static void main(String[] args) { JedisPoolConfig config = new JedisPoolConfig(); config.setMaxIdle(200); config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); // 配置备可用区连接地址、端口、账号密码信息。 String host = "r-bp1vtq8tnrquy****pd.redis.rds.aliyuncs.com"; int port = 6379; String password = "default:Passw***2"; JedisPool pool = new JedisPool(config, host, port, 3000, password); Jedis jedis = null; try { jedis = pool.getResource(); // 执行相关操作，示例如下。 System.out.println(jedis.get("foo")); } catch (JedisDataException e) { // 捕获写操作异常（如果误操作执行了写操作）。 e.getMessage(); } catch (Exception e) { // 超时或其他异常处理。 e.printStackTrace(); } finally { if (jedis != null) { jedis.close(); } } pool.destroy(); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。 } }

## 相关文档

- 

[读写分离功能](products/redis/documents/product-overview/read-or-write-splitting-instances-1.md)

- 

[Tair Proxy](products/redis/documents/product-overview/features-of-proxy-nodes.md)[特性说明](products/redis/documents/product-overview/features-of-proxy-nodes.md)

[上一篇：离线全量Key分析](products/redis/documents/user-guide/offline-key-analysis.md)[下一篇：常见Latency（时延）事件的处理建议](products/redis/documents/user-guide/suggestions-for-handling-common-latency-events.md)

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
