w", "argValue": "on" }], "functionName": "ipv6_origin" }], "DomainNames": "example.com" }
cos_auth
功能说明：配置腾讯云COS云存储的鉴权Bucket。
功能ID（FunctionID/FuncId）：288。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启腾讯云 COS 云存储鉴权 Bucket： on：开启。 off：关闭。 | on |
| cos_valid_period | String | 否 | 鉴权签名的有效时间，单位为秒，不填默认为 3600 秒。 | / |
| cos_secret_id | String | 是 | 腾讯云的鉴权 ID。 | 123456789 |
| cos_secret_key | String | 是 | 腾讯云的鉴权密钥。 | 12345678 |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "cos_secret_id", "argValue": "123456789" }, { "argName": "cos_secret_key", "argValue": "123456789" }], "functionName": "cos_auth" }], "DomainNames": "example.com" }
oss_auth
功能说明：用于配置CDN回源OSS使用的鉴权bucket信息。
功能ID（FunctionID/FuncId）：10。
注意事项：在给加速域名配置了OSS类型的源站地址之后，平台将会自动添加oss_auth配置，无需用户手动添加，也请用户注意不要误删该配置，否则会引起OSS源站无法实现对CDN回源流量的计费减免，在开启OSS私有bucket鉴权的情况下，还会导致CDN回源OSS私有bucket鉴权失败。
参数说明：
