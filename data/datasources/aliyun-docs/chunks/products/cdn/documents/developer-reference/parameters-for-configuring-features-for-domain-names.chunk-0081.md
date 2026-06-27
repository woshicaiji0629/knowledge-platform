属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：75。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ali_remove_args | String | 是 | 删除指定的参数，多个参数之间用空格隔开。 说明 剩余参数将作为 hashkey 中 URL args 部分。 | test |
| keep_oss_args | String | 是 | 回源是否保留参数： on：回源保留所有参数。 off：回源携带的参数与缓存 hashkey 的参数一致。 | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "ali_remove_args", "argValue": "test" }, { "argName": "keep_oss_args", "argValue": "off" }], "functionName": "ali_remove_args" }], "DomainNames": "example.com" }
image_transform
功能说明：配置CDN图片转换，该功能详细介绍请参见控制台配置说明[图片处理概述](../user-guide/image-editing-overview.md)。
功能ID（FunctionID/FuncId）：239。
参数说明：
