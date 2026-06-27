# 各开发语言SDK采集日志总览-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/use-sdks-to-collect-logs

# SDK采集
开发人员可以使用.NET、.NET Core、Java、Python、PHP、Node.js、C、GO、IOS、Android、C++等语言的SDK采集、查询和分析日志等。
## 使用前须知
不同语言的日志服务SDK具体实现细节会有所不同，但是它们都是日志服务API在不同语言上的封装，实现的功能也基本一致。具体包括如下几个方面：
实现对日志服务API接口的统一封装 ，让您不需要关心具体的API请求构建和响应解析。而且各个不同语言的接口使用也非常接近，方便您在不同语言间切换。更多信息，请参见[接口规范](developer-reference/procedure.md)。
实现日志服务API的数字签名逻辑，让您不需要关心API的签名逻辑细节，降低使用日志服务API的难度。更多信息，请参见[请求签名](developer-reference/request-signatures.md)。
实现日志服务日志的ProtoBuffer格式封装，让您在写入日志时不需要关心ProtoBuffer格式的具体细节。更多信息，请参见[ProtoBuffer](developer-reference/data-encoding.md)[格式](developer-reference/data-encoding.md)。
实现日志服务API中定义的压缩方法，让您不用关心压缩实现的细节。部分语言的SDK支持启用压缩模式写入日志（默认为使用压缩方式）。
提供统一的错误处理机制，让您可以使用语言所熟悉的方式处理请求异常。更多信息，请参见[错误处理机制](developer-reference/exception-handling.md)。
目前所有语言实现的SDK仅提供同步请求方式。
## SDK列表
下表列举了日志服务不同语言的SDK的参考文档和GitHub源码。
说明
日志服务对基础资源（例如Project个数、Logstore个数、Shard个数、LogItem大小）设定了合理的限制。建议您在使用前阅读使用限制文档，了解基础资源的使用限制。更多信息，请参见[基础资源使用限制](basic-resources.md)。
使用SDK采集日志到日志服务后，您还需要为日志配置合适的索引，之后您就可以进行日志查询和分析、数据加工等操作。更多信息，请参见[创建索引](create-indexes.md)和[查询和分析日志](quick-guide-to-query-and-analysis.md)。
| SDK 语言 | 参考文档 | GitHub 源码 |
| --- | --- | --- |
| Java | [Java SDK](developer-reference/overview-of-log-service-sdk-for-java.md) [概述](developer-reference/overview-of-log-service-sdk-for-java.md) | [Log Service Java SDK](https://github.com/aliyun/aliyun-log-java-sdk) 、 [Log Service SDK for Java 0.6.0 API](https://log-java-docs.oss-cn-hangzhou.aliyuncs.com/) 、 [Java Producer Library](producer-library.md) |
| .NET Core | [.NET Core SDK](developer-reference/overview-of-log-service-sdk-for-dotnet-core.md) [概述](developer-reference/overview-of-log-service-sdk-for-dotnet-core.md) | [Log Service .NET Core SDK](https://github.com/aliyun/aliyun-log-dotnetcore-sdk) |
| .NET | [.NET SDK](overview-of-log-service-sdk-for-dotnet.md) [概述](overview-of-log-service-sdk-for-dotnet.md) | [Log Service .NET SDK](https://github.com/aliyun/aliyun-log-chsarp-sdk) |
| PHP | [PHP SDK](developer-reference/overview-of-log-service-sdk-for-php.md) [概述](developer-reference/overview-of-log-service-sdk-for-php.md) | [Log Service PHP SDK](https://github.com/aliyun/aliyun-log-php-sdk) |
| Python | [Python SDK](developer-reference/overview-4.md) [概述](developer-reference/overview-4.md) | [Log Service Python SDK](https://github.com/aliyun/aliyun-log-python-sdk) 、 [User Guide](https://aliyun-log-python-sdk.readthedocs.io/README_CN.html) |
| Node.js | [Node.js SDK](developer-reference/overview-of-log-service-sdk-for-node-js.md) [概述](developer-reference/overview-of-log-service-sdk-for-node-js.md) | [Log Service Node.js SDK](https://github.com/aliyun-UED/aliyun-sdk-js/tree/master/samples/sls) |
| C | [C SDK](developer-reference/log-service-sdk-for-c.md) | [Log Service C SDK](https://github.com/aliyun/aliyun-log-c-sdk) 、 [C Producer Library](c-producer-library.md) |
| GO | [Go SDK](developer-reference/overview-14.md) [概述](developer-reference/overview-14.md) | [Log Service Go SDK](https://github.com/aliyun/aliyun-log-go-sdk) |
| iOS | [iOS SDK](developer-reference/overview-of-log-service-sdk-for-ios.md) [概述](developer-reference/overview-of-log-service-sdk-for-ios.md) | [Log Service iOS SDK](https://github.com/aliyun/aliyun-log-ios-sdk) 、 [Objective-C SDK](https://github.com/lujiajing1126/AliyunLogObjc) |
| Android | [Android SDK](developer-reference/overview-of-log-service-sdk-for-android.md) [概述](developer-reference/overview-of-log-service-sdk-for-android.md) | [Log Service Android SDK](https://github.com/aliyun/aliyun-log-android-sdk) |
| C++ | [C++ SDK](developer-reference/overview-of-log-service-sdk-for-cpp.md) [概述](developer-reference/overview-of-log-service-sdk-for-cpp.md) | [Log Service C++ SDK](https://github.com/aliyun/aliyun-log-cpp-sdk) |
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
