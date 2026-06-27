# 实时日志功能介绍-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 投递CDN实时日志到SLS来分析用户访问数据

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何使用实时日志功能对用户访问日志进行分析。

## 概述

阿里云CDN产品的实时日志功能是CDN产品与SLS产品联合推出的一项功能，是一种时效性非常高（延迟在3分钟左右）的日志数据处理服务，能够将CDN节点上采集到的用户访问日志实时推送至[SLS](https://help.aliyun.com/product/28958.html)[日志服务](https://help.aliyun.com/product/28958.html)，然后可以通过SLS来存储和分析用户访问数据。在使用阿里云CDN产品来加速网站域名访问速度的情况下，用户访问网站的图片、视频等资源时，CDN会记录用户的访问日志，如果您需要对用户访问日志进行分析来了解用户构成、访问质量或者快速定位问题，您可以使用实时日志功能来快速实现。

## 前提条件

- 

开通CDN服务：参考[开通](products/cdn/documents/activate-alibaba-cloud-cdn.md)[CDN](products/cdn/documents/activate-alibaba-cloud-cdn.md)[服务](products/cdn/documents/activate-alibaba-cloud-cdn.md)开通了CDN产品，并且添加了加速域名。

- 

开通SLS服务：参考[日志服务快速入门](products/sls/documents/getting-started.md)开通了SLS日志服务产品。

- 

配置实时日志推送：参考[配置实时日志推送](products/cdn/documents/user-guide/configure-real-time-log-delivery.md)为需要分析用户访问数据的CDN加速域名配置实时日志推送。

## CDN提供的实时日志与离线日志服务的区别

- 

日志延迟

CDN实时日志为实时采集的日志数据，日志数据延迟不超过3分钟，而离线日志的数据延迟通常在24小时之内。

- 

日志分析

CDN实时日志打通了SLS日志服务的日志转存和日志分析能力，预制了CDN基础数据、CDN错误分析、CDN热门资源、CDN用户分析这四张常用分析报表，也支持自定义日志分析策略，可以一站式提供日志存储和日志分析能力，而离线日志目前只支持日志转存到OSS云存储，尚未打通日志分析能力。

## 实时日志服务的优势

- 

日志延迟小

日志数据延迟不超过3分钟，可以帮助您快速对访问日志进行分析，及时发现问题并做出应对决策。

- 

一站式服务

传统的离线日志分析模式，需要用户将日志下载，再重新上传至数据仓库，然后在数据仓库进行一系列的清洗和数据模型定义，这一系列操作处理完以后才能进行数据分析，整个过程需要的人力较多，时间较长；CDN实时日志打通了SLS日志服务的日志转存和日志分析能力，免去传统模式下繁琐的离线日志分析流程。

## 使用限制

- 

专属LogStore默认类型为Standard，默认数据存储时间7天，不支持写入其他数据，在查询分析、告警、消费等功能上无特殊限制。

- 

专属LogStore索引支持修改，如遇到不支持修改场景可联系技术同学支持。

- 

目前仅支持推送日志到如下地域的日志服务Project中：华东1（杭州）、华东2（上海）、华北1（青岛）、华北2（北京）、华南1（深圳）、中国（香港）、亚太东南1（新加坡）。

## 适用场景

实时日志可以帮助您分析加速域名遇到的异常问题，也可以帮助您了解用户的访问情况。阿里云CDN实时日志在提供预制日志分析报表的同时，还支持自定义日志分析策略，可以满足不同场景下的需求。

### 预制的日志分析报表

| 日志分析场景 | 报表作用描述 |
| --- | --- |
| CDN 基础数据 | 该数据可以帮助您快速了解到 CDN 整体的服务质量以及终端用户的访问效率（命中率、访问延时、下载速度等），同时也可以在服务质量出现异常情况下及时进行处理。 |
| CDN 访问错误 | 该数据可以帮助您在应用访问出现异常时，快速定位到 CDN 服务问题的源头，例如：部分 URI 问题、源站出现故障、部分节点不可用、部分省份网络问题、部分运营商网络问题等。 |
| CDN 热门资源 | 该数据可以帮助您更好地了解热门资源情况，分析出热门域名、热门 URI、热门省份、热门运营商等，您也可以从热门数据了解到您的运营活动效果是否正常、热点时间内流量的上涨是否符合预期，以帮助您及时调整运营策略。 |
| CDN 用户构成 | 该数据可以帮助您更好地了解网站的用户构成，包括用户的客户端类型、省份、运营商等，也能够统计出访问量 TOP 用户、下载量 TOP 用户。 |


在实时日志功能页面找到需要分析日志的Project名称，然后单击查看报表即可进入日志分析报表模板的查看页面。

在数据查询模板页面，默认情况下查询的是全量域名的数据，也可以查询指定域名或者URI的数据。

具体使用方法您可以参考以下几个章节：

- 

[预制报表：CDN](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[基础数据](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)

- 

[预制报表：CDN](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[访问错误](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)

- 

[预制报表：CDN](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[热门资源](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)

- 

[预制报表：CDN](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[用户构成](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)

- 

[订阅报表模板数据](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)

### 自定义日志分析

在预制的日志分析报表无法满足您的需求时，您可以使用SLS产品强大的日志分析能力来实现自定义日志分析。

例如：查看响应状态码为499的域名排行榜、查看响应状态码为502的域名排行榜。

在实时日志功能页面找到需要分析日志的Project名称，然后单击日志分析即可进入自定义日志分析功能的页面。

在自定义分析界面，您可以在搜索框里面输入查询语句直接查询日志数据（通常适用于比较复杂的查询条件），也可以直接单击左侧原始日志栏的日志字段来过滤日志（通常适用于比较简单的过滤条件）。

日志查询页面顶部为查询输入框（支持输入查询语句、SQL 或 SPL），右侧有查询/分析按钮和时间选择器（可设置查询时间范围，如最近 15 分钟），左侧字段面板列出可筛选的索引字段，下方展示匹配的原始日志记录详情。

具体使用方法您可以参考：[自定义报表](products/sls/documents/ship-and-analyze-alibaba-cloud-cdn-real-time-logs-in-log-service.md)

## 创建实时日志推送Project

您可以参考[配置实时日志推送](products/cdn/documents/user-guide/configure-real-time-log-delivery.md)创建一个SLS日志服务的project，用于存储CDN产品指定域名（例如：aliyun.example.com）推送的实时日志。

创建成功的效果如下图，Project名称为project-example，Logstore名称为project-example，日志存储区域为cn-hangzhou（华东1-杭州）。

## 预制报表：CDN基础数据

CDN基础数据可以帮助您快速了解到CDN整体的服务质量以及终端用户的访问效率（命中率、访问延时、下载速度等），同时也可以在服务质量出现异常情况下及时进行处理。

包括以下数据（可以查看总的数据，也可以按域名或者URI查看）：

- 

健康度：响应正常的状态码总数占比。

- 

缓存命中率：资源的平均缓存命中率（按字节数来统计的命中率）。

- 

下载速度：资源的平均下载速度。

- 

访问状态：每一种响应状态码的占比，可以用于快速查看当前异常状态码的占比。

- 

访问延时分布：每一个延时段的占比。

- 

请求带宽：分钟粒度的带宽值。

- 

访问次数/人数：PV、UV值。

- 

请求命中率：按请求数来统计的命中率。

- 

访问延时：用于下载资源的平均访问延时。

## 预制报表：CDN访问错误

CDN访问错误数据可以帮助您在应用访问出现异常时，快速定位到CDN服务问题的源头，例如：部分URI问题、源站出现故障、部分节点不可用、部分省份网络问题、部分运营商网络问题等。

包括以下数据（可以查看总的数据，也可以按域名或者URI查看）：

- 

错误域名访问Top10：按不同域名访问产生的错误占比统计Top域名。

- 

错误URI访问Top10：按不同URI下产生的错误占比统计Top URI。

- 

请求错误百分比：分时间统计4xx、5xx状态码的占比。

- 

错误请求状态分布：统计各个状态码的数量、占比。

- 

错误运营商统计：统计不同运营商的4xx、5xx状态码数量。

- 

错误按省份统计：统计不同省份的4xx、5xx状态码数量。

- 

错误详情（4xx）：统计不同省份、运营商的4xx状态码数量、占比。

- 

错误详情（5xx）：统计不同省份、运营商的5xx状态码数量、占比。

- 

错误按客户端分布：统计不同的客户端UA（user-agent）对应的4xx、5xx状态码数量及占比。

## 预制报表：CDN热门资源

CDN热门资源数据可以帮助您更好地了解热门资源情况，分析出热门域名、热门URI、热门省份、热门运营商等，您也可以从热门数据了解到您的运营活动效果是否正常、热点时间内流量的上涨是否符合预期，以帮助您及时调整运营策略。

包括以下数据（可以查看总的数据，也可以按域名或者URI查看）：

- 

访问次数Top域名：按总访问次数占比统计Top域名。

- 

下载流量Top域名：按总下载流量占比统计Top域名。

- 

热门访问URI：统计各个URI的访问次数、访问人数、下载总量。

- 

热门访问来源：统计热门Referer来源域名，并且记录访问次数、UV、占比。

- 

全国访问次数统计：分别统计各个省份的平均访问次数。

- 

全国下载网速：分别统计各个省份的平均下载速度。

- 

省份统计：分别统计各个省份的总访问次数、总下载流量、平均下载速度。

- 

运营商流量和速度：分别统计各个运营商的下载总量和平均下载速度。

- 

运营商统计：分别统计各个运营商的总访问次数、总下载流量、平均下载速度。

## 预制报表：CDN用户构成

CDN用户构成数据可以帮助您更好地了解网站的用户构成，包括用户的客户端类型、省份、运营商等，也能够统计出访问TOP用户、下载量TOP用户。

包括以下数据（可以查看总的数据，也可以按域名或者URI查看）：

- 

访问次数：总访问次数，PV。

- 

访问人数：总访问人数，UV。

- 

访问地区分布：分别统计各个省份的访问次数、占比。

- 

访问客户端统计：分别统计各个客户端类型的访问次数、占比。

- 

运营商次数统计：分别统计各个运营商的总访问次数、占比。

- 

下载量Top用户：按IP统计用户的总访问数、错误访问数、下载总量。

- 

有效访问Top用户：按IP统计用户的总访问数、错误访问数、下载总量（去掉4xx、5xx这些无效访问）。

## 订阅报表模板数据

如果您需要SLS日志服务定期将报表模板的数据发送给您，那么您可以使用订阅功能。

### 操作步骤

- 

以CDN基础数据页面为例，单击右上角的订阅，然后单击创建。在报表模板页面右上角，单击订阅按钮。

- 

在侧滑出现的配置窗口中输入订阅名称、频率和全局时间，然后单击下一步。

- 

在通知列表的下拉菜单中选择通知方式并填写相关信息后，单击提交即可成功创建。

通知方式目前支持邮件、WebHook-钉钉机器人、WebHook-飞书机器人、WebHook-企业微信机器人和微信。

## 自定义报表

- 

示例1：查看最近30天内，响应状态码为499的域名排行榜。

日志分析语句：return_code = 499| select domain , count(*) as c group by domain order by c desc limit 10

- 

示例2：查看最近30天内，响应状态码为502的域名排行榜。

日志分析语句：return_code = 502| select domain , count(*) as c group by domain order by c desc limit 10

- 

示例3：查看最近30天内，访问URI为/cpu的日志数据。

可以直接单击左侧原始日志栏的URI字段，然后单击/cpu即可过滤出需要的日志。

过滤后，左侧快速分析面板的uri字段显示/cpu占比 53%，为最主要的请求 URI。查询栏过滤条件为* and uri : "/cpu"，时间范围选择30天（相对），日志总条数为 1,556,698。

[上一篇：阿里云SLS导入火山引擎TLS日志数据](products/sls/documents/import-volcano-engine-tls-log-data-into-alibaba-cloud-sls.md)[下一篇：日志采集失败的 6 大经典雷区](products/sls/documents/6-log-collection-failures.md)

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
