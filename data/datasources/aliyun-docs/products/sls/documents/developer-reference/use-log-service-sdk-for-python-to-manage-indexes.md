# 如何创建、修改、查询、删除索引-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/developer-reference/use-log-service-sdk-for-python-to-manage-indexes

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

# 使用Python SDK管理索引

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

索引是一种倒排的数据存储结构，由关键词和指向实际数据的逻辑指针组成，用于快速根据关键词定位到具体数据行，类似于数据的目录。您只有配置索引后，才能进行查询和分析操作。本文通过代码示例介绍如何创建、修改、查询、删除索引。

## 前提条件

您已完成以下操作：

- 

[开通日志服务](https://www.aliyun.com/product/sls)。

- 

[初始化日志服务](products/sls/documents/developer-reference/initializing-the-sls-python-sdk.md)[Python SDK](products/sls/documents/developer-reference/initializing-the-sls-python-sdk.md)。

- 

已安装日志服务Python SDK。具体操作，请参见[安装日志服务](products/sls/documents/developer-reference/install-the-log-service-python-sdk.md)[Python SDK](products/sls/documents/developer-reference/install-the-log-service-python-sdk.md)。

- 

已创建日志服务Project、Logstore并完成日志采集配置。具体操作，请参见[管理](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)、[创建基础](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)和[数据采集概述](products/sls/documents/data-collection-overview.md)。

## 注意事项

本示例以华东1（杭州）的公网Endpoint为例，其公网Endpoint为https://cn-hangzhou.log.aliyuncs.com。

如果您通过与Project同地域的其他阿里云产品访问日志服务，请使用内网Endpointhttps://cn-hangzhou-intranet.log.aliyuncs.com。

关于日志服务支持的地域与Endpoint的对应关系，请参见[服务入口](products/sls/documents/developer-reference/service-entrance.md)。

## 计费说明

### 按写入数据量计费的LogStore

- 

创建的索引会占用存储空间，存储类型请参见[管理智能存储分层](products/sls/documents/data-tiered-storage-overview.md)。

- 

重建索引不产生费用。

- 

索引流量计费请参见[按写入数据量计费模式计费项](products/sls/documents/billing-items-in-the-pay-per-data-write-mode.md)。

### 按使用功能计费的LogStore

- 

创建的索引会占用存储空间，存储类型请参见[管理智能存储分层](products/sls/documents/data-tiered-storage-overview.md)。

- 

创建索引会产生流量，索引流量计费请参见[按使用功能计费模式计费项](products/sls/documents/billable-items.md)中的索引流量-日志索引和索引流量-日志索引-查询型。降低索引流量的建议，请参见[如何降低索引流量费用？](products/sls/documents/how-do-i-reduce-index-traffic-fees.md)。

- 

重建索引会产生费用。计费项、计费价格和创建索引相同。

## 原始日志样例

body_bytes_sent:1750 host:www.example.com http_referer:www.example.com http_user_agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27 http_x_forwarded_for:203.0.XX.XX remote_addr:203.0.XX.XX remote_user:p288 request_length:13741 request_method:GET request_time:71 request_uri:/request/path-1/file-1 http_code:200 time_local:11/Aug/2021:06:52:27 upstream_response_time:0.66

## 创建索引示例代码

控制台界面支持界面化配置索引，操作更便捷。具体操作，请参见[创建索引](products/sls/documents/create-indexes.md)。

以下代码用于创建索引。该示例中，基于原始日志样例，开启全文索引，为request_method、status字段开启字段索引。

from aliyun.log import LogClient, IndexConfig import os # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # 日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 endpoint = "cn-hangzhou.log.aliyuncs.com" # 创建日志服务Client。 client = LogClient(endpoint, accessKeyId, accessKey) # Project名称。 project_name = "ali-test-project" # LogStore名称。 logstore_name = "ali-test-logstore" if __name__ == '__main__': # 创建索引前，必须规划好全文索引、字段索引配置。该示例中，开启全文索引，为request_method、status字段开启字段索引。 logstore_index = {'line': { 'token': [',', ' ', "'", '"', ';', '=', '(', ')', '[', ']', '{', '}', '?', '@', '&', '<', '>', '/', ':', '\n', '\t', '\r'], 'caseSensitive': False, 'chn': False}, 'keys': {'request_method': {'type': 'text', 'token': [',', ' ', "'", '"', ';', '=', '(', ')', '[', ']', '{', '}', '?', '@', '&', '<', '>', '/', ':', '\n', '\t', '\r'], 'caseSensitive': False, 'alias': '', 'doc_value': True, 'chn': False}, 'status': {'type': 'long', 'alias': '', 'doc_value': True}}, 'log_reduce': False, 'max_text_len': 2048} print("ready to create index") index_config = IndexConfig() index_config.from_json(logstore_index) client.create_index(project_name, logstore_name, index_config) print("create index success ")

预期结果如下：

ready to create index create index success

## 更新索引示例代码

控制台界面支持界面化配置索引，操作更便捷。具体操作，请参见[创建索引](products/sls/documents/create-indexes.md)。

以下代码用于更新索引。该示例中，基于原始日志样例，开启全文索引，为request_method、status开启字段索引，并设置request_method字段大小写敏感为True。

from aliyun.log import LogClient, IndexConfig import os # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # 日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 endpoint = "cn-hangzhou.log.aliyuncs.com" # 创建日志服务Client。 client = LogClient(endpoint, accessKeyId, accessKey) # Project名称。 project_name = "ali-test-project" # Logstore名称。 logstore_name = "ali-test-logstore" if __name__ == '__main__': # 设置request_method字段大小写敏感为True。 logstore_index = {'line': { 'token': [',', ' ', "'", '"', ';', '=', '(', ')', '[', ']', '{', '}', '?', '@', '&', '<', '>', '/', ':', '\n', '\t', '\r'], 'caseSensitive': False, 'chn': False}, 'keys': {'request_method': {'type': 'text', 'token': [',', ' ', "'", '"', ';', '=', '(', ')', '[', ']', '{', '}', '?', '@', '&', '<', '>', '/', ':', '\n', '\t', '\r'], 'caseSensitive': True, 'alias': '', 'doc_value': True, 'chn': False}, 'status': {'type': 'long', 'alias': '', 'doc_value': True}}, 'log_reduce': False, 'max_text_len': 2048} print("ready to update index") index_config = IndexConfig() index_config.from_json(logstore_index) client.update_index(project_name, logstore_name, index_config) print("update index success ")

预期结果如下：

ready to update index update index success

## 查询索引示例代码

以下代码用于查询指定LogStore的索引信息。

from aliyun.log import LogClient, IndexConfig import os # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # 日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 endpoint = "cn-hangzhou.log.aliyuncs.com" # 创建日志服务Client。 client = LogClient(endpoint, accessKeyId, accessKey) # Project名称。 project_name = "ali-test-project" # Logstore名称。 logstore_name = "ali-test-logstore" if __name__ == '__main__': # 查询索引。 print("ready to list index") res = client.get_index_config(project_name, logstore_name) print("The index config is :%s" % res.get_index_config().to_json()) print("list index success ")

预期结果如下：

ready to list index The index config is :{'line': {'token': [',', ' ', "'", '"', ';', '=', '(', ')', '[', ']', '{', '}', '?', '@', '&', '<', '>', '/', ':', '\n', '\t', '\r'], 'caseSensitive': False, 'chn': False}, 'keys': {'request_method': {'type': 'text', 'token': [',', ' ', "'", '"', ';', '=', '(', ')', '[', ']', '{', '}', '?', '@', '&', '<', '>', '/', ':', '\n', '\t', '\r'], 'caseSensitive': True, 'alias': '', 'doc_value': True, 'chn': False}, 'status': {'type': 'long', 'alias': '', 'doc_value': True}}, 'log_reduce': False, 'max_text_len': 2048} list index success

## 删除索引示例代码

以下代码用于删除指定LogStore的索引信息。

from aliyun.log import LogClient, IndexConfig import os # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # 日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 endpoint = "cn-hangzhou.log.aliyuncs.com" # 创建日志服务Client。 client = LogClient(endpoint, accessKeyId, accessKey) # Project名称。 project_name = "ali-test-project" # Logstore名称。 logstore_name = "ali-test-logstore2" if __name__ == '__main__': # 删除索引。 print("ready to delete index") client.delete_index(project_name, logstore_name) print("delete index success ")

预期结果如下：

ready to delete index delete index success

## 相关文档

- 

日志服务除自研的SDK外，还支持公共的阿里云SDK，关于阿里云SDK的使用方式，请参见[日志服务_SDK](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[中心-阿里云](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[OpenAPI](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[开发者门户](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)。

- 

控制台操作索引请参见[创建索引](products/sls/documents/create-indexes.md)。

- 

为满足越来越多的自动化日志服务配置需求，日志服务提供命令行工具CLI（Command Line Interface）。更多信息，请参见[日志服务命令行工具](products/sls/documents/developer-reference/overview-of-log-service-cli.md)[CLI](products/sls/documents/developer-reference/overview-of-log-service-cli.md)。

- 

关于Index API接口说明，请参见如下：

- 

[创建索引](products/sls/documents/developer-reference/api-sls-2020-12-30-createindex.md)

- 

[获取索引](products/sls/documents/developer-reference/api-sls-2020-12-30-getindex.md)

- 

[更新索引](products/sls/documents/developer-reference/api-sls-2020-12-30-updateindex.md)

- 

[删除索引](products/sls/documents/developer-reference/api-sls-2020-12-30-deleteindex.md)

- 

更多示例代码，请参见[Aliyun Log Python SDK on GitHub](https://github.com/aliyun/aliyun-log-python-sdk)。

[上一篇：使用Python SDK管理消费组](products/sls/documents/developer-reference/use-log-service-sdk-for-python-to-manage-consumer-groups.md)[下一篇：使用Python SDK通过消费组消费日志](products/sls/documents/developer-reference/use-consumer-groups-to-consume-logs.md)

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
