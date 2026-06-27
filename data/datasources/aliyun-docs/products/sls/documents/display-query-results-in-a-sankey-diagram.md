# 如何进行桑基图操作-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/display-query-results-in-a-sankey-diagram

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

# 桑基图

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

桑基图通过箭头或流线的宽度来可视化地表示不同节点之间的流量、权重或其他度量值。本文介绍桑基图的基本配置及示例。

## 简介

桑基图 (Sankey Diagram)，是一种特定类型的流图，用于描述一组值到另一组值的流向。适合网络流量等场景，通常包含3组值source、target以及value。source和target描述了节点的关系，而value描述了该source和target之间边的关系。

基本构成如下：

- 

节点

- 

边

例如以下数据可以用桑基图表示。

| source | target | value |
| --- | --- | --- |
| node1 | node2 | 14 |
| node1 | node3 | 12 |
| node3 | node4 | 5 |
| … | .. | … |


使用如下桑基图描述上述数据的关系。

## 配置示例

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。在Project列表区域，单击目标Project。

- 

在左侧导航栏中，选择仪表盘>仪表盘列表。在仪表盘列表中，单击目标仪表盘。在目标仪表盘右上角，单击编辑。在仪表盘编辑模式下，单击添加>添加新图表。

- 

在页面右侧配置图表类型、查询分析配置和图形配置，在页面左侧配置查询时间范围、LogStore、查询分析语句。然后单击页面上方的应用查看图表配置效果。

对于网络请求的数据进行汇总的查询分析语句为：

* | select COALESCE(client_ip, slbid, host) as source, COALESCE(host, slbid, client_ip) as dest, sum(request_length) as inflow group by grouping sets( (client_ip, slbid), (slbid, host))

其中，Logstore选择website_log，图表类型选择桑基图。查询分析配置中，起点列设为source，终点列设为dest，数值列设为inflow。图形配置中，连线颜色设为源节点，对齐方式设为居中对齐。

您还可以通过配置多条查询分析语句，可视化地表示多个节点之间的流向。配置slbid、client_ip和host节点之间的流向。

选择图表类型为桑基图，数据源为website_log。在查询分析配置中，查询 A 的起点列设为slbid、终点列设为client_ip、数值列设为inflow；查询 B 的起点列设为client_ip、终点列设为host、数值列设为inflow。

查询分析语句A：统计不同客户端通过不同负载均衡器的总请求流量。

* | select slbid,client_ip,sum(request_length) as inflow group by client_ip,slbid order by client_ip limit 10

查询分析语句B：统计客户端与主机的流量分布。

* | select client_ip,host,sum(request_length) as inflow group by host,client_ip order by client_ip limit 10

日志服务联合传统型负载均衡CLB推出7层访问日志功能，用于记录所有发送到CLB的请求的详细信息，包括请求时间、客户端IP地址、延迟、请求路径和服务器响应等。您可以通过7层访问日志绘制桑基图。更多信息请参见[开通访问日志功能](products/sls/documents/enable-the-access-log-management-feature.md)。

## 通用配置

通用配置用于对桑基图进行全局配置。

- 

基本配置

| 参数 | 说明 |
| --- | --- |
| 标题 | 设置图表的标题。 |
| 显示标题 | 打开 显示标题 开关后，将在图表中显示标题。 |
| 显示边框 | 打开 显示边框 开关后，将在图表中显示边框。 |
| 显示背景 | 打开 显示背景 开关后，将在图表中显示背景颜色。 |
| 显示时间 | 打开 显示时间 开关后，将在图表中显示查询时间。 |
| 固定时间 | 打开 固定时间 开关后，将固定查询分析的时间，不受仪表盘全局时间的影响。 |


- 

标准配置

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 格式化 | 设置数字的显示格式。 |
| 单位 | 设置数字的单位。 |
| 小数点后位数 | 设置数字的小数点后的位数。 |
| 显示名 | 设置显示字段的名称。 设置了显示名后，该图表中显示字段的名称都将变更为该值。如果您要修改某个名称，可以使用字段配置。 |
| 颜色方案 | 选择图表的颜色方案。 内置 ：使用内置颜色。 单色 ：选择一个颜色。 阈值 ：通过阈值的配置显示颜色。 |


- 

查询分析配置

| 参数 | 说明 |
| --- | --- |
| 起点列 | 描述起始节点。 |
| 终点列 | 描述终点节点。 |
| 数值列 | 起始节点和终点节点之间流量值。 |


- 

图形配置

| 参数 | 说明 |
| --- | --- |
| 连线颜色 | 设置连线颜色。 |
| 对齐方式 | 设置图形的对齐方式。 |


- 

阈值

| 参数 | 说明 |
| --- | --- |
| 阈值 | 设置数据的阈值。 如果设置 颜色方案 为 阈值 且在此处设置了阈值，则图表中的背景将以对应的阈值颜色显示。 |


- 

变量替换

| 参数 | 说明 |
| --- | --- |
| 变量替换 | 变量替换相当于为单个统计图表添加变量类型的过滤器。您在 通用配置 中设置了变量替换后，日志服务将在当前统计图表的左上边添加一个过滤器。您可以在过滤器中选择对应的值，日志服务会自动将查询和分析语句中的变量替换为您所选择的变量值，执行一次查询和分析操作。配置示例，请参见 [示例](products/sls/documents/user-guide/variables.md) [2：设置变量替换](products/sls/documents/user-guide/variables.md) 。 |


- 

文档链接

| 参数 | 说明 |
| --- | --- |
| 添加文档链接 | 支持自定义设置文档链接或描述信息。设置后，相关信息将被展示在桑基图的右上角。 |


## 字段配置

字段配置用于对单个查询分析的结果或单个查询分析结果中的单列数据进行个性化的可视化设置。字段配置中的配置项说明请参见[通用配置](products/sls/documents/display-query-results-on-a-funnel-chart.md)。

例如A > source表示对查询分析A中的source字段进行配置。将颜色设置单色展示。

## 交互事件

交互事件用于对单个查询分析的结果或单个查询分析结果中的单列数据进行交互设置，加深数据分析的维度。交互事件包括打开日志库、打开快速查询、打开仪表盘、打开Trace分析、打开Trace详情和自定义HTTP链接。更多信息，请参见[为仪表盘添加交互事件实现下钻分析](products/sls/documents/drill-down-events.md)。

例如A表示为查询分析A的结果设置交互事件，设置为打开日志库，则您单击查询分析A相关的图表上的任意点，然后单击打开日志库，将跳转到您所设置的日志库中。

[上一篇：高德地图](products/sls/documents/gaud-map.md)[下一篇：词云](products/sls/documents/display-query-results-on-a-word-cloud.md)

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
