cesskey | String | 是 | AWS AccessKey。 | 123456789 |
| secretkey | String | 是 | AWS SecretKey。 | 12345678 |
| region | String | 是 | Amazon S3 存储区域。 | us-east-2 |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enabled", "argValue": "l2" }, { "argName": "accesskey", "argValue": "123456789" }, { "argName": "secretkey", "argValue": "123456789" }, { "argName": "region", "argValue": "us-east-2" }], "functionName": "aws_s3_bucket" }], "DomainNames": "example.com" }
origin_certificate_verification
功能说明：配置回源证书校验（SNI白名单），该功能详细介绍请参见控制台配置说明[Common Name](../user-guide/common-name-whitelist.md)[白名单](../user-guide/common-name-whitelist.md)。
功能ID（FunctionID/FuncId）：223。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enabled | String | 是 | 是否启用回源证书校验： on：启用。 off：关闭。 | on |
| common_name_whitelist | String | 否 | 证书白名单域名列表，支持配置多个域名，多个域名之间使用英文逗号（,）分隔。匹配了这些白名单域名的证书可以通过校验。 | example.com |
