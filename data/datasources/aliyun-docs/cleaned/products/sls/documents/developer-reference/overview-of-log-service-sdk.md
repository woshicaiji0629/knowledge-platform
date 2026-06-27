# 日志服务全流程管理编程开发接口-日志服务SDK-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/developer-reference/overview-of-log-service-sdk

# SDK参考概述
开发人员可以使用.NET Core、Java、Python、PHP、Node.js、C、Go、iOS、Android、C++等语言的SDK采集、查询和分析日志等。
## 使用前须知
不同语言的日志服务SDK具体实现细节会有所不同，但是它们都是日志服务API在不同语言上的封装，实现的功能也基本一致。具体包括如下几个方面：
实现对日志服务API接口的统一封装 ，让您不需要关心具体的API请求构建和响应解析。而且各个不同语言的接口使用也非常接近，方便您在不同语言间切换。更多信息，请参见[接口规范](procedure.md)。
实现日志服务API的数字签名逻辑，让您不需要关心API的签名逻辑细节，降低使用日志服务API的难度。更多信息，请参见[请求签名](request-signatures.md)。
实现日志服务日志的ProtoBuffer格式封装，让您在写入日志时不需要关心ProtoBuffer格式的具体细节。更多信息，请参见[ProtoBuffer](data-encoding.md)[格式](data-encoding.md)。
实现日志服务API中定义的压缩方法，让您不用关心压缩实现的细节。部分语言的SDK支持启用压缩模式写入日志（默认为使用压缩方式）。
提供统一的错误处理机制，让您可以使用语言所熟悉的方式处理请求异常。更多信息，请参见[错误处理机制](exception-handling.md)。
目前所有语言实现的SDK仅提供同步请求方式。
## SDK列表
下表列举了日志服务不同语言的SDK的参考文档和GitHub源码。
说明
日志服务对基础资源（例如Project个数、LogStore个数、Shard个数、LogItem大小）设定了合理的限制。建议您在使用前阅读使用限制文档，了解基础资源的使用限制。更多信息，请参见[基础资源使用限制](../basic-resources.md)。
使用SDK采集日志到日志服务后，您还需要为日志配置合适的索引，之后您就可以进行日志查询和分析、数据加工等操作。更多信息，请参见[创建索引](../create-indexes.md)和[查询与分析快速指引](../quick-guide-to-query-and-analysis.md)。
| SDK 语言 | 参考文档 | GitHub 源码 |
| --- | --- | --- |
| Java | [Java SDK](overview-of-log-service-sdk-for-java.md) [概述](overview-of-log-service-sdk-for-java.md) | [Log Service Java SDK](https://github.com/aliyun/aliyun-log-java-sdk) 、 [Java Producer Library](https://github.com/aliyun/aliyun-log-java-producer) 、 |
| .NET Core | [.NET Core SDK](overview-of-log-service-sdk-for-dotnet-core.md) [概述](overview-of-log-service-sdk-for-dotnet-core.md) | [Log Service .NET Core SDK](https://github.com/aliyun/aliyun-log-dotnetcore-sdk) |
| PHP | [PHP SDK](overview-of-log-service-sdk-for-php.md) [概述](overview-of-log-service-sdk-for-php.md) | [Log Service PHP SDK](https://github.com/aliyun/aliyun-log-php-sdk) |
| Python | [Python SDK](overview-4.md) [概述](overview-4.md) | [Log Service Python SDK](https://github.com/aliyun/aliyun-log-python-sdk) |
| Node.js | [Node.js SDK](overview-of-log-service-sdk-for-node-js.md) [概述](overview-of-log-service-sdk-for-node-js.md) | [Log Service Node.js SDK](https://github.com/aliyun-UED/aliyun-sdk-js/tree/master/samples/sls) |
| C | [C SDK](log-service-sdk-for-c.md) | [Log Service C SDK](https://github.com/aliyun/aliyun-log-c-sdk) |
| GO | [Go SDK](overview-14.md) [概述](overview-14.md) | [Log Service Go SDK](https://github.com/aliyun/aliyun-log-go-sdk) |
| iOS | [iOS SDK](overview-of-log-service-sdk-for-ios.md) [概述](overview-of-log-service-sdk-for-ios.md) | [Log Service iOS SDK](https://github.com/aliyun/aliyun-log-ios-sdk) 、 [Objective-C SDK](https://github.com/lujiajing1126/AliyunLogObjc) |
| Android | [Android SDK](overview-of-log-service-sdk-for-android.md) [概述](overview-of-log-service-sdk-for-android.md) | [Log Service Android SDK](https://github.com/aliyun/aliyun-log-android-sdk) |
| C++ | [C++ SDK](overview-of-log-service-sdk-for-cpp.md) [概述](overview-of-log-service-sdk-for-cpp.md) | [Log Service C++ SDK](https://github.com/aliyun/aliyun-log-cpp-sdk) |
| HarmonyOS | [HarmonyOS SDK](harmonyos-sdk-overview.md) [概述](harmonyos-sdk-overview.md) | [Log Service HarmonyOS SDK](https://github.com/aliyun-sls/alibabacloud_log_harmony_sdk) |
## 调用示例
具体调用示例参考[Python SDK](list-projects.md)[调用日志服务](list-projects.md)[ListProject](list-projects.md)[接口](list-projects.md)。
## 常见问题
### 日志服务SDK都支持哪些功能？
日志服务SDK已经实现日志服务大部分功能，包括日志采集、创建索引、查询和分析、数据加工、日志消费、日志投递管理、告警、定时SQL等。若您在SDK调试中发现未实现功能，建议您升级到最新版本SDK重试或关注后续SDK版本更新。
### 使用日志服务SDK的基本流程是什么？
日志服务SDK提供全流程的日志管理，其使用流程和控制台使用流程基本相似。其使用基本流程大致如下：
开通日志服务。
获取访问密钥。
创建项目Project和日志库LogStore。
日志采集并存储至LogStore。
为日志创建索引。
查询和分析日志，可视化展示。
对日志数据进行加工、投递和告警等操作。
日志服务提供界面化操作控制台，操作更简单。更多信息，请参考[日志服务快速入门](../getting-started.md)。
### SDK调试常见报错如何处理？
日志服务SDK提供错误处理逻辑。SDK可能出现的异常错误可以分成如下几类：
由日志服务端返回的错误。这类错误由日志服务端返回并由SDK处理。关于这类错误的详细信息可以参见具体的API接口说明、API错误码。关于错误码的更多信息，请参见[错误码](error-codes.md)。
由SDK在向服务端发出请求时出现的网络错误。这类错误包括网络连接不通，服务端返回超时等。
由SDK自身产生的、与平台及语言相关的错误，如内存溢出等。
更多信息，请参见[错误处理](exception-handling.md)。
在使用日志服务SDK过程中，您可能遇到日志采集、索引、查询和分析、加工等各类报错，您可以参考日志服务常见问题进行处理。更多信息，请参见[常见问题](../faq-15.md)。
### 使用日志服务SDK是否存在限制？
日志服务对基础资源（例如Project个数、LogStore个数、Shard个数、LogItem大小）设定了合理的限制。建议您在使用前阅读使用限制文档，了解基础资源的使用限制。更多信息，请参见[基础资源使用限制](../basic-resources.md)。
### 是否有使用SDK的代码示例文档？
日志服务提供典型常用操作的代码示例文档，请参考各SDK参考帮助文档。
日志服务Java SDK：
[使用](use-getlogs-to-query-logs.md)[GetLogs](use-getlogs-to-query-logs.md)[接口查询日志](use-getlogs-to-query-logs.md)
[使用](use-log-service-sdk-for-java-to-manage-a-logstore.md)[Java SDK](use-log-service-sdk-for-java-to-manage-a-logstore.md)[管理日志库](use-log-service-sdk-for-java-to-manage-a-logstore.md)[Logstore](use-log-service-sdk-for-java-to-manage-a-logstore.md)
[通过消费组消费日志](use-consumer-groups-to-consume-data.md)
[使用](use-aliyun-log-java-producer-to-write-log-data-to-log-service.md)[Aliyun Log Java Producer](use-aliyun-log-java-producer-to-write-log-data-to-log-service.md)[写入日志数据](use-aliyun-log-java-producer-to-write-log-data-to-log-service.md)
日志服务Python SDK：
[使用](use-getlogs-to-query-logs-46.md)[GetLogs](use-getlogs-to-query-logs-46.md)[接口查询日志](use-getlogs-to-query-logs-46.md)
[使用](use-log-service-sdk-for-python-to-manage-logstores.md)[Python SDK](use-log-service-sdk-for-python-to-manage-logstores.md)[管理日志库](use-log-service-sdk-for-python-to-manage-logstores.md)[Logstore](use-log-service-sdk-for-python-to-manage-logstores.md)
[使用](use-gethistograms-to-query-the-distribution-of-logs-1.md)[GetHistograms](use-gethistograms-to-query-the-distribution-of-logs-1.md)[查询日志分布数量](use-gethistograms-to-query-the-distribution-of-logs-1.md)
[通过消费组消费日志](use-consumer-groups-to-consume-logs.md)
日志服务各语言SDK：
[Go SDK](get-started-with-log-service-sdk-for-go.md)[快速入门](get-started-with-log-service-sdk-for-go.md)
[.NET SDK](../get-started-with-log-service-sdk-for-dotnet.md)[快速入门](../get-started-with-log-service-sdk-for-dotnet.md)
[Node.js SDK](get-started-with-log-service-sdk-for-node-js.md)[快速入门](get-started-with-log-service-sdk-for-node-js.md)
[PHP SDK](get-started-with-log-service-sdk-for-php.md)[快速入门](get-started-with-log-service-sdk-for-php.md)
[C++ SDK](get-started-with-log-service-sdk-for-cpp.md)[快速入门](get-started-with-log-service-sdk-for-cpp.md)
[Android SDK](get-started-with-log-service-sdk-for-android.md)[快速入门](get-started-with-log-service-sdk-for-android.md)
[iOS SDK](get-started-with-log-service-sdk-for-ios.md)[快速入门](get-started-with-log-service-sdk-for-ios.md)
[Flutter SDK](flutter-sdk-quick-start.md)[快速入门](flutter-sdk-quick-start.md)
[HarmonyOS SDK](harmonyos-sdk-quick-start.md)[快速入门](harmonyos-sdk-quick-start.md)
更多源码，请参见[GitHub](https://github.com/orgs/aliyun/repositories?q=log)[阿里云日志源码库](https://github.com/orgs/aliyun/repositories?q=log)。
## 相关文档
日志服务SDK调试平台
阿里云OpenAPI开发者门户提供调试、SDK、示例和配套文档。通过OpenAPI，您无需手动封装请求和签名操作，就可以快速对日志服务API进行调试。更多信息，请参见[OpenAPI](https://next.api.aliyun.com/api/Sls/2020-12-30/CreateProject?lang=JAVA&sdkStyle=dara&params=%7B%7D)[开发者门户](https://next.api.aliyun.com/api/Sls/2020-12-30/CreateProject?lang=JAVA&sdkStyle=dara&params=%7B%7D)。
命令行工具CLI
为满足越来越多的自动化日志服务配置需求，日志服务提供命令行工具CLI。更多信息，请参见[命令行工具](overview-of-log-service-cli.md)[CLI](overview-of-log-service-cli.md)。
## 费用说明
使用SDK、OpenAPI开发者门户和日志服务CLI产生的费用和使用控制台产生的费用一致。更多信息，请参见[计费概述](../billing-overview.md)。
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
