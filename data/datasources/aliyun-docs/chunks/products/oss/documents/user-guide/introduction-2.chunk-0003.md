## 处理参数
OSS支持直接使用一个或多个参数处理视频等音视频文件，也支持将多个参数封装在一个样式中批量处理视频等音视频文件。关于样式的更多信息，请参见[样式](styles.md)。
当存在多个处理参数时，OSS将按照参数顺序对文件进行处理。处理参数说明如下表所示。

| 处理操作 | 参数 | 说明 |
| --- | --- | --- |
| [视频转码](video-transcoding.md) | video/convert | 将 OSS 中的视频文件转换为需要的格式。 |
| [视频转动图](convert-videos-to-animated-images.md) | video/animation | 将 OSS 中的视频文件转换为 GIF、Webp 等动图格式。 |
| [视频截雪碧图](video-cut-sprite.md) | video/sprite | 将 OSS 中的视频文件截帧并拼成雪碧图转为需要的图片格式。 |
| [视频多帧截取](video-frame-cutting.md) | video/snapshots | 将 OSS 中的视频文件截帧并转换为需要的图片格式。 |
| [视频拼接](video-stitching.md) | video/concat | 将 OSS 中的多个视频拼接为一个视频并转换为需要的格式。 |
| [视频信息提取](video-information-extraction.md) | video/info | 提取 OSS 中的视频文件的音视频格式信息和音视频流信息。 |
| [音频转码](audio-transcoding.md) | audio/convert | 将 OSS 中的音频文件转换为需要的格式。 |
| [音频拼接](audio-stitching.md) | audio/concat | 将 OSS 中的多个音频文件拼接为一个音频并转换为需要的格式。 |
| [音频信息提取](audio-information-extraction.md) | audio/info | 提取 OSS 中的音频文件的音视频格式信息和音视频流信息。 |
| [生成边转边播播放列表](generate-video-playlist.md) | hls/m3u8 | 将 OSS 中的视频文件生成可用于边转边播的播放列表。 |
