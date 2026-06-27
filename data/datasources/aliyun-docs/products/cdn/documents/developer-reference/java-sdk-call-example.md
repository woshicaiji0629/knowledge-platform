# Java SDK调用示例-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/developer-reference/java-sdk-call-example

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/cdn/documents/product-overview.md)

- [快速入门](products/cdn/documents/getting-started.md)

- [操作指南](products/cdn/documents/user-guide.md)

- [实践教程](products/cdn/documents/use-cases.md)

- [安全合规](products/cdn/documents/security-and-compliance.md)

- [开发参考](products/cdn/documents/developer-reference.md)

- [服务支持](products/cdn/documents/support.md)

- [视频专区](products/cdn/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# Java SDK调用示例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何使用阿里云Java语言SDK开发包，查询您账号下通过CDN加速的域名。

## 步骤一：查看OpenAPI文档

在调用OpenAPI前，建议您先阅读对应接口文档，了解、学习调用该接口所需要的参数及权限等，更多信息请参见[API](products/cdn/documents/developer-reference/api-cdn-2018-05-10-overview.md)[概览](products/cdn/documents/developer-reference/api-cdn-2018-05-10-overview.md)。

## 步骤二：创建RAM用户并完成授权

重要

阿里云账号拥有所有API的访问权限，建议您创建并使用RAM用户进行API访问或日常运维。

如您已创建RAM用户且已完成授权，可跳过此步骤。

- 

使用阿里云账号登录[RAM](https://ram.console.aliyun.com)[控制台](https://ram.console.aliyun.com)。

- 

创建RAM用户。

- 

在左侧导航栏，选择身份管理>用户。

- 

在用户页面，单击创建用户。

- 

在创建用户页面，设置登录名称和显示名称，设置访问方式为控制台访问和使用永久 AccessKey 访问，单击确定。

重要

RAM用户的AccessKey Secret只在创建时显示，不支持查看，请下载CSV文件后妥善保管。

创建RAM用户成功后，请记录用户登录名称和密码。在调用OpenAPI时，需要使用该RAM用户登录阿里云OpenAPI开发者门户，并使用该RAM用户的AccessKey进行代码调试。

- 

为RAM用户授权。

说明

创建RAM用户后，该RAM用户无任何操作CDN的权限。您需要为该RAM用户授予系统策略（AliyunCDNFullAccess、AliyunCDNReadOnlyAccess）或自定义策略。本案例以授予RAM用户AliyunCDNReadOnlyAccess策略为例，AliyunCDNReadOnlyAccess策略具备CDN资源的只读权限。

- 

在用户页面，单击目标RAM用户对应的添加权限。

- 

在新增授权面板，在系统策略中搜索选中AliyunCDNReadOnlyAccess，然后单击确认新增授权。

- 

确认授权结果，单击关闭。

## 步骤三：调用OpenAPI

- 

使用RAM用户登录[阿里云](https://next.api.aliyun.com/api/Cdn/2018-05-10/DescribeUserDomains?tab=DEBUG&params={%22DomainName%22:%22ipt.shuangxiao.top%22})[OpenAPI](https://next.api.aliyun.com/api/Cdn/2018-05-10/DescribeUserDomains?tab=DEBUG&params={%22DomainName%22:%22ipt.shuangxiao.top%22})[门户](https://next.api.aliyun.com/api/Cdn/2018-05-10/DescribeUserDomains?tab=DEBUG&params={%22DomainName%22:%22ipt.shuangxiao.top%22})。

- 

选择云产品为内容分发。

- 

在顶部菜单栏，选择工具中心>在线调试。

- 

在左侧导航栏，找到并单击DescribeUserDomains接口，服务地址选择华东1（杭州），DomainName参数输入要查询的域名，如果不输入会显示此账号下所有的域名。

- 

单击发起调用。

在调用结果区域，您可以看到查询结果、Request Header、Response Header等信息，状态码200表示调用成功。

## 步骤四：获取SDK示例代码

OpenAPI平台提供了多种编程语言（Java、Go、Python、Node.js、TypeScript、PHP、C++ 等）的SDK。开发者只需要集成SDK，通过SDK暴露的方法直接调用OpenAPI 。SDK统一封装了签名逻辑、超时机制、重试机制，并根据文档返回结构化 Response 对象，易于开发。

以获取Java SDK示例代码为例，其他语言获取方式相同。

- 

在SDK示例页签，选择SDK版本和SDK语言。推荐使用V2.0版本。关于V2.0和V1.0的区别，请参见[V1.0 SDK](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)[和](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)[V2.0 SDK](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)[区别](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)。

- 

单击下载完整工程可以下载完整的SDK工程。下载完后完成解压

说明

- 

在SDK示例显示区域的右上角，单击图标可以复制SDK示例代码。

- 

单击SDK信息，可以获取SDK包名称、SDK包版本、SDK包管理平台、SDK安装命令等基础信息，便于您集成开发。

## 步骤五：运行SDK示例代码

以运行Java SDK示例代码为例。

- 

打开IntelliJ IDEA，单击File->Open，选择解压后的工程文件夹，等待Maven自动安装依赖信息。

- 

在调用之前，需要先获取访问凭证AccessKey，建议使用前面创建的RAM用户AccessKey。更多信息，请参见[创建](products/ram/documents/user-guide/create-an-accesskey-pair.md)[RAM](products/ram/documents/user-guide/create-an-accesskey-pair.md)[用户的](products/ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](products/ram/documents/user-guide/create-an-accesskey-pair.md)。

重要

获取RAM用户的AccessKey之后，还需要在环境变量中设置AccessKey，具体操作步骤请参见[在](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Linux、macOS](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[和](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Windows](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[系统配置环境变量](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)。

- 

运行示例代码。

双击打开Sample，确认无报错后，运行代码。

- 

查看运行结果。在底部控制台按下ctrl+f，搜索statusCode，如果看到"statusCode":200表示调用成功。

[上一篇：SDK概览](products/cdn/documents/developer-reference/sdk-overview.md)[下一篇：Terraform集成CDN参考指南](products/cdn/documents/developer-reference/cdn-setup-with-terraform.md)

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
