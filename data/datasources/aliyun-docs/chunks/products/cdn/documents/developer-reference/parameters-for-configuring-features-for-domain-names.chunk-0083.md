## 视频相关
range
功能说明：配置range回源，该功能详细介绍请参见控制台配置说明[配置](../user-guide/object-chunking.md)[Range](../user-guide/object-chunking.md)[回源](../user-guide/object-chunking.md)。
功能ID（FunctionID/FuncId）：31。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启 range 回源： on：开启。 off：关闭。 force：强制开启。 | on |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }], "functionName": "range" }], "DomainNames": "example.com" }
video_seek
功能说明：配置视频拖拽播放，该功能详细介绍请参见控制台配置说明[配置拖拽播放](../user-guide/video-seeking.md)。
功能ID（FunctionID/FuncId）：30。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启视频拖拽播放： on：开启。 off：关闭。 | on |
| flv_seek_by_time | String | 否 | 是否开启 FLV 按时间拖拽： on：开启。 off：关闭。 | on |
| mp4_seek_start | String | 否 | 自定义 MP4 启动参数。 | mp4starttime |
| mp4_seek_end | String | 否 | 自定义 MP4 结束参数。 | mp4endtime |
| flv_seek_start | String | 否 | 自定义 FLV 启动参数。 | flvstarttime |
| flv_seek_end | String | 否 | 自定义 FLV 结束参数。 | flvendtime |
