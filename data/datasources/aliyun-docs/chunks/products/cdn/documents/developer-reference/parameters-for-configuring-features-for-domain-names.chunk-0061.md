xample.com" }
HSTS
功能说明：配置HSTS，该功能详细介绍请参见控制台配置说明[配置](../user-guide/configure-hsts.md)[HSTS](../user-guide/configure-hsts.md)。
功能ID（FunctionID/FuncId）：112。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enabled | String | 是 | 是否开启 HSTS： on：开启。 off：关闭。 | on |
| https_hsts_max_age | Integer | 是 | 过期时间，单位：秒。 说明 建议填写 5184000s（60 天）。 | 5184000 |
| https_hsts_include_subdomains | String | 否 | 配置 HSTS 头部是否包含子域名参数，取值 on 或者 off。 说明 开启前请确保该加速域名的所有子域名都已开启 HTTPS，否则会导致子域名自动跳转到 HTTPS 后无法访问。 | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enabled", "argValue": "on" }, { "argName": "https_hsts_max_age", "argValue": "5184000" }, { "argName": "https_hsts_include_subdomains", "argValue": "off" }], "functionName": "HSTS" }], "DomainNames": "example.com" }
