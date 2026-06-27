# 如何快速上手查询和分析操作-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/query-and-analyze-website-logs

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

# 查询和分析网站日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文以查询和分析网站日志为例，帮助您快速上手查询和分析操作。

## 前提条件

已采集到网站访问日志。配置Logtail采集配置的步骤，请参见[采集主机文本日志](products/sls/documents/collect-host-logs.md)。

## 步骤一：创建索引

创建索引后，才能对日志进行查询分析，索引分为全文索引和字段索引，索引的概念、类型、配置示例、计费说明等信息，请参见[创建索引](products/sls/documents/create-indexes.md)。本文为网站日志创建字段索引。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在Project列表区域，单击目标Project。

- 

在日志存储>日志库页签中，单击目标Logstore。

- 

在LogStore的查询和分析页面的右上角，选择查询分析属性>属性。如果您还未开启索引，请单击开启索引。

- 

配置字段索引，然后单击确定。可以手动逐条添加字段索引，也可以单击自动生成索引，日志服务会根据预览数据中的第一条日志自动配置索引。

重要

- 

配置索引后，只对新写入的数据生效。如果您要查询历史数据，请使用[重建索引](products/sls/documents/reindex-logs-for-a-logstore.md)。

- 

如果您要使用分析语句（SELECT），必须在配置索引时打开对应字段的统计功能。

- 

日志服务默认已为部分保留字段开启索引。更多信息，请参见[保留字段](products/sls/documents/reserved-fields.md)。

在查询分析对话框中，单击自动生成索引按钮自动生成字段索引。生成的字段包括 body_bytes_sent（long）、client_ip（text）、host（text）、http_host（text）、http_user_agent（text）、request_length（long）、request_method（text）等。text 类型字段的分词符默认为,"';=()[]{}?@&<>/:\n\t\r，大小写敏感和包含中文开关均关闭，开启统计开关均打开。确认后单击确定。

## 步骤二：查询分析日志

在控制台对日志查询与分析的具体步骤，请参见[查询与分析快速指引](products/sls/documents/quick-guide-to-query-and-analysis.md)，查询和分析语句的格式为查询语句|分析语句。查询语句可单独使用，分析语句必须与查询语句一起使用。

重要

执行查询和分析语句后，默认只返回100条结果，您可以使用LIMIT语句控制返回结果数量。更多信息，请参见[LIMIT](products/sls/documents/limit-clause.md)[子句](products/sls/documents/limit-clause.md)。

### 查询语句

- 

查询包含Chrome的日志。

Chrome

- 

查询请求时间大于60秒的日志。

request_time > 60

- 

查询请求时间在60秒~120秒之间的日志。

request_time in [60 120]

- 

查询GET请求成功（状态码为200~299）的日志。

request_method : GET and status in [200 299]

- 

查询request_uri字段值为/request/path-2/file-2的日志。

request_uri:/request/path-2/file-2

### 分析语句

- 

统计网站访问PV。

使用[count](products/sls/documents/aggregate-function.md)[函数](products/sls/documents/aggregate-function.md)统计网站访问PV。

* | SELECT count(*) AS PV

查询结果显示PV值为9685。

- 

根据每分钟的时间粒度，统计网站访问PV。

使用[date_trunc](products/sls/documents/date-and-time-functions-1.md)[函数](products/sls/documents/date-and-time-functions-1.md)将时间对齐到每分钟并根据时间进行分组，然后使用[count](products/sls/documents/aggregate-function.md)[函数](products/sls/documents/aggregate-function.md)计算每分钟的访问PV并根据时间排序。

* | SELECT count(*) as PV, date_trunc('minute', __time__) as time GROUP BY time ORDER BY time

查询结果以折线图展示每分钟的PV趋势。

- 

根据每5分钟的时间粒度，统计每个请求方法的请求次数。

使用__time__ - __time__ %300将时间对齐到5分钟并根据时间进行分组，然后使用[count](products/sls/documents/aggregate-function.md)[函数](products/sls/documents/aggregate-function.md)计算每5分钟的请求次数并根据时间进行排序。

* | SELECT request_method, count(*) as count, __time__ - __time__ %300 as time GROUP BY time, request_method ORDER BY time

执行该查询语句后，返回的示例结果为：GET 请求 778 次、PUT 请求 242 次、POST 请求 231 次、DELETE 请求 101 次、HEAD 请求 4 次，对应时间戳均为 1610673300。

- 

环比上周的网站访问PV。

使用[count](products/sls/documents/aggregate-function.md)[函数](products/sls/documents/aggregate-function.md)计算总PV数，再使用[ts_compare](products/sls/documents/interval-valued-and-periodicity-valued-comparison-functions.md)[函数](products/sls/documents/interval-valued-and-periodicity-valued-comparison-functions.md)得出本周与上周的环比。其中，website_log为LogStore名称。

* | SELECT diff[1] as this_week, diff[2] as last_week, time FROM (SELECT ts_compare(pv, 604800) as diff, time FROM (SELECT COUNT(*) as pv, date_trunc('week', __time__) as time FROM website_log GROUP BY time ORDER BY time) GROUP BY time)

- 

统计客户端地址分布情况。

使用[ip_to_province](products/sls/documents/ip-functions.md)[函数](products/sls/documents/ip-functions.md)获取IP地址对应的省份并根据省份进行分组，然后再使用[count](products/sls/documents/aggregate-function.md)[函数](products/sls/documents/aggregate-function.md)计算每个地址出现的次数并根据次数进行排序。

* | SELECT count(*) as count, ip_to_province(client_ip) as address GROUP BY address ORDER BY count DESC

执行该语句的示例查询结果为：广东省 451 次、江苏省 447 次、北京市 433 次、山东省 425 次。

- 

统计访问前10的请求路径。

根据请求路径进行分组，然后使用[count](products/sls/documents/aggregate-function.md)[函数](products/sls/documents/aggregate-function.md)计算每个路径的访问次数并根据访问次数排序。

* | SELECT count(*) as PV, request_uri as PATH GROUP BY PATH ORDER BY PV DESC LIMIT 10

执行该查询语句后，返回的示例结果展示了访问量排名前10的请求路径（PATH）及其对应的访问次数（PV）。

- 

查询request_uri字段的值以%file-7结尾的日志。

重要

在查询语句中，模糊查询的通配符星号（*）和问号（?）只能出现在词的中间或末尾。如果您要查询以某字符结尾的字段，可以在分析语句中使用LIKE语法进行查询。

* | select * from website_log where request_uri like '%file-7'

其中，website_log为LogStore名称。

- 

统计请求路径访问情况。

使用[regexp_extract](products/sls/documents/regular-expression-functions-1.md)[函数](products/sls/documents/regular-expression-functions-1.md)提取request_uri字段中的文件部分，然后再使用[count](products/sls/documents/aggregate-function.md)[函数](products/sls/documents/aggregate-function.md)计算各个请求路径的访问次数。

* | SELECT regexp_extract(request_uri, '.*\/(file.*)', 1) file, count(*) as count group by file

查询结果中，file列值为file-5，count列值为17127，表示 file-5 的访问次数为 17127。

- 

查询request_uri字段中包含%abc%的日志。

* | SELECT * where request_uri like '%/%abc/%%' escape '/'

查询结果返回匹配的日志记录，其request_uri字段值为/request/path-1/file-92 %abc%qereqwr，其中%abc%部分即为模糊匹配命中的内容。

## 参考信息：网站日志样例

__tag__:__client_ip__:192.0.2.0 __tag__:__receive_time__:1609985755 __source__:198.51.100.0 __topic__:website_access_log body_bytes_sent:4512 client_ip:198.51.100.10 host:example.com http_host:example.com http_user_agent:Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27 http_x_forwarded_for:198.51.100.1 instance_id:i-02 instance_name:instance-01 network_type:vlan owner_id:%abc%-01 referer:example.com region:cn-shanghai remote_addr:203.0.113.0 remote_user:neb request_length:4103 request_method:POST request_time:69 request_uri:/request/path-1/file-0 scheme:https server_protocol:HTTP/2.0 slbid:slb-02 status:200 time_local:07/Jan/2021:02:15:53 upstream_addr:203.0.113.10 upstream_response_time:43 upstream_status:200 user_agent:Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.33 (KHTML, like Gecko) Ubuntu/9.10 Chromium/13.0.752.0 Chrome/13.0.752.0 Safari/534.33 vip_addr:192.0.2.2 vpc_id:3db327b1****82df19818a72

[上一篇：使用SQL语句查询分析日志](products/sls/documents/use-sql-statements-to-query-and-analyze-logs.md)[下一篇：查询和分析JSON日志](products/sls/documents/query-and-analyze-json-logs.md)

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
