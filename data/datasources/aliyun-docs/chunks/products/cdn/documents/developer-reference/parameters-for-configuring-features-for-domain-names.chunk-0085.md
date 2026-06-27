| String | 是 | 是否开启视频试看： on：开启。 off：关闭。 说明 支持 TS、MP3 文件格式，FLV 和 MP4 使用拖拽功能实现。 | on |
| ali_video_preview_argument | String | 是 | 自定义试看参数名，试看参数值的单位必须是秒。 | fds |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "ali_video_preview_argument", "argValue": "fds" }], "functionName": "ali_video_preview" }], "DomainNames": "example.com" }
hls_token_rewrite
功能说明：配置M3U8标准加密改写，该功能详细介绍请参见控制台配置说明[配置](../user-guide/m3u8-encryption-and-rewrite.md)[M3U8](../user-guide/m3u8-encryption-and-rewrite.md)[标准加密改写](../user-guide/m3u8-encryption-and-rewrite.md)。
功能ID（FunctionID/FuncId）：253。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启 M3U8 标准加密改写： on：开启。 off：关闭。 | on |
| hls_token_arg_name | String | 否 | 自定义 hls token 的参数名称。如果不设置，使用 MtsHlsUriToken 作为自定义参数名。 | example |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "hls_token_rewrite" }], "DomainNames": "example.com", }
