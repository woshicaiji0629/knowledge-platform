| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| client_certificate_verify | String | 是 | 是否开启客户端证书认证： on：开启。 off：关闭。 | on |
| client_certificate | String | 是 | 自行签发的客户端证书（公钥），CA 证书的格式有以下要求： 以 -----BEGIN CERTIFICATE----- 开头，以 -----END CERTIFICATE----- 结尾。 | -----BEGIN PUBLIC KEY----- *********** -----END PUBLIC KEY----- |
| client_verify_depth | String | 否 | 认证深度，即 证书链深度 ，是指在验证一个 客户端证书 的有效性时，其所依赖的 证书信任链 中包含的证书层级数量（从 客户端证书本身 回溯到 根 CA 证书 之间的层级数），默认值为 1。 | 1 |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "client_certificate_verify", "argValue": "on" }, { "argName": "client_certificate", "argValue": "-----BEGIN PUBLIC KEY-----***********-----END PUBLIC KEY-----" }], "functionName": "https_client_cert" }], "DomainNames": "example.com" }
HSTS
功能说明：配置HSTS，该功能详细介绍请参见控制台配置说明[配置](../user-guide/configure-hsts.md)[HSTS](../user-guide/configure-hsts.md)。
功能ID（FunctionID/FuncId）：112。
参数说明：
