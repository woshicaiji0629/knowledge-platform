# 配置CDN的用量封顶-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-usage-cap

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

# 配置用量封顶

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

为防止域名被攻击或盗刷产生突发高带宽，导致产生高额账单，可通过配置用量封顶，控制用户访问该域名的带宽、流量、HTTPS请求数上限值，减少因突发流量导致的损失。

## 背景信息

在使用CDN加速业务时，您可能会遇到以下场景：

- 

业务流量突增：由于社会热点事件等原因，您的网站或应用访问量在短时间内激增，导致CDN带宽或流量远超日常用量，产生高额费用。

- 

恶意流量攻击：您的业务遭受CC攻击或DDoS攻击，攻击者在短时间内产生海量请求或消耗巨大带宽，不仅影响正常业务，还会造成严重的经济损失。

为了帮助您主动控制成本、规避风险，阿里云CDN提供了用量封顶功能。您可以为加速域名设置带宽、流量或HTTPS请求数的阈值。当在一个统计周期内，实际用量达到您设定的阈值时，CDN将自动下线该域名，暂停加速服务，从而阻止费用进一步攀升。该功能是您进行CDN成本管理和安全防护的重要工具。

## 功能介绍

用量封顶功能包含带宽封顶、流量封顶和HTTPS请求数封顶三种模式。当任一规则被触发后，对应的加速域名将被自动下线，直到预设的解封时间到达后自动恢复服务。

### 流量封顶

用于累计统计域名在指定周期内产生的总流量。当累计流量超过您设定的阈值时，将触发封顶规则。此功能特别适用于按流量计费的用户，能帮助您将总费用控制在预算范围内。

| 参数名 | 参数介绍 |
| --- | --- |
| 统计周期 | 流量用量的累计统计周期。系统会在此周期内对流量进行累计，并与阈值进行比较。可选值：每 5 分钟、每小时、当天 24 点前、当月。 |
| 阈值 | 在一个统计周期内，允许消耗的总流量上限。当累计流量超过该阈值时，则下线加速域名。支持范围：1 MB ~ 10000 TB。 |
| 解封时间 | 域名被下线后，系统将从触发时刻开始计时。到达您设定的解封时间后，域名将被自动重新上线，恢复 CDN 加速服务。 |


### 带宽封顶

用于监控域名的带宽使用情况。当域名带宽超过您设定的阈值时，将触发封顶规则。此功能特别适用于按带宽峰值计费的用户，能有效控制计费带宽的上限。

| 参数名 | 参数介绍 |
| --- | --- |
| 阈值 | 域名带宽的上限值。当统计周期内的带宽超过该阈值时，则下线加速域名。支持范围：1 Mbps ~ 1 Tbps。 |
| 解封时间 | 域名被下线后，系统将从触发时刻开始计时。到达您设定的解封时间后，域名将被自动重新上线，恢复 CDN 加速服务。可选值：5 分钟、1 小时、1 天、1 月、永不解封。 |


### HTTPS请求数封顶

用于累计统计域名在指定周期内产生的HTTPS请求总数。当累计请求数超过您设定的阈值时，将触发封顶规则。此功能适用于对HTTPS请求量有明确预算控制的业务场景。

| 参数名 | 参数介绍 |
| --- | --- |
| 统计周期 | HTTPS 请求数的累计统计周期。系统会在此周期内对请求数进行累计，并与阈值进行比较。可选值：每 5 分钟、每小时、当天 24 点前、当月。 |
| 阈值 | 在一个统计周期内，允许产生的 HTTPS 请求总数上限。当累计请求数超过该阈值时，则下线加速域名。支持范围：1 百万次 ~ 100 亿次。 |
| 解封时间 | 域名被下线后，系统将从触发时刻开始计时。到达您设定的解封时间后，域名将被自动重新上线，恢复 CDN 加速服务。 |


## 注意事项

- 

数据监控延迟：用量监控数据存在约10分钟的延迟。因此，当实际用量达到阈值后，系统大约需要10分钟才会执行域名下线操作。在此延迟期间产生的资源消耗（流量、带宽、请求数等）将会正常计费。

- 

谨慎评估阈值：配置用量封顶后，一旦达到阈值，您的域名将被下线，导致通过CDN的访问中断，所有请求都将无法访问。请您务必基于历史业务数据和未来预期合理评估阈值，以免对正常业务产生影响。

- 

自动解封逻辑：域名触发封顶被下线后，系统将根据您配置的解封时间自动开始倒计时。在此期间，即使您手动上线域名，到达解封时间后，系统仍会执行一次上线操作。如果您希望域名在封顶后保持下线状态，可以通过删除该用量封顶配置的方式，来阻止系统在解封时间到达时自动上线域名。

- 

配置删除与开关关闭的区别：用量封顶功能存在配置记录即可能生效，仅关闭用量封顶功能的开关无法立即停止策略生效。若您希望彻底取消用量限制并防止域名因历史配置被自动下线，必须进入用量封顶配置页面删除对应的用量封顶配置，而非仅关闭开关。

## 操作步骤

- 

在[域名管理](https://cdn.console.aliyun.com/domain/list)页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击流量限制。

- 

在用量封顶页签中，选择想要配置的封顶策略。

- 

点击修改配置，可以根据自身业务选择合适的统计周期、阈值和解封时间。具体参数配置请参考[功能介绍](products/cdn/documents/user-guide/configure-usage-cap.md)。

- 

单击确定，封顶规则即可创建成功并生效。

如需删除已有的封顶配置，在用量封顶页签中找到对应的封顶策略（流量封顶、带宽封顶或HTTPS请求数封顶），单击删除配置。在弹出的确认对话框中单击确认删除，即可删除该封顶配置。删除后，系统将不再对该项用量进行限制。

重要

删除对应的封顶配置记录以保证用量限制彻底取消。

### 域名触发封顶下线后的表现与恢复

当域名触发用量封顶被自动下线后，您将观察到以下表现：

- 

DNS 解析可能指向无效地址（如offline.*.kunlun*.com）或返回614状态码，导致网站无法正常访问。

- 

在 CDN 控制台域名列表中，该域名的状态将显示为已停止。

恢复方式有两种：

- 

等待自动恢复：系统将按照您配置的解封时间自动倒计时，到达解封时间后域名将自动重新上线。

- 

手动启用：若您希望提前恢复访问，可在 CDN 控制台找到对应域名，手动点击操作列中的启用按钮，将域名重新上线。

说明

若您希望域名在触发封顶后保持下线状态、不被自动解封上线，请删除该用量封顶配置。

## 常见问题

### 为什么域名下线前实际带宽会大于带宽封顶阈值？

由于域名带宽的监控数据存在一定延迟（大约10分钟），实际带宽达到阈值大约10分钟后，域名才会被下线，域名下线前产生的流量、带宽、请求数等资源消耗将会正常计费。具体举例说明如下：

- 

示例1（按带宽峰值计费模式）：

客户A使用“按带宽峰值计费”，只添加了域名example.com，并开启了带宽封顶功能，带宽上限设为10 Gbps。

在2021年02月01日21:00~21:01期间，带宽突增至10 Gbps，由于监控数据有一定的延迟，域名在2021年02月01日21:11左右才被执行下线，下线前带宽峰值达到了25 Gbps。因此，在系统生成的2021年02月01日“按带宽峰值计费”账单中会按照25 Gbps的带宽用量来计算账单金额。

- 

示例2（按流量计费）：

客户B使用“按流量计费”，只添加了域名example.com，为该域名开启了带宽封顶功能，设置的带宽上限为10 Gbps。

在2021年02月01日21:00~21:01带宽突增至10 Gbps，消耗流量30 GB。由于监控数据有一定的延迟，域名在2021年02月01日21:11左右才会被执行下线，数据延迟过程中消耗流量400 GB，域名example.com在下线之前产生的所有流量都会被计算到2021年02月01日21:00~22:00这个时间段的“按流量计费”账单中。

### 为什么删除或关闭用量封顶配置后，域名仍然处于下线状态或自动停用？

如果您发现删除或关闭用量封顶配置后域名仍然处于下线状态，请检查以下原因：

- 

旧版带宽封顶规则冲突：您的域名可能同时配置了旧版带宽封顶规则（云监控中的报警规则）。旧版规则触发后同样会下线域名，且旧版规则不支持直接修改，只能删除。请前往云监控控制台检查并删除旧版带宽封顶规则，仅保留新版用量封顶配置。

- 

用量封顶配置未彻底删除：请确认已将用量封顶配置删除。

- 

域名需手动启用：域名下线后，您需要手动在 CDN 控制台点击启用，或等待配置的解封时间到达后才能恢复访问。

### CDN是否支持对指定IP限速？

不支持。CDN用量封顶是针对整个域名的总用量进行限制，无法将流量或带宽限制细化到单个 IP 上。如需基于客户端 IP 进行限速，建议使用[边缘安全加速的 WAF 频次控制](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/waf-overview/)。

### CDN是否支持设置单个IP的流量限制或针对指定IP限速？

不支持。CDN用量封顶是针对整个域名的总用量（带宽、流量、HTTPS请求数）进行限制，无法细化到单个IP。如果您需要基于客户端IP进行频次控制或拦截，建议使用[边缘安全加速的 WAF 频次控制](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/waf-overview/)，当客户端IP超过设定的频次阈值时会被 403 拦截。

### 为什么域名频繁自动下线或突然无法访问？

当您的 CDN 域名频繁自动下线或突然无法访问时，请按以下步骤排查：

- 

检查用量封顶配置：登录 CDN 控制台，进入域名管理，找到目标域名后在流量限制>用量封顶页面查看是否配置了带宽/流量/HTTPS请求数封顶策略，以及是否已触发阈值。同时查看操作记录确认是否有封顶触发记录。

- 

检查旧版带宽封顶规则：确认是否存在旧版带宽封顶规则（云监控报警规则）与新版用量封顶策略冲突。

- 

排查异常流量：若确认为异常流量攻击，建议通过控制台查看离线日志或开启运营报表，分析 Top IP 和 Top Referer 来源。若确认为异常 IP，可配置 IP 黑白名单；若为空 Referer 恶意刷量，可配置 Referer 防盗链。如需更高级防护，建议考虑升级至 ESA 。

### CDN资源包用完后，能否配置自动停止服务以避免产生按量付费账单？

CDN 不支持直接配置“资源包用完即停”。当您的 CDN 资源包用完后，系统会自动转为按量付费模式，无法直接关闭按量付费。

为避免资源包耗尽后产生高额按量付费账单，建议您采取以下措施：

- 

配置用量封顶：设置合理的带宽或流量阈值。当用量达到阈值时，域名会自动下线，从而阻断后续费用产生。

- 

设置资源包预警：建议设置资源包剩余量预警（如剩余 10 GB 时），以便及时手动干预。请注意流量包预警可能存在延迟，收到预警时可能已产生超额费用。

### 如何合理设置用量封顶阈值？

用量封顶没有通用的默认阈值，需要结合您的业务实际规模来评估。不同用户量级产生的流量差异巨大，建议您按照以下步骤确定合理的阈值：

- 

登录CDN 控制台，在左侧导航栏选择用量查询，查看近 7 天的实际用量数据。

- 

参考历史峰值数据，在峰值基础上预留一定余量来设定阈值，避免因阈值设置过低导致正常业务被误封停。

- 

阈值的参考范围因业务类型而异：

- 

中小型网站：每小时流量通常在几 GB 到几十 GB。

- 

视频、下载类大流量业务：可能达到 TB 级别。

重要

阈值设置过低会导致正常业务流量触发封顶，域名被下线后所有用户将无法访问。请务必基于实际业务数据合理评估。

### 如何查看域名被封顶下线的时间和记录？

您可以通过以下方式查看域名因用量封顶被下线的记录：

- 

登录CDN控制台，进入域名管理，找到目标域名，进入域名详情的流量限制页面，查看各封顶策略的当前配置和状态。

- 

如需查看详细的操作记录（包括域名停用的具体时间和触发原因），建议前往操作审计控制台查询 CDN 相关的操作事件。

### CDN用量封顶功能是否收费？触发后有什么影响？

用量封顶功能（包括带宽封顶、流量封顶、HTTPS请求数封顶）本身不收取额外费用。

当域名在统计周期内的用量超过您设定的阈值时，CDN 将停止为该域名提供加速服务，域名进入下线（offline）状态。此时该域名的所有访问请求（包括正常流量和异常流量）均无法通过 CDN 访问，网站将无法打开。这种机制通过主动暂停服务来避免产生高额流量或带宽费用。

域名下线后，将按照您配置的解封时间自动恢复服务。如需提前恢复，可在 CDN 控制台的域名管理页面手动启用域名。

[上一篇：流量限制](products/cdn/documents/user-guide/traffic-throttling.md)[下一篇：配置单请求限速](products/cdn/documents/user-guide/configuration-order-request-speed-limit.md)

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
