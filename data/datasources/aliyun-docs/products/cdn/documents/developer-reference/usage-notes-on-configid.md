# 使用ConfigId管理域名配置-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/developer-reference/usage-notes-on-configid

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

# ConfigId使用说明

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

调用BatchSetCdnDomainConfig、SetCdnDomainStagingConfig为域名配置功能时会生成ConfigId（功能配置ID，具有唯一性），通过指定ConfigId可更新或删除域名配置项。本文为您介绍ConfigId的生成、查询和使用方法。

## ConfigId使用说明

| 功能 | 接口调用说明 |
| --- | --- |
| 生成 ConfigId | 调用 [BatchSetCdnDomainConfig](products/cdn/documents/api-batchsetcdndomainconfig.md) 、 [SetCdnDomainStagingConfig](products/cdn/documents/api-setcdndomainstagingconfig.md) ，配置完成后生成 ConfigId。 |
| 查询 ConfigId | 调用 [DescribeCdnDomainConfigs](products/cdn/documents/api-describecdndomainconfigs.md) 、 [DescribeCdnDomainStagingConfig](products/cdn/documents/api-describecdndomainstagingconfig.md) ，查询结果返回对应配置的 ConfigId。 |
| 通过 ConfigId 更新配置项 | 调用 [BatchSetCdnDomainConfig](products/cdn/documents/api-batchsetcdndomainconfig.md) 、 [SetCdnDomainStagingConfig](products/cdn/documents/api-setcdndomainstagingconfig.md) ，通过指定 ConfigId 更新配置项。 |
| 通过 ConfigId 删除配置项 | 调用 [DeleteSpecificConfig](products/cdn/documents/api-deletespecificconfig.md) 、 [DeleteSpecificStagingConfig](products/cdn/documents/api-deletespecificstagingconfig.md) ，通过指定 ConfigId 删除配置项。 |


## 生成ConfigId

- 

配置单条规则：

- 

调用[BatchSetCdnDomainConfig](products/cdn/documents/api-batchsetcdndomainconfig.md)给某个域名创建某个功能配置时生成ConfigId，该API调用成功后返回该配置项的ConfigId。

- 

调用[SetCdnDomainStagingConfig](products/cdn/documents/api-setcdndomainstagingconfig.md)给某个域名创建某个功能配置时生成ConfigId，该API调用成功后不返回ConfigId，需要通过[DescribeCdnDomainStagingConfig](products/cdn/documents/api-describecdndomainstagingconfig.md)接口查询。

配置场景：假设加速域名为example.com，CDN节点在响应资源给客户端的时候，告知客户端该资源无需缓存。

示例：为域名example.com的功能set_resp_header配置规则：key=Cache-Control，value=no-cache。接口配置：

action: BatchSetCdnDomainConfig params: { "Functions": [{ "functionArgs": [{ "argName": "value", "argValue": "no-cache" }, { "argName": "key", "argValue": "Cache-Control" } ], "functionName": "set_resp_header" }], "domainNames": "example.com" } product: cdn

配置成功返回结果：返回ConfigId。

{ "code": "200", "data": { "DomainConfigList": { "DomainConfigModel": [ { "FunctionName": "set_resp_header", "DomainName": "example.com", "ConfigId": 19571990834**** } ] }, "RequestId": "4FF61A1D-E697-5E6C-9E5D-7D1E1529****" }, "httpStatusCode": "200", "requestId": "4FF61A1D-E697-5E6C-9E5D-7D1E1529****", "successResponse": true }

- 

配置多条规则：有的功能支持配置多条规则，如果要一次配置多条规则，可以参考如下示例。

示例：为域名example.aliyundoc.com的功能set_resp_header（配置响应头）同时配置以下两条规则：

- 

第一个规则：CDN节点在响应资源给客户端的时候，告知客户端该资源无需缓存。

参数配置如下：key=Cache-Control，value=no-cache

- 

第二个规则：CDN节点在响应资源给客户端的时候，告知客户端该资源的内容类型是文本类型。

参数配置如下：key=Content-Type，value=text/plain

接口配置：

action: BatchSetCdnDomainConfig params: { "domainNames": "example.aliyundoc.com", "functions": [ { "functionArgs": [ { "ArgValue": "Cache-Control", "ArgName": "key" }, { "ArgValue": "no-cache", "ArgName": "value" } ], "functionName": "set_resp_header" }, { "functionArgs": [ { "ArgValue": "Content-Type", "ArgName": "key" }, { "ArgValue": "text/plain", "ArgName": "value" } ], "functionName": "set_resp_header" } ] } product: cdn

配置成功，返回结果，两条不同的规则分别返回了不同的ConfigId。

{ "code":"200", "data":{ "DomainConfigList":{ "DomainConfigModel":[ { "FunctionName":"set_resp_header", "DomainName":"example.aliyundoc.com", "ConfigId":20953663204**** }, { "FunctionName":"set_resp_header", "DomainName":"example.aliyundoc.com", "ConfigId":20953663204**** } ] }, "RequestId":"69A79ACE-FD8E-5993-9CEA-7AAB2F08****" }, "httpStatusCode":"200", "requestId":"69A79ACE-FD8E-5993-9CEA-7AAB2F08****", "successResponse":true }

## 查询ConfigId

调用[DescribeCdnDomainConfigs](products/cdn/documents/api-describecdndomainconfigs.md)、[DescribeCdnDomainStagingConfig](products/cdn/documents/api-describecdndomainstagingconfig.md)，查询结果返回对应配置的ConfigId。

示例：查询域名example.aliyundoc.com的功能set_resp_header的配置。接口调用：

action: DescribeCdnDomainConfigs params: { "domainName": "example.aliyundoc.com", "functionNames": "set_resp_header" } product: cdn

返回结果：显示ConfigId。

{ "code": "200", "data": { "RequestId": "51B7DF03-A7AE-56ED-BF1E-D16F6A6B****", "DomainConfigs": { "DomainConfig": [{ "Status": "configuring", "FunctionName": "set_resp_header", "FunctionArgs": { "FunctionArg": [{ "ArgValue": "no-cache", "ArgName": "value" }, { "ArgValue": "Cache-Control", "ArgName": "key" } ] }, "ConfigId": 19572306654**** }] } }, "httpStatusCode": "200", "requestId": "51B7DF03-A7AE-56ED-BF1E-D16F6A6B****", "successResponse": true }

## 通过ConfigId更新配置项

调用[BatchSetCdnDomainConfig](products/cdn/documents/api-batchsetcdndomainconfig.md)、[SetCdnDomainStagingConfig](products/cdn/documents/api-setcdndomainstagingconfig.md)更新已有的配置，更新配置的时候指定该配置项对应的ConfigId即可。

配置场景：假设加速域名为example.com，CDN节点响应给客户端的资源由不缓存改为缓存1小时。

示例：为域名example.com的功能set_resp_header更新规则配置为：key=Cache-Control，value=max-age=3600。接口调用：

action: BatchSetCdnDomainConfig params: { "Functions": [ { "functionArgs": [ { "argName": "value", "argValue": "max-age=3600" }, { "argName": "key", "argValue": "Cache-Control" } ], "functionName": "set_resp_header", "ConfigId": 19571990834**** } ], "domainNames": "example.com" } product: cdn

## 通过ConfigId删除配置项

调用[DeleteSpecificConfig](products/cdn/documents/api-deletespecificconfig.md)、[DeleteSpecificStagingConfig](products/cdn/documents/api-deletespecificstagingconfig.md)删除某个配置，删除配置的时候指定该配置项对应的ConfigId即可。

示例：为域名example.aliyundoc.com删除功能set_resp_header上指定的规则配置。接口调用：

action: DeleteSpecificConfig params: { "ConfigId": 19571990834****, "functionName": "set_resp_header", "domainName": "example.aliyundoc.com" } product: cdn

[上一篇：域名配置功能函数](products/cdn/documents/developer-reference/parameters-for-configuring-features-for-domain-names.md)[下一篇：HTTP状态码说明](products/cdn/documents/developer-reference/http-status-code-description.md)

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
