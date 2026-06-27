# OSS存储费用的计费项-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/storage-fees

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

# 存储费用

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

只要文件存储在OSS Bucket就会产生存储费用，与文件是否被访问，以及对文件执行何种操作无关。当您在OSS内存储文件时，OSS会根据您的文件存储类型、大小和时长收取存储费用。

## 计费单价

本文仅说明相关计费项及付费方式。有关计费项的定价详情，请参见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)。

OSS产品定价中明确了存储费用的单价为元/GB/月，但账单中的计费项按小时计费，计算方法为实际资源使用量×每小时单价。因此当您需要计算实际存储费用时，需要先将存储费用的单价转换为元/GB/小时。例如标准型（本地冗余存储）单价为0.12元/GB/月，则按小时计费的单价约为0.000167元/GB/小时（0.12÷30÷24）。

## 计费项

- 

已存储时长容量费用

当文件存储在OSS Bucket时，OSS将结合您的文件存储类型、[存储冗余类型](products/oss/documents/user-guide/overview-of-storage-redundancy-types.md)、存储大小以及存储时长收取存储容量费用。

- 

不足规定时长容量费用

部分存储类型有最低存储时长的要求。其中，低频访问最低存储时长为30天、归档最低存储时长为60天、冷归档以及深度冷归档最低存储时长均为180天。当文件以这几种存储类型存储在OSS Bucket，且在不满足规定存储时长要求前转换文件存储类型或者将文件删除，将会产生不足规定时长容量费用。

计算示例：低频访问类型文件存储时间不足30天（即720小时）被覆写或删除，会收取剩余时间（720-已存储时间）的存储费用。归档、冷归档以及深度冷归档计算规则类似，区别在于最低存储时长的差异。

### 已存储时长容量（本地冗余）

| 计费项 | 计费项 Code | 最小计量单位限制 |
| --- | --- | --- |
| 标准存储（本地冗余）容量 | Storage | 无 （按照实际大小计算） |
| 低频访问（本地冗余）容量 | ChargedDatasize | 64 KB （小于 64 KB，按照 64 KB 计算；大于或等于 64 KB，按照实际大小计算） |
| 归档（本地冗余）容量 | ChargedDatasize |  |
| 冷归档（本地冗余）容量 | ChargedDatasizeCA |  |
| 深度冷归档（本地冗余）容量 | ChargedDatasizeDeepCA |  |
| 无地域属性存储容量 | AnywhereReservedCapacityLRS | 无 （按照实际大小计算） |


由于低频、归档、冷归档以及深度冷归档存储类型有最小计量单位64 KB的限制，会导致Bucket内计费容量大于实际存储容量的情况。如需了解这些存储类型的实际容量以及计费容量，请参见[获取](products/oss/documents/developer-reference/query-the-storage-capacity-of-a-bucket-1.md)[Bucket](products/oss/documents/developer-reference/query-the-storage-capacity-of-a-bucket-1.md)[的存储容量](products/oss/documents/developer-reference/query-the-storage-capacity-of-a-bucket-1.md)。

### 已存储时长容量（同城冗余）

| 计费项 | 计费项 Code | 最小计量单位限制 |
| --- | --- | --- |
| 标准存储（同城冗余）容量 | StorageZRS | 无 （按照实际大小计算） |
| 低频访问（同城冗余）容量 | ChargedDatasizeZRS | 64 KB （小于 64 KB，按照 64 KB 计算；大于或等于 64 KB，按照实际大小计算） |
| 归档（同城冗余）容量 | ChargedDataSizeArcZRS |  |


### 不足规定时长容量（本地冗余）

| 计费项 | 计费项 Code | 最低存储时长计算方法 |
| --- | --- | --- |
| 低频访问（本地冗余）不足规定时长容量 | LessthanMonthDatasize | 以文件存储在 OSS 的 Last Modified 时间开始计算 |
| 归档存储（本地冗余）不足规定时长容量 | LessthanMonthDatasize |  |
| 冷归档存储（本地冗余）不足规定时长容量 | EarlyDeletionCA | 以文件转为冷归档或者深度冷归档类型的时间开始计算 |
| 深度冷归档存储（本地冗余）不足规定时长容量 | EarlyDeletionDeepCA |  |


为避免产生不足规定时长容量费用，您需要了解不同存储类型Object的最低存储时长计算方法，确保满足其最低存储时长后再进行转储或者删除。更多信息，请参见[如何避免产生存储不足规定时长容量费用？](products/oss/documents/how-can-i-avoid-the-cost-of-insufficient-storage.md)。

### 不足规定时长容量（同城冗余）

| 计费项 | 计费项 Code | 最低存储时长计算方法 |
| --- | --- | --- |
| 低频访问（同城冗余）不足规定时长容量 | LessthanMonthDatasizeZRS | 以文件存储在 OSS 的 Last Modified 时间开始计算 |
| 归档存储（同城冗余）不足规定时长容量 | LessthanMonthDatasizeArcZRS |  |


## 支付方式

不同存储类型对应存储费用的支付方式存在差异。存储费用共支持5种付费方式，分别为按量付费、存储包、预留空间、无地域属性预留空间和存储容量单位包SCU。

### 选型指导

建议您参考以下多种付费方式的介绍，了解不同付费方式的特点、适用场景等信息，方便您选择适当的付费方式，以降低存储成本。

- 

- 

| 付费方式 | 说明 | 特点 | 适用场景 |
| --- | --- | --- | --- |
| 按量付费 | 所有计费项默认采用按量付费。按照各计费项的实际用量结算费用。先使用，后付费。 | 存储量波动较大、难以预测 | 初创公司或项目初期，存储量不稳定，使用按量付费可以避免资源浪费，根据实际使用量付费，灵活调整资源。 |
| 存储包 | 针对不同存储计费项推出的优惠资源包。在费用结算时，优先从资源包抵扣用量。先购买，后抵扣。 | 各存储类型的存储量相对稳定、可预测 | 大型企业或长期运行的项目，不同存储类型的存储量相对稳定，使用对应的资源包可以降低存储成本。存储包最小规格为 40 GB，最大规格为 20 PB。 |
| [预留空间](products/oss/documents/reserved-capacity.md) | 针对满足地域属性特定存储计费项的预付费产品。先购买，后抵扣。 | 只能抵扣 [有地域属性](products/oss/documents/user-guide/region-attribute-of-buckets.md) [Bucket](products/oss/documents/user-guide/region-attribute-of-buckets.md) 产生的标准存储（本地冗余）容量费用以及 ECS 快照存储 | 适用于有地域属性 Bucket 稳定且较大规模的标准存储（本地冗余）和 ECS 快照存储量的场景。预留空间容量最小规格为 500 GB，最大规格为 1 PB。 |
| [无地域属性预留空间](products/oss/documents/anywhere-reserved-capacity.md) | 针对满足地域属性特定存储计费项的预付费产品。先购买，后抵扣。 | 只能抵扣 [无地域属性](products/oss/documents/user-guide/region-attribute-of-buckets.md) [Bucket](products/oss/documents/user-guide/region-attribute-of-buckets.md) 产生的标准存储（本地冗余）容量费用 | 适用于无地域属性 Bucket 稳定且大规模的标准存储（本地冗余）存储量的场景。无地域属性预留空间容量最小规格为 10 TB，最大规格为 1 PB。 |
| [存储容量单位包](products/oss/documents/scu.md) [SCU](products/oss/documents/scu.md) | 针对多款云产品的多个存储计费项的预付费产品。先购买，后抵扣。 | 抵扣 OSS 多项存储容量费用，以及多种云存储产品存储容量费用 | 使用 OSS 过程中同时产生了多项存储容量费用。 除使用 OSS 以外，还使用了 NAS、快照服务、云备份等产品。 |


### 支持情况

以下为各存储类型付费方式的支持情况：

| 计费项 | 按量付费 | 存储包 | 预留空间 | 无地域属性预留空间 | 存储容量单位包 SCU |
| --- | --- | --- | --- | --- | --- |
| 标准存储（同城冗余）容量 | √ | [标准-同城冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_std_zrs%22,%22region%22:%22china-common%22,%22pack%22:%22FPT_ossbag_absolute_1572089992%22,%22std_zrs_storage_bag_spec%22:%22100%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | √ |
| 标准存储（本地冗余）容量 | √ | [标准-本地冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%226:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage%22,%22region%22:%22china-common%22,%22ossbag_spec%22:%2240%22,%22pack%22:%22FPT_ossbag_absolute_Storage_china_common%22,%22showtime%22:%22now%22%7D&regionId=china-common) | √ | × | √ |
| 低频访问（同城冗余）容量 | √ | [低频-同城冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_ia_zrs%22,%22region%22:%22china-common%22,%22pack%22:%22FPT_ossbag_absolute_1572090490%22,%22ia_zrs_storage_bag_spec%22:%22100%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | √ |
| 低频访问（本地冗余）容量 | √ | [低频-本地冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_ia_lrs%22,%22region%22:%22china-common%22,%22ossbag_storage_ia_lrs_spec%22:%22100%22,%22pack%22:%22FPT_ossbag_absolute_IA_Storage_china_common%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | √ |
| 归档（本地冗余）容量 | √ | [归档-本地冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_archive_lrs%22,%22region%22:%22china-common%22,%22ossbag_storage_archive_spec%22:%22100%22,%22pack%22:%22FPT_ossbag_absolute_Archive_Storage_china_common%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | √ |
| 冷归档（本地冗余）容量 | √ | [冷归档-本地冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_coldarchive%22,%22region%22:%22china-common%22,%22pack%22:%22FPT_ossbag_absolute_1598258389%22,%22ossbag_storage_coldarchive_spec%22:%22512000%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | × |
| 深度冷归档（本地冗余）容量 | √ | × | × | × | × |
| 无地域属性存储容量 | √ | × | × | √ | × |
| 归档（同城冗余）容量 | √ | [归档-同城冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_archive_zrs%22,%22region%22:%22china-common%22,%22ossbag_storage_archive_spec%22:%22100%22,%22pack%22:%22FPT_ossbag_absolute_Archive_Storage_china_common%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | × |
| 低频访问（本地冗余）不足规定时长容量 | √ | [低频-本地冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_ia_lrs%22,%22region%22:%22china-common%22,%22ossbag_storage_ia_lrs_spec%22:%22100%22,%22pack%22:%22FPT_ossbag_absolute_IA_Storage_china_common%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | × |
| 归档存储（本地冗余）不足规定时长容量 | √ | [归档-本地冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_archive_lrs%22,%22region%22:%22china-common%22,%22ossbag_storage_archive_spec%22:%22100%22,%22pack%22:%22FPT_ossbag_absolute_Archive_Storage_china_common%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | × |
| 冷归档存储（本地冗余）不足规定时长容量 | √ | [冷归档-本地冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_coldarchive%22,%22region%22:%22china-common%22,%22pack%22:%22FPT_ossbag_absolute_1598258389%22,%22ossbag_storage_coldarchive_spec%22:%22512000%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | × |
| 深度冷归档存储（本地冗余）不足规定时长容量 | √ | × | × | × | × |
| 低频访问（同城冗余）不足规定时长容量 | √ | [低频-同城冗余存储包](https://common-buy.aliyun.com/?commodityCode=ossbag&request=%7B%22ord_time%22:%221:Month%22,%22order_num%22:1,%22ossbag_type%22:%22storage_ia_zrs%22,%22region%22:%22china-common%22,%22pack%22:%22FPT_ossbag_absolute_1572090490%22,%22ia_zrs_storage_bag_spec%22:%22100%22,%22showtime%22:%22now%22%7D&regionId=china-common) | × | × | × |
| 归档存储（同城冗余）不足规定时长容量 | √ | × | × | × | × |


## 计费案例

- 

[OSS](products/oss/documents/billing-examples.md)[分发静态资源（高频访问）](products/oss/documents/billing-examples.md)

- 

[OSS](products/oss/documents/billing-examples.md)[分发静态资源 （低频访问）](products/oss/documents/billing-examples.md)

- 

[预留空间抵扣案例](products/oss/documents/reserved-capacity.md)

- 

[无地域属性预留空间抵扣案例](products/oss/documents/anywhere-reserved-capacity.md)

- 

[SCU](products/oss/documents/scu.md)[抵扣案例](products/oss/documents/scu.md)

## 常见问题

### 购买低频-本地冗余存储包后，为什么还会在某个计费周期（小时）产生低频访问（本地冗余）不足规定时长容量的大额账单？

当低频访问类型存储时长远不足720小时的情况下，由于OSS是一次性计算低频访问不足规定时长容量，已购买资源包只能抵扣部分容量，因此在数据被转储或被删除的下一个计费周期（小时）会产生大额账单。

例如，您在09月07日06点以低频访问类型存储了10 TB数据，在09月08日06点通过自动或手动的方式将其中1 TB数据转换其他存储类型或者删除。此时，该计费项产生的计量数据为1 TB*（720-24）=696 TB。假设您购买低频-本地冗余存储包容量为10 TB：

- 

如果低频访问存储容量先出账，则已购买资源包可以抵扣（9 TB低频访问存储容量+1 TB低频访问不足规定时长）容量费用，超出部分（696 TB-1 TB）按量付费。

- 

如果低频访问不足规定时长容量先出账，则已购买的资源包可以抵扣10 TB低频访问不足规定时长容量费用， 超出部分低频访问不足规定时长容量（696 TB-10 TB）以及低频存储容量9 TB按量付费。

### 购买归档-本地冗余存储包后，为什么还会在某个计费周期（小时）产生归档（本地冗余）不足规定时长容量的大额账单？

当归档类型存储时长远不足1440小时的情况下，由于OSS是一次性计算归档存储不足规定时长容量，已购买资源包只能抵扣部分容量，因此在数据在被转换存储类型或被删除的下一个计费周期（小时）会产生大额账单。

例如，您在09月07日06点以归档类型存储了10 TB数据，在09月08日06点通过自动或手动的方式将其中1 TB数据转换为其他存储类型或者删除。此时，该计费项产生的计量数据为1 TB*（1440-24）=1416 TB。假设您购买归档-本地冗余存储包容量为10 TB：

- 

如果归档存储容量先出账，则已购买资源包可以抵扣（9 TB归档存储容量+1 TB归档不足规定时长）容量费用，超出部分（1416 TB-1 TB）按量付费。

- 

如果归档不足规定时长容量先出账，则已购买的资源包可以抵扣10 TB归档不足规定时长容量费用， 超出部分归档不足规定时长容量（1416 TB-10 TB）以及归档存储容量9 TB按量付费。

### 为什么连续出现不足规定时长容量费用？

对低频、归档、冷归档、深度冷归档存储类型的Object，在其不足规定时长前对Object进行转储或者删除，均会产生不足规定时长容量费用。

- 

对于该场景下的Object删除操作，会一次性收取不足规定时长容量费用，不会连续出现不足规定时长容量费用。

- 

对于该场景下的Object覆写操作，则可能连续出现不足规定时长容量费用。例如，Object以低频类型上传至Bucket，低频类型Object最低存储时长为30天。在Object存储1天后，您上传了同名Object（覆写操作），此时会产生29天低频不足规定时长容量费用。如果您在上传同名Object 3天后，对Object进行再次覆写或者删除，此时还会产生27天低频不足规定时长容量费用。

## 相关文档

- 

OSS默认以标准类型存储上传的Object。如果因业务需求的变化，需要将标准类型转为更低存储成本的低频、归档、冷归档或者深度冷归档类型，请参见[转换存储类型](products/oss/documents/user-guide/convert-storage-classes.md)。

- 

关于低频访问、归档、冷归档以及深度冷归档存储不足规定时长的计费案例，请参见[Object](products/oss/documents/billing-method-for-objects-whose-storage-duration-is-less-than-the-minimum-storage-duration.md)[在存储不足规定时长时如何计费？](products/oss/documents/billing-method-for-objects-whose-storage-duration-is-less-than-the-minimum-storage-duration.md)。

- 

对于分片上传过程中产生的Part，OSS会根据Part的存储类型、实际大小和时长收取存储费用。更多信息，请参见[碎片如何计费？](products/oss/documents/billing-method-for-parts.md)。

- 

如果您希望查询OSS按小时计量的数据信息，请参见[查询](products/oss/documents/query-oss-billing-data-generated-on-an-hourly-basis.md)[OSS](products/oss/documents/query-oss-billing-data-generated-on-an-hourly-basis.md)[小时数据](products/oss/documents/query-oss-billing-data-generated-on-an-hourly-basis.md)。

- 

如果您希望在具体的计费案例中了解该计费项的计费详情，请参见[计费案例](products/oss/documents/billing-examples.md)。

- 

如果您希望查看该计费项的费用明细，请参见[账单查询](products/oss/documents/query-bills.md)。

[上一篇：基础计费项](products/oss/documents/basic-billing-item.md)[下一篇：流量费用](products/oss/documents/traffic-fees.md)

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
