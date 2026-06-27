### 视频和大文件加速
对于视频点播、大文件下载等场景，需要特殊配置以确保良好的用户体验。
必要配置
开启Range回源：为加速域名[开启](../../../cdn/documents/user-guide/object-chunking.md)[Range](../../../cdn/documents/user-guide/object-chunking.md)[回源](../../../cdn/documents/user-guide/object-chunking.md)，允许CDN节点按需分片请求大文件，支持视频拖拽播放和断点续传。
配置合理的缓存时间：视频文件通常不频繁更新，建议设置较长的缓存时间（如30天以上），避免频繁回源。
使用资源预热：在视频发布前，使用CDN的[刷新和预热资源](../../../cdn/documents/user-guide/refresh-and-prefetch-resources.md)功能将视频提前分发至边缘节点。
视频码率建议
视频加载速度与码率密切相关。如果用户反馈视频播放卡顿，请检查视频码率：

| 码率范围 | 适用场景 | 说明 |
| --- | --- | --- |
| 500kbps~2000kbps | 移动端、普通画质 | 推荐范围，加载流畅。 |
| 2000kbps~4000kbps | PC 端、高清画质 | 需确保用户带宽充足。 |
| >6000kbps | 超高清/4K | 可能导致加载缓慢，建议提供多码率版本。 |

说明
如果视频码率过高（>10Mbps），即使开启CDN加速也可能出现加载缓慢的问题。建议使用[视频转码](video-transcoding.md)服务降低码率，或提供多码率自适应播放。
