# 使用日志服务PythonSDK完成常见操作-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/developer-reference/get-started-with-log-service-sdk-for-python

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

# Python SDK快速入门

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何快速使用日志服务Python SDK完成常见操作，包括创建项目（Project）、创建日志库（Logstore）、写入日志和查询日志等。

## 前提条件

- 

已创建RAM用户并完成授权。具体操作，请参见[创建](products/sls/documents/using-the-openapi-example.md)[RAM](products/sls/documents/using-the-openapi-example.md)[用户并完成授权](products/sls/documents/using-the-openapi-example.md)。

- 

已配置环境变量ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET。具体操作，请参见[在](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Linux、macOS](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[和](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Windows](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[系统配置环境变量](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)。

重要

阿里云账号的AccessKey拥有所有API的访问权限，建议您使用RAM用户的AccessKey进行API访问或日常运维。

强烈建议不要把AccessKey ID和AccessKey Secret保存到工程代码里，否则可能导致AccessKey泄露，威胁您账号下所有资源的安全。

- 

已完成日志服务Python SDK安装。更多信息，请参见[安装日志服务](products/sls/documents/developer-reference/install-the-log-service-python-sdk.md)[Python SDK](products/sls/documents/developer-reference/install-the-log-service-python-sdk.md)。

## 示例

- 

直接编写Python代码采集日志

本示例中，创建一个SLSQuickStart.py文件，并调用接口分别完成创建Project、创建Logstore、创建索引、写入日志数据和查询日志数据。示例如下：

from aliyun.log import LogClient, PutLogsRequest, LogItem, GetLogsRequest, IndexConfig import time import os # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # 日志服务的服务接入点。此处以杭州为例，其它地域请根据实际情况填写。 endpoint = "cn-hangzhou.log.aliyuncs.com" # 创建日志服务Client。 client = LogClient(endpoint, accessKeyId, accessKey) # Project名称。 project_name = "aliyun-test-project" # Logstore名称 logstore_name = "aliyun-test-logstore" # 查询语句。 query = "*| select dev,id from " + logstore_name # 索引。 logstore_index = {'line': { 'token': [',', ' ', "'", '"', ';', '=', '(', ')', '[', ']', '{', '}', '?', '@', '&', '<', '>', '/', ':', '\n', '\t', '\r'], 'caseSensitive': False, 'chn': False}, 'keys': {'dev': {'type': 'text', 'token': [',', ' ', "'", '"', ';', '=', '(', ')', '[', ']', '{', '}', '?', '@', '&', '<', '>', '/', ':', '\n', '\t', '\r'], 'caseSensitive': False, 'alias': '', 'doc_value': True, 'chn': False}, 'id': {'type': 'long', 'alias': '', 'doc_value': True}}, 'log_reduce': False, 'max_text_len': 2048} # from_time和to_time表示查询日志的时间范围，Unix时间戳格式。 from_time = int(time.time()) - 3600 to_time = time.time() + 3600 # 创建Project。 def create_project(): print("ready to create project %s" % project_name) client.create_project(project_name, project_des="") print("create project %s success " % project_name) time.sleep(60) # 创建Logstore。 def create_logstore(): print("ready to create logstore %s" % logstore_name) client.create_logstore(project_name, logstore_name, ttl=3, shard_count=2) print("create logstore %s success " % project_name) time.sleep(30) # 创建索引。 def create_index(): print("ready to create index for %s" % logstore_name) index_config = IndexConfig() index_config.from_json(logstore_index) client.create_index(project_name, logstore_name, index_config) print("create index for %s success " % logstore_name) time.sleep(60 * 2) # 向Logstore写入数据。 def put_logs(): print("ready to put logs for %s" % logstore_name) log_group = [] for i in range(0, 100): log_item = LogItem() contents = [ ('dev', 'test_put'), ('id', str(i)) ] log_item.set_contents(contents) log_group.append(log_item) request = PutLogsRequest(project_name, logstore_name, "", "", log_group, compress=False) client.put_logs(request) print("put logs for %s success " % logstore_name) time.sleep(60) # 通过SQL查询日志。 def get_logs(): print("ready to query logs from logstore %s" % logstore_name) request = GetLogsRequest(project_name, logstore_name, from_time, to_time, query=query) response = client.get_logs(request) for log in response.get_logs(): for k, v in log.contents.items(): print("%s : %s" % (k, v)) print("*********************") if __name__ == '__main__': # 创建Project。 create_project() # 创建Logstore。 create_logstore() # 创建索引。 create_index() # 向Logstore写入数据。 put_logs() # 通过SQL查询日志。 get_logs()

返回结果示例如下：

ready to create project aliyun-test-project create project aliyun-test-project success ready to create logstore aliyun-test-logstore create logstore aliyun-test-project success ready to create index for aliyun-test-logstore create index for aliyun-test-logstore success ready to put logs for aliyun-test-logstore put logs for aliyun-test-logstore success ready to query logs from logstore aliyun-test-logstore dev : test_put id : 0 ********************* dev : test_put id : 1 ********************* dev : test_put id : 2 ********************* dev : test_put id : 3 ********************* ........

更多示例代码，请参见[Aliyun Log Python SDK](https://github.com/aliyun/aliyun-log-python-sdk)。

- 

通过Logtail采集Python日志

通过Logtail方式，以采集Python的logging模块日志为例，采集Python日志。更多信息，请参见[采集](products/sls/documents/collect-python-logs.md)[Python](products/sls/documents/collect-python-logs.md)[日志](products/sls/documents/collect-python-logs.md)。

## 相关文档

- 

在调用API接口过程中，若服务端返回结果中包含错误信息，则表示调用API接口失败。您可以参考API错误码对照表查找对应的解决方法。更多信息，请参见[API](products/sls/documents/developer-reference/error-codes.md)[错误处理对照表](products/sls/documents/developer-reference/error-codes.md)。

- 

日志服务除自研的SDK外，还支持公共的阿里云SDK，关于阿里云SDK的使用方式，请参见[日志服务_SDK](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[中心-阿里云](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[OpenAPI](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)[开发者门户](https://next.api.aliyun.com/api-tools/sdk/Sls?version=2020-12-30&language=python-tea&tab=primer-doc)。

- 

为满足越来越多的自动化日志服务配置需求，日志服务提供命令行工具CLI（Command Line Interface）。更多信息，请参见[日志服务命令行工具](products/sls/documents/developer-reference/overview-of-log-service-cli.md)[CLI](products/sls/documents/developer-reference/overview-of-log-service-cli.md)。

[上一篇：初始化日志服务Python SDK](products/sls/documents/developer-reference/initializing-the-sls-python-sdk.md)[下一篇：管理Project](products/sls/documents/developer-reference/manage-project.md)

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
