ents/user-guide/create-an-accesskey-pair.md) [AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md) 。 | access_id=123 access_secret=123abc |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "host", "argValue": "example.oss-cn-hangzhou.aliyuncs.com" },{ "argName": "key", "argValue": "access_id=123 access_secret=123abc" }], "functionName": "oss_key_list" }], "DomainNames": "example.com" }
https_origin_sni
功能说明：配置回源SNI，该功能详细介绍请参见控制台配置说明[配置默认回源](../user-guide/configure-sni.md)[SNI](../user-guide/configure-sni.md)。
功能ID（FunctionID/FuncId）：114。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enabled | String | 是 | 是否开启回源 SNI 功能： on：开启。 off：关闭。 | on |
| https_origin_sni | String | 是 | 回源请求携带的 SNI 信息（即回源请求需要访问的源站地址）。 | origin.example.com |
