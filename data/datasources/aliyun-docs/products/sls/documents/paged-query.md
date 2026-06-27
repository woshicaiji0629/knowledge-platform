# 分页获取查询结果与分析结果-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/paged-query

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

# 分页显示查询分析结果

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

查询分析日志时，查询分析结果内容过多会影响显示速度和查询体验。日志服务提供分页功能，可控制每次返回的日志数量。本文介绍查询结果和分析结果的分页方法。

## 分页方式概述

日志服务支持在使用[GetLogs API](products/sls/documents/developer-reference/api-sls-2020-12-30-getlogs.md)查询分析日志时对查询分析结果内容进行分页，查询结果和分析结果使用不同的分页方法。若要提前获取总的日志行数，请参见[GetHistograms](products/sls/documents/developer-reference/api-sls-2020-12-30-gethistograms.md)。

- 

查询语句：使用关键字查询，获取原始日志内容。通过GetLogs API中的offset和line参数实现分页。更多信息，请参见[查询概述](products/sls/documents/log-search-overview.md)。

- 

分析语句：使用SQL对查询结果进行分析，获取统计结果。通过SQL中的LIMIT语法实现分页。更多信息，请参见[查询与分析概述](products/sls/documents/log-analysis-overview.md)和[LIMIT](products/sls/documents/limit-clause.md)[子句](products/sls/documents/limit-clause.md)。

## 分页方式示例

下文为您介绍查询结果与分析结果的分页示例，请按需要选择：

- 

### 查询结果分页示例

在分页读取时，不停地增大offset的值，直到读取到某个offset值后，获取的结果行数为0，并且结果的progress为complete状态，则表示读取了所有数据。

- 

分页的示例代码逻辑

offset = 0 #指定从某一行开始读取查询结果，此处从第0行开始读取。 line = 100 #指定当前请求读取的行数，最大值为100。如果大于100，则仍然返回100行。此处每次读取100行。 query = "status:200" #查询status字段是200的所有日志。 while True: response = get_logstore_logs(query, offset, line) #执行读取请求。 process (response) #调用自定义逻辑，处理返回结果。 如果 response.get_count() == 0 && response.is_complete() 则读取结束，跳出当前循环 否则 offset += 100 # offset增加到100，读取下一个100行。

## Python代码示例

更多信息，请参见[Python SDK](products/sls/documents/developer-reference/overview-4.md)[概述](products/sls/documents/developer-reference/overview-4.md)。

# 日志服务的服务接入点。 endpoint = '' # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # Project名称。 project = '' # Logstore名称。 logstore = '' client = LogClient(endpoint, accessKeyId, accessKey) topic = "" From = int(time.time()) - 600 To = int(time.time()) log_line = 100 offset = 0 while True: res4 = None for retry_time in range(0, 3): req4 = GetLogsRequest(project, logstore, From, To, topic=topic, line=log_line, offset=offset) res4 = client.get_logs(req4) if res4 is not None and res4.is_completed(): break time.sleep(1) offset += 100 if res4.is_completed() and res4.get_count() == 0: break; if res4 is not None: # 处理结果。 res4.log_print()

## Java代码示例

更多信息，请参见[Java SDK](products/sls/documents/developer-reference/overview-of-log-service-sdk-for-java.md)[概述](products/sls/documents/developer-reference/overview-of-log-service-sdk-for-java.md)。

int log_offset = 0; int log_line = 100; //log_line的最大值为100，每次获取100行数据。若需要读取更多数据，请使用offset分页。offset和line只对关键字查询有效，若使用SQL查询，则无效。在SQL查询中返回更多数据，请使用limit语法。 while (true) { GetLogsResponse res4 = null; // 对于每个Offset，一次读取100行日志，如果读取失败，最多重复读取3次。 for (int retry_time = 0; retry_time < 3; retry_time++) { GetLogsRequest req4 = new GetLogsRequest(project, logstore, from, to, topic, query, log_offset, log_line, false); res4 = client.GetLogs(req4); if (res4 != null && res4.IsCompleted()) { break; } Thread.sleep(200); } System.out.println("Read log count:" + String.valueOf(res4.GetCount())); log_offset += log_line; if (res4.IsCompleted() && res4.GetCount() == 0) { break; } }

- 

### 分析结果分页示例

您可以使用SQL中的Limit语法实现分析结果分析显示，例如通过* | select count(1) , url group by url语句进行查询分析，指定返回1000行日志。您可以通过分页指定每次读取500行，共2次读取完成，示例如下：

* | select count(1) , url group by url limit 0, 500 * | select count(1) , url group by url limit 500, 500

- 

分析结果分页的示例代码逻辑

offset = 0 //指定从某一行开始读取查询结果，此处从第0行开始读取。 line = 500 //指定当前请求读取的行数，最大值为1,000,000。如果一次读取太多，会影响网络延时和客户端的处理速度。此处每次读取500行。 query = "* | select count(1) , url group by url limit " while True: real_query = query + offset + "," + line response = get_logstore_logs(real_query) //执行读取请求。 process (response) //调用自定义逻辑，处理返回的结果。 如果 response.get_count() == 0 则读取结束，跳出当前循环 否则 offset += 500 //offset增加到500，读取下一个500行。

## Python代码示例

更多信息，请参见[Python SDK](products/sls/documents/developer-reference/overview-4.md)[概述](products/sls/documents/developer-reference/overview-4.md)。

# 日志服务的服务接入点 endpoint = '' # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # Project名称。 project = '' # Logstore名称。 logstore = '' client = LogClient(endpoint, accessKeyId, accessKey) topic = "" origin_query = "* | select * limit " From = int(time.time()) - 600 To = int(time.time()) log_line = 100 offset = 0 while True: res4 = None query = origin_query + str(offset) + " , " + str(log_line) for retry_time in range(0, 3): req4 = GetLogsRequest(project, logstore, From, To, topic=topic, query=query) res4 = client.get_logs(req4) if res4 is not None and res4.is_completed(): break time.sleep(1) offset += 100 if res4.is_completed() and res4.get_count() == 0: break; if res4 is not None: # 处理结果。 res4.log_print()

## Java代码示例

更多信息，请参见[Java SDK](products/sls/documents/developer-reference/overview-of-log-service-sdk-for-java.md)[概述](products/sls/documents/developer-reference/overview-of-log-service-sdk-for-java.md)。

int log_offset = 0; int log_line = 500; String origin_query = "* | select count(1) , url group by url limit " while (true) { GetLogsResponse res4 = null; // 对于每个Offset，一次读取500行日志。如果读取失败，最多重复读取3次。 query = origin_query + log_offset + "," + log_line; for (int retry_time = 0; retry_time < 3; retry_time++) { GetLogsRequest req4 = new GetLogsRequest(project, logstore, from, to, topic, query); res4 = client.GetLogs(req4); if (res4 != null && res4.IsCompleted()) { break; } Thread.sleep(200); } System.out.println("Read log count:" + String.valueOf(res4.GetCount())); log_offset += log_line; if (res4.GetCount() == 0) { break; } }

[上一篇：分析负载均衡7层访问日志](products/sls/documents/analyze-layer-7-access-logs-of-slb.md)[下一篇：分析-行车轨迹日志](products/sls/documents/analyze-vehicle-track-logs.md)

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
