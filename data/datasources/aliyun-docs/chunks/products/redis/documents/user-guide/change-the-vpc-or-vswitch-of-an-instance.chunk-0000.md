## 前提条件
若经典版集群架构实例开通了[直连地址](enable-the-direct-connection-mode.md)，请临时释放直连地址，待修改专有网络VPC后再重新启用。
但云原生版集群架构直连模式实例不支持修改VPC。
若实例已开启[专有网络免密访问](enable-password-free-access.md)，请临时关闭该功能。
若存在正在运行的[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)数据迁移或同步任务，请临时暂停任务，否则将提示错误。
