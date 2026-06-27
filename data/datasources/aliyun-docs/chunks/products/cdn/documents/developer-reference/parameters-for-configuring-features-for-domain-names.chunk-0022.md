用空格隔开。 | value=123 |
| modify_argument | String | 否 | 修改参数，优先级最低，若参数被删除则不会保留，多个参数用空格隔开。 | value=321 |
| enable | String | 是 | 是否开启改写回源参数： on：开启。 off：关闭 。 | on |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "delete_argument", "argValue": "" }, { "argName": "save_argument", "argValue": "" }, { "argName": "add_argument", "argValue": "" }, { "argName": "modify_argument", "argValue": "" }, { "argName": "ignore_all_argument", "argValue": "on" }, { "argName": "enable", "argValue": "on" }], "functionName": "back_to_origin_argument_rewrite" }], "DomainNames": "example.com" }
aws_s3_bucket
功能说明：配置Amazon S3鉴权Bucket。
功能ID（FunctionID/FuncId）：186。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enabled | String | 是 | 是否开启 Amazon S3 鉴权 Bucket： l2：开启。 off：关闭。 | l2 |
| bucketname | String | 否 | Amazon S3 Bucket 名称。 | / |
| accesskey | String | 是 | AWS AccessKey。 | 123456789 |
| secretkey | String | 是 | AWS SecretKey。 | 12345678 |
| region | String | 是 | Amazon S3 存储区域。 | us-east-2 |
