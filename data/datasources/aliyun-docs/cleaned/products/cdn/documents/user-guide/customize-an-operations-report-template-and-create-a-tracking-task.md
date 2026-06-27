# 定制和订阅加速域名的运营报表离线分析数据-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/customize-an-operations-report-template-and-create-a-tracking-task

# 定制和订阅运营报表
通过运营报表功能，您可以查询加速域名在各个不同时间段的离线分析数据；通过分析数据，便于您了解加速域名的运行状况，帮助您进行业务状态分析。
## 前提条件
您已成功添加加速域名。如果未添加，请参见[添加加速域名](../add-a-domain-name.md)进行添加。
## 功能介绍
运营报表统计并默认展示了用户访问的PV/UV、地区和运营商、域名排行、热门referer、热门URL、回源热门URL和Top客户端IP等内容，您可以根据业务需求，定制和订阅报表，订阅成功后系统会将报表发送到您的指定邮箱，您可以对报表内容进行分析，了解加速域名的运行状况。
| 报表内容 | 描述 |
| --- | --- |
| PV/UV | 支持按时间查询域名的 PV 和 UV。 |
| 地区和运营商 | 查看中国内地、中国香港、中国澳门和中国台湾及海外地区指定时间区间的用户访问区域分布和用户运营商分布情况。 |
| 域名排行 | 展示各个加速域名的访问排名，包含占比、流量或带宽峰值、峰值时刻和访问次数。 说明 查询域名排行以天为最小粒度。例如当您选择需要查询的日期后，系统为您显示对应日期的 TOP200 信息。 |
| 热门 referer | 展示热门 Referer 防盗链的流量、流量占比、访问次数和访问占比。 说明 运营报表功能在分析用户日志的时候，会统计用户请求日志中的 http_referer 字段信息，统计结果包含以下两种情况： 如果用户请求中携带的 referer 信息为规范的 URL 地址，那么运营报表将会统计和记录其中的域名信息，例如以下几种情况都会被统计为 example.com 。 http://example.com/aliyundoc/ https://example.com/aliyundoc/image 如果用户请求中携带的 referer 信息不是规范的 URL 地址，那么运营报表将会全部统计为符号“-”。 |
| 热门 URL | 查询您指定域名、指定状态码、指定日期的热门 URL，包括流量、流量占比、访问次数和访问占比。 说明 查询热门 URL 以天为最小粒度。例如当您选择需要查询的日期后，系统为您显示对应日期的 TOP3000 信息。 |
| 回源热门 URL | 查询您指定域名、指定状态码、指定日期的回源热门 URL，包括流量、流量占比、访问次数和访问占比。 说明 查询回源热门 URL 以天为最小粒度。例如当您选择需要查询的日期后，系统为您显示对应日期的 TOP100 信息。 |
| Top 客户端 IP | 查询您指定域名、指定区域、指定日期的 Top 客户端 IP，支持按流量或请求数进行排行。 说明 Top 客户端 IP 以天为最小粒度。当您选择需要查询的日期后，如果您查询的是全部区域，系统为您显示对应日期的 TOP200 信息；如果您查询的是单个区域，系统为您显示对应日期的 TOP20 信息。 |
说明
订阅运营报表之后，阿里云CDN将会定期给您的邮箱发送报表邮件，邮件的报表中展示的“流量”数据，其单位为byte。
## 定制运营报表
使用运营报表功能前，您需要先定制运营报表才能进行数据生产统计。由于受日志完整性延迟的影响，数据生产时延较长，定制的报表通常需要在T+1天的6点左右才能查看到。例如，2025年7月16日定制的报表，在2025年7月17日6点左右可以查看到。
说明
T日创建运营报表，能获取T+1日及之后的运营报表数据，T日及之前的运营报表数据无法获取；运营报表数据获取延迟6小时以上，不同指标项的生产间隔不同（1-6小时不等），故至少T+1日 6点后才能看到T+1日的运营报表数据；
不同指标项的报表数据生产间隔时间：
热门URL（支持按请求数或者流量排序）：6小时
热门Referer（支持按请求数或者流量排序）：1小时
回源热门URL（支持按请求数或者流量排序）：1小时
Top客户端IP（支持按请求数或者流量排序）：6小时
域名排行（仅支持按流量排序）：1
PV/UV：1小时
访问区域分布：1小时
运营商分布：1小时
其它报表相关的数据默认不在控制台展示，您可以通过报表订阅的方式，发送至指定邮箱，再查询相关数据。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，选择统计分析>运营报表。
在运营报表页签下，打开定制运营报表按钮。
您可观测到您账号下PV/UV、地区和运营商、域名排行、热门referer、热门URL、回源热门URL和Top客户端IP的具体信息。
## 订阅运营报表
订阅运营报表前需确保已经成功定制了运营报表，否则将无法订阅成功。成功订阅运营报表后，系统会将报表发送到您的指定邮箱，您可以对报表内容进行分析。
说明
目前订阅功能处于试运行阶段，一个阿里云账号（包含RAM用户）最多可以创建五个订阅任务。
由于受日志完整性延迟的影响，数据生产时延较长，系统需完全获取到所有数据后才会发送报表。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，选择统计分析>运营报表。
在运营报表页面，单击订阅任务页签。
单击订阅任务，配置订阅信息。
| 参数 | 描述 |
| --- | --- |
| 任务名称 | 输入订阅任务名称。 |
| 报告类型 | 支持日报、周报和月报三种报告类型，同时只能选择其中一种报告类型。 日报：前一天的日志数据统计完整并计算完成后由系统发送至您的邮箱。 周报：按照自然周计算，当一周的日志数据统计完整并计算完成后由系统发送至您的邮箱。通常前一周的报表，会在下一周的周一上午发送。 月报：按照自然月计算，当一个月的日志数据统计完整并计算完成后由系统发送至您的邮箱。 |
| 邮件地址 | 接收运营报表的邮箱地址。支持同时输入多个邮箱地址，多个邮箱地址用英文逗号（,）分隔。 |
| 包含域名 | 选择您要订阅运营报表的加速域名。 |
| 报表内容 | 选择您要订阅的报表内容。 |
单击确定，系统提示订阅任务创建成功。
说明
报表订阅成功后，如果您在定制运营报表中删除了某个报表内容，此时您在订阅任务中单击编辑查看任务时，被删除的报表内容会显示异常（显示的是报表ID），表示该报表未定制，您将无法订阅该报表内容。报表ID与报表名称的对应关系，请参见[报表对应关系](customize-an-operations-report-template-and-create-a-tracking-task.md)。
报表中展示“流量”数据，其单位均为byte。
可选：修改订阅任务。
选择需要修改的订阅任务，单击编辑，根据[步骤](customize-an-operations-report-template-and-create-a-tracking-task.md)[4](customize-an-operations-report-template-and-create-a-tracking-task.md)配置方法，完成修改后，单击确定。
## 报表对应关系
报表ID与报表名称的对应关系见下表。
| 报表 ID | 英文名称 | 中文名称 | 计算方法 |
| --- | --- | --- | --- |
| 1 | TopUrlByAcc | 热门 URL（按请求数排序） | 按照 URL 的条数统计。 |
| 3 | TopUrlByTraf | 热门 URL（按流量排序） | 按照流量排行次序统计排序，流量数值会增加上 TCP 包头系数。详细信息，请参见 [为什么监控查询流量、用量查询流量与日志统计流量有差异？](../product-overview/traffic-amount-in-the-monitoring-and-usage-analytics-or-in-the-usage-statistics-feature-different-from-the-logged-traffic-amount.md) 。 |
| 5 | TopReferByAcc | 热门 Referer（按请求数排序） | 按照访问次数统计。 |
| 7 | TopReferByTraf | 热门 Referer（按流量排序） | 按照流量排行次序统计排序，流量数值会增加上 TCP 包头系数。详细信息，请参见 [为什么监控查询流量、用量查询流量与日志统计流量有差异？](../product-overview/traffic-amount-in-the-monitoring-and-usage-analytics-or-in-the-usage-statistics-feature-different-from-the-logged-traffic-amount.md) 。 |
| 9 | OriginTopUrlByAcc | 回源热门 URL（按请求数排序） | 按照 URL 的条数统计。 |
| 11 | OriginTopUrlByTraf | 回源热门 URL（按流量排序） | 按照流量排行次序统计排序，流量数值会增加上 TCP 包头系数。详细信息，请参见 [为什么监控查询流量、用量查询流量与日志统计流量有差异？](../product-overview/traffic-amount-in-the-monitoring-and-usage-analytics-or-in-the-usage-statistics-feature-different-from-the-logged-traffic-amount.md) 。 |
| 13 | TopIpByAcc | Top 客户端 IP（按请求数排序） | 按照访问 IP 的访问次数进行排序。 |
| 15 | TopIpByTraf | Top 客户端 IP（按流量排序） | 按照流量排行次序统计排序，流量数值会增加上 TCP 包头系数。详细信息，请参见 [为什么监控查询流量、用量查询流量与日志统计流量有差异？](../product-overview/traffic-amount-in-the-monitoring-and-usage-analytics-or-in-the-usage-statistics-feature-different-from-the-logged-traffic-amount.md) 。 |
| 17 | DomainByTraf | 域名排行（按流量排序） | 按照域名的流量排序。 |
| 19 | DomainPvUv | PV/UV | PV：按照每天的终端访问数进行统计。 UV：按照独立 IP 的访问数进行统计，同一个 IP 只统计一次。 |
| 21 | AreaTrafStat | 访问区域分布 | 统计某个域名在某个地域的分布。 |
| 23 | IspTrafStat | 运营商分布 | 统计某个域名在某个运营商的分布。 |
## 关闭定制的运营报表
关闭定制运营报表，所有的订阅任务都会停止产生数据但订阅任务还在，如果您的业务不再需要该订阅任务，可在订阅任务页签手动删除即可，删除方法请参见[删除订阅任务](customize-an-operations-report-template-and-create-a-tracking-task.md)。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，选择运营报表。
在运营报表页面，单击关闭定制运营报表。
单击确定关闭定制运营报表。
## 删除订阅任务
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，选择运营报表。
在订阅任务页面，选择需要删除的订阅任务，单击删除。
单击确定删除订阅任务。
## 常见问题
### 为什么运营报表定制成功了没有数据？
由于受日志完整性延迟的影响，数据生产时延较长，当日定制的报表通常隔天生成。例如，2021年08月01日定制的报表，会在2021年08月02日6点左右生成。
如果您第二天在控制台查询仍没有数据，有以下两种原因：
您在定制运营报表时添加的域名没有流量。您可以点击定制运营报表，查看已选域名是否为您要使用的目标域名，确认该域名是否有流量。如果配置的域名有问题，您需要重新定制实际要查询的报表，并且等待数据生产。
您在定制域名时并未勾选相关的报表内容。例如，您需要查看热门URL的报表，但是您在定制运营报表时，并没有勾选热门URL这一内容，导致报表没有数据。此时，您需要重新选择域名的报表内容，并且等待数据生产。
### 支持订阅几个报表任务？
一个阿里云账号（包含RAM用户）最多可以创建五个报表订阅任务。订阅报表任务前，需确保已经成功定制了运营报表，否则订阅不成功。
### 如何查看当天的CDN访问数据？
运营报表数据以天为粒度统计，通常在T+1日6点左右生成，因此无法通过运营报表查看当天的CDN访问数据。如果您需要实时查看当天的CDN访问数据（如访问URL、访问次数等），可以开通实时日志推送功能，将CDN日志实时投递到日志服务SLS进行查询和分析。实时日志推送为额外计费功能。具体操作，请参见[配置实时日志推送](configure-real-time-log-delivery.md)。
## 相关文档
运营报表相关API接口，请参见[运营报表](../developer-reference/api-cdn-2018-05-10-dir-operations-reports.md)。
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
