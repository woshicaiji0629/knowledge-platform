。
功能ID（FunctionID/FuncId）：35。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启页面 Gzip 优化： on：开启。 off：关闭。 | on |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "gzip" }], "DomainNames": "example.com" }
brotli
功能说明：配置页面Brotli压缩，该功能详细介绍请参见控制台配置说明[Brotli](../user-guide/configure-brotli-compression.md)[压缩](../user-guide/configure-brotli-compression.md)。
功能ID（FunctionID/FuncId）：97。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启页面 Brotli 压缩： on：开启。 off：关闭。 | on |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "brotli" }], "DomainNames": "example.com" }
set_hashkey_args
功能说明：配置忽略URL参数（保留），该功能详细介绍请参见控制台配置说明[忽略参数](../user-guide/ignore-parameters.md)。
功能冲突说明：忽略URL参数（保留）功能与忽略URL参数（删除）功能（功能函数：ali_remove_args，功能ID：75）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：19。
参数说明：
