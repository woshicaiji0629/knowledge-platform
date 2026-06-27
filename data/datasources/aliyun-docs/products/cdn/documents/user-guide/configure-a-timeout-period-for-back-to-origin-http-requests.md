# 如何配置回源HTTP请求超时时间及注意事项-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-a-timeout-period-for-back-to-origin-http-requests

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/cdn/documents/product-overview.md)

- [快速入门](products/cdn/documents/getting-started.md)

- [操作指南](products/cdn/documents/user-guide.md)

- [实践教程](products/cdn/documents/use-cases.md)

- [安全合规](products/cdn/documents/security-and-compliance.md)

- [开发参考](products/cdn/documents/developer-reference.md)

- [服务支持](products/cdn/documents/support.md)

- [视频专区](products/cdn/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 配置回源HTTP请求超时时间

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

通过配置回源HTTP请求超时时间，可以控制回源HTTP请求的超时时间。如果回源HTTP请求超时时间设置的较短，可能会因为网络波动而频繁出现回源失败；如果回源HTTP请求超时时间设置的过长，也可能会在源站处理能力达到上限、响应失败的情况下，失败请求仍然会长时间占用连接数，导致正常请求无法访问。建议您根据网络链路情况以及源站数据处理能力，合理设置回源HTTP请求超时时间，保障请求能够正常回源。

## 背景信息

回源HTTP请求时间指的是，CDN回源时，七层HTTP请求时间，不包括回源建连时间（即四层TCP连接时间）。

## 注意事项

阿里云CDN当前可以设置的全链路（包括CDN节点内部链路以及CDN节点到源站之间的链路）超时时间最长不能超过150秒，默认为30秒，建议配置不超过60秒。

## 回源重试、回源超时、源站探测相关说明

- 

回源重试顺序：

- 

对域名基础信息的源站地址列表内的源站地址按优先级从高到低进行重试。

- 

如果有优先级相同的源站地址，则按权重比例进行重试。

- 

回源重试的颗粒度：

- 

重试是IP地址级别的，如果源站是域名，将会对域名解析出的所有IP地址进行重试，只有域名下的所有IP都连接失败后才会访问其他可用源站。

- 

重试时系统会自动过滤dead table中不可用的源站。

- 

回源重试状态码：

- 

CDN节点在收到源站响应的5xx状态码的时候进行重试。

- 

回源超时时间：在源站主动响应重试状态码时，CDN节点收到重试状态码之后就会重试。如果没有收到源站主动响应的重试状态码，则会遵循回源超时时间处理逻辑，达到超时时间之后就会触发CDN节点重试。

- 

源站TCP建连超时：10秒。

- 

源站写超时：默认为30秒（源站建连后写入内容超时）。

- 

源站读超时：默认为30秒（源站建连后在一定时间内没有把CDN节点请求的内容完整响应回去）。

- 

源站写超时时间和源站读超时时间可以通过配置回源HTTP请求超时时间来调整。

- 

源站探测逻辑：

- 

TCP连接异常：如果CDN节点与源站IP地址之间连续两次出现TCP连接不可用（建连失败或连接超时），CDN会从可用源站地址列表中剔除该源站IP地址，并将该IP地址加入dead table中，这样后续的回源请求就不会去访问这个源站IP地址；此后CDN节点会每隔5秒使用TCP建连去探测一次该源站IP地址，如果建连成功，则将该源站IP地址恢复到可用源站地址列表中。

- 

TCP连接正常：如果CDN节点与源站IP地址之间TCP连接正常，但收到源站响应的重试状态码（例如：5xx），此时虽然会触发重试的逻辑，但该源站IP地址仍然还在可用源站地址列表中，下次访问还会按权重去请求该源站（即TCP四层连接正常的情况下，七层HTTP请求异常不会主动屏蔽源站IP地址，如果需要在七层HTTP请求异常的情况下主动屏蔽源站IP地址，则需要提交工单申请配置）。

## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击回源配置。

- 

在回源HTTP请求超时时间区域，单击修改配置。

- 

在回源HTTP请求超时时间对话框，设置超时时间。

默认超时时间为36秒，建议配置不超过60秒，超过150秒将不会生效。设置完成后单击确定。

- 

单击确定完成配置。

## 相关文档

- 

[批量配置域名](products/cdn/documents/api-batchsetcdndomainconfig.md)

[上一篇：其他回源配置](products/cdn/documents/user-guide/other-origin-fetch-configurations.md)[下一篇：配置回源301/302跟随](products/cdn/documents/user-guide/configure-301-or-302-redirection.md)

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
