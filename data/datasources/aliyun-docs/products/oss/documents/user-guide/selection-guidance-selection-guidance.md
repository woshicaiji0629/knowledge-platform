# OSS选型指导-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/selection-guidance-selection-guidance

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

# OSS选型指导

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云对象存储服务（OSS）支持存储所有类型的数据，如图片、音频、视频、文档、软件包、CSV、JSON、Parquet、备份文件等。在OSS中，每个对象（Object）都有特定的存储类型。默认情况下，Object使用标准存储，但OSS还提供低频访问、归档存储、冷归档存储、深度冷归档存储等存储类型。

## 选型因素

在选择存储类型时，您需要考虑以下因素：

- 

访问频率：从OSS读取和写入数据的频繁程度。不同的业务可能对访问频率有不同的要求，从经常访问到非常少访问。

- 

取回时间：从OSS读取数据所需的时间。不同的业务可能对取回时间有不同的要求，从实时访问，到接受几小时或几天取回。

- 

可用性：OSS服务在特定时间内可正常使用的概率。不同的业务可能对可用性有不同的要求，从99.00%到99.995%。

- 

可靠性：在一定时间内OSS数据存储的安全性和完整性。不同的业务可能对可靠性有不同的要求，从11个9到12个9。

## 选型参考

根据业务对数据的访问频率、取回时间、可用性、可靠性等要求，选择合适的存储类型：

| 存储类型 | 访问频率 | 取回时间 | 可用性 | 可靠性 |
| --- | --- | --- | --- | --- |
| 标准存储-同城冗余 | 经常访问 | 实时访问 | 99.995% | 99.9999999999%（12 个 9） |
| 标准存储-本地冗余 | 经常访问 | 实时访问 | 99.99% | 99.999999999%（11 个 9） |
| 低频访问-同城冗余 | 不经常访问 | 实时访问 | 99.50% | 99.9999999999%（12 个 9） |
| 低频访问-本地冗余 | 不经常访问 | 实时访问 | 99.00% | 99.999999999%（11 个 9） |
| 归档存储-同城冗余 | 非常少访问 | 实时访问或 1 分钟 | 99.50% | 99.9999999999%（12 个 9） |
| 归档存储-本地冗余 | 非常少访问 | 实时访问或 1 分钟 | 99.00% | 99.999999999%（11 个 9） |
| 冷归档存储-本地冗余 | 几乎不访问 | 1~12 小时 | 99.00% | 99.999999999%（11 个 9） |
| 深度冷归档存储-本地冗余 | 几乎不访问 | 12 小时或 48 小时 | 99.00% | 99.999999999%（11 个 9） |


关于不同存储类型的具体价格，请参见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)。

[上一篇：功能特性](products/oss/documents/user-guide/product-function-node-oss.md)[下一篇：快速入门](products/oss/documents/user-guide/get-started-with-oss.md)

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
