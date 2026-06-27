uncId）：10。
注意事项：在给加速域名配置了OSS类型的源站地址之后，平台将会自动添加oss_auth配置，无需用户手动添加，也请用户注意不要误删该配置，否则会引起OSS源站无法实现对CDN回源流量的计费减免，在开启OSS私有bucket鉴权的情况下，还会导致CDN回源OSS私有bucket鉴权失败。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| oss_bucket_id | String | 是 | OSS bucket 的公网域名地址。 | cdn-test.oss-cn-hongkong.aliyuncs.com |
| oss_pri_buckets | String | 是 | OSS bucket 的公网域名地址及其对应的 bucket 名称。 | cdn-test.oss-cn-hongkong.aliyuncs.com|cdn-test |

配置示例：
{ "Functions": [ { "ArgValue": "cdn-test.oss-cn-hongkong.aliyuncs.com", "ArgName": "oss_bucket_id" }, { "ArgValue": "cdn-test.oss-cn-hongkong.aliyuncs.com|cdn-test", "ArgName": "oss_pri_buckets" } ], "functionName": "oss_auth" }], "DomainNames": "example.com" }
