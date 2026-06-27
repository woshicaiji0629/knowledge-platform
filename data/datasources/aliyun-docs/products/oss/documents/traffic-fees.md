# 流量费用-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/traffic-fees

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/oss/documents/user-guide.md)

- [开发参考](products/oss/documents/developer-reference.md)

- [产品计费](products/oss/documents/billing.md)

- [常见问题](products/oss/documents/oss-faq.md)

- [动态与公告](products/oss/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 流量费用

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

使用OSS传输数据过程中会产生流量，OSS将根据数据传输实际产生的流量计算流量费用。流量主要包括流入流量、流出流量、回源流量和跨区域复制流量。

## 计费单价

本文仅说明相关计费项及付费方式。有关计费项的定价详情，请参见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)。

## 计费项

以下计费项中，返回码为4xx、5xx的请求不产生流量费用。

### 流入流量

| 计费项 | 计费项 Code | 计费规则 | 是否计费 |
| --- | --- | --- | --- |
| 外网流入流量 | 不涉及 | 通过外网 Endpoint（示例值 oss-cn-hangzhou.aliyuncs.com）或者传输加速 Endpoint（示例值 oss-accelerate.aliyuncs.com）调用 PutObject 等上传类接口上传文件产生的流量。 说明 使用传输加速 Endpoint 向 Bucket 上传数据时，还会产生 [传输加速费用](products/oss/documents/transfer-acceleration-fees.md) 。 | 否 |
| 内网流入流量 | 不涉及 | 通过内网 Endpoint（示例值 oss-cn-hangzhou-internal.aliyuncs.com）调用 PutObject 等上传类接口上传文件产生的流量。 | 否 |


### 流出流量

| 计费项 | 计费项 Code | 计费规则 | 是否计费 |
| --- | --- | --- | --- |
| 外网流出流量 | NetworkOut | 通过外网 Endpoint（示例值 oss-cn-hangzhou.aliyuncs.com）或者传输加速 Endpoint（示例值 oss-accelerate.aliyuncs.com）调用 GetObject 接口访问、下载、预览文件或者进行图片处理操作产生的流量。 说明 使用传输加速 Endpoint 请求 OSS 资源时，还会产生 [传输加速费用](products/oss/documents/transfer-acceleration-fees.md) 。 外网流出流量费用=外网流出流量（GB）×每 GB 单价 | 是 |
| 内网流出流量 | 不涉及 | 通过内网 Endpoint（示例值 oss-cn-hangzhou-internal.aliyuncs.com）调用 GetObject 接口访问、下载、预览文件或者进行图片处理操作产生的流量。 | 否 |


### CDN回源流出流量

| 计费项 | 计费项 Code | 计费规则 | 是否计费 |
| --- | --- | --- | --- |
| CDN 回源流出流量 | CdnOut | OSS 将用户请求的资源传输到 CDN 缓存节点产生的回源流出流量。 CDN 回源流出流量费用=CDN 回源流出流量（GB）×每 GB 单价 | 是 |


### 跨区域复制流量

| 计费项 | 计费项 Code | 计费规则 | 是否计费 |
| --- | --- | --- | --- |
| 跨区域复制流量 | ReplicationDatasize | 使用 [跨区域复制](products/oss/documents/user-guide/cross-region-replication-overview.md) 功能将源 Bucket 的数据同步复制到目标 Bucket 时产生的流出流量。 跨区域复制流量费用=跨区域复制流量（GB）×每 GB 单价 | 是 |


## 支付方式

### 选型指导

建议您参考以下多种付费方式的介绍，了解不同付费方式的特点、适用场景等信息，方便您选择适当的付费方式，以降低流量成本。

| 付费方式 | 说明 | 特点 | 适用场景 |
| --- | --- | --- | --- |
| 按量付费 | 所有计费项默认采用按量付费。按照各计费项的实际用量结算费用。先使用，后付费。 | 数据下行流量波动较大，难以预测 | 初创公司正在开发一款新的移动应用，预计用户数量和流量会在推广期间大幅增长，但具体增长速度和规模难以预测 |
| 下行流量包 | 针对 外网流出流量 计费项推出的资源包。在费用结算时，优先从资源包抵扣用量。先购买，后抵扣。 | 数据下行流量相对稳定、可预测 | 一家大型电商网站每天都有稳定大量外网访问量和下载量 |
| 回源流量包 | 针对 OSS 流出到 CDN 边缘节点流量 场景推出的资源包。在费用结算时，优先从资源包抵扣用量。先购买，后抵扣。 | OSS 流出到 CDN 边缘节点流量相对稳定、可预测 | 您的业务具有稳定的 OSS 流出至 CDN 边缘节点的流量需求，即每日或每月有规律地向 CDN 缓存节点分发内容，且流量量级可预估。例如，大型网站或视频平台每日需同步大量静态资源至 CDN 以加速全球用户访问。 |


### 支持情况

以下是各计费项付费方式的支持情况：

| 计费项 | 按量付费 | 资源包 |
| --- | --- | --- |
| 外网流出流量 | √ | [下行流量包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22flowout%22,%22region%22:%22china-common%22,%22flowout_spec%22:%220.09765625%22,%22pack%22:%22FPT_ossbag_periodMonthlyAcc_NetworkOut_china_common%22,%22showtime%22:%22now%22%7D&regionId=china-common) |
| CDN 回源流出流量 | √ | [回源流量包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%226:Month%22,%22order_num%22:1,%22ossbag_type%22:%22cdn2oss_flow_out%22,%22region%22:%22china-common%22,%22cdn2oss_flowout_spec%22:%221024%22,%22pack%22:%22FPT_ossbag_deadlineAcc_CdnOut_china_common%22,%22showtime%22:%22now%22%7D&regionId=china-common) |
| 跨区域复制流量 | √ | × |


资源包不支持抵扣无地域属性的下行流量。

## 计费案例

- 

[标准存储（本地冗余）+数据访问](products/oss/documents/billing-examples.md)

- 

[标准存储（本地冗余）+跨区域复制](products/oss/documents/billing-examples.md)

- 

[OSS](products/oss/documents/billing-examples.md)[结合](products/oss/documents/billing-examples.md)[CDN](products/oss/documents/billing-examples.md)[加速服务](products/oss/documents/billing-examples.md)

## 常见问题

### 外网流出流量出现非预期增长怎么解决？

当您的Bucket出现外网流出流量异常突增的情况，您可以参考以下方法进行排查解决。

- 

确认流量异常情况。

Bucket已开启实时日志查询

- 

登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。

- 

单击Bucket 列表，然后单击目标Bucket名称。

- 

在左侧导航栏，选择日志管理>实时查询。

- 

在实时查询页签下，输入以下查询和分析语句，查询examplebucket中高频访问文件及其对应的热门访问IP，并按访问次数排序，返回前5条记录。

* and __topic__: oss_access_log and bucket: examplebucket | SELECT client_ip AS ip_address, request_uri AS file_path, COUNT(*) AS access_count, SUM(response_body_length) AS total_bytes_sent FROM log WHERE http_status = 200 GROUP BY request_uri, client_ip ORDER BY access_count DESC LIMIT 5;

查询和分析结果如下：

### Bucket未开启实时日志查询

- 

登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。

- 

单击Bucket 列表，然后单击目标Bucket名称。

- 

在左侧导航栏，选择用量查询>热点统计，然后单击热点 Referer/IP页签，查看Top 10（Referer/IP）。

- 

在左侧导航栏，选择用量查询>文件访问统计，查看高频访问文件的文件名、产生的流出流量。

- 

识别是否为异常流量。

- 

如果发现某些IP地址频繁请求特定对象，可能是恶意行为，请执行[步骤](products/oss/documents/traffic-fees.md)[3](products/oss/documents/traffic-fees.md)检查相关配置。

- 

如果发现多个IP地址访问不同对象，可能是内容被大规模分发（如社交媒体传播），请执行[步骤](products/oss/documents/traffic-fees.md)[4](products/oss/documents/traffic-fees.md)配置CDN加速访问OSS。

- 

检查相关配置。

| 配置项 | 风险说明 | 解决方法 |
| --- | --- | --- |
| Bucket ACL 设置了公共读或公共读写 | 任何人（包括匿名访问者）都可以对该 Bucket 中的文件进行读操作，从而产生大量的下行流量费用。 | 将 Bucket ACL 设置为私有。设置为私有后，所有不带签名或者没有权限的请求都会失败。 具体步骤，请参见 [Bucket ACL](products/oss/documents/user-guide/bucket-acl-2.md) 。 |
| 高频访问的文件 ACL 设置了公共读或者公共读写 | 任何人（包括匿名访问者）都可以对该文件进行读操作，从而产生大量的下行流量费用。 | 将 Object ACL 设置为私有。具体步骤，请参见 [Object ACL](products/oss/documents/user-guide/object-acl.md) 。 完成以上配置后，用户需要通过预签名 URL 在指定有效期内才能访问该文件。 |
| Bucket Policy 没有对允许访问 Bucket 的 IP 地址进行限制 | 如果某些未知来源的 IP 地址频繁请求特定对象，也会产生大量的下行流量费用。 | 通过 Bucket Policy 限制 [步骤](products/oss/documents/traffic-fees.md) [1](products/oss/documents/traffic-fees.md) 查询到的未知来源的热门访问 IP 地址访问 Bucket。 具体步骤，请参见 [通过](products/oss/documents/user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) [Bucket Policy](products/oss/documents/user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) [授权访问](products/oss/documents/user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) [OSS](products/oss/documents/user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) 。 |
| 没有配置 Referer 防盗链来阻止其他网站引用 OSS 文件 | 其他网站可以通过直接引用 OSS 文件的 URL（如图片、视频等），将流量压力转移到您的 OSS 上。这会导致您的 OSS 下行流量激增，产生高额的带宽费用。 | 通过配置防盗链黑名单 Referer 的方式限制 [步骤](products/oss/documents/traffic-fees.md) [1](products/oss/documents/traffic-fees.md) 查询到恶意 Referer 访问 OSS，同时允许对访问来源设置白名单的机制，避免 OSS 资源被其他人盗用。具体步骤，请参见 [防盗链](products/oss/documents/user-guide/hotlink-protection.md) 。 |


- 

配置CDN加速访问OSS。

如果确认是内容分发引起的下行流量突增，建议使用CDN分发OSS中的图片、视频、文档等静态资源，降低OSS下行流量费用，提升资源加载速度。具体步骤，请参见[通过](products/oss/documents/user-guide/cdn-acceleration.md)[CDN](products/oss/documents/user-guide/cdn-acceleration.md)[加速访问](products/oss/documents/user-guide/cdn-acceleration.md)[OSS](products/oss/documents/user-guide/cdn-acceleration.md)。

### 是否支持请求者支付，而不是Bucket拥有者支付外网流出流量费用、CDN回源流出流量费用？

如果您希望通过请求者支付，而不是Bucket拥有者支付外网流出流量费用、CDN回源流出流量费用时，可以开启请求者付费模式。具体操作，请参见[请求者付费](products/oss/documents/user-guide/enable-pay-by-requester-1.md)。

重要

- 

下行流量包不支持抵扣开启请求者付费模式后，请求者通过互联网从OSS传输到客户端产生的外网流出流量费用。

- 

回源流量包不支持抵扣开启请求者付费模式后，请求者从OSS传输到阿里云CDN边缘节点所产生的回源流量费用。

### 为什么产生外网流出流量费用的同时还出现了请求费用？

外网流出流量是从OSS传输到客户端产生的流量，而数据传输到客户端是通过调用OSS API接口实现的，OSS会根据调用的API次数收取请求费用。因此，产生外网流出流量的同时通常也会同步产生请求费用。

## 相关文档

- 

如果您希望查询OSS按小时计量的数据信息，请参见[查询](products/oss/documents/query-oss-billing-data-generated-on-an-hourly-basis.md)[OSS](products/oss/documents/query-oss-billing-data-generated-on-an-hourly-basis.md)[小时数据](products/oss/documents/query-oss-billing-data-generated-on-an-hourly-basis.md)。

- 

如果您希望在具体的计费案例中了解该计费项的计费详情，请参见[计费案例](products/oss/documents/billing-examples.md)。

- 

如果您希望查看该计费项的费用明细，请参见[账单查询](products/oss/documents/query-bills.md)。

[上一篇：存储费用](products/oss/documents/storage-fees.md)[下一篇：请求费用](products/oss/documents/api-operation-calling-fees.md)

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
