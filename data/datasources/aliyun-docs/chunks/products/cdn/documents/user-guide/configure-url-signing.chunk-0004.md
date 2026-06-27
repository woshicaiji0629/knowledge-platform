| 参数 | 说明 |
| --- | --- |
| 鉴权类型 | 阿里云 CDN 提供了 4 种鉴权签名计算方式。您可以根据访问加密 URL 格式，选择合适的鉴权方式，实现对源站资源的有效保护。URL 鉴权类型如下： [鉴权方式](type-a-signing.md) [A](type-a-signing.md) [说明](type-a-signing.md) [鉴权方式](type-b-signing.md) [B](type-b-signing.md) [说明](type-b-signing.md) [鉴权方式](type-c-signing.md) [C](type-c-signing.md) [说明](type-c-signing.md) [鉴权方式](authentication-method-f-description.md) [F](authentication-method-f-description.md) [说明](authentication-method-f-description.md) 说明 URL 鉴权错误会返回 403 报错： MD5 计算类错误 例如： X-Tengine-Error:denied by req auth: invalid md5hash=de7bfdc915ced05e17380a149bd760be 时间类报错 例如： X-Tengine-Error:denied by req auth: expired timestamp=1439469547 |
| 主 KEY | 输入鉴权方式对应的主用密码。由 6~128 个字符组成，支持大写字母、小写字母、数字。 |
| 备 KEY | 输入鉴权方式对应的备用密码。由 6~128 个字符组成，支持大写字母、小写字母、数字。主、备 KEY 至少要填写一个。 |
| 鉴权 URL 有效时长 | CDN 配置的鉴权 URL 有效时长，用户可在（timestamp+CDN 上鉴权 URL 有效时长）时间区间内访问 CDN，超出该区间，鉴权失效。 单位：秒 取值范围：1~31536000 默认值：1800（30 分钟） 示例： 例如签算服务器生成鉴权 URL 的时间（timestamp）为 2020-08-15 15:00:00（UTC+8），CDN 上鉴权 URL 有效时长为 1800 秒，则鉴权 URL 失效时间为 2020-08-15 15:30:00（UTC+8）。 |
| 签名参数 | 通过设置签名参数，可以自定义签名参数名称。仅在鉴权类型设置为 F 方式的时候有效。 |
| 时间戳参数 | 通过设置时间戳参数，可以自定义时间戳参数名称。仅在鉴权类型设置为 F 方式的时候有效。 |
| 时间戳格式 | 设置时间戳格式，支持十进制（Unix 时间戳）和十六进制
