### 通用型实例规格族g5
适用场景：
高网络包收发场景，例如视频弹幕、电信业务转发等。
各种类型和规模的企业级应用。
中小型数据库系统、缓存、搜索集群。
数据分析和计算。
计算集群、依赖内存的数据处理。
计算：
处理器与内存配比为1:4。
处理器：2.5 GHz主频的Intel®Xeon®Platinum 8163（Skylake）或者8269CY（Cascade Lake），计算性能稳定。
说明
该规格族的实例有可能部署在不同的服务器平台，如果您的业务需要将实例部署在同一服务器平台，建议您选用g9i。
存储：
I/O优化实例。
支持的云盘类型：[ESSD](essds.md)[云盘](essds.md)、[ESSD AutoPL](essd-autopl-disks.md)[云盘](essd-autopl-disks.md)、SSD云盘和高效云盘。更多云盘信息，请参见[块存储概述](elastic-block-storage-devices.md)。
说明
不同实例规格族的云盘性能上限不同，本规格族的单台实例最高支持20万IOPS。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
具备超高网络收发包PPS能力。
说明
不同实例规格族提供的网络性能不同，如果需要更高的并发连接能力和网络收发包能力，建议您选用g7ne。
实例网络性能与实例规格对应，规格越高网络性能越强。
g5包括的实例规格及指标数据如下表所示：
