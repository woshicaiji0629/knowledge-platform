# 调用API接口配置域名功能及功能参数用法-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/developer-reference/parameters-for-configuring-features-for-domain-names

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

# 域名配置功能函数

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

调用BatchSetCdnDomainConfig、SetCdnDomainStagingConfig可批量配置域名功能，本文为您介绍该API可以配置哪些功能及功能参数用法。

说明

- 

本文中介绍的功能均能够被以下接口引用：

- 

生产环境：[BatchSetCdnDomainConfig](products/cdn/documents/api-batchsetcdndomainconfig.md)、[DescribeCdnDomainConfigs](products/cdn/documents/api-describecdndomainconfigs.md)、[BatchDeleteCdnDomainConfig](products/cdn/documents/api-batchdeletecdndomainconfig.md)和[DescribeCdnUserDomainsByFunc](products/cdn/documents/api-describecdnuserdomainsbyfunc.md)。

- 

模拟环境：[SetCdnDomainStagingConfig](products/cdn/documents/api-setcdndomainstagingconfig.md)、[DescribeCdnDomainStagingConfig](products/cdn/documents/api-describecdndomainstagingconfig.md)、[RollbackStagingConfig](products/cdn/documents/api-rollbackstagingconfig.md)和[PublishStagingConfigToProduction](products/cdn/documents/api-publishstagingconfigtoproduction.md)。

- 

调用BatchSetCdnDomainConfig、SetCdnDomainStagingConfig可以实现域名的批量配置，并生成唯一的ConfigId，通过ConfigId可以实现对指定配置的更新和删除。具体使用方法，请参见[ConfigId](products/cdn/documents/developer-reference/usage-notes-on-configid.md)[使用说明](products/cdn/documents/developer-reference/usage-notes-on-configid.md)。

## 基本信息

ipv6

- 

功能说明：IPv6访问配置，该功能详细介绍请参见控制台配置说明[IPv6](products/cdn/documents/user-guide/configure-ipv6.md)[配置](products/cdn/documents/user-guide/configure-ipv6.md)。

- 

功能ID（FunctionID/FuncId）：194。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| switch | String | 是 | 是否开启 IPv6 访问： on：开启。 off：关闭。 | on |
| region | String | 是 | 开启 IPv6 功能的地区，支持星号（*）。 说明 星号（*）表示所有区域都开启 IPv6（目前仅支持针对所有区域都开启 IPv6，如果需要仅针对某个特定区域开启 IPv6，请 [填写信息](https://page.aliyun.com/form/act2017566026/index.htm) 申请）。 不传该参数，表示默认所有区域都开启 IPv6。 | * |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "switch", "argValue": "on" }, { "argName": "region", "argValue": "*" }], "functionName": "ipv6" }], "DomainNames": "example.com" }

## 回源配置

set_req_host_header

- 

功能说明：配置默认回源HOST，该功能详细介绍请参见控制台配置说明[配置默认回源](products/cdn/documents/user-guide/configure-the-default-origin-host.md)[HOST](products/cdn/documents/user-guide/configure-the-default-origin-host.md)。

- 

功能ID（FunctionID/FuncId）：18。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| domain_name | String | 是 | 回源 HOST 头内容。 | example.com |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "domain_name", "argValue": "example.com" }], "functionName": "set_req_host_header" }], "DomainNames": "example.com" }

forward_scheme

- 

功能说明：配置回源协议，该功能详细介绍请参见控制台配置说明[配置回源协议](products/cdn/documents/user-guide/configure-the-origin-protocol-policy.md)。

- 

功能ID（FunctionID/FuncId）：47。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启回源协议： on：开启。 off：关闭。 | on |
| scheme_origin | String | 否 | 回源类型，取值： http：CDN 以 HTTP 协议回源。 https：CDN 以 HTTPS 协议回源。 follow（跟随）：客户端以 HTTP 或者 HTTPS 协议请求 CDN，CDN 跟随客户端的协议请求源站。 说明 scheme_origin 不配置时，默认取值为 follow。 | follow |
| scheme_origin_port | String | 否 | 回源自定义端口，需要与 scheme_origin 参数搭配使用，取值： scheme_origin 取值为 http 时，只需要配置一个 HTTP 协议的回源端口，例如：80。 scheme_origin 取值为 https 时，只需要配置一个 HTTPS 协议的回源端口，例如：443。 scheme_origin 取值为 follow 时，需要同时配置 HTTP 协议和 HTTPS 协议的回源端口，中间用半角冒号（:）分隔，例如：80:443。 | 80:443 |


- 

配置示例一：CDN跟随客户端的请求协议回源，回源访问的端口为协议默认端口，即HTTP协议对应80端口，HTTPS协议对应443端口。

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "scheme_origin", "argValue": "follow" }], "functionName": "forward_scheme" }], "DomainNames": "example.com" }

- 

配置示例二：CDN跟随客户端的请求协议回源，回源访问的端口为自定义端口，HTTP协议对应8080端口，HTTPS协议对应443端口。

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "scheme_origin", "argValue": "follow" }, { "argName": "scheme_origin_port", "argValue": "8080:4433" }], "functionName": "forward_scheme" }], "DomainNames": "example.com" }

l2_oss_key

- 

功能说明：配置私有Bucket回源。注意，首次使用该功能时，需要进行默认权限策略的一键开启操作，开启后将会授予CDN产品对您同账号下OSS产品的所有Bucket的只读访问权限。该功能详细介绍请参见控制台配置说明[OSS](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[私有](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[Bucket](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[回源](products/cdn/documents/user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)。

- 

功能ID（FunctionID/FuncId）：85。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| private_oss_auth | String | 是 | 是否开启私有 Bucket 回源： on：开启。 off：关闭。 功能开启以后，系统会自动配置 STS 安全令牌，配置更简单，但是仅支持 CDN 域名回源到同一个阿里云账号下的 OSS 私有 Bucket。关于 STS 安全令牌更多信息，请参见 [什么是](products/ram/documents/user-guide/what-is-sts.md) [STS](products/ram/documents/user-guide/what-is-sts.md) 。 | on |
| perm_private_oss_tbl | String | 否 | 永久安全令牌配置，配置格式是 access_id=123 access_secret=123abc （中间用空格分隔）。 配置了永久安全令牌以后，除了支持 CDN 域名回源到同一个阿里云账号下的 OSS 私有 Bucket，还支持 CDN 域名回源到其他阿里云账号下的 OSS 私有 Bucket。关于永久安全令牌更多信息，请参见 [创建](products/ram/documents/user-guide/create-an-accesskey-pair.md) [AccessKey](products/ram/documents/user-guide/create-an-accesskey-pair.md) 。 | access_id=123 access_secret=123abc |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "private_oss_auth", "argValue": "on" },{ "argName": "perm_private_oss_tbl", "argValue": "access_id=123 access_secret=123abc" }], "functionName": "l2_oss_key" }], "DomainNames": "example.com" }

oss_key_list

- 

功能说明：OSS回源私钥列表，可以配置一条或者多条规则，代表多个不同的OSS私有Bucket与对应的安全令牌。

- 

功能ID（FunctionID/FuncId）：183。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| host | String | 是 | OSS Bucket 的完整地址。 | example.oss-cn-hangzhou.aliyuncs.com |
| key | String | 是 | 永久安全令牌配置，配置格式是 access_id=123 access_secret=123abc （中间用空格分隔）。 配置了永久安全令牌以后，除了支持 CDN 域名回源到同一个阿里云账号下的 OSS 私有 Bucket，还支持 CDN 域名回源到另一个阿里云账号下的 OSS 私有 Bucket。关于永久安全令牌更多信息，请参见 [创建](products/ram/documents/user-guide/create-an-accesskey-pair.md) [AccessKey](products/ram/documents/user-guide/create-an-accesskey-pair.md) 。 | access_id=123 access_secret=123abc |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "host", "argValue": "example.oss-cn-hangzhou.aliyuncs.com" },{ "argName": "key", "argValue": "access_id=123 access_secret=123abc" }], "functionName": "oss_key_list" }], "DomainNames": "example.com" }

https_origin_sni

- 

功能说明：配置回源SNI，该功能详细介绍请参见控制台配置说明[配置默认回源](products/cdn/documents/user-guide/configure-sni.md)[SNI](products/cdn/documents/user-guide/configure-sni.md)。

- 

功能ID（FunctionID/FuncId）：114。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enabled | String | 是 | 是否开启回源 SNI 功能： on：开启。 off：关闭。 | on |
| https_origin_sni | String | 是 | 回源请求携带的 SNI 信息（即回源请求需要访问的源站地址）。 | origin.example.com |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "https_origin_sni", "argValue": "origin.example.com" }, { "argName": "enabled", "argValue": "on" }], "functionName": "https_origin_sni" }], "DomainNames": "example.com" }

forward_timeout

- 

功能说明：配置回源请求超时时间，该功能详细介绍请参见控制台配置说明[配置回源](products/cdn/documents/user-guide/configure-a-timeout-period-for-back-to-origin-http-requests.md)[HTTP](products/cdn/documents/user-guide/configure-a-timeout-period-for-back-to-origin-http-requests.md)[请求超时时间](products/cdn/documents/user-guide/configure-a-timeout-period-for-back-to-origin-http-requests.md)。

- 

功能ID（FunctionID/FuncId）：124。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| forward_timeout | Integer | 是 | 请求超时时间，单位：秒。 说明 建议设置时间小于 100 秒。 | 30 |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "forward_timeout", "argValue": "30" }], "functionName": "forward_timeout" }], "DomainNames": "example.com" }

advanced_origin

- 

功能说明：配置高级回源，该功能详细介绍请参见控制台配置说明[高级回源](products/cdn/documents/user-guide/configure-advanced-origin-settings.md)。

- 

功能冲突说明：高级回源功能与条件源站功能（功能函数：origin_dns_host，功能ID：212）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：235。

- 

参数说明：

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| variable_type | String | 是 | 变量类型，取值： header：用户请求中携带的 header（request header）。 arg：用户请求 URL 中携带的参数（query string parameter）。 uri：用户请求 URL 中携带的路径（path）。 cookie：用户请求中携带的 cookie（request cookie）。 | uri |
| variable | String | 是 | 变量名称。 说明 variable_type=uri 的情况下，variable 只能固定=uri。 | uri |
| conditions | String | 是 | 条件，取值： ==：表示“等于”。 !=：表示“不等于”。 | == |
| value | String | 是 | 变量的取值。 | /image |
| origin | String | 是 | 回源查询 DNS 使用的域名（即用户请求中对应的变量值，匹配后需要回源到指定的源站地址）。 | origin.example.com |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "conditions", "argValue": "==" }, { "argName": "variable_type", "argValue": "uri" }, { "argName": "value", "argValue": "/image" }, { "argName": "origin", "argValue": "origin.example.com" }, { "argName": "variable", "argValue": "uri" }], "functionName": "advanced_origin" }], "DomainNames": "example.com", }

follow_302

- 

功能说明：配置回源302跟随，该功能详细介绍请参见控制台配置说明[配置回源](products/cdn/documents/user-guide/configure-301-or-302-redirection.md)[301/302](products/cdn/documents/user-guide/configure-301-or-302-redirection.md)[跟随](products/cdn/documents/user-guide/configure-301-or-302-redirection.md)。

- 

功能ID（FunctionID/FuncId）：219。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启回源 302 跟随： on：开启。 off：关闭。 | on |
| max_tries | Integer | 否 | 302 跟随次数上限。 默认值：2。 取值范围：[1,5]。 说明 回源次数-1（次）=302 跟随次数，即默认的回源次数上限为 3，可配置范围是[2,6]。 | 2 |
| retain_args | String | 否 | 302 跟随时是否保留原请求参数返回目标源： on：保留。 off（默认）：不保留。 | off |
| retain_header | String | 否 | 302 跟随时是否保留原请求头回目标源： on：保留。 off（默认）：不保留。 | off |
| response_header | String | 否 | 302 跟随响应头，表示源站给 CDN 的 302 跟随响应头的名称，该响应头名称默认为 Location。 | X-Alicdn-Redirect |
| retain_host | String | 否 | 302 跟随保留回源域名，当开启时，表示 CDN 在 302 跟随时保留回源域名，只在跟随到目标域名时生效。可以配置的值为： on：开启 off（默认）：关闭 | off |
| modify_host | String | 否 | 302 跟随修改回源域名，表示 CDN 在 302 跟随时修改回源域名，只在跟随到目标域名时生效。默认情况下不修改回源域名。 | example.com |
| cache | String | 否 | 302 跟随缓存跟随结果，当开启时，表示 CDN 在 302 跟随时缓存同 URL 的跟随结果，提升 CDN 的响应性能。可以配置的值为： on：开启 off（默认）：关闭 | off |
| expired_time | Integer | 否 | 302 跟随缓存跟随结果的超时时间，表示 CDN 在 302 跟随时缓存同 URL 的跟随结果的超时时间，需要配合缓存功能一起使用，单位秒，默认：3600 秒 | 7200 |
| follow_origin_host | String | 否 | 302 跟随回源 host 使用源站域名，当开启时，表示 CDN 会使用源站域名作为回源 host（即使主备切换也会使用最新的源站域名）。可以配置的值为： on：开启 off（默认）：关闭 | off |
| follow_5xx_retry_origin | String | 否 | 源站主备切换，当开启时，表示 CDN 如果收到源站响应的 5xx 状态码，会切换到下一个可用的源站。可以配置的值为： on：开启 off（默认）：关闭 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "max_tries", "argValue": 2 }, { "argName": "retain_args", "argValue": "off" }, { "argName": "retain_header", "argValue": "off" }, { "argName": "response_header", "argValue": "X-Alicdn-Redirect" }, { "argName": "retain_header", "argValue": "off" }, { "argName": "modify_host", "argValue": "example.com" }, { "argName": "cache", "argValue": "off" }, { "argName": "expired_time", "argValue": "7200" }, { "argName": "follow_origin_host", "argValue": "off" }, { "argName": "follow_5xx_retry_origin", "argValue": "off" }], "functionName": "follow_302" }], "DomainNames": "example.com" }

set_req_header

- 

功能说明：配置自定义回源HTTP头，该功能详细介绍请参见控制台配置说明[修改入站请求头](products/cdn/documents/configure-custom-request-headers-old.md)。

说明

set_req_header是v1版本，建议您使用v2版本：origin_request_header，v2版本支持更丰富的自定义回源HTTP头功能。

- 

功能ID（FunctionID/FuncId）：39。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| key | String | 是 | 回源头名称。 | Accept-Encoding |
| value | String | 是 | 回源头的值。如果要删除某个回源头，设置回源头的值为 null。 | gzip |


- 

配置示例一：添加一个回源HTTP请求头。

{ "Functions": [{ "functionArgs": [{ "argName": "value", "argValue": "gzip" }, { "argName": "key", "argValue": "Accept-Encoding" }], "functionName": "set_req_header" }], "DomainNames": "example.com" }

- 

配置示例二：删除一个回源HTTP请求头（将value值设置为null）。

{ "Functions":[{ "functionArgs":[{ "argName":"value", "argValue":"null" }, { "argName":"key", "argValue":"User-Agent" }], "functionName":"set_req_header" }], "DomainNames":"example.com" }

origin_request_header

- 

功能说明：配置回源HTTP请求头（新），该功能详细介绍请参见控制台配置说明[修改出站请求头](products/cdn/documents/user-guide/configure-custom-request-headers.md)。

- 

功能ID（FunctionID/FuncId）：228。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| header_operation_type | String | 是 | 请求头操作，取值： add：添加。 delete：删除。 modify：变更。 rewrite：替换。 | add |
| header_name | String | 是 | 请求头名称。 | Accept-Encoding |
| header_value | String | 否 | 请求头值。一个请求头参数中可以配置多个值，多个值用英文逗号（,）分隔。 | gzip |
| duplicate | String | 否 | 是否允许重复添加名称相同的请求头。当 header_operation_type 使用 add 时（即执行增加操作），需要设置是否允许重复： on：允许。 off：不允许。 | off |
| header_source | String | 否 | 查找需要替换的参数值。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置该参数，取值支持正则表达式。 | value1 |
| header_destination | String | 否 | 替换后的参数值。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置该参数。 | value123 |
| match_all | String | 否 | 设置匹配模式。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置匹配模式： on：匹配所有（所有匹配上的值都会被替换）。 off：仅匹配第一个（只有第一个匹配上的值会被替换）。 | off |


- 

配置示例：为加速域名example.com添加自定义回源请求头，请求头名称=Accept-Encoding，请求头值=gzip。

{ "Functions": [{ "functionArgs": [{ "argName": "header_operation_type", "argValue": "add" }, { "argName": "header_name", "argValue": "Accept-Encoding" }, { "argName": "header_value", "argValue": "gzip" }, { "argName": "duplicate", "argValue": "off" }], "functionName": "origin_request_header" }], "DomainNames": "example.com" }

origin_response_header

- 

功能说明：配置回源HTTP响应头，该功能详细介绍请参见控制台配置说明[修改入站响应头](products/cdn/documents/user-guide/rewrite-http-response-headers.md)。

- 

功能ID（FunctionID/FuncId）：229。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| header_operation_type | String | 是 | 响应头操作，取值： add：添加。 delete：删除。 modify：变更。 rewrite：替换。 | add |
| header_name | String | 是 | 响应头名称。 | Cache-Control |
| header_value | String | 否 | 响应头值。一个响应头参数中可以配置多个值，多个值用英文逗号（,）分隔。 | no-cache |
| duplicate | String | 否 | 是否允许重复添加名称相同的响应头。当 header_operation_type 使用 add 时（即执行增加操作），需要设置是否允许重复： on：允许重复。 off：不允许重复。 | off |
| header_source | String | 否 | 查找需要替换的参数值。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置该参数，取值支持正则表达式。 | value1 |
| header_destination | String | 否 | 替换后的参数值。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置该参数。 | value123 |
| match_all | String | 否 | 匹配模式。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置匹配模式： on：匹配所有（所有匹配上的值都会被替换）。 off：仅匹配第一个（只有第一个匹配上的值会被替换）。 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "header_operation_type", "argValue": "add" }, { "argName": "header_name", "argValue": "Cache-Control" }, { "argName": "header_value", "argValue": "no-cache" }, { "argName": "duplicate", "argValue": "off" }], "functionName": "origin_response_header" }], "DomainNames": "example.com" }

back_to_origin_url_rewrite

- 

功能说明：改写回源URI，该功能详细介绍请参见控制台配置说明[重写回源路径](products/cdn/documents/user-guide/rewrite-urls-in-back-to-origin-requests.md)。

- 

功能ID（FunctionID/FuncId）：225。

- 

参数说明：

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| source_url | String | 是 | 被重写的 URI。 | ^/hello$ |
| target_url | String | 是 | 重写的目标 URI。 | /hello/test |
| flag | String | 否 | 改写操作的执行规则，取值： 空：执行完该条规则后，后续 rewrite 规则会继续执行。 break：执行完该条规则后，后续 rewrite 规则不再执行。 enhance_break：类似 break，区别在于会带着参数一起进行处理，并且针对 flv 直播也会生效。 | break |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "flag", "argValue": "break" }, { "argName": "source_url", "argValue": "^/hello$" }, { "argName": "target_url", "argValue": "/hello/test" }], "functionName": "back_to_origin_url_rewrite" }], "DomainNames": "example.com", }

back_to_origin_argument_rewrite

- 

功能说明：改写回源参数，该功能详细介绍请参见控制台配置说明[重写回源参数](products/cdn/documents/user-guide/rewrite-url-parameters-in-back-to-origin-requests.md)。

说明

回源参数改写，改写的是回源请求URL的查询参数，支持配置多个不同的改写规则，改写动作的优先级为添加参数＞删除参数＞仅保留＞修改参数。当不同的改写规则作用于同一个参数时，只有高优先级的规则会生效。

- 

功能ID（FunctionID/FuncId）：224。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| delete_argument | String | 否 | 删除参数列表，多个参数用空格分隔。 | code1 |
| save_argument | String | 否 | 保留参数列表，多个参数用空格隔开。仅保留列出的参数，添加参数和删除参数仍会生效。 | 空 |
| ignore_all_argument | String | 否 | 是否忽略所有参数： on：忽略所有参数，除了添加参数功能仍能生效以外，删除参数、仅保留、修改参数功能都将失效。 off（默认）：关闭忽略所有参数功能，保留参数、添加参数、删除参数仍会生效。 | on |
| add_argument | String | 否 | 添加参数，优先级最高，多个参数用空格隔开。 | value=123 |
| modify_argument | String | 否 | 修改参数，优先级最低，若参数被删除则不会保留，多个参数用空格隔开。 | value=321 |
| enable | String | 是 | 是否开启改写回源参数： on：开启。 off：关闭 。 | on |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "delete_argument", "argValue": "" }, { "argName": "save_argument", "argValue": "" }, { "argName": "add_argument", "argValue": "" }, { "argName": "modify_argument", "argValue": "" }, { "argName": "ignore_all_argument", "argValue": "on" }, { "argName": "enable", "argValue": "on" }], "functionName": "back_to_origin_argument_rewrite" }], "DomainNames": "example.com" }

aws_s3_bucket

- 

功能说明：配置Amazon S3鉴权Bucket。

- 

功能ID（FunctionID/FuncId）：186。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enabled | String | 是 | 是否开启 Amazon S3 鉴权 Bucket： l2：开启。 off：关闭。 | l2 |
| bucketname | String | 否 | Amazon S3 Bucket 名称。 | / |
| accesskey | String | 是 | AWS AccessKey。 | 123456789 |
| secretkey | String | 是 | AWS SecretKey。 | 12345678 |
| region | String | 是 | Amazon S3 存储区域。 | us-east-2 |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enabled", "argValue": "l2" }, { "argName": "accesskey", "argValue": "123456789" }, { "argName": "secretkey", "argValue": "123456789" }, { "argName": "region", "argValue": "us-east-2" }], "functionName": "aws_s3_bucket" }], "DomainNames": "example.com" }

origin_certificate_verification

- 

功能说明：配置回源证书校验（SNI白名单），该功能详细介绍请参见控制台配置说明[Common Name](products/cdn/documents/user-guide/common-name-whitelist.md)[白名单](products/cdn/documents/user-guide/common-name-whitelist.md)。

- 

功能ID（FunctionID/FuncId）：223。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enabled | String | 是 | 是否启用回源证书校验： on：启用。 off：关闭。 | on |
| common_name_whitelist | String | 否 | 证书白名单域名列表，支持配置多个域名，多个域名之间使用英文逗号（,）分隔。匹配了这些白名单域名的证书可以通过校验。 | example.com |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "common_name_whitelist", "argValue": "example.com" }], "functionName": "origin_certificate_verification" }], "DomainNames": "example.com" }

origin_dns_host

- 

功能说明：配置条件源站，可以通过与规则引擎功能（功能函数：condition，功能ID：250）配合使用，实现基于用户请求中的路径、URL参数、请求头等信息来回源到指定源站。该功能详细介绍请参见控制台配置说明[配置条件源站](products/cdn/documents/user-guide/configure-a-conditional-origin.md)。

- 

前提条件：在添加条件源站配置之前，您需要至少先创建一条规则引擎的规则条件，在添加条件源站配置时，您必须配置一条关联的规则条件，具体请参见[规则引擎](products/cdn/documents/developer-reference/parameters-for-configuring-features-for-domain-names.md)。如果添加条件源站配置时没有关联规则条件，则会使CDN回源的所有流量都指向这个唯一的源站地址（也就失去了通过规则条件来控制回源地址的意义）。

- 

功能冲突说明：条件源站功能与高级回源功能（功能函数：advanced_origin，功能ID：235）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：212。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ali_origin_dns_host | String | 是 | 回源查询 DNS 使用的域名。 | example.com |


- 

配置示例：通过设置parentid来引用已经使用规则引擎功能（功能函数：condition，功能ID：250）创建好的某个规则条件（通过添加配置时生成的configid来引用），实现在用户请求命中这个规则条件的情况下，回源到指定的源站地址。

{ "Functions": [{ "functionArgs": [{ "argName": "ali_origin_dns_host", "argValue": "example.com" }], "functionName": "origin_dns_host", "parentId":30119730104**** }], "DomainNames": "example.com" }

origin_host

- 

功能说明：配置指定源站回源HOST，可以对指定源站设置指定的回源HOST，该功能详细介绍请参见控制台配置说明[指定源站回源](products/cdn/documents/user-guide/specify-an-origin-host-for-each-origin.md)[HOST](products/cdn/documents/user-guide/specify-an-origin-host-for-each-origin.md)。

- 

功能ID（FunctionID/FuncId）：242。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| origin | String | 是 | 指定源站地址（也可以不指定源站地址，不指定源站地址时，参数 origin 的值设置为 all，代表所有源站）。 | example.com |
| host | String | 是 | 指定 HOST（也可以不指定 HOST，参数 host 的值设置为 ali_follow_origin 代表跟随源站地址作为 host 值）。 | host.example.com |


- 

配置示例一：用户请求回源到源站example.com时，使用的host值为host.example.com。

{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "example.com" }, { "argName": "host", "argValue": "host.example.com" }], "functionName": "origin_host" }], "DomainNames": "example.com" }

- 

配置示例二：用户回源到所有的源站（源站值用all来代表）都是用同一个host值host.example.com。

{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "host", "argValue": "host.example.com" }], "functionName": "origin_host" }], "DomainNames": "example.com" }

- 

配置示例三：用户回源到所有的源站（源站值用all来代表）都跟随源站地址作为host值（用ali_follow_origin来表示）。

{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "host", "argValue": "ali_follow_origin" }], "functionName": "origin_host" }], "DomainNames": "example.com" }

ali_origin_port_scheme

- 

功能说明：配置回源端口和协议。

- 

功能ID（FunctionID/FuncId）：276。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| port | String | 是 | 回源端口。 说明 当 scheme 设置为 follow 时，需填写 http:80|https:443 这样的格式。 | 80 |
| scheme | String | 是 | 回源协议：自定义回源协议（支持 http、https、follow、https_sm、follow_sm）。 http：按照 HTTP 协议回源。 https：按照 HTTPS 协议回源，采用国际算法。 follow：回源协议跟随（使用 HTTPS 协议回源时，仅支持国际算法）。 客户端采用 HTTP 协议，按照 HTTP 协议回源。 客户端采用 HTTPS 协议。 客户端为国际算法，按照 HTTPS 协议回源，采用国际算法。 客户端为国密算法，按照 HTTPS 协议回源，采用国际算法。 https_sm：按照 HTTPS 协议回源，采用国密算法。 follow_sm：回源协议跟随（使用 HTTPS 协议回源时，既支持国际算法，也支持国密算法）。 客户端采用 HTTP 协议，按照 HTTP 协议回源。 客户端采用 HTTPS 协议。 客户端为国际算法，按照 HTTPS 协议回源，采用国际算法。 客户算作国密算法，按照 HTTPS 协议回源，采用国密算法。 说明 国际算法指的是国际标准的加密算法，国密算法指的是中国国家密码管理局认定的国产加密算法。 | http |


- 

配置示例一：回源协议设置为http，回源端口设置为80。

{ "Functions": [{ "functionArgs": [{ "argName": "port", "argValue": "80" }, { "argName": "scheme", "argValue": "http" }], "functionName": "ali_origin_port_scheme" }], "DomainNames": "example.com" }

- 

配置示例二：回源协议follow用户请求使用的协议，使用HTTP协议回源时，回源到源站的80端口，使用HTTPS协议回源时，回源到源站的443端口。

{ "Functions":[{ "functionArgs": [{ "argName": "port", "argValue": "http:80|https:443" }, { "argName": "scheme", "argValue": "follow" }], "functionName":"ali_origin_port_scheme" }], "DomainNames":"example.com" }

origin_sni

- 

功能说明：配置指定源站回源SNI，可以对指定源站设置指定的回源SNI。

- 

功能ID（FunctionID/FuncId）：262。

- 

参数说明：

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| origin | String | 是 | 源站地址（也可以不指定源站地址，不指定源站地址的时候，参数 origin 的值设置为 all）。 | example.com |
| sni_host | String | 是 | sni host 值： 可以设置为固定值，例如： example.org 。 跟随源站地址作为 SNI，设置为 ali_follow_origin 。 跟随回源 host 作为 SNI，设置为 ali_follow_host 。 | example.org |
| keepalive_sni | String | 否 | 是否开启长连接 SNI 匹配： on：开启。 off：关闭。 说明 开启后，不同回源 SNI 将使用不同长连接。 | / |


- 

配置示例一：用户请求回源到源站origin.example.com时，使用的SNI值为host.example.com。

{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "origin.example.com" }, { "argName": "sni_host", "argValue": "host.example.com" }], "functionName": "origin_sni" }], "DomainNames": "example.com" }

- 

配置示例二：用户回源到所有的源站（源站值用all来表示）都使用同一个SNI值host.example.com。

{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "sni_host", "argValue": "host.example.com" }], "functionName":"origin_sni" }], "DomainNames":"example.com" }

- 

配置示例三：用户回源到所有的源站（源站值用all来表示）都跟随源站地址作为SNI值（使用参数值ali_follow_origin来表示）。

{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "sni_host", "argValue": "ali_follow_origin" }], "functionName": "origin_sni" }], "DomainNames": "example.com" }

- 

配置示例四：用户回源到所有的源站（源站值用all来表示）都跟随回源host作为SNI值（使用参数值ali_follow_host来表示）。

{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "sni_host", "argValue": "ali_follow_host" }], "functionName": "origin_sni" }], "DomainNames": "example.com" }

source_group

- 

功能说明：源站组设置。

- 

功能ID（FunctionID/FuncId）：294。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| source_group_name | String | 是 | 源站组名称，支持小写英文字母、数字和下划线，最大长度不超过 128 个字节。 | example_origin |
| source_info | String | 是 | 源站信息，格式为 源站地址_优先级_权重_端口 ，不同参数值之间用下划线分隔，多个源站之间用英文逗号（,）分隔。 源站地址：支持 IPv4、IPv6、域名。 优先级：支持 1~65535（值越小优先级越高）。 权重：支持 1~100（CDN 回源的时候将按照源站权重来分配发送给不同源站的请求比例）。 端口：支持 1~65535。 | 单个源站：192.168.0.1_10_33_80 多个源站：192.168.0.1_10_33_80,192.0.2.1_10_67_80 |
| retry_times | Integer | 否 | 回源重试次数。 | 3 |
| retry_status_rule | Integer | 否 | 回源重试状态码，目前仅支持配置以下五种：4xx、5xx、404、404-or-5xx、4xx-or-5xx，配置其中一个即可。 | 404-or-5xx |
| failback_source | String | 否 | 备份使用基础源信息，取值： on：在源站组内的所有源站都不可用的情况下，将会使用 基本配置-源站信息 里面的源站地址。 off：在源站组内的所有源站都不可用的情况下，将会直接给客户端返回表示源站不可用的 5xx 状态码。 | on |


说明

回源重试逻辑：

- 

重试次数：回源重试的次数。

- 

回源重试只会在同一个源站组内的不同IP地址之间进行重试。

- 

实际最大重试次数受限于同一个源站组内的可用IP数量。

- 

如果不配置重试次数retry_times，默认重试次数是在3次和可用源站IP数之间取最小值。

- 

如果配置重试次数retry_times，则在配置的重试次数和可用源站IP数之间取最小值。

- 

重试状态码：节点在收到某种状态码的时候进行重试。

- 

如果不配置重试状态码retry_status_rule，默认在源站响应5xx状态码的时候进行重试。

- 

如果配置重试状态码retry_status_rule，将会按照配置的状态码进行故障转移重试。重试状态码目前仅支持配置以下五种：4xx、5xx、404、404-or-5xx、4xx-or-5xx，配置其中一个即可。

- 

配置重试状态码retry_status_rule后，默认5xx状态码仍生效。例如配置了404，则CDN节点收到404或者5xx的时候都会进行重试。

- 

回源重试顺序：按照同一个源站组内IP地址的优先级从高到低进行重试。

- 

回源超时场景：源站主动响应重试状态码的时候，CDN节点收到重试状态码之后就会重试。如果没有收到源站主动响应的重试状态码，则会遵循超时时间处理流程，达到超时时间之后就会触发CDN节点重试。

- 

源站TCP建连超时：10秒。

- 

源站写超时：30秒（源站建立建连接写入内容超时）。

- 

源站读超时：30秒（源站建立建连接在一定时间内没有把CDN节点请求的内容完整响应回去）。

- 

源站探测逻辑：

- 

四层连接异常：如果CDN节点与某个源站IP四层连接失败，会把该源站IP放到一个dead table中，这样后续的回源请求就不会去访问这个源站IP；此后CDN节点会每隔5秒对该源站IP进行四层探测，如果建立建连接功，则将该源站IP恢复到可用列表中。

- 

四层连接正常：如果CDN节点与源站IP四层连接正常，但收到源站响应的重试状态码（例如：5xx），此时虽然会触发重试的逻辑，但该源站IP仍然在可用列表中，下次访问还会按权重请求该源站（即四层连接正常的情况下，七层异常不会主动屏蔽源站IP，如果需要主动屏蔽源站IP，则需要另外配置“回源7层监控检查”功能）。

- 

配置示例：

{ "Functions":[{ "functionArgs":[{ "argName":"source_group_name", "argValue":"test_yidong" },{ "argName":"source_info", "argValue":"192.168.0.1_10_33_80,192.0.2.1_10_67_80" },{ "argName":"retry_times", "argValue":"3" },{ "argName":"retry_status_rule", "argValue":"404,502" },{ "argName":"failback_source", "argValue":"on" }], "functionName":"source_group" }], "DomainNames":"example.com" }

ipv6_origin

- 

功能说明：配置IPv6回源，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-back-to-origin-routing-over-ipv6.md)[IPv6](products/cdn/documents/user-guide/configure-back-to-origin-routing-over-ipv6.md)[回源](products/cdn/documents/user-guide/configure-back-to-origin-routing-over-ipv6.md)。

- 

功能ID（FunctionID/FuncId）：265

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启 IPv6 回源功能。 on：开启。 off：关闭。 说明 开启 IPv6 回源功能后，CDN 回源侧将提供 IPv6 服务。 CDN 节点和源站都具备可用的 IPv6 地址，则使用 IPv6 建立建连接 以下场景使用 IPv4 建立建连接 CDN 节点不具备可用的 IPv6 地址。 源站不具备可用的 IPv6 地址。 CDN 节点和源站都不具备可用的 IPv6 地址。 | on |
| follow | String | 是 | 是否开启回源跟随客户端 IP 协议版本功能。 on：开启。 off：关闭。 说明 开启回源跟随客户端 IP 协议版本功能后，CDN 回源将会跟随客户端请求使用的 IP 协议版本。 客户端请求使用 IPv6，则 CDN 优先回源 IPv6 源站，如果没有 IPv6 源站，则使用 IPv4 源站。 客户端请求使用 IPv4，则 CDN 优先回源 IPv4 源站，如果没有 IPv4 源站，则使用 IPv6 源站。 | on |
| ipv6_v4_mix_used | String | 否 | 是否开启“源站 IPv4 地址/IPv6 地址轮询”功能。 on：开启。 off：关闭。 说明 “源站 IPv4 地址/IPv6 地址轮询”功能与“IPv6 回源”、“回源跟随客户端 IP 协议版本”这两个功能是互斥的，“回源 v4/v6 轮询”功能一旦开启，“IPv6 回源”、“回源跟随客户端 IP 协议版本”这两个功能就会失效。 “源站 IPv4 地址/IPv6 地址轮询”功能的作用是不论客户端请求使用的是 IPv4 还是 IPv6，也不论源站有几个 IPv4 地址、几个 IPv6 地址，都会统一使用轮询方式回源到各个源站地址。 如果 IPv4、IPv6 地址配置了权重比例，那么还会按照权重比例回源。 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" },{ "argName": "follow", "argValue": "on" }], "functionName": "ipv6_origin" }], "DomainNames": "example.com" }

cos_auth

- 

功能说明：配置腾讯云COS云存储的鉴权Bucket。

- 

功能ID（FunctionID/FuncId）：288。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启腾讯云 COS 云存储鉴权 Bucket： on：开启。 off：关闭。 | on |
| cos_valid_period | String | 否 | 鉴权签名的有效时间，单位为秒，不填默认为 3600 秒。 | / |
| cos_secret_id | String | 是 | 腾讯云的鉴权 ID。 | 123456789 |
| cos_secret_key | String | 是 | 腾讯云的鉴权密钥。 | 12345678 |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "cos_secret_id", "argValue": "123456789" }, { "argName": "cos_secret_key", "argValue": "123456789" }], "functionName": "cos_auth" }], "DomainNames": "example.com" }

oss_auth

- 

功能说明：用于配置CDN回源OSS使用的鉴权bucket信息。

- 

功能ID（FunctionID/FuncId）：10。

- 

注意事项：在给加速域名配置了OSS类型的源站地址之后，平台将会自动添加oss_auth配置，无需用户手动添加，也请用户注意不要误删该配置，否则会引起OSS源站无法实现对CDN回源流量的计费减免，在开启OSS私有bucket鉴权的情况下，还会导致CDN回源OSS私有bucket鉴权失败。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| oss_bucket_id | String | 是 | OSS bucket 的公网域名地址。 | cdn-test.oss-cn-hongkong.aliyuncs.com |
| oss_pri_buckets | String | 是 | OSS bucket 的公网域名地址及其对应的 bucket 名称。 | cdn-test.oss-cn-hongkong.aliyuncs.com|cdn-test |


- 

配置示例：

{ "Functions": [ { "ArgValue": "cdn-test.oss-cn-hongkong.aliyuncs.com", "ArgName": "oss_bucket_id" }, { "ArgValue": "cdn-test.oss-cn-hongkong.aliyuncs.com|cdn-test", "ArgName": "oss_pri_buckets" } ], "functionName": "oss_auth" }], "DomainNames": "example.com" }

## 缓存配置

filetype_based_ttl_set

- 

功能说明：配置文件过期时间，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[CDN](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[缓存过期时间](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)。

- 

功能ID（FunctionID/FuncId）：6。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ttl | Integer | 是 | 缓存时间，单位为秒，取值范围是 1~99999999（3 年多一些）。 | 500000 |
| file_type | String | 是 | 文件类型，区分大小写。多个文件类型用半角逗号（,）分隔。例如 jpg,txt。 | jpg |
| weight | Integer | 否 | 权重。取值：1~99。 说明 默认为 1，数字越大优先级越高。 | 1 |
| swift_origin_cache_high | String | 否 | 源站响应缓存策略优先，当开启时，表示在源站响应缓存相关头（比如 Cache-Control、Pragma 等）的时候，源站的缓存策略优先生效。可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_no_cache_low | String | 否 | 忽略源站不缓存响应头，当开启时，表示忽略源站的以下响应头（均表示不缓存）。 Cache-Control: no-store Cache-Control: no-cache Cache-Control: max-age=0 Pragme: no-cache 可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_follow_cachetime | String | 否 | 客户端跟随 CDN 缓存策略，当开启时，表示将最终生效的 CDN 缓存策略响应给客户端。可以配置的值为： on：开启 off（默认）：关闭 | off |
| force_revalidate | String | 否 | 过期时间为 0 时强制内容验证，可以配置的值为： on：开启。 过期时间为 0 时，支持在 CDN 节点上缓存内容，并且每次请求都需要回源验证缓存内容。 off（默认）：关闭。 过期时间为 0 时，CDN 节点不缓存内容，每次请求都需要回源重新获取内容。 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "file_type", "argValue": "jpg" }, { "argName": "weight", "argValue": "1" }, { "argName": "ttl", "argValue": "500000" }, { "argName": "swift_origin_cache_high", "argValue": "off" }, { "argName": "swift_no_cache_low", "argValue": "off" }, { "argName": "swift_follow_cachetime", "argValue": "off" },{ "argName": "force_revalidate", "argValue": "off" }], "functionName": "filetype_based_ttl_set" }], "DomainNames": "example.com" }

path_based_ttl_set

- 

功能说明：配置目录过期时间，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[CDN](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[缓存过期时间](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)。

- 

功能ID（FunctionID/FuncId）：7。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ttl | Integer | 是 | 缓存时间，单位为秒，取值范围是 1~99999999（3 年多一些）。 | 500000 |
| path | String | 是 | 目录，必须以正斜线（/）开头。 | /example/demo |
| weight | Integer | 否 | 权重。取值：1~99。 说明 默认为 1，数字越大优先级越高。 | 1 |
| swift_origin_cache_high | String | 否 | 源站响应缓存策略优先，当开启时，表示在源站响应缓存相关头（比如 Cache-Control、Pragma 等）的时候，源站的缓存策略优先生效。可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_no_cache_low | String | 否 | 忽略源站不缓存响应头，当开启时，表示忽略源站的以下响应头（均表示不缓存）。 Cache-Control: no-store Cache-Control: no-cache Cache-Control: max-age=0 Pragme: no-cache 可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_follow_cachetime | String | 否 | 客户端跟随 CDN 缓存策略，当开启时，表示将最终生效的 CDN 缓存策略响应给客户端。可以配置的值为： on：开启 off（默认）：关闭 | off |
| force_revalidate | String | 否 | 过期时间为 0 时强制内容验证，可以配置的值为： on：开启。 过期时间为 0 时，支持在 CDN 节点上缓存内容，并且每次请求都需要回源验证缓存内容。 off（默认）：关闭。 过期时间为 0 时，CDN 节点不缓存内容，每次请求都需要回源重新获取内容。 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "path", "argValue": "/example/demo" }, { "argName": "weight", "argValue": "1" }, { "argName": "ttl", "argValue": "500000" }, { "argName": "swift_origin_cache_high", "argValue": "off" }, { "argName": "swift_no_cache_low", "argValue": "off" }, { "argName": "swift_follow_cachetime", "argValue": "off" }, { "argName": "force_revalidate", "argValue": "off" }], "functionName": "path_based_ttl_set" }], "DomainNames": "example.com" }

filetype_force_ttl_code

- 

功能说明：配置文件状态码过期时间，该功能详细介绍请参见控制台配置说明[配置状态码过期时间](products/cdn/documents/user-guide/create-a-cache-rule-for-http-status-codes.md)。

- 

功能ID（FunctionID/FuncId）：63。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| file_type | String | 是 | 文件类型，区分大小写，多个用半角逗号（,）分隔，例如：jpg,txt。 | jpg |
| code_string | String | 是 | 状态码及其缓存时间，单位为秒，取值范围是 1~99999999（3 年多一些），多个用半角逗号（,）分隔。例如：302=0,301=0,4xx=2。 | 403=10 |
| swift_code_origin_cache_high | String | 否 | 源站响应缓存策略优先，当开启时，表示在源站响应缓存相关头（比如 Cache-Control、Pragma 等）的时候，源站的缓存策略优先生效。可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_code_no_cache_low | String | 否 | 忽略源站不缓存响应头，当开启时，表示忽略源站的以下响应头（均表示不缓存）。 Cache-Control: no-store Cache-Control: no-cache Cache-Control: max-age=0 Pragme: no-cache 可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_code_follow_cachetime | String | 否 | 客户端跟随 CDN 缓存策略，当开启时，表示将最终生效的 CDN 缓存策略响应给客户端。可以配置的值为： on：开启 off（默认）：关闭 | off |
| force_revalidate | String | 否 | 过期时间为 0 时强制内容验证，可以配置的值为： on：开启。 过期时间为 0 时，支持在 CDN 节点上缓存内容，并且每次请求都需要回源验证缓存内容。 off（默认）：关闭。 过期时间为 0 时，CDN 节点不缓存内容，每次请求都需要回源重新获取内容。 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "file_type", "argValue": "jpg" }, { "argName": "code_string", "argValue": "403=10" }, { "argName": "swift_code_origin_cache_high", "argValue": "off" }, { "argName": "swift_code_no_cache_low", "argValue": "off" }, { "argName": "swift_code_follow_cachetime", "argValue": "off" }, { "argName": "force_revalidate", "argValue": "off" }], "functionName": "filetype_force_ttl_code" }], "DomainNames": "example.com" }

path_force_ttl_code

- 

功能说明：配置路径状态码过期时间，该功能详细介绍请参见控制台配置说明[配置状态码过期时间](products/cdn/documents/user-guide/create-a-cache-rule-for-http-status-codes.md)。

- 

功能ID（FunctionID/FuncId）：65。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| path | String | 是 | 目录，必须以正斜线（/）开头，例如：/image。 | /example/demo |
| code_string | String | 是 | 状态码及其缓存时间，单位为秒，取值范围是 1~99999999（3 年多一些），多个用半角逗号（,）分隔。例如：302=0,301=0,4xx=2。 | 403=10,404=15 |
| swift_code_origin_cache_high | String | 否 | 源站响应缓存策略优先，当开启时，表示在源站响应缓存相关头（比如 Cache-Control、Pragma 等）的时候，源站的缓存策略优先生效。可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_code_no_cache_low | String | 否 | 忽略源站不缓存响应头，当开启时，表示忽略源站的以下响应头（均表示不缓存）。 Cache-Control: no-store Cache-Control: no-cache Cache-Control: max-age=0 Pragme: no-cache 可以配置的值为： on：开启 off（默认）：关闭 | off |
| swift_code_follow_cachetime | String | 否 | 客户端跟随 CDN 缓存策略，当开启时，表示将最终生效的 CDN 缓存策略响应给客户端。可以配置的值为： on：开启 off（默认）：关闭 | off |
| force_revalidate | String | 否 | 过期时间为 0 时强制内容验证，可以配置的值为： on：开启。 过期时间为 0 时，支持在 CDN 节点上缓存内容，并且每次请求都需要回源验证缓存内容。 off（默认）：关闭。 过期时间为 0 时，CDN 节点不缓存内容，每次请求都需要回源重新获取内容。 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "path", "argValue": "/example/demo" }, { "argName": "code_string", "argValue": "403=10,404=15" }, { "argName": "swift_code_origin_cache_high", "argValue": "off" }, { "argName": "swift_code_no_cache_low", "argValue": "off" }, { "argName": "swift_code_follow_cachetime", "argValue": "off" }, { "argName": "force_revalidate", "argValue": "off" }], "functionName": "path_force_ttl_code" }], "DomainNames": "example.com" }

default_ttl_code

- 

功能说明：配置状态码过期时间（源站优先），该功能详细介绍请参见控制台配置说明[配置状态码过期时间（源站优先）](products/cdn/documents/create-a-status-code-expiration-rule-that-honors-origin.md)。

- 

功能ID（FunctionID/FuncId）：207。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| default_ttl_code | String | 是 | 状态码及其缓存时间，单位为秒，取值范围是 1~99999999（3 年多一些），多个状态码之间用半角逗号（,）分隔。 | 4xx=3,200=3600,5xx=1 |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "default_ttl_code", "argValue": "4xx=3,200=3600,5xx=1" }], "functionName": "default_ttl_code" }], "DomainNames": "example.com" }

set_resp_header

- 

功能说明：配置自定义HTTP响应头，该功能详细介绍请参见控制台配置说明[修改出站响应头](products/cdn/documents/user-guide/create-a-custom-http-response-header.md)。

- 

功能ID（FunctionID/FuncId）：27。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| key | String | 是 | 响应头。 | Cache-Control |
| value | String | 是 | 响应头值，多个值之间用英文逗号（,）分隔。 说明 如果要删除某个响应头，请设置响应头的值为 null。 | no-cache |
| header_operation_type | String | 否 | 请求头操作，取值： add：添加。 delete：删除。 modify：变更。 rewrite：替换。 | add |
| duplicate | String | 否 | 是否允许重复添加名称相同的请求头。当 header_operation_type 使用 add 时（即执行增加操作），需要设置是否允许重复： on：允许重复。 off：不允许重复。 | off |
| header_source | String | 否 | 查找需要替换的参数值。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置该参数，取值支持正则表达式。 | value1 |
| header_destination | String | 否 | 替换后的参数值。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置该参数。 | value123 |
| match_all | String | 否 | 设置匹配模式。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置匹配模式： on：匹配所有（所有匹配上的值都会被替换）。 off：仅匹配第一个（只有第一个匹配上的值会被替换）。 | / |
| access_origin_control | String | 否 | 是否开启跨域校验： on：开启 CDN 节点对用户请求的跨域校验。 off：关闭该功能。 | / |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "header_operation_type", "argValue": "add" }, { "argName": "key", "argValue": "Cache-Control" }, { "argName": "value", "argValue": "no-cache" }, { "argName": "duplicate", "argValue": "off" }], "functionName": "set_resp_header" }], "DomainNames": "example.com" }

error_page

- 

功能说明：配置自定义页面，该功能详细介绍请参见控制台配置说明[配置自定义页面](products/cdn/documents/user-guide/create-a-custom-error-page.md)。

- 

功能ID（FunctionID/FuncId）：15。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| error_code | Integer | 是 | 错误码。 | 404 |
| rewrite_page | String | 是 | 重定向页面。 | http://example.aliyundoc.com/error404.html |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "error_code", "argValue": "404" }, { "argName": "rewrite_page", "argValue": "http://example.aliyundoc.com/error404.html" }], "functionName": "error_page" }], "DomainNames": "example.com" }

host_redirect

- 

功能说明：配置URI重写规则，该功能详细介绍请参见控制台配置说明[重写访问](products/cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)[URL](products/cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)。

- 

功能ID（FunctionID/FuncId）：43。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| regex | String | 是 | 需要重写的 URI，以“/”开头，不含“http://”头及域名。支持 PCRE 正则表达式，例如：^/hello$。 | ^/hello$ |
| replacement | String | 是 | 执行规则设置为“Break”的情况下，仅支持以/开头的 Path，不含协议头和域名；执行规则设置为“Redirect”的情况下，可以包含协议头和域名。支持 PCRE 正则表达式，例如：常用$1、$2 来捕获待改写 Path 中圆括号内的字符串。 | /hello/test |
| flag | String | 否 | 指定 CDN 节点在 URI 改写完成之后执行的动作，取值： 空 ：默认为空，指的是不传 flag 参数。在配置了多条规则的情况下，如果请求 URL 匹配了某条规则，执行完当前规则以后，还会继续匹配后续规则。 break ：如果请求 URL 匹配了某条规则，该请求将会被重写为目标 URL（不修改原始 URI 中的参数）。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则。 redirect ：如果请求 URL 匹配某条规则，该请求将会被 302 重定向到目标 URL，CDN 节点将返回给客户端的 Location 信息为目标 URL（不修改原始 URI 中的参数）。执行完当前规则后，当存在其他配置规则时，会继续匹配剩余规则。 enhance_break ：和 break 类似，但是会修改包含参数在内的整个 URL。 enhance_redirect ：和 redirect 类似，但是会修改包含参数在内的整个 URL。 说明 不同的执行规则使用的重写方式不同，重写后的 URL 是否支持其他域名、其他协议也存在差异： 空 、 break 、 enhance_break 采用直接重写用户请求 URL 的方式，不支持重写为其他域名，也不支持重写为其他协议（例如从 HTTP 协议重写为 HTTPS 协议）。 redirect 、 enhance_redirect 采用 302 跳转方式实现 URL 重写，支持重写为其他域名，也支持重写为其他协议： 302 Location 地址除了可以设置为当前的加速域名，还支持设置为其他域名，可以实现这样的效果：原始 URL 使用的域名是 example.com，重写后的 URL 使用新的域名 aliyundoc.com。 302 Location 地址支持使用其他协议，可以实现这样的效果：原始 URL 使用 HTTP 协议，重写后的 URL 使用 HTTPS 协议。 | redirect |
| rewrite_method | String | 否 | 重定向方式，支持 302、303、307 状态码： 302：默认重定向方式，GET 请求方式不会发生变更，其他请求方式有可能会变更为 GET 请求。 303：GET 请求方式不会发生变更，其他请求方式会变更为 GET 请求方式（消息主体会丢失）。 307：请求方式和消息主体都不发生变化。 | 302 |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "flag", "argValue": "redirect" }, { "argName": "regex", "argValue": "^/hello$" }, { "argName": "replacement", "argValue": "/hello/test" }, { "argName": "rewrite_method", "argValue": "302" }], "functionName": "host_redirect" }], "DomainNames": "example.com" }

self_defined_cachekey

- 

功能说明：配置自定义Cachekey，该功能详细介绍请参见控制台配置说明[自定义](products/cdn/documents/user-guide/create-custom-cache-keys.md)[Cachekey](products/cdn/documents/user-guide/create-custom-cache-keys.md)。

- 

功能ID（FunctionID/FuncId）：227。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| uri | Array of String | 否 | 将请求中的源 URI 改写为目标 URI，然后存为 cachekey。 uri_to_rewrite 用于指定源 uri。 ai_uri_regex 用于指定目标 uri。 | [{"uri_to_rewrite":"/hello","ai_uri_regex":"/hello/test"}] |
| args | Array of String | 否 | 请求中的参数进行增、删、改和保留操作，然后后存为 cachekey，取值： args_operation_type：指定参数操作类型，支持 add（修改）、delete（删除）、modify（变更）和 keep（保留）。 args：指定参数操作对应的参数值。 | [{"args":"test=123","args_operation_type":"add"}] |
| headers | String | 否 | 用于增加多个 HTTP header，并且拼接到 cachekey 中，多个 HTTP header 之间使用空格分隔。 | example |
| variable | Array of String | 否 | 自定义变量，可使用正则表达式从请求 URL 中的请求参数、HTTP header、cookie 和 URI 中截取出任意字段，然后拼接到 cachekey 中。 | [] |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "uri", "argValue": [{ "uri_to_rewrite": "/hello", "ai_uri_regex": "/hello/test" }] }, { "argName": "args", "argValue": [{ "args": "test=123", "args_operation_type": "add" }] }, { "argName": "headers", "argValue": "" }, { "argName": "variable", "argValue": [] }], "functionName": "self_defined_cachekey" }], "DomainNames": "example.com" }

rewrite_host

- 

功能说明：共享缓存。

- 

功能ID（FunctionID/FuncId）：54。

- 

参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| share_host | String | 是 | 可以与当前域名共享缓存的目标域名。该配置不修改用户请求的回源 HOST，只是在查询缓存资源的时候，使用 share_host 值来生成查询用的 cachekey。 | example.com |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "share_host", "argValue": "example.com" }], "functionName": "rewrite_host" }], "DomainNames": "example.com" }

serving_stale_content

- 

功能说明：响应过期缓存。

- 

功能ID（FunctionID/FuncId）：260。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| origin_error_status_code | String | 否 | 自定义源站异常状态码。 功能说明：用于设置在源站返回哪些状态码时适用于此功能配置。 默认值：默认不填写。默认情况下，源站异常的定义是超时+所有的 5xx 状态码。 配置说明：支持直接输入 4xx、5xx 来模糊匹配，也支持输入 502、504 这样的状态码来精确匹配；支持输入多个状态码，输入多个状态码的情况下，各个状态码之间用英文逗号进行分隔。 | 502 |
| extend_expiration_time | Integer | 否 | 过期延长时间。 功能说明：缓存过期后，希望保留旧缓存的最长时间。 默认值：默认不填写。默认情况下，过期延长时间是 1 小时。 配置说明：输入值为大于等于 1 的正整数，单位为秒。 | 60 |
| origin_first | String | 否 | 源站策略优先。 功能说明：参数配置为 on 的情况下可以开启源站策略优先，这时候如果源站返回文件时携带了缓存策略 Cache-Control: stale-if-error=xx ，将优先遵循源站响应信息里面 stale-if-error 参数设置的时间来作为过期延长时间。 默认值：默认不填写。默认情况下，等同于 off，这时候使用的是通过参数 extend_expiration_time 设置的过期延长时间 配置说明：支持 on （开启）、 off （关闭）。 | on |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "origin_error_status_code", "argValue": "502" }, { "argName": "extend_expiration_time", "argValue": "60" }, { "argName": "origin_first", "argValue": "off" }], "functionName": "serving_stale_content" }], "DomainNames": "example.com" }

## HTTPS配置

https_option

- 

功能说明：配置HTTPS基础参数，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-an-ssl-certificate.md)[HTTPS](products/cdn/documents/user-guide/configure-an-ssl-certificate.md)[证书](products/cdn/documents/user-guide/configure-an-ssl-certificate.md)、[配置](products/cdn/documents/user-guide/enable-http-or-2.md)[HTTP/2](products/cdn/documents/user-guide/enable-http-or-2.md)和[配置](products/cdn/documents/user-guide/configure-ocsp-stapling.md)[OCSP Stapling](products/cdn/documents/user-guide/configure-ocsp-stapling.md)。

- 

功能ID（FunctionID/FuncId）：78。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| http2 | String | 否 | 是否开启 HTTP/2 开关： on：开启。 off：关闭。 | on |
| ocsp_stapling | String | 否 | 是否开启 OCSP Stapling 开关： on：开启。 off：关闭。 | on |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "http2", "argValue": "on" }, { "argName": "ocsp_stapling", "argValue": "on" }], "functionName": "https_option" }], "DomainNames": "example.com" }

http_force

- 

功能说明：配置强制HTTP跳转，该功能详细介绍请参见控制台配置说明[配置协议重定向](products/cdn/documents/user-guide/configure-url-redirection.md)。

- 

功能冲突说明：强制HTTP跳转功能与强制HTTPS跳转功能（功能函数：https_force，功能ID：44）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：45。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启强制 HTTP 跳转： on：开启。 off：关闭。 | on |
| http_rewrite | String | 否 | 跳转方式，支持 301、308 状态码： 301：GET 请求方式不会发生变更，其他请求方式有可能会变更为 GET 请求方式。 308：请求方式和消息主体都不发生变化。 | 301 |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "http_rewrite", "argValue": "301" }], "functionName": "http_force" }], "DomainNames": "example.com" }

https_force

- 

功能说明：配置强制HTTPS跳转，该功能详细介绍请参见控制台配置说明[配置协议重定向](products/cdn/documents/user-guide/configure-url-redirection.md)。

- 

功能冲突说明：强制HTTPS跳转功能与强制HTTP跳转功能（功能函数：http_force，功能ID：45）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另外一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：44。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启强制 HTTPS 跳转： on：开启。 off：关闭。 | on |
| https_rewrite | String | 否 | 跳转方式，支持 301、308 状态码： 301：GET 请求方式不会发生变更，其他请求方式有可能会变更为 GET 请求方式。 308：请求方式和消息主体都不发生变化。 | 301 |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "https_rewrite", "argValue": "301" }], "functionName": "https_force" }], "DomainNames": "example.com" }

https_tls_version

- 

功能说明：配置TLS协议版本，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-tls-version-control.md)[TLS](products/cdn/documents/user-guide/configure-tls-version-control.md)[版本与加密套件](products/cdn/documents/user-guide/configure-tls-version-control.md)。

- 

功能ID（FunctionID/FuncId）：110。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| tls10 | String | 否 | 是否开启 TLSv1.0： on（默认）：开启。 off：关闭。 | on |
| tls11 | String | 否 | 是否开启 TLSv1.1： on（默认）：开启。 off：关闭。 | on |
| tls12 | String | 否 | 是否开启 TLSv1.2： on（默认）：开启。 off：关闭。 | on |
| tls13 | String | 否 | 是否开启 TLSv1.3： on（默认）：开启。 off：关闭。 | on |
| ciphersuitegroup | String | 否 | 加密算法套件组： all（默认）：全部加密算法套件。 strict：强加密算法套件。 custom：自定义加密算法套件。 | all |
|  | String | 否 | 加密算法套件，配合 ciphersuitegroup 参数（自定义加密算法套件）使用，可以配置多个加密算法套件，中间用英文逗号分隔。 | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 |


- 

配置示例：

- 

默认配置，开启TLS1.0、1.1、1.2，使用全部加密算法套件。

{ "Functions": [{ "functionArgs": [ { "ArgValue": "on", "ArgName": "tls10" }, { "ArgValue": "on", "ArgName": "tls11" }, { "ArgValue": "on", "ArgName": "tls12" }, { "ArgValue": "off", "ArgName": "tls13" }, { "ArgValue": "all", "ArgName": "ciphersuitegroup" } ], "functionName": "https_tls_version" }], "DomainNames": "example.com" }

- 

开启TLS1.2、1.3，使用强加密算法套件。

{ "Functions": [{ "functionArgs": [ { "ArgValue": "off", "ArgName": "tls10" }, { "ArgValue": "off", "ArgName": "tls11" }, { "ArgValue": "on", "ArgName": "tls12" }, { "ArgValue": "on", "ArgName": "tls13" }, { "ArgValue": "strict", "ArgName": "ciphersuitegroup" } ], "functionName": "https_tls_version" }], "DomainNames": "example.com" }

- 

开启TLS1.2、1.3，使用自定义加密算法套件。

{ "Functions": [{ "functionArgs": [ { "ArgValue": "off", "ArgName": "tls10" }, { "ArgValue": "off", "ArgName": "tls11" }, { "ArgValue": "on", "ArgName": "tls12" }, { "ArgValue": "on", "ArgName": "tls13" }, { "ArgValue": "custom", "ArgName": "ciphersuitegroup" }, { "ArgValue": "TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8,TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "ArgName": "ciphersuite" } ], "functionName": "https_tls_version" }], "DomainNames": "example.com" }

https_client_cert

- 

功能说明：配置客户端认证证书，该功能详细介绍请参见控制台配置说明[客户端认证证书](products/cdn/documents/user-guide/client-authentication-certificate.md)。

- 

功能ID（FunctionID/FuncId）：111。

- 

参数说明：

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| client_certificate_verify | String | 是 | 是否开启客户端证书认证： on：开启。 off：关闭。 | on |
| client_certificate | String | 是 | 自行签发的客户端证书（公钥），CA 证书的格式有以下要求： 以 -----BEGIN CERTIFICATE----- 开头，以 -----END CERTIFICATE----- 结尾。 | -----BEGIN PUBLIC KEY----- *********** -----END PUBLIC KEY----- |
| client_verify_depth | String | 否 | 认证深度，即 证书链深度 ，是指在验证一个 客户端证书 的有效性时，其所依赖的 证书信任链 中包含的证书层级数量（从 客户端证书本身 回溯到 根 CA 证书 之间的层级数），默认值为 1。 | 1 |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "client_certificate_verify", "argValue": "on" }, { "argName": "client_certificate", "argValue": "-----BEGIN PUBLIC KEY-----***********-----END PUBLIC KEY-----" }], "functionName": "https_client_cert" }], "DomainNames": "example.com" }

HSTS

- 

功能说明：配置HSTS，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-hsts.md)[HSTS](products/cdn/documents/user-guide/configure-hsts.md)。

- 

功能ID（FunctionID/FuncId）：112。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enabled | String | 是 | 是否开启 HSTS： on：开启。 off：关闭。 | on |
| https_hsts_max_age | Integer | 是 | 过期时间，单位：秒。 说明 建议填写 5184000s（60 天）。 | 5184000 |
| https_hsts_include_subdomains | String | 否 | 配置 HSTS 头部是否包含子域名参数，取值 on 或者 off。 说明 开启前请确保该加速域名的所有子域名都已开启 HTTPS，否则会导致子域名自动跳转到 HTTPS 后无法访问。 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enabled", "argValue": "on" }, { "argName": "https_hsts_max_age", "argValue": "5184000" }, { "argName": "https_hsts_include_subdomains", "argValue": "off" }], "functionName": "HSTS" }], "DomainNames": "example.com" }

## 访问控制

referer_white_list_set

- 

功能说明：配置Referer白名单，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](products/cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](products/cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)。

- 

功能冲突说明：Referer白名单功能与Referer黑名单功能（功能函数：referer_black_list_set，功能ID：5）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：1。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| refer_domain_allow_list | String | 是 | 白名单列表，多个用半角逗号（,）分隔。 | example.aliyundoc.com,demo.aliyundoc.com |
| allow_empty | String | 否 | 是否允许空 referer 字段访问 CDN 资源。取值： on：允许。 off（默认值）：禁止。 | off |
| redirect_url | String | 否 | 重定向 URL，即用户请求中的 referer 信息未匹配上白名单列表，被拦截后不会再返回 403，而是会返回 302 加 Location 头，该项为 Location 头的值，以 http:// 或者 https:// 开头。 | http://www.example.com |
| disable_ast | String | 否 | 使用精确匹配模式，控制“白名单列表”项中填写的域名是否为精确匹配。如果勾选（on）则精确匹配域名。 取值为 on 时： 支持精确匹配 白名单列表填写 example.com ，匹配 example.com 。 白名单列表填写 a*b.example.com ，匹配 a<任意字符>b.example.com 。 不支持后缀匹配 取值为 off（默认值）时： 不支持精确匹配 支持后缀匹配 白名单列表填写 example.com ，匹配 example.com 和 <任意字符>.example.com 。 白名单列表填写 a*b.example.com ，匹配 a<任意字符>b.example.com 和 <任意字符>.a<任意字符>b.example.com 。 | off |
| ignore_scheme | String | 否 | 开启忽略 scheme。开启后，如果用户请求中的 referer 没有带上 HTTP 或 HTTPS 协议头部，则依然视为有效 referer 进行处理。示例： 取值为 on 时，referer 格式如下： referer: www.example.com 取值为 off（默认值）时，referer 格式如下： referer: https://www.example.com | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "allow_empty", "argValue": "off" }, { "argName": "refer_domain_allow_list", "argValue": "example.aliyundoc.com,demo.aliyundoc.com" }], "functionName": "referer_white_list_set" }], "DomainNames": "example.com" }

referer_black_list_set

- 

功能说明：配置Referer黑名单，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](products/cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](products/cdn/documents/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)。

- 

功能冲突说明：Referer黑名单功能与Referer白名单功能（功能函数：referer_white_list_set，功能ID：1）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：5。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| refer_domain_deny_list | String | 是 | 黑名单列表，多个用半角逗号（,）分隔。 | example.aliyundoc.com,demo.aliyundoc.com |
| allow_empty | String | 否 | 是否允许空 referer 字段访问 CDN 资源： on：允许。 off：禁止。 | off |
| redirect_url | String | 否 | 重定向 URL，即用户请求中的 referer 信息匹配上黑名单列表，被拦截后不会再返回 403，而是会返回 302 加 Location 头，该项为 Location 头的值，以 http:// 或者 https:// 开头。 | http://www.example.com |
| disable_ast | String | 否 | 使用精确匹配模式，控制“黑名单列表”项中填写的域名是否为精确匹配。如果勾选（on）则精确匹配。 取值为 on 时： 支持精确匹配 黑名单列表填写 example.com ，匹配 example.com 。 黑名单列表填写 a*b.example.com ，匹配 a<任意字符>b.example.com 。 不支持后缀匹配 取值为 off（默认值）时： 不支持精确匹配 支持后缀匹配 黑名单列表填写 example.com ，匹配 example.com 和 <任意字符>.example.com 。 黑名单列表填写 a*b.example.com ，匹配 a<任意字符>b.example.com 和 <任意字符>.a<任意字符>b.example.com 。 | off |
| ignore_scheme | String | 否 | 开启忽略 scheme。开启后，如果用户请求中的 referer 没有带上 HTTP 或 HTTPS 协议头部，则依然视为有效 referer 进行处理。示例： 取值为 on 时，referer 格式如下： referer: www.example.com 取值为 off（默认值）时，referer 格式如下： referer: https://www.example.com | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "allow_empty", "argValue": "off" }, { "argName": "refer_domain_deny_list", "argValue": "example.aliyundoc.com,demo.aliyundoc.com" }], "functionName": "referer_black_list_set" }], "DomainNames": "example.com" }

aliauth

- 

功能说明：配置URL鉴权，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-url-signing.md)[URL](products/cdn/documents/user-guide/configure-url-signing.md)[鉴权](products/cdn/documents/user-guide/configure-url-signing.md)。

- 

功能ID（FunctionID/FuncId）：25。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| auth_m3u8 | String | 否 | 开启 m3u8 内容改写，对 m3u8 里面的 ts 补齐对应的鉴权，可以避免 ts 的访问鉴权失败，取值 on（默认值）和 off。 | on |
| auth_type | String | 是 | 鉴权类型。取值： no_auth：无鉴权。 type_a：鉴权方式 A。 type_b：鉴权方式 B。 type_c：鉴权方式 C。 type_d：鉴权方式 D。 type_e：鉴权方式 E。 type_f：鉴权方式 F。 | type_a |
| auth_key1 | String | 是 | 鉴权 key1（16~128 个字符支持大写字母、小写字母和数字）。 | 1234567890123456789 |
| auth_key2 | String | 否 | 鉴权 key2（16~128 个字符支持大写字母、小写字母和数字）。 | 1234567890123456789 |
| ali_auth_delta | Integer | 否 | 鉴权 URL 有效时长，默认 1800，单位：秒。 | 1800 |
| req_auth_ip_white | String | 否 | 白名单例外 IP 列表，白名单中的 IP 不进行鉴权校验。 支持输入多个 IP 地址，多个 IP 地址之间使用英文逗号分隔。 | 192.168.0.1 |
| req_auth_ip_acl_xfwd | String | 否 | 客户端例外 IP 的提取方式，取值支持： on：该模式为默认模式。该模式校验的是用户请求中 x-forwarded-for 请求头携带的左边第一个 IP，这个 IP 对应客户端真实 IP。 off：该模式校验的是客户端与 CDN 节点之间建立建连接用的 IP。 all：同时校验以下两个 IP 地址信息： 用户请求中 x-forwarded-for 请求头携带的左边第一个 IP，即客户端真实 IP。 客户端与 CDN 节点之间建立建连接用的 IP。 | all |
| sign_param | String | 否 | 签名参数名称。仅在鉴权类型设置为 F 方式的时候有效。 | sign |
| time_param | String | 否 | 时间戳参数名称。仅在鉴权类型设置为 F 方式的时候有效。 | time |
| time_format | String | 否 | 时间戳格式。仅在鉴权类型设置为 F 方式的时候有效。 dec：十进制 hex：十六进制 | hec |
| path_encoding | String | 否 | URL 编码开关，支持 on/off。仅在鉴权类型设置为 F 方式的时候有效。 | on |


- 

配置示例：

- 

鉴权方式A

{ "Functions": [{ "functionArgs": [{ "argName": "auth_type", "argValue": "type_a" }, { "argName": "auth_key1", "argValue": "1234567890123456789" }, { "argName": "auth_key2", "argValue": "1234567890123456789" }, { "argName": "ali_auth_delta", "argValue": 1800 }, { "argName": "req_auth_ip_white", "argValue": "192.168.0.1" }, { "argName": "req_auth_ip_acl_xfwd", "argValue": "all" }], "functionName": "aliauth" }], "domainNames": "example.com" }

- 

鉴权方式F

{ "Functions": [{ "functionArgs": [{ "argName": "auth_type", "argValue": "type_f" },{ "argName": "auth_key1", "argValue": "1234567890123456789" },{ "argName": "auth_key2", "argValue": "1234567890123456789" },{ "argName": "ali_auth_delta", "argValue": 1800 },{ "argName": "sign_param", "argValue": "sign" },{ "argName": "time_param", "argValue": "time", },{ "argName": "time_format", "argValue": "hec" },{ "argName": "path_encoding", "argValue": "on" }], "functionName": "aliauth" }], "domainNames": "example.com" }

cdn_remote_auth

- 

功能说明：配置远程鉴权，该功能详细介绍请参见控制台配置说明[配置远程鉴权](products/cdn/documents/user-guide/configure-remote-authentication.md)。

- 

功能ID（FunctionID/FuncId）：258。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启远程鉴权： on：开启。 off：关闭。 | on |
| remote_auth_addr | String | 是 | 鉴权服务器地址。格式： https://cdn.aliyun.com/auth 或者 http://10.10.10.10/auth 。 | https://example.aliyundoc.com/auth |
| remote_auth_method | String | 是 | 请求方法，支持 GET/POST/HEAD。 | get |
| remote_auth_type | String | 是 | 鉴权文件类型。all 表示所有类型，多个文件类型用竖线分隔、区分大小写（jpg 不等同于 JPG）。 | all |
| remote_auth_reserve_args | String | 是 | 保留参数设置，多个请求头用竖线分隔，不区分大小写（key 等同于 KEY）。 all：保留所有参数。 ali_delete_all_args：表示删除所有 URL 参数。 | all |
| remote_auth_custom_args | String | 否 | 添加自定义参数，多个参数用竖线分隔、区分大小写（key 不等同于 KEY）。 | 空 |
| remote_auth_reserve_header | String | 是 | 保留请求头设置，多个请求头用竖线分隔，不区分大小写（http_remote_addr 等同于 HTTP_Remote_Addr）。 all：保留所有请求头。 ali_delete_all_headers：删除所有请求头。 | all |
| remote_auth_custom_header | String | 否 | 添加自定义请求头，多个请求头用竖线分隔、不区分大小写（http_remote_addr 等同于 HTTP_Remote_Addr）。 | 空 |
| remote_auth_success_code | Integer | 是 | 鉴权成功状态码，指鉴权服务器在鉴权成功之后传给 CDN 的鉴权结果。例如：200。支持配置多个状态码，多个状态码之间用英文逗号分隔。 | 200 |
| remote_auth_fail_code | Integer | 是 | 鉴权失败状态码，指鉴权服务器在鉴权失败之后传给 CDN 的鉴权结果。例如：403。支持配置多个状态码，多个状态码之间用英文逗号分隔。 | 403,404 |
| remote_auth_other_code_act | String | 否 | 其他状态码是否放行，表示在鉴权服务器返回的状态码既不是鉴权成功状态码，也不是鉴权失败状态码的情况下，CDN 对用户请求的处理方式，取值： pass：通过（默认值）。 reject：拒绝。 | pass |
| remote_auth_fail_resp_code | Integer | 是 | 鉴权失败 CDN 响应状态码。例如：403，CDN 传给用户的状态码。 | 403 |
| remote_auth_timeout | Integer | 是 | 鉴权超时配置，单位 ms，最大值为 3000。 | 500 |
| remote_auth_timeout_action | String | 是 | 鉴权超时行为，取值： pass：CDN 将直接通过用户请求。 reject：CDN 将响应上面配置的“鉴权失败 CDN 响应状态码”给用户。 | pass |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "remote_auth_addr", "argValue": "https://example.aliyundoc.com/auth" }, { "argName": "remote_auth_method", "argValue": "get" }, { "argName": "remote_auth_type", "argValue": "all" }, { "argName": "remote_auth_reserve_args", "argValue": "all" }, { "argName": "remote_auth_custom_args", "argValue": "" }, { "argName": "remote_auth_reserve_header", "argValue": "all" }, { "argName": "remote_auth_custom_header", "argValue": "" }, { "argName": "remote_auth_success_code", "argValue": "200" }, { "argName": "remote_auth_fail_code", "argValue": "403" }, { "argName": "remote_auth_other_code_act", "argValue": "pass" }, { "argName": "remote_auth_fail_resp_code", "argValue": "403" }, { "argName": "remote_auth_timeout", "argValue": 500 }, { "argName": "remote_auth_timeout_action", "argValue": "pass" }], "functionName": "cdn_remote_auth" }], "DomainNames": "example.com" }

ip_allow_list_set

- 

功能说明：配置IP白名单，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-an-ip-blacklist-or-whitelist.md)[IP](products/cdn/documents/user-guide/configure-an-ip-blacklist-or-whitelist.md)[黑/白名单](products/cdn/documents/user-guide/configure-an-ip-blacklist-or-whitelist.md)。

- 

功能冲突说明：IP白名单功能与IP黑名单功能（功能函数：ip_black_list_set，功能ID：13）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：69。

- 

参数说明：

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ip_list | String | 是 | IP 列表，多个用半角逗号（,）分隔。 | 192.168.0.1/24 |
| customize_response_status_code | String | 否 | 自定义响应状态码，默认为空（表示响应状态码设置为 403）。可以输入 3 位数值来设置自定义响应状态码。 | 429 |
| ip_acl_xfwd | String | 否 | 使用 X-Forwarded-For 请求头中的 IP，取值范围： on：默认取值，使用用户请求中的 x-forwarded-for 请求头（从左向右取第一个 IP）作为判断依据。 off：使用 真实建连 ip 作为判断依据。 all：同时使用 x-forwarded-for 和 真实连接 ip 作为判断依据。 | all |
| ip_list_notes | String | 否 | 备注信息，用于记录 IP 列表的备注说明信息。 | 192.x.x.1（恶意 IP 地址） 192.x.x.2（灰产 IP 地址） |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "ip_list", "argValue": "192.168.0.1/24" }], "functionName": "ip_allow_list_set" }], "DomainNames": "example.com" }

ip_black_list_set

- 

功能说明：配置IP黑名单，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-an-ip-blacklist-or-whitelist.md)[IP](products/cdn/documents/user-guide/configure-an-ip-blacklist-or-whitelist.md)[黑/白名单](products/cdn/documents/user-guide/configure-an-ip-blacklist-or-whitelist.md)。

- 

功能冲突说明：IP黑名单功能与IP白名单功能（功能函数：ip_allow_list_set，功能ID：69）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：13。

- 

参数说明：

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ip_list | String | 是 | IP 列表，多个用半角逗号（,）分隔。 | 192.168.0.1 |
| customize_response_status_code | String | 否 | 自定义响应状态码，默认为空（表示响应状态码设置为 403）。可以输入 3 位数值来设置自定义响应状态码。 | 429 |
| ip_acl_xfwd | String | 否 | 使用 X-Forwarded-For 请求头中的 IP，取值范围： on：默认取值，使用用户请求中的 x-forwarded-for 请求头（从左向右取第一个 IP）作为判断依据。 off：使用 真实建连 ip 作为判断依据。 all：同时使用 x-forwarded-for 和 真实连接 ip 作为判断依据。 | all |
| ip_list_notes | String | 否 | 备注信息，用于记录 IP 列表的备注说明信息。 | 192.x.x.1（恶意 IP 地址） 192.x.x.2（灰产 IP 地址） |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "ip_list", "argValue": "192.168.0.1" }], "functionName": "ip_black_list_set" }], "DomainNames": "example.com" }

ali_ua

- 

功能说明：配置User-Agent限制访问，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/configure-a-user-agent-blacklist-or-whitelist.md)[UA](products/cdn/documents/user-guide/configure-a-user-agent-blacklist-or-whitelist.md)[黑白名单](products/cdn/documents/user-guide/configure-a-user-agent-blacklist-or-whitelist.md)。

- 

功能ID（FunctionID/FuncId）：58。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ua | String | 是 | 填写 User-Agent，支持通配符*（匹配任意字符串）和多个值（多个值用|分割。例如： *curl*|*IE*|*chrome*|*firefox*） 。 | *curl*|*IE*|*chrome*|*firefox* |
| type | String | 是 | 名单类型，取值： black：黑名单。 white：白名单。 说明 黑、白名单互斥，同一时间只支持其中一种方式生效。 | black |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "ua", "argValue": "*curl*|*IE*|*chrome*|*firefox*" }, { "argName": "type", "argValue": "black" }], "functionName": "ali_ua" }], "DomainNames": "example.com" }

## 性能优化

tesla

- 

功能说明：配置页面优化加速，该功能详细介绍请参见控制台配置说明[页面优化](products/cdn/documents/user-guide/enable-html-optimization.md)。

- 

功能ID（FunctionID/FuncId）：16。

- 

参数说明：

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启页面优化加速： on：开启。 off：关闭。 | on |
| trim_js | String | 否 | 是否优化 HTML 中内嵌的 JS 代码： on：开启。 off（默认）：关闭。 | off |
| trim_css | String | 否 | 是否优化 HTML 中内嵌的 CSS 代码： on：开启。 off（默认）：关闭。 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "trim_css", "argValue": "off" }, { "argName": "trim_js", "argValue": "off" }], "functionName": "tesla" }], "DomainNames": "example.com" }

gzip

- 

功能说明：页面Gzip优化，该功能详细介绍请参见控制台配置说明[Gzip](products/cdn/documents/user-guide/use-the-gzip-compression-feature.md)[压缩](products/cdn/documents/user-guide/use-the-gzip-compression-feature.md)。

- 

功能ID（FunctionID/FuncId）：35。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启页面 Gzip 优化： on：开启。 off：关闭。 | on |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "gzip" }], "DomainNames": "example.com" }

brotli

- 

功能说明：配置页面Brotli压缩，该功能详细介绍请参见控制台配置说明[Brotli](products/cdn/documents/user-guide/configure-brotli-compression.md)[压缩](products/cdn/documents/user-guide/configure-brotli-compression.md)。

- 

功能ID（FunctionID/FuncId）：97。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启页面 Brotli 压缩： on：开启。 off：关闭。 | on |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "brotli" }], "DomainNames": "example.com" }

set_hashkey_args

- 

功能说明：配置忽略URL参数（保留），该功能详细介绍请参见控制台配置说明[忽略参数](products/cdn/documents/user-guide/ignore-parameters.md)。

- 

功能冲突说明：忽略URL参数（保留）功能与忽略URL参数（删除）功能（功能函数：ali_remove_args，功能ID：75）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：19。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| hashkey_args | String | 否 | 保留参数列表，多个用半角逗号（,）分隔，最多支持填写 10 个。 | key1,key2 |
| disable | String | 是 | 是否忽略所有参数： on：忽略所有参数，除了添加参数功能仍能生效以外，删除参数、仅保留、修改参数功能都将失效。 off（默认）：关闭忽略参数功能，保留参数、添加参数、删除参数仍会生效。 说明 缓存 hashkey 忽略所有参数，优先级低于保留缓存参数列表功能。 | on |
| keep_oss_args | String | 是 | 是否保留回源参数： on：回源保留所有参数。 off：回源携带的参数与缓存 hashkey 的参数一致。 | on |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "hashkey_args", "argValue": "" }, { "argName": "keep_oss_args", "argValue": "on" }, { "argName": "disable", "argValue": "on" }], "functionName": "set_hashkey_args" }], "DomainNames": "example.com" }

ali_remove_args

- 

功能说明：配置忽略URL参数（删除），该功能详细介绍请参见控制台配置说明[忽略参数](products/cdn/documents/user-guide/ignore-parameters.md)。

- 

功能冲突说明：忽略URL参数（删除）功能与忽略URL参数（保留）功能（功能函数：set_hashkey_args，功能ID：19）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](products/cdn/documents/developer-reference/api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。

- 

功能ID（FunctionID/FuncId）：75。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ali_remove_args | String | 是 | 删除指定的参数，多个参数之间用空格隔开。 说明 剩余参数将作为 hashkey 中 URL args 部分。 | test |
| keep_oss_args | String | 是 | 回源是否保留参数： on：回源保留所有参数。 off：回源携带的参数与缓存 hashkey 的参数一致。 | off |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "ali_remove_args", "argValue": "test" }, { "argName": "keep_oss_args", "argValue": "off" }], "functionName": "ali_remove_args" }], "DomainNames": "example.com" }

image_transform

- 

功能说明：配置CDN图片转换，该功能详细介绍请参见控制台配置说明[图片处理概述](products/cdn/documents/user-guide/image-editing-overview.md)。

- 

功能ID（FunctionID/FuncId）：239。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启图片转换： on：开启。 off：关闭。 | on |
| filetype | String | 是 | 支持转码的图片格式，以竖线分割符号分隔。支持以下参数值： JPEG：JPEG 图片格式。 JPG：JPG 图片格式。 PNG：PNG 图片格式。 WEBP：WEBP 图片格式。 BMP：BMP 图片格式。 GIF：GIF 图片格式。 TIFF：TIFF 图片格式。 JP2：JPEG 2000 图片格式。 | jpg|jpeg|png |
| webp | String | 否 | 是否开启自适应转换 WEBP： on：开启。 off：关闭。 | on |
| orient | String | 否 | 是否开启图片自旋转： on：开启。 off：关闭。 说明 只对有自旋转属性的图片生效。 | on |
| slim | Integer | 否 | 图片瘦身，设置瘦身的百分比，可配置范围是[0,100]。在不改变分辨率、尺寸、格式的前提下，缩小图片质量达到省流目的。 | 10 |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "filetype", "argValue": "jpg|jpeg|png" }, { "argName": "webp", "argValue": "on" }, { "argName": "orient", "argValue": "on" }, { "argName": "slim", "argValue": "" }, { "argName": "enable", "argValue": "on" }], "functionName": "image_transform" }], "DomainNames": "example.com" }

## 视频相关

range

- 

功能说明：配置range回源，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/object-chunking.md)[Range](products/cdn/documents/user-guide/object-chunking.md)[回源](products/cdn/documents/user-guide/object-chunking.md)。

- 

功能ID（FunctionID/FuncId）：31。

- 

参数说明：

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启 range 回源： on：开启。 off：关闭。 force：强制开启。 | on |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "range" }], "DomainNames": "example.com" }

video_seek

- 

功能说明：配置视频拖拽播放，该功能详细介绍请参见控制台配置说明[配置拖拽播放](products/cdn/documents/user-guide/video-seeking.md)。

- 

功能ID（FunctionID/FuncId）：30。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启视频拖拽播放： on：开启。 off：关闭。 | on |
| flv_seek_by_time | String | 否 | 是否开启 FLV 按时间拖拽： on：开启。 off：关闭。 | on |
| mp4_seek_start | String | 否 | 自定义 MP4 启动参数。 | mp4starttime |
| mp4_seek_end | String | 否 | 自定义 MP4 结束参数。 | mp4endtime |
| flv_seek_start | String | 否 | 自定义 FLV 启动参数。 | flvstarttime |
| flv_seek_end | String | 否 | 自定义 FLV 结束参数。 | flvendtime |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "video_seek" }], "DomainNames": "example.com" }

ali_video_split

- 

功能说明：配置听视频，该功能详细介绍请参见控制台配置说明[配置听视频](products/cdn/documents/user-guide/audio-extraction.md)。

- 

功能ID（FunctionID/FuncId）：204。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启听视频： on：开启。 off：关闭。 | on |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "ali_video_split" }], "DomainNames": "example.com" }

ali_video_preview

- 

功能说明：配置视频试看，该功能详细介绍请参见控制台配置说明[配置音视频试看](products/cdn/documents/user-guide/audio-and-video-preview.md)。

- 

功能ID（FunctionID/FuncId）：205。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启视频试看： on：开启。 off：关闭。 说明 支持 TS、MP3 文件格式，FLV 和 MP4 使用拖拽功能实现。 | on |
| ali_video_preview_argument | String | 是 | 自定义试看参数名，试看参数值的单位必须是秒。 | fds |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "ali_video_preview_argument", "argValue": "fds" }], "functionName": "ali_video_preview" }], "DomainNames": "example.com" }

hls_token_rewrite

- 

功能说明：配置M3U8标准加密改写，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/m3u8-encryption-and-rewrite.md)[M3U8](products/cdn/documents/user-guide/m3u8-encryption-and-rewrite.md)[标准加密改写](products/cdn/documents/user-guide/m3u8-encryption-and-rewrite.md)。

- 

功能ID（FunctionID/FuncId）：253。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启 M3U8 标准加密改写： on：开启。 off：关闭。 | on |
| hls_token_arg_name | String | 否 | 自定义 hls token 的参数名称。如果不设置，使用 MtsHlsUriToken 作为自定义参数名。 | example |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "hls_token_rewrite" }], "DomainNames": "example.com", }

## 流量限制

limit_rate

- 

功能说明：配置单请求限速。

- 

功能ID（FunctionID/FuncId）：72。

- 

参数说明：

可以仅配置ali_limit_rate，也可以根据用户请求URL中携带的参数来限速，还可以设定限速开始和结束时间。

根据用户请求URL中携带的参数来限速：通过traffic_limit_arg和traffic_limit_unit这两个参数的组合来实现。

设定限速开始和结束时间：通过ali_limit_start_hour和ali_limit_end_hour这两个参数的组合来实现。

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ali_limit_rate | String | 是 | 指定单请求限速的具体速率（例如：200 KByte/s、1 MByte/s 等），支持“数值+字母单位”的参数值（字母单位支持 k、m），单位 Byte/s。 最小只能设定为 100k，低于 100k 的值将会按 100k 来执行。 | 1m：表示单请求限速为 1 MByte/s 100k：表示单请求限速为 100 KByte/s |
| ali_limit_rate_after | String | 否 | 不限速大小，在发送了多少数据之后才开始限速。支持“数值+字母单位”的参数值（字母单位支持 k、m），单位 Byte。 | 1000 |
| traffic_limit_arg | String | 否 | 限速参数名称，根据 URL 中提取的 arg 进行限速，例如：rate。 当请求中不带限速参数时，按默认限速值 ali_limit_rate 限速，如果想达到请求中没限速参数时不限速的效果，则把默认限速值 ali_limit_rate 配置为 0k。 | rate |
| traffic_limit_unit | String | 否 | 限速参数 traffic_limit_arg 的单位，支持 m（MByte/s）、k（KByte/s）。限速参数单位设定为 m 的情况下，当用户请求 URL 中携带的 rate=1 时，实际限速值为 1MByte/s。 最小只能设定为 100k，低于 100k 的值将会按 100k 来执行。 | m |
| ali_limit_start_hour | Integer | 否 | 限速开始时间，取值范围[0,24]，小于限速结束时间，默认值为 0。 说明 表示时间点，24 小时制的整点，例如：0 表示 00:00:00，24 表示 24:00:00。 | 20 |
| ali_limit_end_hour | Integer | 否 | 限速结束时间，取值范围[0,24]，大于限速开始时间，默认值为 24。 | 23 |


- 

配置示例一：设置单请求限速为1 MByte/s。

{ "Functions": [{ "functionArgs": [{ "argName": "ali_limit_rate", "argValue": "1m" }], "functionName": "limit_rate" }], "DomainNames": "example.com" }

- 

配置示例二：默认情况下，单请求限速为1 MByte/s，如果用户请求URL中携带了参数rate，则会按照参数rate的实际数值来执行限速。例如：用户请求中携带了参数rate=200，则实际将会被限速为200 KByte/s。

{ "Functions": [{ "functionArgs": [{ "argName": "ali_limit_rate", "argValue": "1m" },{ "argName": "traffic_limit_arg", "argValue": "rate" },{ "argName": "traffic_limit_unit", "argValue": "k" }], "functionName": "limit_rate" }], "DomainNames": "example.com" }

## EdgeScript边缘脚本/边缘函数

edge_function

- 

功能说明：边缘脚本EdgeScript，该功能详细介绍请参见控制台配置说明[EdgeScript](products/cdn/documents/user-guide/edgescript-overview.md)[概述](products/cdn/documents/user-guide/edgescript-overview.md)。

- 

功能ID（FunctionID/FuncId）：180。

- 

参数说明：

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| rule | String | 是 | DSL 规则。 | if eq($uri, '/') {\n rewrite('https://example.com/index.html', 'redirect')\n} |
| pri | Integer | 是 | 优先级，取值：[0,999]，数字越小优先级越高。 说明 头部执行和尾部执行的优先级互相独立。 | 0 |
| enable | String | 是 | 本条规则是否生效： on：生效。 off：无效。 | on |
| name | String | 是 | 规则名称，仅支持英文字母和下划线（_）。 | test |
| pos | String | 否 | 规则执行位置，取值： head（默认值）：请求处理流程头部介入。 foot：请求处理流程尾部介入。 | head |
| brk | String | 否 | 中断执行，取值： on：命中本条规则后，当前执行位置剩余规则均跳过。 off（默认值）：命中本条规则后，还会执行剩余规则。 | off |
| option | String | 否 | 扩展字段。 | 空 |
| grammar | String | 否 | 规则语法，取值：es2（默认值）和 js。 | / |
| jsmode | String | 否 | JS 执行模式，取值： redirect：拦截模式。 bypass（默认值）：旁路模式。 | / |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "name", "argValue": "test" }, { "argName": "rule", "argValue": "if eq($uri, '/') {\n rewrite('https://example.com/index.html', 'redirect')\n}" }, { "argName": "pri", "argValue": "0" }, { "argName": "pos", "argValue": "head" }, { "argName": "enable", "argValue": "on" }, { "argName": "brk", "argValue": "off" }, { "argName": "option", "argValue": "" }], "functionName": "edge_function" }], "DomainName": "example.com" }

## 边缘函数

edgeroutine

- 

功能说明：边缘函数，该功能详细介绍请参见控制台配置说明[什么是边缘函数](products/cdn/documents/developer-reference/what-is-er.md)。

- 

功能ID（FunctionID/FuncId）：275。

- 

该功能需要申请再开通，您需要[填写信息](https://page.aliyun.com/form/act2017566026/index.htm)申请开通该功能。

## 规则引擎

condition

- 

功能说明：规则引擎，该功能能够使用图形化的方式来配置各种条件规则。条件规则支持对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效，可用于更加灵活、更加精确地控制CDN的各种配置策略的执行效果。该功能详细介绍请参见控制台配置说明[规则引擎](products/cdn/documents/user-guide/rules-engine.md)。

- 

功能ID（FunctionID/FuncId）：250。

- 

该功能需要申请再开通，您需要[填写信息](https://page.aliyun.com/form/act2017566026/index.htm)申请开通该功能。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| rule | Array | 是 | 规则条件的具体内容，包括名称、状态、逻辑判断、条件表达式。 | 规则条件内容： {\"match\":{\"logic\":\"and\",\"criteria\":[{\"matchType\":\"clientipVer\",\"matchObject\":\"CONNECTING_IP\",\"matchOperator\":\"equals\",\"matchValue\":\"v6\",\"negate\":false}]},\"name\":\"example\",\"status\":\"enable\"} 实现效果： 规则名称：example 状态：enable 逻辑判断：and 条件表达式：客户端建联 IP 的协议版本等于 v6 |


条件表达式的格式（即argValue的格式）说明如下：

| 参数 | 说明 |
| --- | --- |
| \"match\": | match 表示条件匹配表达式。 |
| \"logic\":\"and\" | logic 表示条件匹配表达式的逻辑判断参数，取值为 and 和 or。 |
| \"criteria\" | criteria 表示条件表达式的判断内容。 |
| \"matchType\":\"clientipVer\" | matchType 表示对用户请求中携带的某一类型信息进行匹配。 |
| \"matchObject\":\"CONNECTING_IP\" | matchObject 表示对匹配类型进行进一步的细分，例如：客户端 IP 可以进一步细分为“建联 IP”和“XFF IP”。 |
| \"matchOperator\":\"equals\" | matchOperator 表示匹配操作执行的具体动作。 |
| \"matchValue\":\"v6\" | matchValue 表示预先设定的匹配值，将会与用户请求中携带的信息进行匹配。 |
| \"negate\":false | negate 表示是否对条件表达式的结果取反，取值为 true 和 false。 |
| \"name\":\"example\" | name 表示规则条件的名称。 |
| \"status\":\"enable\" | status 表示规则条件的生效状态。 |


- 

配置示例：

以下示例演示了如何通过OpenAPI来给加速域名example.com添加一个规则引擎配置，实现对客户端IP协议版本是否为IPv6的匹配和过滤。对于规则引擎功能的详细说明请参见[规则引擎](products/cdn/documents/user-guide/rules-engine.md)。

{ "Functions": [{ "functionArgs": [{ "argName": "rule", "argValue": "{\"match\":{\"logic\":\"and\",\"criteria\":[{\"matchType\":\"clientipVer\",\"matchObject\":\"CONNECTING_IP\",\"matchOperator\":\"equals\",\"matchValue\":\"v6\",\"negate\":false}]},\"name\":\"example\",\"status\":\"enable\"}" }], "functionName": "condition" }], "DomainNames": "example.com" }

创建完成的规则引擎配置，可以供其他功能配置时关联引用（当前支持引用规则引擎配置的功能列表请参见[规则引擎](products/cdn/documents/user-guide/rules-engine.md)），以实现更加灵活、更加精确地控制CDN各种配置策略的执行效果。例如：[条件源站功能](products/cdn/documents/user-guide/configure-a-conditional-origin.md)（功能函数是origin_dns_host）的配置就可以关联引用规则引擎的配置，配置示例可以参见[origin_dns_host](products/cdn/documents/developer-reference/parameters-for-configuring-features-for-domain-names.md)。

注意事项：

- 

其他功能在关联引用规则引擎配置的时候，需要通过设置parentid来引用已经使用规则引擎功能创建好的某个规则条件，这里的parentid等于添加规则引擎配置时生成的configid。

- 

功能函数是condition（规则引擎）的时候，不支持设置parentId参数。

## 安全配置

ali_location

- 

功能说明：区域封禁，该功能详细介绍请参见控制台配置说明[区域封禁](products/cdn/documents/user-guide/configure-a-region-blacklist-or-whitelist.md)。

- 

功能ID（FunctionID/FuncId）：57。

- 

参数说明：

- 

- 

- 

- 

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| location | String | 是 | 用于设置封禁策略应用的区域，输入的值包含两种格式： 支持设置区域为某个国家，使用两位大写英文字母组成的国家编码（遵循 ISO3166 标准规范），支持同时输入多个值（不同值之间使用空格分隔）。 支持设置区域为全球（global）。 | CN |
| type | String | 是 | 用于设置封禁策略的类型，取值范围： black：黑名单，封禁对应区域的客户端 IP white：白名单，封禁对应区域以外的客户端 IP | black |


- 

配置示例：

{ "Functions": [{ "functionArgs": [{ "argName": "location", "argValue": "CN" }, { "argName": "type", "argValue": "black" }], "functionName": "ali_location" }], "DomainNames": "example.com" }

## QUIC

iquic

- 

功能说明：QUIC基础参数，该功能详细介绍请参见控制台配置说明[配置](products/cdn/documents/user-guide/what-is-the-quic-protocol.md)[QUIC](products/cdn/documents/user-guide/what-is-the-quic-protocol.md)[协议](products/cdn/documents/user-guide/what-is-the-quic-protocol.md)。

- 

功能ID（FunctionID/FuncId）：281。

- 

参数说明：

- 

- 

| 参数 | 类型 | 是否必填 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| iquic_enable | String | 是 | 是否开启 QUIC 协议： on：开启 off：关闭 | on |


- 

配置示例

{ "Functions": [{ "functionArgs": [{ "argName": "iquic_enable", "argValue": "on" }], "functionName": "iquic" }], "DomainNames": "example.com" }

[上一篇：附录](products/cdn/documents/developer-reference/apiappendix.md)[下一篇：ConfigId使用说明](products/cdn/documents/developer-reference/usage-notes-on-configid.md)

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
