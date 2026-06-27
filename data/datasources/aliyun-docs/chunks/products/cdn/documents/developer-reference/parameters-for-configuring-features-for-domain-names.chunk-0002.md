## 回源配置
set_req_host_header
功能说明：配置默认回源HOST，该功能详细介绍请参见控制台配置说明[配置默认回源](../user-guide/configure-the-default-origin-host.md)[HOST](../user-guide/configure-the-default-origin-host.md)。
功能ID（FunctionID/FuncId）：18。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| domain_name | String | 是 | 回源 HOST 头内容。 | example.com |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "domain_name", "argValue": "example.com" }], "functionName": "set_req_host_header" }], "DomainNames": "example.com" }
forward_scheme
功能说明：配置回源协议，该功能详细介绍请参见控制台配置说明[配置回源协议](../user-guide/configure-the-origin-protocol-policy.md)。
功能ID（FunctionID/FuncId）：47。
参数说明：
