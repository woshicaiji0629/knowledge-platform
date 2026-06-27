# 如何创建/修改/查询/删除索引-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/developer-reference/use-log-service-sdk-for-java-to-manage-indexes

# 使用Java SDK管理索引
索引是一种倒排的数据存储结构，由关键词和指向实际数据的逻辑指针组成，用于快速根据关键词定位到具体数据行，类似于数据的目录。您只有配置索引后，才能进行查询和分析操作。本文通过代码示例介绍如何创建、修改、查询、删除索引。
## 前提条件
您已完成以下操作：
[开通日志服务](https://www.aliyun.com/product/sls)。
[初始化日志服务](initializing-the-sls-python-sdk.md)[Python SDK](initializing-the-sls-python-sdk.md)。
已安装日志服务Java SDK。具体操作，请参见[安装](install-log-service-sdk-for-java.md)[Java SDK](install-log-service-sdk-for-java.md)。
已写入日志到LogStore。具体操作，请参见[数据采集概述](../data-collection-overview.md)。
## 注意事项
本示例以华东1（杭州）的公网Endpoint为例，其公网Endpoint为https://cn-hangzhou.log.aliyuncs.com。
如果您通过与Project同地域的其他阿里云产品访问日志服务，请使用内网Endpointhttps://cn-hangzhou-intranet.log.aliyuncs.com。
关于日志服务支持的地域与Endpoint的对应关系，请参见[服务入口](service-entrance.md)。
## 原始日志样例
body_bytes_sent:1750 host:www.example.com http_referer:www.example.com http_user_agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27 http_x_forwarded_for:203.0.XX.XX remote_addr:203.0.XX.XX remote_user:p288 request_length:13741 request_method:GET request_time:71 request_uri:/request/path-1/file-1 http_code:200 time_local:11/Aug/2021:06:52:27 upstream_response_time:0.66
## 创建索引示例代码
控制台界面支持界面化配置索引，操作更便捷。具体操作，请参见[创建索引](../create-indexes.md)。
以下代码用于创建名为testindex的索引。该示例中，基于原始日志样例，开启全文索引，为request_method、status字段开启字段索引。
import com.aliyun.openservices.log.Client; import com.aliyun.openservices.log.common.Index; import com.aliyun.openservices.log.exception.LogException; public class CreateIndex { public static void main(String[] args) throws LogException { // 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 String accessId = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"); String accessKey = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"); // 输入Project名称。 String projectName = "ali-test-project"; // 输入LogStore名称。 String logstoreName = "ali-test-logstore"; // 设置日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 String host = "https://cn-hangzhou.log.aliyuncs.com"; // 创建日志服务Client。 Client client = new Client(host, accessId, accessKey); try { //索引。 //创建索引前，必须规划好全文索引、字段索引配置。该示例中，开启全文索引，为request_method、status字段开启字段索引。 String logstoreindex = "{\"line\": {\"token\": [\",\", \" \", \"'\", \"\\\"\", \";\", \"=\", \"(\", \")\", \"[\", \"]\", \"{\", \"}\", \"?\", \"@\", \"&\", \"<\", \">\", \"/\", \":\", \"\\n\", \"\\t\", \"\\r\"], \"caseSensitive\": false, \"chn\": false}, \"keys\": {\"request_method\": {\"type\": \"text\", \"token\": [\",\", \" \", \"'\", \"\\\"\", \";\", \"=\", \"(\", \")\", \"[\", \"]\", \"{\", \"}\", \"?\", \"@\", \"&\", \"<\", \">\", \"/\", \":\", \"\\n\", \"\\t\", \"\\r\"], \"caseSensitive\": false, \"alias\": \"\", \"doc_value\": true, \"chn\": false}, \"status\": {\"type\": \"long\", \"alias\": \"\", \"doc_value\": true}}, \"log_reduce\": false, \"max_text_len\": 2048}"; Index index = new Index(); System.out.println("ready to create index"); index.FromJsonString(logstoreindex); client.CreateIndex(projectName, logstoreName, index); System.out.println(String.format("create index for %s success", logstoreName)); } catch (LogException e) { System.out.println("LogException e :" + e.toString()); System.out.println("error code :" + e.GetErrorCode()); System.out.println("error message :" + e.GetErrorMessage()); throw e; } } }
预期结果如下：
ready to create index create index for ali-test-logstore success
## 更新索引示例代码
控制台界面支持界面化配置索引，操作更便捷。具体操作，请参见[创建索引](../create-indexes.md)。
以下代码用于更新索引。该示例中，基于原始日志样例，开启全文索引，为request_method、status开启字段索引，并设置request_method字段大小写敏感为True。
import com.aliyun.openservices.log.Client; import com.aliyun.openservices.log.common.Index; import com.aliyun.openservices.log.exception.LogException; public class UpdateIndex { public static void main(String[] args) throws LogException { // 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 String accessId = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"); String accessKey = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"); // 输入Project名称。 String projectName = "ali-test-project"; // 输入LogStore名称。 String logstoreName = "ali-test-logstore"; // 设置日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 String host = "https://cn-hangzhou.log.aliyuncs.com"; // 创建日志服务Client。 Client client = new Client(host, accessId, accessKey); try { // 更新索引。 String logstoreindex = "{\"line\": {\"token\": [\",\", \" \", \"'\", \"\\\"\", \";\", \"=\", \"(\", \")\", \"[\", \"]\", \"{\", \"}\", \"?\", \"@\", \"&\", \"<\", \">\", \"/\", \":\", \"\\n\", \"\\t\", \"\\r\"], \"caseSensitive\": false, \"chn\": false}, \"keys\": {\"request_method\": {\"type\": \"text\", \"token\": [\",\", \" \", \"'\", \"\\\"\", \";\", \"=\", \"(\", \")\", \"[\", \"]\", \"{\", \"}\", \"?\", \"@\", \"&\", \"<\", \">\", \"/\", \":\", \"\\n\", \"\\t\", \"\\r\"], \"caseSensitive\": true, \"alias\": \"\", \"doc_value\": true, \"chn\": false}, \"status\": {\"type\": \"long\", \"alias\": \"\", \"doc_value\": true}}, \"log_reduce\": false, \"max_text_len\": 2048}"; Index index = new Index(); System.out.println("ready to update index"); index.FromJsonString(logstoreindex); client.UpdateIndex(projectName, logstoreName, index); System.out.println(String.format("update index for %s success", logstoreName)); } catch (LogException e) { System.out.println("LogException e :" + e.toString()); System.out.println("error code :" + e.GetErrorCode()); System.out.println("error message :" + e.GetErrorMessage()); throw e; } } }
预期结果如下：
ready to update index update index for ali-test-logstore success
## 查询索引示例代码
以下代码用于查询指定LogStore的索引信息。
import com.aliyun.openservices.log.Client; import com.aliyun.openservices.log.common.Index; import com.aliyun.openservices.log.exception.LogException; import com.aliyun.openservices.log.response.GetIndexResponse; public class ListIndex { public static void main(String[] args) throws LogException { // 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 String accessId = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"); String accessKey = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"); // 输入Project名称。 String projectName = "ali-test-project"; // 输入LogStore名称。 String logstoreName = "ali-test-logstore"; // 设置日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 String host = "https://cn-hangzhou.log.aliyuncs.com"; // 创建日志服务Client。 Client client = new Client(host, accessId, accessKey); try { Index index = new Index(); System.out.println("ready to get index"); GetIndexResponse response = client.GetIndex(projectName, logstoreName); index = response.GetIndex(); // 输出索引。 System.out.println("The index is ：" + index.ToJsonString()); System.out.println(String.format("get index for %s success", logstoreName)); } catch (LogException e) { System.out.println("LogException e :" + e.toString()); System.out.println("error code :" + e.GetErrorCode()); System.out.println("error message :" + e.GetErrorMessage()); throw e; } } }
预期结果如下：
ready to get index The index is ：{"log_reduce":false,"line":{"caseSensitive":false,"chn":false,"token":[","," ","'","\"",";","=","(",")","[","]","{","}","?","@","&","<",">","/",":","\n","\t","\r"]},"keys":{"request_method":{"doc_value":true,"caseSensitive":true,"chn":false,"alias":"","type":"text","token":[","," ","'","\"",";","=","(",")","[","]","{","}","?","@","&","<",">","/",":","\n","\t","\r"]},"status":{"doc_value":true,"alias":"","type":"long"}},"ttl":30,"max_text_len":2048} get index for ali-test-logstore success
## 删除索引示例代码
以下代码用于删除指定LogStore的索引信息。
import com.aliyun.openservices.log.Client; import com.aliyun.openservices.log.exception.LogException; public class DeleteIndex { public static void main(String[] args) throws LogException { // 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 String accessId = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"); String accessKey = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"); // 输入Project名称。 String projectName = "ali-test-project"; // 输入LogStore名称。 String logstoreName = "ali-test-logstore"; // 设置日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 String host = "https://cn-hangzhou.log.aliyuncs.com"; // 创建日志服务Client。 Client client = new Client(host, accessId, accessKey); try { System.out.println("ready to delete index"); client.DeleteIndex(projectName, logstoreName); System.out.println(String.format("delete index for %s success", logstoreName)); } catch (LogException e) { System.out.println("LogException e :" + e.toString()); System.out.println("error code :" + e.GetErrorCode()); System.out.println("error message :" + e.GetErrorMessage()); throw e; } } }
预期结果如下：
ready to delete index delete index for ali-test-logstore success
## 相关文档
在调用API接口过程中，若服务端返回结果中包含错误信息，则表示调用API接口失败。您可以参考API错误码对照表查找对应的解决方法。更多信息，请参见[API](error-codes.md)[错误处理对照表](error-codes.md)。
日志服务除自研的SDK外，还支持公共的阿里云SDK，关于阿里云SDK的使用方式，请参见[日志服务_SDK](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[中心-阿里云](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[OpenAPI](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[开发者门户](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)。
为满足越来越多的自动化日志服务配置需求，日志服务提供命令行工具CLI（Command Line Interface）。更多信息，请参见[日志服务命令行工具](overview-of-log-service-cli.md)[CLI](overview-of-log-service-cli.md)。
关于Index API接口说明，请参见如下：
[创建索引](api-sls-2020-12-30-createindex.md)
[获取索引](api-sls-2020-12-30-getindex.md)
[更新索引](api-sls-2020-12-30-updateindex.md)
[删除索引](api-sls-2020-12-30-deleteindex.md)
更多示例代码，请参见[Aliyun Log Java SDK on GitHub](https://github.com/aliyun/aliyun-log-java-sdk)。
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
