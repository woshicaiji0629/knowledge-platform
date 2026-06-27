## 影响与风险
节省停机模式的成本优势源于其特殊的资源回收机制，但也引入了风险，请仔细评估是否可接受：
- 启动不确定性（不能100%启动成功）
由于节省停机模式会释放计算资源，再次启动实例相当于重新申请资源，如果所在可用区的资源库存不足，实例将无法启动。此风险在资源热门地域和时段更高。对于需要保证高可用性的生产环境，请谨慎使用此模式。
- 实例固定公网IP必然变更
如果服务依赖此实例的固定公网IP（非弹性公网IP），该IP将在停机后被释放。实例再次启动时，系统会为其分配一个新的固定公网IP。如需保留公网IP，请在启用节省停机模式前，[将固定公网](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[转为弹性公网](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)。
- 突发性能实例CPU积分清零
对于[突发性能实例](burst-performance-instance-overview.md)（如t5、t6等规格族），进入节省停机模式后，当前累积的所有[CPU](burst-performance-instance-overview.md)[积分](burst-performance-instance-overview.md)将全部清零，将影响实例的突发能力。
