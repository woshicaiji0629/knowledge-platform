ents/user-guide/create-an-accesskey-pair.md) [AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md) 。 | access_id=123 access_secret=123abc |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "private_oss_auth", "argValue": "on" },{ "argName": "perm_private_oss_tbl", "argValue": "access_id=123 access_secret=123abc" }], "functionName": "l2_oss_key" }], "DomainNames": "example.com" }
oss_key_list
功能说明：OSS回源私钥列表，可以配置一条或者多条规则，代表多个不同的OSS私有Bucket与对应的安全令牌。
功能ID（FunctionID/FuncId）：183。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| host | String | 是 | OSS Bucket 的完整地址。 | example.oss-cn-hangzhou.aliyuncs.com |
| key | String | 是 | 永久安全令牌配置，配置格式是 access_id=123 access_secret=123abc （中间用空格分隔）。 配置了永久安全令牌以后，除了支持 CDN 域名回源到同一个阿里云账号下的 OSS 私有 Bucket，还支持 CDN 域名回源到另一个阿里云账号下的 OSS 私有 Bucket。关于永久安全令牌更多信息，请参见 [创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md) [AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md) 。 | access_id=123 access_secret=123abc |
