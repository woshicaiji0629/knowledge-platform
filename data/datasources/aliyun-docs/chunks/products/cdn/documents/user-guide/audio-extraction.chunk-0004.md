### 什么是 MP4 Box Header Size
MP4 文件由多个 Box（容器单元）组成，例如 moov box、mdat box 等。每个 Box 包含一个 Header，用于描述该 Box 的大小和类型。Header 有以下两种规格：

| 规格 | Header 大小 | 说明 |
| --- | --- | --- |
| 标准 Header | 8 字节（32 位） | 包含 size（4 字节）和 box type（4 字节）。size 字段直接存储 Box 的实际大小。适用于 Box 数据量可用 4 字节表示的场景。 |
| 扩展 Header | 16 字节（64 位） | 包含 size（4 字节，固定值为 1）、box type（4 字节）和 largesize（8 字节）。当 size 值为 1 时，表示启用 largesize 机制，真实大小存储在 largesize 字段中。常见于 mdat Box 数据量较大的场景。 |
