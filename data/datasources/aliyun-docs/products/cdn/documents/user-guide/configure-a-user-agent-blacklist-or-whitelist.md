# 配置User-Agent黑白名单实现访问控制-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-a-user-agent-blacklist-or-whitelist

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

# 配置UA黑白名单

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

User-Agent是HTTP请求头的一部分，包含用户访问时所使用的操作系统及版本、浏览器类型及版本等标识信息。您可以通过配置User-Agent黑白名单规则，限制访问CDN资源的用户，提升CDN的安全性。

## 注意事项

- 

User-Agent黑名单与User-Agent白名单二选一，不可同时配置。

- 

如果用户请求中携带的User-Agent字段的值命中了User-Agent黑名单中的值，则带有该UserAgent值的请求仍可访问到CDN节点，但是会被CDN节点拒绝并返回403状态码，并且CDN日志中仍会记录该请求记录。

- 

配置User-Agent黑白名单规则，限制访问CDN资源的用户，提升CDN的安全性，因此在恶意请求被CDN节点拦截的同时，会产生少量的流量费用，如果客户端使用HTTPS协议访问，还会产生HTTPS请求数费用（因为拦截恶意请求的时候，也同时消耗了CDN节点的处理资源）。

## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击访问控制。

- 

单击UA黑/白名单页签。

- 

在UA黑/白名单页签下，单击修改配置。

- 

根据界面提示，配置User-Agent的黑名单或白名单。

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 类型 | User-Agent 名单类型如下： 黑名单 HTTP 请求头中的 User-Agent 字段命中黑名单的情况下，用户将无法访问所请求的资源，并返回 403 状态码。 白名单 只有 HTTP 请求头中的 User-Agent 字段命中白名单的情况下，用户才能访问加速域名下的资源。 |
| 规则 | 配置 User-Agent 字段时，用竖线（|）分割多个值，支持通配符号（*）。例如： *curl*|*IE*|*chrome*|*firefox* 。 UA 黑白名单规则采用全值匹配模式，不支持子串匹配。例如，直接填写 curl/7.68.0 只会匹配 User-Agent 值恰好等于 curl/7.68.0 的请求，不会匹配包含该字符串的其他 User-Agent 值。如果您需要匹配 User-Agent 中包含某个关键字的所有请求，请使用通配符（*）包裹该关键字，例如填写 *7.68.0* 或 *curl* 。 说明 如果您需要对用户请求中携带了 User-Agent 请求头，但是值为空的情况做访问控制，您可以使用参数 this-is-empty-ua 来表示 User-Agent 值为空。 白名单下：规则中包含 this-is-empty-ua ，表示如果用户请求中携带了 User-Agent 请求头，但是值为空，则允许该请求。 黑名单下：规则中包含 this-is-empty-ua ，表示如果用户请求中携带了 User-Agent 请求头，但是值为空，则拒绝该请求。 如果您需要对用户请求中不携带 User-Agent 请求头的情况做访问控制，目前 UA 黑白名单功能暂不支持。您可以通过边缘脚本功能来实现，具体请参见 [边缘脚本](products/cdn/documents/user-guide/edgescript-overview.md) ；或者 [填写信息](https://page.aliyun.com/form/act2017566026/index.htm) 申请后台配置。 |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |


- 

单击确定，完成配置。

## 配置示例

- 

示例一：白名单

规则：*IE*|*firefox*

结果说明：只有当请求来源于IE或者火狐浏览器时，才可以访问所请求的资源，其余请求均不可访问。

- 

示例二：黑名单

规则：*IE*|this-is-empty-ua

结果说明：当请求来源于IE浏览器或者请求头中携带的User-Agent字段值为空时，均不可访问所请求的资源。

- 

示例三：黑名单（通配符匹配）

错误规则：curl/7.68.0

正确规则：*curl/7.68.0*或*7.68.0*

结果说明：直接填写curl/7.68.0无法拦截User-Agent中包含该字符串的请求，因为UA黑白名单规则采用全值匹配，不支持子串匹配。需使用通配符（*）包裹关键字实现模糊匹配。

[上一篇：其他安全访问控制](products/cdn/documents/user-guide/other-security-access-control.md)[下一篇：URL鉴权配置](products/cdn/documents/user-guide/url-signing.md)

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
