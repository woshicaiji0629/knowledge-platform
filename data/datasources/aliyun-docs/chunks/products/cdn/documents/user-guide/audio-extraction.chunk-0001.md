## 背景信息
当客户端请求访问视频文件时，向服务器端发送URL请求，例如：http://www.aliyun.com/test.flv?ali_audio_only=1，CDN服务器端仅向客户端发送纯音频数据。客户端必须支持Transfer-Encoding:chunked传输方式。
说明
听视频功能不支持Range请求，但是播放视频时许多客户端都会发起Range请求（包括但不限于Safari、iOS设备上的浏览器），建议您使用自研的客户端对接该功能。
听视频过程中如果需要拖动进度条播放，需同时配置拖拽功能。进行拖拽时，会先读取原音视频文件的meta信息获取播放时长，将播放时长作为播放进度来实现播放进度的拖拽具体操作。更多信息，请参见[配置拖拽播放](video-seeking.md)。
目前听视频功能不支持 MP4 Box Header Size 等于 16 的场景（64 位），仅支持 MP4 Box Header Size 等于 8 的场景。关于 Header Size 的详细说明和查看方法，请参见下方 MP4 Box Header Size 说明。
