cy，单击确认新增授权。
确认新增授权之后，回到CDN控制台的回源配置页面，可以看到阿里云OSS私有Bucket回源功能已经完成授权，
开启阿里云OSS私有Bucket回源并配置回源类型。
找到阿里云OSS私有Bucket回源区域，打开其开关。
在弹出的阿里云OSS私有Bucket回源对话框中，选择回源类型，单击确定。

| 回源类型 | 推荐场景与说明 |
| --- | --- |
| 同账号回源 | （推荐） 适用于 CDN 和 OSS Bucket 在同一个阿里云账号下的场景。系统将自动使用 STS 临时安全令牌进行鉴权，配置简单，无需管理密钥，安全性更高。 STS 临时安全令牌也可以实现跨账号回源，详情请参见 [CDN](back-to-source-faq.md) [使用](back-to-source-faq.md) [STS](back-to-source-faq.md) [实现跨账号回源](back-to-source-faq.md) [OSS](back-to-source-faq.md) [私有](back-to-source-faq.md) [Bucket](back-to-source-faq.md) [操作指引](back-to-source-faq.md) 。 |
| 跨账号回源或同账号回源 | 适用于 CDN 和 OSS Bucket 分属不同阿里云账号的场景，也支持同账号。此方式需要您手动提供回源目标 OSS 私有 Bucket 所属阿里云账号的 AccessKey ID 和 AccessKey Secret。具体请参见 [创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md) [AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md) 。 |

说明
访问范围说明：开启后，该加速域名将可以访问其源站私有Bucket内的所有资源，无法在CDN侧对Bucket内的部分资源做访问限制。
签名冲突说明：为避免OSS鉴权失败，请确保回源请求的URL参数中不携带签名信息。单个请求不能同时在Header和URL中携带签名。
功能冲突说明：本功能与OSS的静态网站托管功能的默认首页配置存在冲突。如需同时使用，请参考[说明文档](../you-are-forbidden-to-list-buckets-after-access-to-private-oss-buckets-is-enabled.md)。
