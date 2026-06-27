### 阿里云持久化存储卷
对于需要持久化存储数据的有状态应用，应选择由阿里云存储服务提供的持久化存储卷。这些存储卷的生命周期独立于Pod，通过CSI实现与Kubernetes的集成。
方案对比
为便于快速选型，表格中各存储方案的标题下方提供了部分核心属性的快速索引。以云盘为例：
[云盘](../../../../ecs/documents/user-guide/elastic-block-storage-devices.md)：方案详细说明。单击可查看详情。
[静态](use-a-statically-provisioned-disk-volume.md)/[动态](use-dynamically-provisioned-disk-volumes.md)：方案支持的[存储卷挂载方式](storage-basics.md)，包括静态存储卷（PV/PVC）和动态存储卷（StorageClass/PVC）。单击可查看具体操作文档。
RWO：方案支持的[存储卷访问模式](storage-basics.md)（accessModes），包括RWO（ReadWriteOnce）、RWX（ReadWriteMany）、ROX（ReadOnlyMany）。
[计费](../../../../ecs/documents/block-storage-devices.md)：方案计费说明。单击可查看详情。
