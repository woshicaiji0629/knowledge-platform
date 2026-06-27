### 存储

| 组件名称 | 组件类型 | 描述 |
| --- | --- | --- |
| [storage-operator](../../product-overview/storage-operator.md) | 系统组件 | 用于管理存储组件的生命周期。 |
| [csi-plugin](../../product-overview/csi-plugin.md) | 可选组件 | 支持存储卷的挂载、卸载功能。 创建集群时，默认安装该组件。 |
| [csi-provisioner](../../product-overview/csi-provisioner.md) | 可选组件 | 支持存储卷的自动创建能力。 创建集群时，如果选择 CSI 插件实现阿里云存储的接入能力，默认安装该组件。 |
| [csi-compatible-controller](../../product-overview/csi-compatible-controller.md) | 可选组件 | 可以使 csi-plugin 和 Flexvolume 存储组件实现共存。 |
