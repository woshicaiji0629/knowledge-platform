# 重写回源请求URL中携带的参数-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/rewrite-url-parameters-in-back-to-origin-requests

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

# 重写回源参数

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

如果用户发起的原始请求URL中携带的参数与需要发送给源站的参数不一致，您可以通过回源参数重写功能重写回源请求URL中携带的参数。实现忽略所有参数、添加参数、删除参数、保留参数、修改参数等操作。

## URL参数组成

- 

URL参数是追加在URL上的一个或多个名称/值对，位于?后面，格式为name=value。多个参数之间用&隔开。

- 

有时URL中还会包含#及其后面的字符，#用于指引浏览器定位到网页中的特定位置。

例如：http://www.example.com/index.html#segment，这里的#segment代表网页index.html的segment位置，浏览器打开URL对应的页面之后，将会自动定位至该位置。

## 参数优先级

- 

回源参数重写，重写的是回源请求URL的查询参数，支持配置多个不同的重写操作，优先级为添加参数>删除参数>仅保留＞修改参数。当不同的重写操作用于同一个参数时，只有高优先级的规则会生效。

- 

开启忽略参数的情况下，在剩余的重写操作里面，仅添加参数还会生效。

## 冲突说明

重写回源参数与[重写回源路径](products/cdn/documents/user-guide/rewrite-urls-in-back-to-origin-requests.md)的enhance break规则和[忽略参数](products/cdn/documents/user-guide/ignore-parameters.md)功能可能会冲突；最后配置的功能生效。

## 对缓存key的影响

- 

重写回源参数功能是在CDN回源节点上完成，不影响CDN的内部链路，且不重写缓存key。

- 

[忽略参数](products/cdn/documents/user-guide/ignore-parameters.md)功能是在CDN边缘节点上完成，会影响CDN的内部链路，且会重写缓存key。

重要

功能配置在引用规则引擎上的规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。

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

单击重写回源参数页签。

- 

打开功能开关。

- 

配置需要重写的回源参数。

根据实际业务需求，按照界面提示配置不同的重写操作，您也可以在一种操作类型的文本框中添加多个参数。更多信息，请参见[配置示例](products/cdn/documents/user-guide/rewrite-url-parameters-in-back-to-origin-requests.md)。

- 

单击确定，重写操作开始执行和生效。

您也可以在重写回源参数页面，单击修改配置，修改已配置的规则。

## 配置示例

- 

配置示例一：忽略所有参数。

| 配置项 | 填写示例 |
| --- | --- |
| 忽略参数 | 开启 |
| 添加参数 | 无 |
| 删除参数 | 无 |
| 仅保留 | 无 |
| 修改参数 | 无 |
| 规则条件 | 不使用 |
| 结果说明 | 原始请求： http://example.com/index.html?code1=1&code2=2&code3=3 重写后的回源请求： http://example.com/index.html |


- 

配置示例二：保留指定参数。

| 配置项 | 填写示例 |
| --- | --- |
| 忽略参数 | 关闭 |
| 添加参数 | 无 |
| 删除参数 | 无 |
| 仅保留 | code2 |
| 修改参数 | 无 |
| 规则条件 | 不使用 |
| 结果说明 | 原始请求： http://example.com/index.html?code1=1&code2=2&code3=3 重写后的回源请求： http://example.com/index.html?code2=2 |


- 

配置示例三：添加参数+删除参数+修改参数。

| 配置项 | 填写示例 |
| --- | --- |
| 忽略参数 | 关闭 |
| 添加参数 | code4=4 |
| 删除参数 | code2 |
| 仅保留 | 无 |
| 修改参数 | code3=0 |
| 规则条件 | 不使用 |
| 结果说明 | 原始请求： http://example.com/index.html?code1=1&code2=2&code3=3 重写后的回源请求： http://example.com/index.html?code1=1&code3=0&code4=4 |


## 相关文档

[批量配置域名](products/cdn/documents/api-batchsetcdndomainconfig.md)

[上一篇：修改出站请求头](products/cdn/documents/user-guide/configure-custom-request-headers.md)[下一篇：其他回源配置](products/cdn/documents/user-guide/other-origin-fetch-configurations.md)

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
