# 封装API调用操作ECS资源-ECS SDK-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/developer-reference/ecs-v2-0-sdk-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# ECS V2.0 SDK概览

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云服务器ECS SDK是一个简化开发工作的依赖包，通过封装底层API调用，可以让开发者在使用时轻松实现对ECS资源（如实例、安全组、镜像等）的创建、查询、更新和删除操作。ECS SDK内部处理了网络通信、请求格式化和响应解析等复杂细节，并支持多种语言，使开发者能够专注于业务逻辑，而无需关心底层实现。

## SDK代系

ECS SDK包含V2.0 SDK和V1.0 SDK两个代系。V2.0 SDK为最新发布的代系，相较于V1.0 SDK，它支持更多的编程语言，解决了V1.0 SDK中存在的单Client线程安全问题，同时具备更强的健壮性和易用性，从而为开发者在开发过程中提供更优质的使用体验。

说明

推荐使用V2.0 SDK。若您使用的是V1.0 SDK，建议升级到V2.0 SDK，详细信息请参见[升级](https://help.aliyun.com/zh/sdk/developer-reference/upgrade-v1-sdk-guide)[V1.0 SDK](https://help.aliyun.com/zh/sdk/developer-reference/upgrade-v1-sdk-guide)[指南](https://help.aliyun.com/zh/sdk/developer-reference/upgrade-v1-sdk-guide)。

## SDK下载地址

ECS V2.0 SDK支持多种编程语言。您可以在OpenAPI门户获取SDK的安装方式，也可以在开源平台GitHub中查看源码及相关安装指引。建议使用各编程语言主流的依赖管理工具进行安装。

- 

- 

- 

- 

| 语言 | SDK 安装方式 | GitHub 地址 | 快速入门 |
| --- | --- | --- | --- |
| Java | [SDK for Java](https://api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=java-tea) [SDK for Java（异步）](https://api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=java-async-tea) | [alibabacloud-java-sdk/ecs-20140526](https://github.com/aliyun/alibabacloud-java-sdk/tree/master/ecs-20140526) [alibabacloud-java-async-sdk/ecs-20140526](https://github.com/aliyun/alibabacloud-java-async-sdk/tree/master/ecs-20140526) | [通过](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-sdk-through-the-ide) [IDE](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-sdk-through-the-ide) [使用阿里云](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-sdk-through-the-ide) [Java SDK](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-sdk-through-the-ide) |
| Go | [SDK for Go](https://api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=go-tea) | [alibabacloud-go/ecs-20140526](https://github.com/alibabacloud-go/ecs-20140526) | [通过](https://help.aliyun.com/zh/sdk/developer-reference/use-alibaba-cloud-go-sdk-through-ide) [IDE](https://help.aliyun.com/zh/sdk/developer-reference/use-alibaba-cloud-go-sdk-through-ide) [使用阿里云](https://help.aliyun.com/zh/sdk/developer-reference/use-alibaba-cloud-go-sdk-through-ide) [Go SDK](https://help.aliyun.com/zh/sdk/developer-reference/use-alibaba-cloud-go-sdk-through-ide) |
| Python | [SDK for Python](https://api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=python-tea) | [alibabacloud-python-sdk/ecs-20140526](https://github.com/aliyun/alibabacloud-python-sdk/tree/master/ecs-20140526) | [通过](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-python-sdk-through-the-ide) [IDE](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-python-sdk-through-the-ide) [使用阿里云](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-python-sdk-through-the-ide) [Python SDK](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-python-sdk-through-the-ide) |
| Node.js | [SDK for TypeScript](https://api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=typescript-tea) | [alibabacloud-typescript-sdk/ecs-20140526](https://github.com/aliyun/alibabacloud-typescript-sdk/tree/master/ecs-20140526) | [通过](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-node-js-sdk-through-the-ide) [IDE](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-node-js-sdk-through-the-ide) [使用阿里云](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-node-js-sdk-through-the-ide) [Node.js SDK](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-node-js-sdk-through-the-ide) |
| C# | [SDK for C#](https://api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=csharp-tea) | [alibabacloud-csharp-sdk/ecs-20140526](https://github.com/aliyun/alibabacloud-csharp-sdk/tree/master/ecs-20140526) | [通过](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-net-sdk-through-ide) [IDE](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-net-sdk-through-ide) [使用阿里云.NET SDK](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-net-sdk-through-ide) |
| PHP | [SDK for PHP](https://api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=php-tea) | [alibabacloud-sdk-php/ecs-20140526](https://github.com/alibabacloud-sdk-php/Ecs-20140526) | [通过](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-php-sdk-through-the-ide) [IDE](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-php-sdk-through-the-ide) [使用阿里云](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-php-sdk-through-the-ide) [PHP SDK](https://help.aliyun.com/zh/sdk/developer-reference/use-the-alibaba-cloud-php-sdk-through-the-ide) |
| C++ | [SDK for C++](https://api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=cpp-tea) | [alibabacloud-sdk-cpp/ecs-20140526](https://github.com/alibabacloud-sdk-cpp/ecs-20140526) | / |
| Swift | [SDK for Swift](https://api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=swift-tea) | [alibabacloud-sdk-swift/ecs-20140526](https://github.com/alibabacloud-sdk-swift/ecs-20140526) | / |


## 使用示例

以调用查询一台或多台ECS实例的详细信息接口为例，为您演示如何使用云服务器ECS SDK。

- 

[Java SDK](products/ecs/documents/developer-reference/use-sdk-for-java.md)[调用示例](products/ecs/documents/developer-reference/use-sdk-for-java.md)

- 

[Go SDK](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-go.md)[调用示例](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-go.md)

- 

[Python SDK](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-python.md)[调用示例](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-python.md)

- 

[Node.js SDK](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-node-js.md)[调用示例](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-node-js.md)

- 

[.NET SDK](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-net.md)[调用示例](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-net.md)

- 

[PHP SDK](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-php.md)[调用示例](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-php.md)

[上一篇：SDK参考](products/ecs/documents/developer-reference/ecs-sdk-reference.md)[下一篇：通过SDK创建并使用ECS实例](products/ecs/documents/developer-reference/use-an-sdk-to-create-ecs-instances.md)

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
