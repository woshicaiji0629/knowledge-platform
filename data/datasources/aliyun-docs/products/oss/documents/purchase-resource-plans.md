# 购买OSS资源包-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/purchase-resource-plans

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

# 购买OSS资源包

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在资源使用量稳定的情况下，建议购买资源包，以更低的成本使用OSS。例如，预计未来3个月内，标准存储（同城冗余）容量约为100 GB，建议购买100 GB、时长为3个月的标准-同城冗余存储包。

## 步骤一：确定要购买的资源包

### 计费项检测工具

借助[计费项检测工具](https://oss.console.aliyun.com/package-recommend-tool)了解当前OSS产生的存储、请求、流量及传输加速等资源的使用情况。根据系统建议，购买资源包。

例如，当前账号下共有 2 个地域产生了标准存储（同城冗余）计费项，产生费用的原因为该计费项的未购买符合抵扣条件的资源包，查看地域详情显示华东1（杭州）地域最近 3 天的标准存储（同城冗余）用量约 1.82 GB，可根据提示购买标准-同城冗余（ZRS）存储包。

### 根据账单分析

您也可直接根据[账单](https://billing-cost.console.aliyun.com/finance/expense-report/expense-detail-by-instance?BillingCycle=2025-08&StatisticItem=DEFAULT_CHARGE_ITEM&StatisticCycle=MONTHLY)中的计费项和用量选择合适的资源包类型和规格。

- 

计费项匹配：如果账单中显示标准存储（同城冗余）容量为主要费用来源，可以选择购买标准-同城冗余存储包抵扣该费用。

- 

用量匹配：如果账单显示每小时的存储容量为40 GB，则可以购买40 GB的标准-同城冗余存储包以精准覆盖实际用量。

## 步骤二：购买资源包

### 购买单个资源包

根据检测的计费项或账单中分析出的计费项购买对应的资源包。

- 

登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。

- 

在左侧导航栏，选择资源用量>资源包管理。

- 

在资源包管理页面，单击购买资源包。

- 

根据您的实际情况选择资源包类型、地域、规格、时长等参数，然后单击立即购买。

重要

- 

资源包购买后，不支持切换资源包类型。一种类型的资源包只能抵扣使用该资源包对应计费项产生的费用，不能抵扣所有费用。购买时，请选择合适的[资源包类型](products/oss/documents/resource-plan.md)。

- 

资源包购买后，立即生效，无需手动建立连接即可通过对应资源包自动抵扣关联计费项。

- 

按照页面指引，完成购买流程。

### 购买数据处理与分发组合资源包

对于图片、视频转码、格式转换及内容分发等业景，可以购买[数据分发和处理组合资源包](https://common-buy.aliyun.com/package?spm=5176.29458312.J_IAo1LV8Q2O3jy2JXGN8Oo.2.41cf15c73AyCCs&planCode=package_ossimm_cn&accounttraceid=8fb4109b000a450abdb7cab8f7be2579jydr)，可用于抵扣对象存储 OSS 和智能媒体管理（IMM）的计费项。

## 选购示例

陈先生2022年3月购买了500 GB的中国内地通用标准-本地冗余存储包和100 GB的中国内地通用下行流量包，其3月份的资源使用量为：

- 

华东1（杭州）地域当月标准存储（本地冗余）类型文件存储量为300 GB、外网流出流量110 GB、API请求次数10万次。

- 

华东2（上海）地域当月标准存储（本地冗余）类型文件存储量为100 GB、标准存储（同城冗余）类型文件存储量为200 GB。

计费说明如下：

| 地域 | 资源包抵扣 | 按量付费 |
| --- | --- | --- |
| 华东 1（杭州） | 使用 500 GB 的 标准-本地冗余存储包 抵扣 300 GB 标准存储（本地冗余）容量费用。 | 10 万次 API 请求费用。 |
| 使用 100 GB 下行流量包抵扣其中 100 GB 外网流出流量费用。 | 剩余 10 GB 外网流出流量费用。 |  |
| 华东 2（上海） | 使用 500 GB 的 标准-本地冗余存储包 抵扣 100 GB 标准存储（本地冗余）容量费用。 | 200 GB 标准存储（同城冗余）容量费用。 |


## 常见问题

### 买错了资源包怎么办？

如果购买的资源包不符合预期，请根据购买资源包的天数以及是否使用的情况，选用恰当的解决方案。

- 

适用于新购5天内未使用的OSS资源包。

申请全额退订。退订完成后，重新购买正确的资源包。

- 

适用于5天内已使用，超过5天未使用的OSS资源包。

需要根据购买的资源包的抵扣方式，选择恰当的解决方法。

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

- 

| 资源包抵扣方式 | 购买的资源包 | 解决方法 | 说明 |
| --- | --- | --- | --- |
| 总量恒定型 | 标准-本地冗余存储包 低频-本地冗余存储包 | 申请非全额退订。 | 退款金额=订单实付金额 -（订单原价/订单实际购买天数）*已使用天数 |
| 如果不希望采用非全额退订的方式，可以将 Bucket 冗余类型从本地冗余转换为同城冗余，以便直接使用同城冗余存储包抵扣对应的存储量。 | 转换完成后，Bucket 不再按照本地冗余存储的价格收费，而是按照同城冗余存储的价格收费，同城冗余存储的价格高于本地冗余存储的价格。具体价格，请参见 [OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss) [产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss) 。 |  |  |
| 归档-本地冗余存储包 冷归档-本地冗余存储包 标准-同城冗余存储包 低频-同城冗余存储包 高防基础包 OSS 加速器包 | 申请非全额退订。 | 退款金额=订单实付金额 -（订单原价/订单实际购买天数）*已使用天数 |  |
| 总量递减型 | 传输加速包 回源流量包 请求包-标准存储 请求包-非标准存储 | 申请非全额退订。 | 退款金额=订单实付金额 -（订单原价/订单实际购买天数）*已使用天数 |
| 包月周期型 | 下行流量包 | 不支持退订 | 不支持退订 |


关于全额退订或者非全额退订的具体操作，请参见[资源包退款指南](products/oss/documents/refund-resource-plans.md)。

### 资源包购买页没有我要购买的资源包规格怎么办？

OSS资源包购买页通常只提供100 GB、500 GB、1 TB、10 TB等规格的资源包。对于没有符合预期规格（例如9 TB）的资源包，您需要根据资源包是否支持叠加操作，选择非整数倍规格资源包的购买方法。

- 

资源包支持叠加

对于支持叠加的资源包（例如下行流量包），您可以通过叠加的方式购买9 TB的资源包。例如，您可以分别购买5 TB、2 TB、2 TB的下行流量包。

- 

资源包不支持叠加

对于不支持叠加的资源包（例如标准-本地冗余存储包），您可以通过以下两种方式购买资源包：

- 

直接购买10 TB的标准-本地冗余存储包。

- 

购买5 TB的标准-本地冗余存储包。对于超出部分，采用按量付费。

关于资源包是否支持叠加操作的更多信息，请参见[资源包支持的操作](products/oss/documents/resource-plan.md)。

[上一篇：资源包](products/oss/documents/resource-plan.md)[下一篇：资源包换购指南](products/oss/documents/resource-pack-exchange-guide.md)

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
