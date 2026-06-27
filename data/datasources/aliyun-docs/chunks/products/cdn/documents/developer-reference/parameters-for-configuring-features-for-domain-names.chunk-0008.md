- | --- |
| enabled | String | 是 | 是否开启回源 SNI 功能： on：开启。 off：关闭。 | on |
| https_origin_sni | String | 是 | 回源请求携带的 SNI 信息（即回源请求需要访问的源站地址）。 | origin.example.com |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "https_origin_sni", "argValue": "origin.example.com" }, { "argName": "enabled", "argValue": "on" }], "functionName": "https_origin_sni" }], "DomainNames": "example.com" }
forward_timeout
功能说明：配置回源请求超时时间，该功能详细介绍请参见控制台配置说明[配置回源](../user-guide/configure-a-timeout-period-for-back-to-origin-http-requests.md)[HTTP](../user-guide/configure-a-timeout-period-for-back-to-origin-http-requests.md)[请求超时时间](../user-guide/configure-a-timeout-period-for-back-to-origin-http-requests.md)。
功能ID（FunctionID/FuncId）：124。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| forward_timeout | Integer | 是 | 请求超时时间，单位：秒。 说明 建议设置时间小于 100 秒。 | 30 |
