## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击视频相关。
在听视频区域，打开听视频开关。
开启听视频功能后，需要配合请求参数ali_audio_only使用。支持的文件格式如下表所示。

| 文件格式 | meta 信息 | ali_audio_only 参数 | 举例 |
| --- | --- | --- | --- |
| MP4 | 源站视频的 meta 信息必须在文件头部，不支持 meta 信息在尾部的视频。 | ali_audio_only 参数表示该请求为音视频分离请求，服务端只返回 meta 信息和音频信息，视频信息会被过滤掉。如果不带该参数或参数值非 1，则该功能失效。 | 请求 http://domain/video.mp4?ali_audio_only=1 。 |
| FLV | 无要求。 | ali_audio_only 参数表示该请求为音视频分离请求，服务端只返回 meta 信息和音频信息，视频信息会被过滤掉。如果不带该参数或参数值非 1，则该功能失效。 | 请求 http://domain/video.flv?ali_audio_only=1 。 |
