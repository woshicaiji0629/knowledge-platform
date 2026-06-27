# 如何分析网站日志并可视化展示分析结果-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/analyze-website-logs

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

# 分析网站日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务支持通过SQL92语法分析日志，并提供丰富的统计图表展示分析结果。本文介绍如何在日志服务控制台上分析网站日志，并通过合适的统计图表可视化展示分析结果。

## 前提条件

- 

已采集网站日志。具体操作，请参见[数据采集](products/sls/documents/data-collection-overview.md)。

- 

已创建索引。具体操作，请参见[创建索引](products/sls/documents/create-indexes.md)。

## 背景信息

网站日志是网站运维的重要信息，包含PV、UV、访问地域分布以及访问前十页面等信息。日志服务提供多样化的日志采集方式及一站式分析功能，您可通过查询+SQL92语法对日志进行实时分析，并以图表形式直观展示分析结果。日志服务还支持通过自带的仪表盘、DataV、Grafana、Tableau（通过JDBC链接）、Quick BI等可视化方式创建多种场景下的日志数据分析大盘。

## 操作步骤

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

输入查询和分析语句，然后单击最近15分钟，设置查询和分析的时间范围。

更多信息，请参见[步骤一：配置索引](products/sls/documents/quick-guide-to-query-and-analysis.md)。

- 

通过表格展示最近1天客户端访问情况，并降序排列。

* | SELECT remote_addr, count(*) as count GROUP BY remote_addr ORDER BY count DESC

- 

通过折线图展示最近15分钟PV、UV以及平均响应时间的变化情况。

* | select date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as minutes, approx_distinct(remote_addr) as uv, count(1) as pv, avg(request_time) as avg group by minutes order by minutes asc limit 100000

在查询分析配置中，设置x轴字段为minutes，y轴字段为pv、uv和avg，统计图表如下所示。

- 

通过柱状图展示最近15分钟不同来源地址的访问次数。

* | select referer, count(1) as count group by referer

- 

通过条形图展示最近15分钟访问前十的页面。

* | select request_uri, count(1) as count group by request_uri order by count desc limit 10

- 

通过饼图展示最近15分钟页面访问情况。

* | select request_uri as uri , count(1) as c group by uri limit 10

- 

通过单值图展示最近15分钟的PV数。

* | select count(1) as PV

- 

通过面积图展示最近1天某IP地址的访问情况。

remote_addr: 10.0.XX.XX | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, count(1) as PV group by time order by time limit 1000

配置x轴为time，y轴为PV，统计图表如下所示。

- 

通过流图展示最近15分钟不同方法的请求次数随时间的变化趋势。

* | select date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as minute, count(1) as c, request_method group by minute, request_method order by minute asc limit 100000

配置x轴为minute，y轴为c，聚合列为request_method，统计图表如下所示。

- 

添加统计图表到仪表盘。

您可以单击添加到仪表盘，完成操作。具体操作，请参见[添加统计图表到仪表盘](products/sls/documents/add-a-chart-to-a-dashboard-1.md)。

[上一篇：查询分析程序日志](products/sls/documents/query-and-analyze-application-logs.md)[下一篇：分析负载均衡7层访问日志](products/sls/documents/analyze-layer-7-access-logs-of-slb.md)

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
