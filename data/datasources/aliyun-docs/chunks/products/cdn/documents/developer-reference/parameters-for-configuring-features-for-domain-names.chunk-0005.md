ermissions-on-private-oss-buckets.md)[回源](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)。
功能ID（FunctionID/FuncId）：85。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| private_oss_auth | String | 是 | 是否开启私有 Bucket 回源： on：开启。 off：关闭。 功能开启以后，系统会自动配置 STS 安全令牌，配置更简单，但是仅支持 CDN 域名回源到同一个阿里云账号下的 OSS 私有 Bucket。关于 STS 安全令牌更多信息，请参见 [什么是](../../../ram/documents/user-guide/what-is-sts.md) [STS](../../../ram/documents/user-guide/what-is-sts.md) 。 | on |
| perm_private_oss_tbl | String | 否 | 永久安全令牌配置，配置格式是 access_id=123 access_secret=123abc （中间用空格分隔）。 配置了永久安全令牌以后，除了支持 CDN 域名回源到同一个阿里云账号下的 OSS 私有 Bucket，还支持 CDN 域名回源到其他阿里云账号下的 OSS 私有 Bucket。关于永久安全令牌更多信息，请参见 [创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md) [AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md) 。 | access_id=123 access_secret=123abc |
