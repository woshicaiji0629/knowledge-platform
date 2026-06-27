### 查看 MP4 文件的 Box Header Size
可以使用以下工具查看 MP4 文件的 Box Header Size。
方式一：使用 MP4Box.js 在线工具（推荐）
打开[MP4Box.js ISOBMFF Box Structure Viewer](https://gpac.github.io/mp4box.js/test/filereader.html)。
上传 MP4 文件。
在左侧 Box View 的 Tree View 中，单击mdat (MediaDataBox)。
在右侧Box Property View中查看original_size字段，判断 Header Size：
original_size显示为 1：mdat Box Header Size 为 16 字节，不支持听视频功能。
original_size不显示或不为 1：mdat Box Header Size 为 8 字节，支持听视频功能。
以下为两种情况的属性对比：

| 属性字段 | Header Size = 8 字节（支持） | Header Size = 16 字节（不支持） |
| --- | --- | --- |
| size | 实际大小数值 | 实际大小数值 |
| box_name | MediaDataBox | MediaDataBox |
| start | 偏移字节数 | 偏移字节数 |
| original_size | 不显示 | 显示为 1 |

方式二：使用 Bento4 命令行工具
运行以下命令：
./mp4dump 文件名.mp4 | grep -E "\[mdat\]|\[moov\]"
根据输出结果判断：
[mdat] size=8+xxxxxx：Header Size 为 8 字节，支持听视频功能。
[mdat] size=16+xxxxxx：Header Size 为 16 字节，不支持听视频功能。
