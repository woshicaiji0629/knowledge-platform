ionID/FuncId）：124。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| forward_timeout | Integer | 是 | 请求超时时间，单位：秒。 说明 建议设置时间小于 100 秒。 | 30 |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "forward_timeout", "argValue": "30" }], "functionName": "forward_timeout" }], "DomainNames": "example.com" }
advanced_origin
功能说明：配置高级回源，该功能详细介绍请参见控制台配置说明[高级回源](../user-guide/configure-advanced-origin-settings.md)。
功能冲突说明：高级回源功能与条件源站功能（功能函数：origin_dns_host，功能ID：212）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：235。
参数说明：
