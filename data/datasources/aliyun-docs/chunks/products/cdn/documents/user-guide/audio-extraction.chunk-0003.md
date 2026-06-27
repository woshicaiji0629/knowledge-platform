## MP4 Box Header Size 说明
如果 MP4 文件在使用听视频功能时无法正常提取音频，可能是文件的 mdat Box 使用了扩展 Header（16 字节），不符合当前听视频功能的要求。
说明
此限制主要针对 mdat Box（存储实际音视频数据的容器）。moov 等其他 Box 通常默认使用 8 字节 Header，不受此限制影响。
通过本节可以了解 Header Size 的概念，并检查文件是否兼容。
