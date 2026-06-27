# 产品各项功能的使用限制-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/user-guide/limits

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

# OSS使用限制及性能指标

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍对象存储OSS的一些使用限制及性能指标。

## 带宽

单个阿里云账号在各地域的最大带宽限制如下：

| 地域 | 内外网总下载带宽 | 外网下载带宽 | 内外网总上传带宽 | 外网上传带宽 |
| --- | --- | --- | --- | --- |
| 华东 2（上海） | 100 Gbps | 10 Gbps | 20 Gbps | 10 Gbps |
| 华南 1（深圳） | 100 Gbps | 10 Gbps | 20 Gbps | 10 Gbps |
| 华北 2（北京） | 100 Gbps | 10 Gbps | 20 Gbps | 10 Gbps |
| 华东 1（杭州） | 100 Gbps | 20 Gbps | 20 Gbps | 20 Gbps |
| 新加坡 | 100 Gbps | 5 Gbps | 20 Gbps | 5 Gbps |
| 华北 3（张家口） | 20 Gbps | 无额外限制，受内外网总下载带宽限制 | 20 Gbps | 无额外限制，受内外网总上传带宽限制 |
| 华东 5（南京-本地地域-关停中） | 2 Gbps | 无额外限制，受内外网总下载带宽限制 | 2 Gbps | 无额外限制，受内外网总上传带宽限制 |
| 华东 6（福州-本地地域-关停中） | 2 Gbps | 无额外限制，受内外网总下载带宽限制 | 2 Gbps | 无额外限制，受内外网总上传带宽限制 |
| 华中 1（武汉-本地地域） | 2 Gbps | 无额外限制，受内外网总下载带宽限制 | 2 Gbps | 无额外限制，受内外网总上传带宽限制 |
| 韩国（首尔） | 2 Gbps | 无额外限制，受内外网总下载带宽限制 | 2 Gbps | 无额外限制，受内外网总上传带宽限制 |
| 泰国（曼谷） | 2 Gbps | 无额外限制，受内外网总下载带宽限制 | 2 Gbps | 无额外限制，受内外网总上传带宽限制 |
| 其他中国内地地域 | 10 Gbps | 无额外限制，受内外网总下载带宽限制 | 10 Gbps | 无额外限制，受内外网总上传带宽限制 |
| 其他非中国内地地域 | 5 Gbps | 无额外限制，受内外网总下载带宽限制 | 5 Gbps | 无额外限制，受内外网总上传带宽限制 |
| 无地域属性 | 10 Gbps | 无额外限制，受内外网总下载带宽限制 | 10 Gbps | 无额外限制，受内外网总上传带宽限制 |


如果达到阈值，请求会被流控。当请求被流控时，请求返回的Header中会携带x-oss-qos-delay-time: number。其中number为请求被流控的时长，单位为ms。上传类请求会返回精确的被流控的时长；下载类请求会返回根据流控程度和文件大小估算出的被流控的时长。

OSS 后台系统任务（如生命周期规则、跨区域复制、同区域复制、访问时间更新等）产生的请求不计入用户账户的 QPS 和带宽流控统计，仅通过 AssumeRole 获取临时凭证后发起的读写删操作会正常计入流控。例如，生命周期策略自动删除过期对象不占用账户删除操作 QPS 配额，跨区域复制功能有独立的 QPS 限额与账户 QPS 配额相互独立。

## 每秒请求数QPS（Query Per Second）

单个阿里云账号的总QPS为10,000，但在不同的读写方式下，实际能达到的值如下：

| 读写方式 | QPS |
| --- | --- |
| 顺序读写 | 2,000 |
| 非顺序读写 | 10,000 |


单文件上传和下载的总QPS最高为2,000，峰值带宽不超过10 Gbps（同时受阿里云账号在各地域及对应Bucket的带宽和QPS上限限制）。

如果您在上传大量文件时，在命名上使用了顺序前缀（如时间戳或字母顺序），可能会出现大量文件索引集中存储于存储空间中某个特定分区的情况，此时如果您的请求速率过大，会导致请求速率下降。建议您在上传大量文件时，不要使用顺序前缀的文件名。关于如何将顺序前缀改为随机性前缀的方法，请参见[OSS](products/oss/documents/user-guide/oss-performance-best-practices.md)[性能最佳实践](products/oss/documents/user-guide/oss-performance-best-practices.md)。

## 存储空间（Bucket）

- 

同一阿里云账号在同一地域内创建的存储空间总数不能超过100个。如果您的业务需要创建更多数量的存储空间，请通过[配额中心](https://quotas.console.aliyun.com/products/oss/quotas)提交申请。

- 

存储空间名称在OSS范围内必须全局唯一。有关存储空间的命名规范，请参见[存储空间命名](products/oss/documents/user-guide/bucket-naming-conventions.md)。

- 

存储空间创建后，其名称、所处地域、存储类型不支持修改。

- 

单个存储空间的容量不限制。

## 文件（Object）

- 

上传文件的大小

通过[简单上传](products/oss/documents/user-guide/simple-upload.md)、[表单上传](products/oss/documents/user-guide/form-upload.md)、[追加上传](products/oss/documents/user-guide/append-upload-11.md)的方式上传单个文件，文件的大小不能超过5 GB。

通过[分片上传](products/oss/documents/user-guide/multipart-upload.md)的方式上传单个文件，文件的大小不能超过48.8 TB。

- 

重命名文件的大小

控制台仅支持重命名1 GB及1 GB以下的文件，1 GB以上的文件建议使用SDK或者命令行ossutil工具。更多信息，请参见[重命名文件](products/oss/documents/user-guide/rename-objects.md)。

- 

删除文件的数量

通过OSS控制台一次最多可删除100个文件，通过SDK一次最多可删除1000个文件，通过命令行工具ossutil以及图形化管理工具ossbrowser一次最多可删除的文件个数无限制。

警告

文件删除后无法恢复，请谨慎操作。

- 

同名文件被覆盖

默认情况下，如果上传的文件与已有文件同名，则覆盖已有文件。

警告

文件被覆盖后将丢失原有文件，请谨慎操作。为防止文件被意外覆盖，您可以通过为文件所在的Bucket开启版本控制，或者在上传请求的Header中携带参数x-oss-forbid-overwrite，并指定其值为true。

## 数据解冻

在访问归档存储（未开启归档直读）、冷归档存储、深度冷归档存储类型的数据之前，需要先等待数据解冻完成。解冻优先级越高，解冻时间越短，解冻涉及的数据取回费用越高。更多信息，请参见[数据取回费用](https://www.aliyun.com/price/product?spm=a2c4g.173537.0.0.55084b78TQ4oq5#/oss/detail/ossbag)。

- 

- 

- 

- 

- 

| 存储类型 | 解冻时间 | 解冻配额 |
| --- | --- | --- |
| 归档 | 通常 1 分钟。 | 不涉及 |
| 冷归档 | 高优先级（Expedited）：通常 1 小时内完成解冻。 标准（Standard）：通常 2~5 小时内完成解冻。 批量（Bulk）：通常 5~12 小时内完成解冻。 | 单个阿里云账号在单个地域的冷归档类型的 Object 的解冻配额参考值：平均每秒 500 个 Object，三种解冻优先级总解冻配额为每天 100 TB~120 TB。 |
| 深度冷归档 | 高优先级（Expedited）：通常 12 小时内完成解冻。 标准（Standard）：通常 48 小时内完成解冻。 | 单个阿里云账号在单个地域的深度冷归档类型的 Object 解冻配额参考值：平均每秒 100 个 Object，两种解冻优先级总解冻配额为每天 10 TB~15 TB。 |


超出冷归档以及深度冷归档的解冻配额参考值后，仍可以提交解冻请求。解冻请求将排入队列中，且解冻完成时间可能超出指定优先级对应的完成时间。

## 域名绑定

- 

中国内地各地域绑定的域名必须在工信部备案，其他地域的域名绑定不需要在工信部备案。

- 

一个域名只能绑定在一个存储空间上，一个存储空间最多可以绑定100个域名。

- 

一个账号可绑定的域名个数无限制。

## 生命周期规则

- 

一个存储空间最多可配置1,000条生命周期规则。

- 

执行完成时间：

- 

规则生效后，华东1（杭州）、华东2（上海）、华北2（北京）、华北 3（张家口）、华北6（乌兰察布）、华南1（深圳）、新加坡地域，执行 Object 数在 10 亿以内的生命周期相关操作（包括 Object 删除、 Object 存储类型转换以及碎片过期），通常情况下在 24 小时内完成；其他地域，执行 Object 数在 1 亿以内的生命周期相关操作（包括 Object 删除、 Object 存储类型转换以及碎片过期），通常情况下在 24 小时内完成。

- 

如出现以下情况，则可能使任务执行时间超过 24 小时，甚至持续数天到数周：扫描 Object 数过多、待执行生命周期的 Object 数过多、标签数较多、单 Object 的历史版本数量过多、生命周期任务执行时新上传的 Object 过多等。

说明

如果存储空间开启了版本控制，则对Object的每个版本均记为一次操作。

## 回源规则

- 

一个存储空间最多可配置20条回源规则。

- 

对于镜像回源，中国内地各地域和中国香港默认QPS为2,000、流量为2 Gbps；海外各地域默认QPS为1,000、流量为1 Gbps。

## 图片处理

- 

图片限制

- 

原图

- 

图片格式只支持JPG、PNG、BMP、GIF、WebP、TIFF、HEIC、AVIF。

- 

原图大小不能超过20 MB。

- 

除图片旋转对应的原图高或者宽不能超过4,096 px外，其他图片操作对应的原图高或者宽不能超过30,000 px，且总像素不能超过2.5亿 px。

动态图片（例如GIF图片）的像素计算方式为宽*高*图片帧数；非动态图片（例如PNG图片）的像素计算方式为宽*高。

- 

缩放后的图片

宽或高不能超过16,384 px，且总像素不能超过16,777,216 px。

- 

样式限制

每个存储空间下最多能创建50个样式。

- 

处理能力限制

- 

每秒图片处理量（按原图大小计）

- 

华东1（杭州）、华东2（上海）、华北2（北京）、华北 3（张家口）、华南1（深圳）：20 MB/s。

- 

其他地域：2 MB/s。

- 

每秒请求数QPS（Query Per Second）

- 

华东1（杭州）、华东2（上海）、华北2（北京）、华北 3（张家口）、华南1（深圳）：50。

- 

其他地域：5。

## 资源包

- 

地域资源包仅支持在归属地域使用；中国内地通用资源包可以抵扣中国内地所有地域的对应计费项，例如华东1（杭州）、华东2（上海）、华南1（深圳）等，不能抵扣中国香港和海外地域的对应计费项。

- 

已购资源包不支持更换地域。

- 

资源包中的存储包不支持叠加购买，但支持对已购存储包进行[升级](products/oss/documents/resource-plan.md)。

- 

资源包中的传输加速包和回源流量包支持叠加购买，但不支持升级和续费。

- 

资源包中的下行流量包和高防基础包支持叠加购买和续费，但不支持升级。

- 

[请求费用](products/oss/documents/api-operation-calling-fees.md)、[数据处理费用](products/oss/documents/data-processing-fees.md)和[流量费用](products/oss/documents/traffic-fees.md)中的跨区域复制流量费用暂时无对应的资源包，即不支持包年包月，仅支持按量计费。

[上一篇：地域和Endpoint](products/oss/documents/user-guide/regions-and-endpoints.md)[下一篇：访问域名与网络连接](products/oss/documents/user-guide/access-domain-name-and-network-connection.md)

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
