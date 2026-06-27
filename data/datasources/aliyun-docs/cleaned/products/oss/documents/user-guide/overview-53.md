# OSS有哪几种存储类型-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/overview-53

# 存储类型
对象存储OSS提供标准、低频访问、归档、冷归档、深度冷归档多种存储类型，全面覆盖从热到冷的各种数据存储场景。
说明
各存储类型的定价，请参见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)。各存储类型的计费方式，请参见[存储费用](../storage-fees.md)。
## 标准存储（Standard）
提供高可靠、高可用、高性能的对象存储服务，能够支持频繁的数据访问。适用于各种社交、分享类的图片、音视频应用、大型网站、大数据分析等业务场景。标准存储类型支持同城冗余ZRS（Zone-redundant storage）和本地冗余LRS（Locally redundant storage）两种数据冗余存储方式。
标准存储-同城冗余（推荐）
对于可用区数大于等于3个的地域（Region），采用多可用区的数据冗余存储机制，将用户的数据冗余存储在同一地域的3个或以上可用区，当某个可用区不可用时，仍然能够保障数据的正常访问。对于可用区数等于2个的地域，采用双可用区的数据冗余存储机制，将用户的数据冗余存储在同一地域的2个可用区，当某个可用区不可用时，仍然能够保障数据的正常访问。当前双可用区的同城冗余仅支持标准存储类型。
说明
华东1（杭州）、华东2（上海）、华北2（北京）、华北 3（张家口）、华北6（乌兰察布）、华南1（深圳）、中国香港、日本（东京）、新加坡、印度尼西亚（雅加达）、德国（法兰克福）、马来西亚（吉隆坡）地域对标准存储类型的数据采用多可用区的数据冗余存储机制。美国（硅谷）、菲律宾（马尼拉）、泰国（曼谷）、韩国（首尔）、阿联酋（迪拜）、英国（伦敦）地域对标准存储类型的数据采用双可用区的数据冗余存储机制。美国（弗吉尼亚）地域如需采用双可用区的数据冗余存储机制请联系[技术支持](https://selfservice.console.aliyun.com/ticket/createIndex)申请开通。
标准存储-本地冗余
采用单可用区（AZ）内的数据冗余存储机制，将用户的数据冗余存储在同一个可用区内多个设施的多个设备上，确保硬件失效时的数据持久性和可用性。
重要
本地冗余存储类型的数据冗余在某个特定的可用区内。当该可用区不可用时，会导致相关数据不可访问。如您的业务需要更高的可用性保障，建议您使用同城冗余的存储类型来存储和使用数据。
## 低频访问存储（Infrequent Access）
提供高持久性、较低存储成本的对象存储服务。有最小计量单位（64 KB）和最低存储时间（30天）的要求。支持数据实时访问，访问数据时会产生数据取回费用，适用于较低访问频率（平均每月访问频率1到2次）的业务场景。低频访问存储支持同城冗余和本地冗余两种数据冗余存储方式。
说明
最小计量单位（64 KB）表示不足64 KB的文件也要按64 KB大小来计费。最低存储时间（30天）表示以低频访问类型存储时长不足30天将收取低频访问不足规定时长容量费用。更多信息，请参见[存储费用](../storage-fees.md)。
低频访问-同城冗余（推荐）
采用多可用区（AZ）内的数据冗余存储机制，将用户的数据冗余存储在同一地域（Region）的多个可用区。当某个可用区不可用时，仍然能够保障数据的正常访问。
说明
华东1（杭州）、华东2（上海）、华北2（北京）、华北 3（张家口）、华北6（乌兰察布）、华南1（深圳）、中国香港、日本（东京）、新加坡、印度尼西亚（雅加达）、德国（法兰克福）、马来西亚（吉隆坡）地域对低频访问类型的数据采用多可用区的数据冗余存储机制。
低频访问-本地冗余
采用单可用区（AZ）内的数据冗余存储机制，将用户的数据冗余存储在同一个可用区内多个设施的多个设备上，确保硬件失效时的数据持久性和可用性。
重要
本地冗余存储类型的数据冗余在某个特定的可用区内。当该可用区不可用时，会导致相关数据不可访问。如您的业务需要更高的可用性保障，建议您使用同城冗余的存储类型来存储和使用数据。
## 归档存储（Archive）
提供高持久性、极低存储成本的对象存储服务。有最小计量单位（64 KB）和最低存储时间（60天）要求。归档存储数据支持解冻（约1分钟）后访问或直接访问。解冻后访问会产生归档存储数据取回容量费用，直接访问会产生归档直读数据取回容量费用。归档存储适用于数据长期保存的业务场景，例如档案数据、医疗影像、科学资料、影视素材等。归档存储支持同城冗余和本地冗余两种数据冗余存储方式。
说明
最小计量单位（64 KB）表示不足64 KB的文件也要按64 KB大小来计费。最低存储时间（60天）表示文件以归档类型存储时长不足60天将收取归档存储不足规定时长容量费用。更多信息，请参见[存储费用](../storage-fees.md)。
归档存储-同城冗余 （推荐）
采用多可用区（AZ）内的数据冗余存储机制，将用户的数据冗余存储在同一地域（Region）的多个可用区。当某个可用区不可用时，仍然能够保障数据的正常访问。
说明
华东1（杭州）、华东2（上海）、华北2（北京）、华北 3（张家口）、华北6（乌兰察布）、华南1（深圳）、中国香港、日本（东京）、新加坡、印度尼西亚（雅加达）、德国（法兰克福）、马来西亚（吉隆坡）地域对归档存储类型的数据采用多可用区的数据冗余存储机制。
归档存储-本地冗余
采用单可用区（AZ）内的数据冗余存储机制，将用户的数据冗余存储在同一个可用区内多个设施的多个设备上，确保硬件失效时的数据持久性和可用性。
重要
本地冗余存储类型的数据冗余在某个特定的可用区内。当该可用区不可用时，会导致相关数据不可访问。如您的业务需要更高的可用性保障，建议您使用同城冗余的存储类型来存储和使用数据。
## 冷归档存储（Cold Archive）
提供高持久性、比归档存储的存储成本更低的对象存储服务。有最小计量单位（64 KB）和最低存储时间（180天）的要求。数据需解冻后访问，解冻时间根据数据大小和选择的解冻模式决定，解冻会产生数据取回费用以及取回请求费用。适用于需要超长时间存放的冷数据，例如因合规要求需要长期留存的数据、大数据及人工智能领域长期积累的原始数据、影视行业长期留存的媒体资源、在线教育行业的归档视频等业务场景。冷归档仅支持本地冗余的数据冗余存储方式。
重要
本地冗余存储类型的数据冗余在某个特定的可用区内。当该可用区不可用时，会导致相关数据不可访问。如您的业务需要更高的可用性保障，建议您使用支持同城冗余的存储类型（标准存储、低频访问存储、归档存储）来存储和使用数据。
说明
华东1（杭州）、华东2（上海）、华北1（青岛）、华北2（北京）、华北 3（张家口）、华北5（呼和浩特）、华北6（乌兰察布）、华南1（深圳）、华南2（河源）、华南3（广州）、西南1（成都）、中国香港、美国（硅谷）、美国（弗吉尼亚）、墨西哥、日本（东京）、新加坡、马来西亚（吉隆坡）、印度尼西亚（雅加达）、菲律宾（马尼拉）、德国（法兰克福）、英国（伦敦）、阿联酋（迪拜）地域对冷归档存储类型的数据采用单可用区的数据冗余存储机制。
最小计量单位（64 KB）表示不足64 KB的文件也要按64 KB大小来计费。最低存储时间（180天）表示文件以冷归档类型存储时长不足180天将收取冷归档存储不足规定时长容量费用。更多信息，请参见[存储费用](../storage-fees.md)。
## 深度冷归档存储（Deep Cold Archive）
提供高持久性、比冷归档存储成本更低的对象存储服务。有最小计量单位（64 KB）和最低存储时间（180天）的要求。数据需解冻后访问，解冻时间根据数据大小和选择的解冻模式决定，解冻会产生数据取回费用以及取回请求费用。适用于需要超长时间存放的极冷数据，例如大数据及人工智能领域的原始数据的长期积累留存、媒体数据的长期保留、法规和合规性存档、磁带替换等业务场景。深度冷归档仅支持本地冗余的数据冗余存储方式。
重要
本地冗余存储类型的数据冗余在某个特定的可用区内。当该可用区不可用时，会导致相关数据不可访问。如您的业务需要更高的可用性保障，建议您使用支持同城冗余的存储类型（标准存储、低频访问存储、归档存储）来存储和使用数据。
说明
华东1（杭州）、华东2（上海）、华北2（北京）、华北 3（张家口）、华北6（乌兰察布）、华南1（深圳）、新加坡地域对深度冷归档存储类型的数据采用单可用区的数据冗余存储机制。
最小计量单位（64 KB）表示不足64 KB的文件也要按64 KB大小来计费。最低存储时间（180天）表示文件以深度冷归档类型存储时长不足180天将收取深度冷归档存储不足规定时长容量费用。更多信息，请参见[存储费用](../storage-fees.md)。
## 存储类型对比
| 存储类型 | Bucket 地域属性 | 存储冗余类型 | 数据持久性 | 服务可用性 | 最小计量单位 | 最低存储时间 | 数据访问特点 | 访问延迟 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 标准存储 | 有地域属性 | 同城冗余（2AZ） | 99.9999999999%（12 个 9） | 99.99% | 按照对象实际大小计算 | 无 | 单文件月访问大于 1 次 | 实时访问 |
| 标准存储 | 有地域属性 | 同城冗余（多 AZ） | 99.9999999999%（12 个 9） | 99.995% | 按照对象实际大小计算 | 无 | 单文件月访问大于 1 次 | 实时访问 |
| 低频访问存储 | 99.50% | 64 KB | 30 天 | 单文件月访问不到 1 次 | 实时访问 |  |  |  |
| 归档存储 | 99.50% | 64 KB | 60 天 | 单文件 90 天访问不到 1 次 | 既可以通过归档直读支持实时访问，也支持解冻后才能读取。 解冻时间 1 分钟 |  |  |  |
| 标准存储 | 有地域属性 | 本地冗余 | 99.999999999%（11 个 9） | 99.99% | 按照对象实际大小计算 | 无 | 单文件月访问大于 1 次 | 实时访问 |
| 低频访问存储 | 99.00% | 64 KB | 30 天 | 单文件月访问不到 1 次 | 实时访问 |  |  |  |
| 归档存储 | 99.00% | 64 KB | 60 天 | 单文件 90 天访问不到 1 次 | 既可以通过归档直读支持实时访问，也支持解冻后才能读取。 解冻时间 1 分钟 |  |  |  |
| 冷归档存储 | 99.00% | 64 KB | 180 天 | 单文件年访问不到 1 次 | 解冻后才能读取 解冻时间 1~12 小时 |  |  |  |
| 深度冷归档存储 | 99.00% | 64 KB | 180 天 | 单文件年访问不到 1 次 | 解冻后才能读取 解冻时间 12/48 小时 |  |  |  |
| 标准存储 | 无地域属性 | 99.00% | 按照对象实际大小计算 | 无 | 单文件月访问大于 1 次 | 实时访问 |  |  |
## 相关文档
默认情况下，上传到Bucket内Object的存储类型默认采用标准存储。标准存储适用于频繁访问、低延迟数据存取的场景。如果您识别到部分Object不再需要频繁访问，或者为了节省存储成本，您可以考虑将标准存储类型的Object转换为更为经济的存储类型，例如低频访问、归档类型等。具体操作，请参见[转换存储类型](convert-storage-classes.md)。
深度冷归档存储提供高持久性、低成本的存储服务，适用于需要超长时间存放的极冷数据。具体操作，请参见[深度冷归档存储使用最佳实践](deep-cold-archive-storage-usage-best-practices.md)。
如果您希望了解存储类型转换后，目标Object存储类型存储容量增加了，但是源Object存储类型容量没有减少的原因以及解决方法，请参见[为什么存储类型转换后，源](../why-does-the-storage-capacity-of-the-source-object-remain-unchanged-after-the-storage-type-conversion.md)[Object](../why-does-the-storage-capacity-of-the-source-object-remain-unchanged-after-the-storage-type-conversion.md)[存储类型容量保持不变？](../why-does-the-storage-capacity-of-the-source-object-remain-unchanged-after-the-storage-type-conversion.md)。
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
