ing | 否 | 自定义 MP4 结束参数。 | mp4endtime |
| flv_seek_start | String | 否 | 自定义 FLV 启动参数。 | flvstarttime |
| flv_seek_end | String | 否 | 自定义 FLV 结束参数。 | flvendtime |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "video_seek" }], "DomainNames": "example.com" }
ali_video_split
功能说明：配置听视频，该功能详细介绍请参见控制台配置说明[配置听视频](../user-guide/audio-extraction.md)。
功能ID（FunctionID/FuncId）：204。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启听视频： on：开启。 off：关闭。 | on |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "ali_video_split" }], "DomainNames": "example.com" }
ali_video_preview
功能说明：配置视频试看，该功能详细介绍请参见控制台配置说明[配置音视频试看](../user-guide/audio-and-video-preview.md)。
功能ID（FunctionID/FuncId）：205。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启视频试看： on：开启。 off：关闭。 说明 支持 TS、MP3 文件格式，FLV 和 MP4 使用拖拽功能实现。 | on |
| ali_video_preview_argument | String | 是 | 自定义试看参数名，试看参数值的单位必须是秒。 | fds |
