# 弹性临时盘为ECS实例提供临时数据存储空间-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/elastic-ephemeral-disks

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 弹性临时盘

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

弹性临时盘（Elastic Ephemeral Disk）是一款可灵活随实例创建或单独创建的、由用户自定义选择容量大小的块存储设备，作为临时数据存储使用，为ECS实例提供临时数据存储，具备高性能、高性价比等特点。本文主要介绍弹性临时盘的规格、计费、使用限制、常用操作等信息。

## 弹性临时盘简介

### 弹性临时盘与本地盘对比

弹性临时盘是一款具备弹性容量能力的块存储设备，与本地盘（只能随ECS实例购买）相比有如下不同：

性能对比请查看[块存储性能](products/ecs/documents/user-guide/block-storage-performance.md)。

- 

- 

- 

- 

| 对比项 | 弹性临时盘 | 本地盘 |
| --- | --- | --- |
| 性价比 | 独立定价。 | 本地盘存储价格不独立定价，价格通过实例进行计算，存在浮动变化。 |
| 灵活性 | 可自定义容量大小，支持扩容，无需为冗余资源付费。 可随实例创建或单独创建，支持单独卸载、释放等操作。 | 随 ECS 实例规格自动选择固定容量大小，不支持扩容。 重要 如需扩大容量，必须相应购买计算和存储资源，这可能会造成资源浪费。 只能随部分实例规格的 ECS 实例创建和释放，不支持单独卸载、释放等操作。 |
| 可运维性 | 故障后可在小时级恢复。 | 故障之后，无法快速修复，需等待维修或直接更换实例，运维难度高，维修时间长。 |


### 应用场景

- 

临时数据存储

适用于存放临时数据，例如临时计算中间结果、缓存数据、临时文件等。

- 

高性能计算

对IOPS（数十万到百万）和吞吐量（数百MB/s至数GB/s）要求高的计算任务，弹性临时盘可以提供高性能的临时存储支持。

### 生命周期

弹性临时盘的生命周期与ECS实例部分耦合。

- 

如果ECS实例为包年包月，弹性临时盘仅支持包年包月。生命周期与实例一致，随实例到期强制释放。欠费时，您可以正常使用已有的弹性临时盘，但不能新购。更多信息，请参见[包年包月](products/ecs/documents/subscription.md)。

- 

如果ECS实例为按量付费，欠费时，您无法正常使用弹性临时盘。更多信息，请参见[按量付费](products/ecs/documents/pay-as-you-go-1.md)。

关于欠费的更多信息，请参见[欠费说明](products/ecs/documents/overdue-payments.md)。

### 计费说明

- 

计费项及计费规则

弹性临时盘收取云盘容量费，支持按量付费和包年包月。详细的计费规则，请参见[弹性临时盘计费](products/ecs/documents/block-storage-devices.md)。

- 

定价

弹性临时盘的定价详情，请参见[块存储定价](https://www.aliyun.com/price/product#/disk/detail)。

## 使用限制

### 地域限制

- 

弹性临时盘标准版：华东1（杭州）的可用区B、可用区J和可用区K，华东2（上海）的可用区M、可用区N和可用区E，华北2（北京）的可用区F、可用区I和可用区L，西南1（成都）的可用区B，新加坡的可用区A、可用区B和可用区C，德国（法兰克福）的可用区A、可用区B和可用区C。

- 

弹性临时盘高级版：华东1（杭州）的可用区J，华东2（上海）的可用区M和可用区N，华北2（北京）的可用区I，西南1（成都）的可用区B，日本（东京）的可用区A，中国香港的可用区D。

### 实例规格限制

弹性临时盘支持以下实例规格族：

- 

[海光通用型实例规格族](products/ecs/documents/user-guide/general-purpose-instance-families.md)[g9h](products/ecs/documents/user-guide/general-purpose-instance-families.md)

- 

[存储增强通用型实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)[g8ise](products/ecs/documents/user-guide/overview-of-instance-families.md)

- 

[通用型实例规格族](products/ecs/documents/user-guide/general-purpose-instance-families.md)[g8a](products/ecs/documents/user-guide/general-purpose-instance-families.md)

- 

[通用型实例规格族](products/ecs/documents/user-guide/general-purpose-instance-families.md)[g8i](products/ecs/documents/user-guide/general-purpose-instance-families.md)

- 

[通用型实例规格族](products/ecs/documents/user-guide/general-purpose-instance-families.md)[g8y](products/ecs/documents/user-guide/general-purpose-instance-families.md)

- 

[计算型实例规格族](products/ecs/documents/user-guide/compute-optimized-instance-families.md)[c8a](products/ecs/documents/user-guide/compute-optimized-instance-families.md)

- 

[计算型实例规格族](products/ecs/documents/user-guide/compute-optimized-instance-families.md)[c8i](products/ecs/documents/user-guide/compute-optimized-instance-families.md)

- 

[计算型实例规格族](products/ecs/documents/user-guide/compute-optimized-instance-families.md)[c8y](products/ecs/documents/user-guide/compute-optimized-instance-families.md)

- 

[内存型实例规格族](products/ecs/documents/user-guide/memory-optimized-instance-families-1.md)[r8a](products/ecs/documents/user-guide/memory-optimized-instance-families-1.md)

- 

[内存型实例规格族](products/ecs/documents/user-guide/memory-optimized-instance-families-1.md)[r8i](products/ecs/documents/user-guide/memory-optimized-instance-families-1.md)

- 

[内存型实例规格族](products/ecs/documents/user-guide/memory-optimized-instance-families-1.md)[r8y](products/ecs/documents/user-guide/memory-optimized-instance-families-1.md)

- 

[GPU](products/ecs/documents/user-guide/gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md)[云服务器（gn/vgn/sgn](products/ecs/documents/user-guide/gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md)[系列）](products/ecs/documents/user-guide/gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md)

- 

[GPU](products/ecs/documents/user-guide/overview-of-instance-families.md)[计算型实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)[gn9gc](products/ecs/documents/user-guide/overview-of-instance-families.md)

- 

[GPU](products/ecs/documents/user-guide/gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md)[计算型实例规格族](products/ecs/documents/user-guide/gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md)[gn8v/gn8v-tee](products/ecs/documents/user-guide/gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md)

- 

[GPU](products/ecs/documents/user-guide/elastic-bare-metal-server-overview.md)[计算型弹性裸金属服务器实例规格族](products/ecs/documents/user-guide/elastic-bare-metal-server-overview.md)[ebmgn8v](products/ecs/documents/user-guide/elastic-bare-metal-server-overview.md)

- 

[GPU](products/ecs/documents/user-guide/elastic-bare-metal-server-overview.md)[计算型弹性裸金属服务器实例规格族](products/ecs/documents/user-guide/elastic-bare-metal-server-overview.md)[ebmgn8is](products/ecs/documents/user-guide/elastic-bare-metal-server-overview.md)

- 

[高性能计算优化型实例规格族](products/ecs/documents/user-guide/overview-of-hpc-optimized-instance-families.md)[hpc8i](products/ecs/documents/user-guide/overview-of-hpc-optimized-instance-families.md)

- 

[通用型实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)[g9i](products/ecs/documents/user-guide/overview-of-instance-families.md)

- 

[计算型实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)[c9i](products/ecs/documents/user-guide/overview-of-instance-families.md)

- 

[内存型实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)[r9i](products/ecs/documents/user-guide/overview-of-instance-families.md)

- 

[通用算力型实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)[u2i](products/ecs/documents/user-guide/overview-of-instance-families.md)

- 

[本地](products/ecs/documents/user-guide/overview-of-instance-families.md)[SSD](products/ecs/documents/user-guide/overview-of-instance-families.md)[型实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)[i5e](products/ecs/documents/user-guide/overview-of-instance-families.md)

- 

[本地](products/ecs/documents/user-guide/overview-of-instance-families.md)[SSD](products/ecs/documents/user-guide/overview-of-instance-families.md)[型实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md)[i5](products/ecs/documents/user-guide/overview-of-instance-families.md)

### 功能限制

| 功能 | 弹性临时盘 | 其他云盘 |
| --- | --- | --- |
| 单独创建 | 是 | 是 |
| 单独挂载/卸载 | 是 重要 弹性临时盘支持单独卸载，但卸载后不支持挂载到其他实例。 | 是 |
| 释放 | 是 重要 挂载至实例后，弹性临时盘会随实例释放而释放。 | 是 |
| 初始化 | 是 | 是 |
| 扩容 | 是 | 是 |
| 创建快照/通过快照回滚 | 否 | 是 |
| 加密 | 否 | 是 |
| 多重挂载 | 否 | 是 |
| 异步复制 | 否 | 是 |
| 单独转换云盘计费方式 | 否 重要 弹性临时盘只能随实例转换计费方式。 | 是 |
| 变更云盘类型 | 否 | 是 |
| 作为系统盘 | 否 | 是 |


## 弹性临时盘类型及性能

提供标准版和高级版两种规格的弹性临时盘，标准版更适合数据量较大、对吞吐量要求较高的场景，高级版更适合容量小但对IOPS要求高的场景。不同类型可达到的性能说明如下表所示：

| 性能类别 | 弹性临时盘标准版 | 弹性临时盘高级版 |
| --- | --- | --- |
| 单盘容量范围（GiB） | 64~8,192 | 64~8,192 |
| 单盘最大读 IOPS | min ② {100*容量, 820,000} | min{300*容量, 1,000,000} |
| 单盘最大写 IOPS | min{20*容量, 160,000} | min{150*容量, 500,000} |
| 单盘最大读吞吐量（MB/s） | min{0.8*容量, 4,096} | min{1.6*容量, 4,096} |
| 单盘最大写吞吐量（MB/s） | min{0.4*容量, 2,048} | min{1*容量, 2,048} |
| 写 I/O 密度 ① | 20 | 150 |
| 读 I/O 密度 ① | 100 | 300 |


①：IO密度=IOPS/云盘容量，单位是IOPS/GiB，表示每GiB可达到的IOPS能力。

②：min{A，B}，表示返回A和B两个数值中的较小值。

## 使用弹性临时盘

### 创建弹性临时盘

随实例创建

- 

前往[实例创建页](https://ecs-buy.aliyun.com/wizard/#/)。

- 

选择自定义购买页签。

- 

按需选择付费类型、地域、实例规格、镜像等配置。创建弹性临时盘需注意以下参数：

- 

在地域及网络及可用区区域选择弹性临时盘支持的地域及可用区。

- 

在实例参数处选择符合要求的实例规格。

- 

在存储区域展开弹性临时盘｜文件存储 NAS（选填），并单击添加弹性临时盘。

- 

选择弹性临时盘的类型、容量大小及数量。其他更多的参数说明，请参见[自定义购买实例](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)。

说明

可挂载的数量与实例规格相关，最多只能挂载16块弹性临时盘。

单独创建

- 

访问[ECS](https://ecs.console.aliyun.com/disk/)[控制台-块存储-云盘](https://ecs.console.aliyun.com/disk/)。

- 

在弹性临时盘页签，单击创建弹性临时盘。

- 

设置配置参数。

- 

选择支持弹性临时盘的地域及可用区。

- 

选择弹性临时盘的类型以及容量大小。

更多参数说明，请参见[创建空数据盘](products/ecs/documents/user-guide/create-a-disk.md)。

- 

将创建的弹性临时盘挂载至ECS实例，并进行初始化操作，才能正常使用。

更多信息，请参见[挂载数据盘](products/ecs/documents/user-guide/attach-a-data-disk.md)。

### 其他操作

弹性临时盘与云盘功能相比有一些使用限制，仅支持以下操作。使用限制的详细信息，请参见[功能限制](products/ecs/documents/user-guide/elastic-ephemeral-disks.md)。

支持的详细操作可参考云盘相关文档：

- 

[挂载数据盘](products/ecs/documents/user-guide/attach-a-data-disk.md)

- 

[初始化数据盘](products/ecs/documents/user-guide/initialize-a-data-disk.md)

- 

[扩容云盘](products/ecs/documents/user-guide/resize-cloud-disks.md)

- 

[修改云盘标签](products/ecs/documents/user-guide/modify-the-tags-of-a-disk.md)

- 

[转换云盘计费方式](products/ecs/documents/switch-the-billing-method-of-a-disk.md)

- 

[卸载数据盘](products/ecs/documents/user-guide/detach-a-data-disk.md)

- 

[释放云盘](products/ecs/documents/user-guide/release-a-disk.md)

## 常见问题

如何理解弹性临时盘的可靠性？

弹性临时盘的故障率设计目标介于本地盘和云盘之间，阿里云采用多种技术方式来降低故障率，但无法保证在故障后数据不丢失。

弹性临时盘相比ESSD系列云盘有何不同？

弹性临时盘不具备ESSD系列云盘的高可靠性、在线变配、多种数据保护和容灾功能。另外，弹性临时盘不支持卸载后挂载至其他实例使用。

[上一篇：ESSD云盘](products/ecs/documents/user-guide/essds.md)[下一篇：本地盘](products/ecs/documents/user-guide/local-disks.md)

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
