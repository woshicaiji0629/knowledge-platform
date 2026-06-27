属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：19。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| hashkey_args | String | 否 | 保留参数列表，多个用半角逗号（,）分隔，最多支持填写 10 个。 | key1,key2 |
| disable | String | 是 | 是否忽略所有参数： on：忽略所有参数，除了添加参数功能仍能生效以外，删除参数、仅保留、修改参数功能都将失效。 off（默认）：关闭忽略参数功能，保留参数、添加参数、删除参数仍会生效。 说明 缓存 hashkey 忽略所有参数，优先级低于保留缓存参数列表功能。 | on |
| keep_oss_args | String | 是 | 是否保留回源参数： on：回源保留所有参数。 off：回源携带的参数与缓存 hashkey 的参数一致。 | on |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "hashkey_args", "argValue": "" }, { "argName": "keep_oss_args", "argValue": "on" }, { "argName": "disable", "argValue": "on" }], "functionName": "set_hashkey_args" }], "DomainNames": "example.com" }
ali_remove_args
功能说明：配置忽略URL参数（删除），该功能详细介绍请参见控制台配置说明[忽略参数](../user-guide/ignore-parameters.md)。
功能冲突说明：忽略URL参数（删除）功能与忽略URL参数（保留）功能（功能函数：set_hashkey_args，功能ID：19）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：75。
参数说明：
