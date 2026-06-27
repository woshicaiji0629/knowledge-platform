# 安装和使用Java V2.0 SDK调用API-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/developer-reference/use-sdk-for-java

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

# ECS Java V2.0 SDK调用示例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文以调用查询一台或多台ECS实例的详细信息（DescribeInstances）接口为例，为您介绍Java V2.0 SDK的安装和使用。

## 前提条件

- 

由于阿里云账号（主账号）拥有资源的所有权限，其AccessKey一旦泄露风险巨大，所以建议您使用满足最小化权限需求的RAM用户的AccessKey。具体操作方式请参见[创建](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair)[AccessKey](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair)。

- 

给RAM用户授予操作云服务器ECS相关资源的权限。本文提供的示例代码为查询示例，所以选择AliyunECSReadonlyAccess系统权限策略，您在使用的时候可以根据业务需求进行自定义授权。

- 

使用自定义权限策略。

关于如何创建自定义权限策略，请参见[创建自定义权限策略](https://help.aliyun.com/zh/ram/create-a-custom-policy#task-glf-vwf-xdb)和[授权信息](products/ecs/documents/developer-reference/api-ecs-2014-05-26-ram.md)。

云服务器ECS依据最佳实践提供了一些自定义权限策略示例，您可以参考这些示例以快速创建符合自身业务需求的自定义权限策略，具体详情请参见[云服务器](products/ecs/documents/user-guide/custom-policies-for-ecs.md)[ECS](products/ecs/documents/user-guide/custom-policies-for-ecs.md)[自定义权限策略参考](products/ecs/documents/user-guide/custom-policies-for-ecs.md)。

- 

使用系统权限策略。

云服务器ECS支持的所有系统权限策略及其对应的权限描述，请参见[云服务器 ECS](products/ecs/documents/user-guide/ecs.md)[系统权限策略参考](products/ecs/documents/user-guide/ecs.md)。

- 

在环境变量中配置AccessKey，具体操作步骤请参见[在](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Linux、macOS](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[和](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Windows](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[系统配置环境变量](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)。

## 安装SDK

Java SDK支持多种安装方式，本示例以Apache Maven安装方式为例，更多安装方式获取方式，请参见[SDK 中心](https://next.api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=java-tea&tab=primer-doc)。

打开Maven项目的pom.xml文件，在<dependencies>节点中加入依赖配置，并刷新Maven配置。

<dependency> <groupId>com.aliyun</groupId> <artifactId>ecs20140526</artifactId> <version>5.3.0</version> </dependency>

## 使用SDK

### 1. 初始化客户端

阿里云SDK支持多种访问凭据用于初始化客户端，例如AccessKey和STS Token等，更多方式请参见[管理访问凭据](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。本示例以通过AccessKey初始化客户端为例。

import com.aliyun.ecs20140526.Client; import com.aliyun.teaopenapi.models.Config; public class Sample { private static Client createClient() throws Exception { Config config = new Config() // 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。 .setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")) // 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。 .setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")) // Endpoint 请参考 https://api.aliyun.com/product/Ecs .setEndpoint("ecs.cn-hangzhou.aliyuncs.com"); return new Client(config); } }

### 2. 构建接口的请求对象

在构建请求对象之前，请查看该接口的[API](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)[文档](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)获取参数信息。

说明

请求对象命名规则：{API名称}Request，例如DescribeInstances该接口的请求对象为DescribeInstancesRequest。

// 构造请求对象 DescribeInstancesRequest request = new DescribeInstancesRequest().setRegionId("cn-hangzhou");

### 3. 发起调用

通过客户端调用OpenAPI时，支持设置运行时参数，例如超时配置、代理配置等，更多信息请查看[进阶配置](https://help.aliyun.com/zh/sdk/developer-reference/advanced-configuration/)。

说明

接口返回对象命名规则：{API名称}Response，例如DescribeInstances该接口的返回对象为DescribeInstancesResponse。

// 设置运行时参数 RuntimeOptions runtime = new RuntimeOptions(); // 调用 DescribeInstances 接口 DescribeInstancesResponse response = client.describeInstancesWithOptions(request, runtime); System.out.println(response.body.toMap());

### 4. 异常处理

Java SDK将异常进行了细致的分类，主要划分为TeaUnretryableException和TeaException。

- 

TeaUnretryableException：主要是因为网络问题造成，一般是网络问题达到最大重试次数后抛出。

- 

TeaException：主要以业务报错为主的异常。

建议采取合理的措施来处理异常，比如合理地传播异常、记录日志、尝试恢复等，以确保系统的健壮性和稳定性。

### 5. 完整示例

import com.aliyun.ecs20140526.Client; import com.aliyun.ecs20140526.models.DescribeInstancesRequest; import com.aliyun.ecs20140526.models.DescribeInstancesResponse; import com.aliyun.tea.TeaException; import com.aliyun.tea.TeaUnretryableException; import com.aliyun.teaopenapi.models.Config; import com.aliyun.teautil.models.RuntimeOptions; public class Sample { private static Client createClient() throws Exception { Config config = new Config() // 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。 .setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")) // 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。 .setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")) // Endpoint 请参考 https://api.aliyun.com/product/Ecs .setEndpoint("ecs.cn-hangzhou.aliyuncs.com"); return new Client(config); } public static void main(String[] args) { try { Client client = Sample.createClient(); // 构造请求对象 DescribeInstancesRequest request = new DescribeInstancesRequest() .setRegionId("cn-hangzhou"); // 设置运行时参数 RuntimeOptions runtime = new RuntimeOptions(); // 调用 DescribeInstances 接口 DescribeInstancesResponse response = client.describeInstancesWithOptions(request, runtime); System.out.println(response.body.toMap()); } catch (TeaUnretryableException ue) { // 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。 ue.printStackTrace(); // 打印错误信息 System.out.println(ue.getMessage()); // 打印请求记录，查询错误发生时的请求信息 System.out.println(ue.getLastRequest()); } catch (TeaException e) { // 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。 e.printStackTrace(); // 打印错误码 System.out.println(e.getCode()); // 打印错误信息，错误信息中包含 RequestId System.out.println(e.getMessage()); // 打印服务端返回的具体错误内容 System.out.println(e.getData()); } catch (Exception e) { // 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。 e.printStackTrace(); } } }

## 场景化示例

- 

[批量创建](https://api.aliyun.com/api-tools/demo/Ecs/806fd7fc-a916-4085-be13-d0f8b35a7aa8)[ECS](https://api.aliyun.com/api-tools/demo/Ecs/806fd7fc-a916-4085-be13-d0f8b35a7aa8)[实例](https://api.aliyun.com/api-tools/demo/Ecs/806fd7fc-a916-4085-be13-d0f8b35a7aa8)

- 

[ECS](https://api.aliyun.com/api-tools/demo/Ecs/8c4656ff-2710-4d74-b5cb-5f9593e13b4a)[实例列表查询](https://api.aliyun.com/api-tools/demo/Ecs/8c4656ff-2710-4d74-b5cb-5f9593e13b4a)

- 

[续费](https://api.aliyun.com/api-tools/demo/Ecs/09f1786e-106a-4726-b58c-909da95ea202)[ECS](https://api.aliyun.com/api-tools/demo/Ecs/09f1786e-106a-4726-b58c-909da95ea202)[实例](https://api.aliyun.com/api-tools/demo/Ecs/09f1786e-106a-4726-b58c-909da95ea202)

- 

[释放](https://api.aliyun.com/api-tools/demo/Ecs/f4643bff-a520-4c90-bee8-42edf8c9b071)[ECS](https://api.aliyun.com/api-tools/demo/Ecs/f4643bff-a520-4c90-bee8-42edf8c9b071)[实例](https://api.aliyun.com/api-tools/demo/Ecs/f4643bff-a520-4c90-bee8-42edf8c9b071)

- 

[查询可用的变配资源](https://api.aliyun.com/api-tools/demo/Ecs/b4e36cdf-2db4-4a79-ab88-075e1e154872)

- 

[查询抢占式实例库存](https://api.aliyun.com/api-tools/demo/Ecs/51a231f0-ee16-4731-80e2-6ba89957e6e1)

- 

[查询抢占式实例当前价格](https://api.aliyun.com/api-tools/demo/Ecs/65dabc40-8983-4d9a-b4ed-864e454941dd)

- 

[创建抢占式实例](https://api.aliyun.com/api-tools/demo/Ecs/adc4b58a-139e-4f4d-9df9-8033594485c4)

- 

[增加安全组规则](https://api.aliyun.com/api-tools/demo/Ecs/94406fd9-425f-443e-97f5-fdff3a0a8891)

- 

[新建安全组并将指定资源加入到安全组](https://api.aliyun.com/api-tools/demo/Ecs/d8a1f12d-4fa2-419f-a36c-9c907eff3a06)

- 

[创建弹性网卡](https://api.aliyun.com/api-tools/demo/Ecs/1d32980f-7dba-43e7-ab84-8684252fdadf)

- 

[附加弹性网卡](https://api.aliyun.com/api-tools/demo/Ecs/059b780d-9551-4ca3-8211-efeec3092bb6)

- 

[分离弹性网卡](https://api.aliyun.com/api-tools/demo/Ecs/01b7e0c3-9f1f-4532-aec3-f02926a21d6d)

- 

[删除弹性网卡](https://api.aliyun.com/api-tools/demo/Ecs/83a01923-5db8-4a56-a09d-65c0290f05b7)

- 

[变更](https://api.aliyun.com/api-tools/demo/Ecs/56ccacea-2cc5-431f-b6d5-5931c80c3968)[ECS](https://api.aliyun.com/api-tools/demo/Ecs/56ccacea-2cc5-431f-b6d5-5931c80c3968)[实例规格](https://api.aliyun.com/api-tools/demo/Ecs/56ccacea-2cc5-431f-b6d5-5931c80c3968)

- 

[调整实例的实例规格和公网带宽](https://api.aliyun.com/api-tools/demo/Ecs/9e85058e-bb8e-4f30-ba85-83f6b5633e8f)

- 

[指定实例规格获取一个或多个备选的实例规格](https://api.aliyun.com/api-tools/demo/Ecs/bc152ba0-369e-4327-a7eb-245d193e29d3)

- 

[通过备选实例规格创建](https://api.aliyun.com/api-tools/demo/Ecs/19532d20-fd67-4022-ad96-824cb8751b25)[ECS](https://api.aliyun.com/api-tools/demo/Ecs/19532d20-fd67-4022-ad96-824cb8751b25)[实例最佳实践](https://api.aliyun.com/api-tools/demo/Ecs/19532d20-fd67-4022-ad96-824cb8751b25)

## 更多内容

除了使用上述调用方式外，您还可以使用泛化调用方式调用ECS的OpenAPI，详细介绍请参见[泛化调用](https://help.aliyun.com/zh/sdk/developer-reference/generalized-call-java)。

若您当前使用的是V1.0 SDK，并希望进一步了解V1.0 SDK的相关内容，请参见[V1.0 Java SDK](https://help.aliyun.com/zh/sdk/developer-reference/v1-0-java-sdk/)。

[上一篇：通过SDK创建并使用ECS实例](products/ecs/documents/developer-reference/use-an-sdk-to-create-ecs-instances.md)[下一篇：Go SDK调用示例](products/ecs/documents/developer-reference/example-on-how-to-use-ecs-sdk-for-go.md)

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
