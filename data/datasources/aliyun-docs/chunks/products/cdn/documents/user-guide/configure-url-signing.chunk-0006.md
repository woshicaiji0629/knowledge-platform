## 验证鉴权URL正确性
为保证服务器正确实现了鉴权逻辑，配置鉴权URL后，建议您在CDN控制台生成对应的鉴权URL，校验鉴权URL的正确性。
在鉴权URL生成工具区域，配置原始URL（未编码）和鉴权信息。

| 参数 | 说明 |
| --- | --- |
| 原始 URL（未编码） | 输入完整的原始 URL 地址，例如： https://www.aliyun.com 。生成鉴权 URL 时，工具将自动编码原始 URL。 |
| 鉴权类型 | 按照您在 [配置鉴权](configure-url-signing.md) [URL](configure-url-signing.md) [并开启鉴权](configure-url-signing.md) 的配置，选择 URL 鉴权类型。 |
| 鉴权 KEY | 按照您在 [配置鉴权](configure-url-signing.md) [URL](configure-url-signing.md) [并开启鉴权](configure-url-signing.md) 的配置，输入您配置的 主 KEY 或 备 KEY 。 |
| 鉴权 URL 有效时长 | 按照您在 [配置鉴权](configure-url-signing.md) [URL](configure-url-signing.md) [并开启鉴权](configure-url-signing.md) 的配置，输入 URL 鉴权的有效时长，单位为秒。 |

单击开始生成，即可获得鉴权URL和Timestamp。
