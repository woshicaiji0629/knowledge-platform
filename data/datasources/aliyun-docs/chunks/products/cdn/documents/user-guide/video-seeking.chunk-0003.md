### MP4文件请求

| start/end 取值 | 示例 | 拖拽处理逻辑 |
| --- | --- | --- |
| 无效 start ，无效 end | start=foo&end=bar | 忽略拖拽参数，响应完整视频。 |
| 有效 start ，无效 end | start=10 | 拖拽处理 10 文件时长。 |
| 无效 start ，有效 end | end=10 | 拖拽处理 0-10 。 |
| 有效 start ，有效 end | start=0&end=10 | 拖拽处理 0-10 。 |
| start 和 end 同时为 0 | start=0&end=0 | 忽略拖拽参数，响应完整视频。 |
| start 大于 end | start=10&end=0 | 拖拽处理 10 文件时长。 |
| start 等于 end | start=10&end=10 | 拖拽处理 10 文件时长。 |
| start 大于视频时长 | start 大于视频时长 | 返回 400 。 |
