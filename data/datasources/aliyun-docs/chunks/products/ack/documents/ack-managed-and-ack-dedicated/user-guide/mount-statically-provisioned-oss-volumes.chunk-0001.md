## 适用范围
集群和CSI组件（csi-plugin和csi-provisioner）版本需符合要求：
通过RRSA鉴权方式挂载时：集群版本为1.26及以上，CSI版本为v1.30.4及以上。
若在1.30.4之前的版本中使用了RRSA功能，需参见[【产品变更】CSI ossfs](../../product-overview/announcement-on-csi-oss-driver-upgrade.md)[版本升级与挂载流程优化](../../product-overview/announcement-on-csi-oss-driver-upgrade.md)增加RAM角色授权配置。
通过AccessKey鉴权方式挂载时：为确保挂载稳定性，CSI版本建议不低于 v1.18.8.45。
如需升级集群，请参见[手动升级集群](update-the-kubernetes-version-of-an-ack-cluster.md)；如需升级组件，请参见[升级](install-and-upgrade-the-csi-plug-in.md)[CSI](install-and-upgrade-the-csi-plug-in.md)[组件](install-and-upgrade-the-csi-plug-in.md)。
自CSI v1.30.4-*版本起，[OSS](../../product-overview/announcement-on-csi-oss-driver-upgrade.md)[静态卷挂载已依赖](../../product-overview/announcement-on-csi-oss-driver-upgrade.md)[csi-provisioner](../../product-overview/announcement-on-csi-oss-driver-upgrade.md)[组件](../../product-overview/announcement-on-csi-oss-driver-upgrade.md)。
