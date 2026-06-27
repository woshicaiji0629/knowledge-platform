# 开启专有网络免密访问-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/enable-password-free-access

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

# 开启专有网络免密访问

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）实例支持在专有网络环境下开启免密访问，在保障安全性的前提下，实现更便捷的数据库连接。设置免密访问后，同一专有网络内的客户端无需使用密码即可连接实例，同时也继续兼容通过用户名和密码的方式连接实例。

## 前提条件

实例的网络类型为专有网络。

## 注意事项

- 

开启专有网络免密访问后，连接实例使用的是默认账号（即与实例ID同名的账号，例如r-bp1zxszhcgatnx****），该账号拥有读写权限。

- 

跨专有网络之间如果通过[云企业网](products/cen/documents/product-overview/what-is-cen.md)[CEN](products/cen/documents/product-overview/what-is-cen.md)实现互通，则被视为同一专有网络。

- 

为保障安全性，开启专有网络免密访问后，通过公网地址连接实例仍需密码验证。

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在连接信息的右侧，单击设置免密访问。

- 

在右侧弹出的面板中，阅读相关提示并单击确定。

请刷新页面，当设置免密访问按钮转变为关闭免密访问时，表示已开启该功能。

- 

若实例为云原生版，您必须将同一专有网络客户端的IP地址添加到实例的白名单中，才能使用VPC免密连接。

若实例为经典版，则无需添加白名单即可连接。经典版实例可以通过#no_loose_check-whitelist-always参数进行控制：

- 

默认情况下，#no_loose_check-whitelist-always参数被设置为no，即开启免密访问后，同一专有网络的客户端连接可直接访问Tair实例时，无需将其IP地址添加至实例的白名单中，更多信息请参见[Redis](products/redis/documents/user-guide/supported-parameters.md)[开源版配置参数列表](products/redis/documents/user-guide/supported-parameters.md)。

- 

在对已启用VPC免密访问的实例进行部分配置变更的场景下，需要预先完成两项前置操作以确保服务的连续性。将实例所属的专有网络IP地址段加入访问白名单 ，并设置no_loose_check-whitelist-always参数的值为yes。若未执行这些步骤，实例在配置变更后将有访问失败的风险。

说明

云原生版不支持设置#no_loose_check-whitelist-always参数。

## 连接示例

开启专有网络免密后的连接示例如下。

说明

关于如何获取实例的连接地址和密码，请参见[查看连接地址](products/redis/documents/user-guide/view-endpoints.md)。

## redis-cli免密登录

redis-cli -h host -p port // 例如：redis -h r-bp10noxlhcoim2****.redis.rds.aliyuncs.com -p 6379

## Jedis免密登录

JedisPoolConfig config = new JedisPoolConfig(); // 最大空闲连接数，需自行评估，不超过实例的最大连接数。 config.setMaxIdle(100); // 最大连接数，需自行评估，不超过实例的最大连接数。 config.setMaxTotal(200); config.setTestOnBorrow(false); config.setTestOnReturn(false); // host和port的值替换为实例的连接地址、端口，不需要密码参数。 String host = "r-bp10noxlhcoim2****.redis.rds.aliyuncs.com"; int port = 6379; JedisPool pool = new JedisPool(config, host, port); Jedis jedis = null; try { jedis = pool.getResource(); /// ... do stuff here ... for example jedis.set("foo", "bar"); System.out.println(jedis.get("foo")); jedis.zadd("sose", 0, "car"); jedis.zadd("sose", 0, "bike"); System.out.println(jedis.zrange("sose", 0, -1)); } finally { if(jedis != null) { // 需要在每一次API调用结束之后close，close是将连接还回连接池，不是销毁。 jedis.close(); } } // 只在最终程序退出时候调用一次。 pool.destroy();

## 相关操作

单击关闭免密访问按钮即可关闭免密功能。

重要

关闭该功能会导致使用免密访问功能的客户端无法连接到实例。

若您需要关闭该功能，为保障不影响客户端连接，请提前将客户端的验证方式修改为账号和密码的方式。

## 相关API

| API 接口 | 说明 |
| --- | --- |
| [ModifyInstanceVpcAuthMode](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-modifyinstancevpcauthmode-redis.md) | 开启或关闭专有网络免密访问。 |


## 常见问题

- 

Q：开启免密访问后，为什么仍会返回WRONGPASS invalid username-password pair报错？

A：Redis开源版6.0实例开启免密访问后，若输入错误的账号密码，系统会返回以上报错。请输入正确的账号密码或不输入账号密码。

说明

密码格式：

- 

默认账号（即以实例ID命名的账号）：直接填写密码。

- 

新创建的账号：密码格式为<user>:<password>，例如testaccount:Rp829dlwa。

- 

Q：开启免密访问后，为什么使用同一专有网络的客户端连接Tair实例，仍报错(error) ERR illegal address？

A：该客户端的IP地址未添加至实例的白名单。您可以将客户端的IP地址添加至实例的白名单中后重试。

[上一篇：开启透明数据加密TDE](products/redis/documents/user-guide/enable-tde.md)[下一篇：开启实例释放保护](products/redis/documents/user-guide/enable-the-release-protection-feature.md)

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
