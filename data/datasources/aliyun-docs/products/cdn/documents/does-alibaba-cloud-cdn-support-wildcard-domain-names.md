# 阿里巴巴云CDN支持泛域名加速-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/does-alibaba-cloud-cdn-support-wildcard-domain-names

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

# CDN支持泛域名加速吗？

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

CDN支持泛域名加速。您可以通过本文了解泛域名加速的概念和配置泛域名加速的操作步骤。

## 什么是泛域名加速？

泛域名加速是指使用通配符做加速域名以实现所有的次级域名的加速效果。例如.aliyundoc.com是一个泛域名，example.aliyundoc.com是这个泛域名对应的次级域名，image.developer.aliyundoc.com是这个泛域名对应的三级域名。

示例：您添加.aliyundoc.com泛域名作为加速域名。当您将.aliyundoc.com泛域名解析至CDN生成的CNAME域名时，所有此泛域名的次级域名（例如example.aliyundoc.com、demo.aliyundoc.com等）均可以解析到CDN上添加的泛域名.aliyundoc.com的CNAME加速。

重要

- 

CDN泛域名加速不支持次级域名再往下级域名的加速，例如泛域名.aliyundoc.com的次级域名example.aliyundoc.com在CDN上面可以正常加速，而三级域名image.developer.aliyundoc.com将无法通过CDN平台实现加速，如果三级域名image.developer.aliyundoc.com的请求访问到CDN节点上，CDN节点将会拒绝该请求，并响应403状态码。

- 

对于类似“.com.cn、.net.cn、.gov.cn、.edu.cn、.org.cn”这样的域名后缀（全量域名后缀参考官方链接[https://publicsuffix.org/list/public_suffix_list.dat](https://publicsuffix.org/list/public_suffix_list.dat)），CDN平台将会识别为顶级域名，即.aliyundoc.com.cn是一个泛域名，example.aliyundoc.com.cn是这个泛域名对应的次级域名，image.developer.aliyundoc.com.cn是这个泛域名对应的三级域名。

- 

刷新或预热缓存时不支持泛域名URL或泛域名文件目录，但支持刷新或预热精确域名（包含次级域名）的URL和目录。例如不支持http://.aliyundoc.com/example/b.mp4的刷新或预热，支持http://example.aliyundoc.com/example/b.mp4的刷新或预热。

## 泛域名CNAME回源与匹配规则

CDN泛域名加速场景下，域名不要求必须CNAME到控制台分配的指定CNAME地址才能回源。只要域名通过CNAME解析指向CDN，且CDN后端已配置对应的源站，即可正常回源。

泛域名会自动匹配符合规则的次级域名请求。当同一域名同时存在精确域名配置和泛域名配置时，精确域名的配置规则优先于泛域名规则。例如，如果您同时配置了泛域名*.aliyundoc.com和精确域名example.aliyundoc.com，则访问example.aliyundoc.com时将优先匹配精确域名的配置。

## 泛域名添加规则

泛域名添加规则如下：

- 

域名（例如：image.example.com）总长度不超过100字符。

- 

域名去掉根域名之后的子域名部分（例如：域名image.example.com去掉根域名example.com之后的子域名是image）的长度不超过64字符。

- 

泛域名添加支持两种格式：.aliyundoc.com和*.aliyundoc.com，两种添加方式效果相同，添加之后控制台上显示都是.aliyundoc.com。

- 

CDN支持多级泛域名，例如：*.example.aliyundoc.com、*.image.example.aliyundoc.com、*.cat.image.example.aliyundoc.com等。

- 

泛域名的所有次级域名的流量都会和普通域名一样产生费用，资源监控中会将泛域名产生的流量做汇总，单个泛域名加速将按照一个加速域名计费，即不提供单个准确次域名的计费数据。

## 泛域名日志

每个时段将为单个泛域名的提供一份日志文件，日志中将包含该泛域名的所有次级加速域名的日志信息。查询日志信息请参见[日志管理](products/cdn/documents/user-guide/overview.md)。

## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

将泛域名作为加速域名，详细操作请参见[添加加速域名](products/cdn/documents/add-a-domain-name.md)。

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
