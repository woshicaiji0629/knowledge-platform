# 查询分析JSON日志的步骤和示例-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/query-and-analyze-json-logs

# 查询和分析JSON日志
本文以JSON类型的网站日志为例，介绍查询和分析的步骤，并提供SQL示例。
## 前提条件
为了进行后续的日志分析，您需要先[采集](collect-json-formatted-text-logs.md)[JSON](collect-json-formatted-text-logs.md)[格式文本日志](collect-json-formatted-text-logs.md)。
## 步骤一：创建索引
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
在LogStore的查询和分析页面的右上角，选择查询分析属性>属性。如果还未创建索引，需要先单击开启索引。全文索引和字段索引的更多信息、创建索引的详细步骤，请参见[创建索引](create-indexes.md)。
说明
如果需要查询日志中的所有字段，建议使用全文索引。如果只需查询部分字段、建议使用字段索引，减少索引流量。如果需要对字段进行分析（SELECT语句），必须创建字段索引。
配置字段索引。以下是JSON格式的日志示例和对应字段的配置。
{ "@timestamp": "2023-01-01T00:00:00+08:00", "remote_addr": "192.168.0.1", "remote_user": "-", "request": { "request_length": 123, "request_method": "GET", "request_uri": "/index.html" }, "status": 200, "http_referer": "http://example.com", "http_user_agent": "Mozilla/5.0", "server_protocal": "HTTP/1.1", "http_x_forward_for": "192.168.0.1", "upstream_addr": "10.0.0.1:8080", "time": { "request_time": 0.006, "upstream_response_time": 0.004 }, "body_bytes_sent": [123, 456] }
将content字段类型设为json，request下的叶子节点还包括request.request_length（long）、request.request_method（text）、request.request_uri（text）。所有字段均打开开启统计开关。
__topic__、__source__、__tag__是系统的保留字段，更多信息请参见[保留字段](reserved-fields.md)。
@timestamp、remote_addr、remote_user、http_referer、http_user_agent、status、server_protocal、http_x_forward_for、upstream_addr字段不包含叶子节点，可以在content字段下直接建立索引。
request、time字段包含叶子节点，而且叶子节点不是JSON数组。
不能为request、time这两个父字段本身建立索引，也不能查询分析这两个父字段。
可以为request、time下的叶子节点建立索引，需要指定完整的路径，从最外层的父字段到最内层的叶子节点。格式为KEY1.KEY2.KEY3，例如time.request_time、time.upstream_response_time。建立索引后，可以查询time.request_time、time.upstream_response_time字段。
body_bytes_sent字段的值为JSON数组，不能建立索引，也不能为叶子节点建立索引。不能查询分析body_bytes_sent字段或body_bytes_sent的叶子节点。
## 步骤二：重建索引
配置索引后，只对新采集的数据生效。如果您要查询历史数据，请使用重建索引功能。具体操作，请参见[重建索引](reindex-logs-for-a-logstore.md)。
## 步骤三：查询和分析日志
您可以在LogStore的查询和分析页面，输入查询和分析语句，选择时间范围，进行日志查询操作。对于分析语句（SELECT语句），必须使用双引号（""）包裹字段名称，使用单引号（''）包裹字符串。查询和分析日志的详细步骤，请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。查询分析JSON日志的常见问题，请参见[查询和分析](faq-about-the-query-and-analysis-of-json-logs.md)[JSON](faq-about-the-query-and-analysis-of-json-logs.md)[日志的常见问题](faq-about-the-query-and-analysis-of-json-logs.md)。
查询请求状态为200的日志。
content.status:200
查询请求长度大于70的日志。
content.request.request_length > 70
查询GET请求的日志。
content.request.request_method:GET
统计不同请求状态对应的日志数量。
* | SELECT "content.status", COUNT(*) AS PV GROUP BY "content.status"
查询结果将以表格形式展示各请求状态码（如200、null）及其对应的页面访问量（PV）。
计算不同请求时长对应的请求数量，并按照请求时长进行升序排序。
* | SELECT "content.time.request_time", COUNT(*) AS count GROUP BY "content.time.request_time" ORDER BY "content.time.request_time"
计算不同请求方法对应的平均请求时长。
* | SELECT avg("content.time.request_time") AS avg_time,"content.request.request_method" GROUP BY "content.request.request_method"
查询结果显示，GET 请求方法的avg_time为 45，PUT 请求方法的avg_time为 11。
## 相关文档
[查询和分析](faq-about-the-query-and-analysis-of-json-logs.md)[JSON](faq-about-the-query-and-analysis-of-json-logs.md)[日志的常见问题](faq-about-the-query-and-analysis-of-json-logs.md)
[查询不到日志的排查思路](user-guide/what-do-i-do-if-no-results-are-returned-when-i-query-a-log.md)
[如何模糊查询日志？](how-do-i-query-logs-by-using-fuzzy-match.md)
[如何精确查询日志？](how-do-i-query-logs-by-using-exact-match.md)
[日志查询常见问题](user-guide/faq-about-log-query.md)
[查询与分析日志的常见报错](resolve-common-errors-that-may-occur-when-i-query-and-analyze-logs.md)
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
