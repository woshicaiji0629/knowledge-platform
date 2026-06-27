## 关键组件与概念
CSI组件（csi-plugin、csi-provisioner）
Kubernetes社区推荐的存储插件实现方案，已在集群中默认部署。负责与阿里云存储服务的API进行交互，实现存储卷的自动创建、挂载、卸载等全生命周期管理。详见[管理](install-and-upgrade-the-csi-plug-in.md)[CSI](install-and-upgrade-the-csi-plug-in.md)[组件](install-and-upgrade-the-csi-plug-in.md)。
容器网络文件系统 (CNFS)
ACK托管集群Pro版提供的存储增强功能，将NAS、OSS、CPFS等抽象为Kubernetes CRD对象，提供更精细化的管理能力，如子目录动态创建、配额管理、IO性能监控、回收站、分布式缓存等。详见[容器网络文件系统](cnfs-overview.md)[CNFS](cnfs-overview.md)。
