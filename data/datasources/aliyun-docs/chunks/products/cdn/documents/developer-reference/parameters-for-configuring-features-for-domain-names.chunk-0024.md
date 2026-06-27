String | 是 | 是否启用回源证书校验： on：启用。 off：关闭。 | on |
| common_name_whitelist | String | 否 | 证书白名单域名列表，支持配置多个域名，多个域名之间使用英文逗号（,）分隔。匹配了这些白名单域名的证书可以通过校验。 | example.com |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "common_name_whitelist", "argValue": "example.com" }], "functionName": "origin_certificate_verification" }], "DomainNames": "example.com" }
origin_dns_host
功能说明：配置条件源站，可以通过与规则引擎功能（功能函数：condition，功能ID：250）配合使用，实现基于用户请求中的路径、URL参数、请求头等信息来回源到指定源站。该功能详细介绍请参见控制台配置说明[配置条件源站](../user-guide/configure-a-conditional-origin.md)。
前提条件：在添加条件源站配置之前，您需要至少先创建一条规则引擎的规则条件，在添加条件源站配置时，您必须配置一条关联的规则条件，具体请参见[规则引擎](parameters-for-configuring-features-for-domain-names.md)。如果添加条件源站配置时没有关联规则条件，则会使CDN回源的所有流量都指向这个唯一的源站地址（也就失去了通过规则条件来控制回源地址的意义）。
功能冲突说明：条件源站功能与高级回源功能（功能函数：advanced_origin，功能ID：235）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：212。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ali_origin_dns_host | String | 是 | 回源查询 DNS 使用的域名。 | example.com |
