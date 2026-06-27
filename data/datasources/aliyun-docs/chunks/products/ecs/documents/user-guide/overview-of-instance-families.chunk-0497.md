### video-trans
规格族介绍：
提供专属硬件资源和物理隔离
高密度转码，例如显示格式1080P、帧速率30 FPS、编码格式HEVC时，硬件支持84路码流
支持主流H.264、H.265码流，分辨率最大支持8192*4096
面向视频转码应用配备了ASIC转码专用加速器，大幅提升转码速度并降低成本
适用场景：
视频格式、码流转换
图像与视频内容处理
图像识别前的帧图像提取
计算：2.5 GHz主频的Intel®Xeon®Platinum 8269CY（Cascade Lake），睿频3.2 GHz，计算性能稳定
存储：
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、[ESSD](regional-essd-disks.md)[同城冗余云盘](regional-essd-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
video-trans包括的实例规格及指标数据如下表所示：

| 实例规格 | vCPU | 内存（GiB） | 硬件转码单元 | 网络带宽（Gbit/s） | 网络收发包 PPS（万） | 支持 IPv6 | 多队列 | 弹性网卡 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ecs.video-trans.26xhevc | 104 | 192.0 | 12 | 30.0 | 1800 | 是 | 16 | 15 |

该文章对您有帮助吗？
反馈
