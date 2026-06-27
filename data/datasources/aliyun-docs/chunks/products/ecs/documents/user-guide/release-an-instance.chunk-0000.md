## 影响与风险
数据丢失：释放实例时，本地盘、设置了随实例释放的数据盘及系统盘会一起释放，此外，设置了随云盘释放的自动快照也会一起被删除。
规避方法：提前[手动创建快照](create-a-snapshot.md)或[自定义镜像](create-a-custom-image-from-a-snapshot-1.md)备份数据。
IP丢失：实例的固定公网IP将被回收，无法找回。
规避方法：[将固定公网](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[转为弹性公网](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)。
可能持续计费：未设置随实例释放的云盘、弹性公网IP（EIP）、云盘快照等独立云资源不会被删除，并会继续计费。
规避方法：释放实例后，通过[账单](../view-billing-details.md)辅助排查并手动释放其余资源。
